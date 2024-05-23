import os
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def enviar_email():
    try:
        # Obter a data e hora atual
        agora = datetime.datetime.now()
        data_atual = agora.strftime('%d-%m-%Y')
        hora_atual = agora.strftime('%H-%M-%S')

        nome_atual = 'Final.zip'
        novo_nome = f'Final_{data_atual}_{hora_atual}.zip'
        os.rename(nome_atual, novo_nome)
        
        arquivos_intermed = "MHCintermediariesFILES.zip"

        with open("email.str", "r") as email_file:
            email_content = email_file.read().strip()

        with open('analysisname.str', 'w') as file:
            assunto = assunto.read().strip()

        # Definir informações do e-mail
        de = "vaxpipeline@outlook.com"
        para = email_content
        assunto += " VaxPIPE Analysis Result"
        mensagem = "VaxPIPE Results\nThanks for using"

        # Criar mensagem multipart (para enviar anexo)
        msg = MIMEMultipart()
        msg['From'] = de
        msg['To'] = para
        msg['Subject'] = assunto

        # Adicionar mensagem de texto
        msg.attach(MIMEText(mensagem, 'plain'))

        # Adicionar primeiro anexo
        caminho_anexo = novo_nome
        nome_anexo = os.path.basename(caminho_anexo)
        with open(caminho_anexo, 'rb') as arquivo_anexo:
            parte_anexo = MIMEBase('application', 'octet-stream')
            parte_anexo.set_payload(arquivo_anexo.read())
            encoders.encode_base64(parte_anexo)
            parte_anexo.add_header('Content-Disposition', f"attachment; filename={nome_anexo}")
            msg.attach(parte_anexo)

        # Adicionar segundo anexo
        caminho_anexo2 = arquivos_intermed
        nome_anexo2 = os.path.basename(caminho_anexo2)
        with open(caminho_anexo2, 'rb') as arquivo_anexo2:
            parte_anexo2 = MIMEBase('application', 'octet-stream')
            parte_anexo2.set_payload(arquivo_anexo2.read())
            encoders.encode_base64(parte_anexo2)
            parte_anexo2.add_header('Content-Disposition', f"attachment; filename={nome_anexo2}")
            msg.attach(parte_anexo2)

        # Enviar e-mail
        senha = "!Gipsysiomar"
        smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtp.starttls()
        smtp.login(de, senha)
        smtp.sendmail(de, para, msg.as_string())
        smtp.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

def apagar_arquivos():
    diretorio_atual = os.getcwd()
    extensoes = ['.txt', '.csv', '.faa', '.png', '.zip', '.str', '.log']
    for arquivo in os.listdir(diretorio_atual):
        if any(arquivo.endswith(extensao) for extensao in extensoes):
            caminho_arquivo = os.path.join(diretorio_atual, arquivo)
            try:
                os.remove(caminho_arquivo)
                print(f"Arquivo {arquivo} excluído com sucesso.")
            except Exception as e:
                print(f"Erro ao excluir o arquivo {arquivo}: {e}")

# Exemplo de chamada das funções
enviar_email()
apagar_arquivos()
