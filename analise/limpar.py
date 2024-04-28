import os
import shutil
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
def enviar_email():
    try:
        agora = datetime.datetime.now()
        data_atual = agora.strftime('%d-%m-%Y')
        hora_atual = agora.strftime('%H-%M-%S')
        nome_atual = 'Final.zip'
        novo_nome = f'Final_{data_atual}_{hora_atual}.zip'
        os.rename(nome_atual, novo_nome)
        arquivos_intermed = "MHCintermediariesFILES.zip"

        with open("email.str", "r") as email_file:
            email_content = email_file.read().strip()  # Remover espaços em branco extras
            print(email_content)

        # Definir informações do e-mail
        de = "vaxpipeline@outlook.com"
        para = email_content
        assunto = "VaxPIPE Results"
        mensagem = "VaxPIPE Results\nThanks for using"

        # Criar mensagem multipart (para enviar anexo)
        msg = MIMEMultipart()
        msg['From'] = de
        msg['To'] = para
        msg['Subject'] = assunto

        # Adicionar mensagem de texto
        msg.attach(MIMEText(mensagem, 'plain'))

        # Adicionar anexo
        caminho_anexo = novo_nome
        nome_anexo = os.path.basename(caminho_anexo)
        arquivo_anexo = open(caminho_anexo, 'rb')
        parte_anexo = MIMEBase('application', 'octet-stream')
        parte_anexo.set_payload(arquivo_anexo.read())
        encoders.encode_base64(parte_anexo)
        parte_anexo.add_header('Content-Disposition', f"attachment; filename= {nome_anexo}")
        msg.attach(parte_anexo)

        # Adicionar segundo anexo (arquivos_intermed)
        caminho_anexo2 = arquivos_intermed
        nome_anexo2 = os.path.basename(caminho_anexo2)
        arquivo_anexo2 = open(caminho_anexo2, 'rb')
        parte_anexo2 = MIMEBase('application', 'octet-stream')
        parte_anexo2.set_payload(arquivo_anexo2.read())
        encoders.encode_base64(parte_anexo2)
        parte_anexo2.add_header('Content-Disposition', f"attachment; filename= {nome_anexo2}")
        msg.attach(parte_anexo2)

        # Enviar e-mail
        senha = "!Gipsysiomar"
        smtp = smtplib.SMTP('smtp-mail.outlook.com', 587)
        smtp.starttls()
        smtp.login(de, senha)
        texto = msg.as_string()
        smtp.sendmail(de, para, texto)
        smtp.quit()
        print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar o e-mail: {e}")

def apagar_arquivos():
    diretorio_atual = os.getcwd()
    extensoes = ['.txt', '.csv', '.faa', '.png', 'zip', 'str']
    for arquivo in os.listdir(diretorio_atual):
        # Verificar se o arquivo tem uma das extensões a serem excluídas
        if any(arquivo.endswith(extensao) for extensao in extensoes):
            # Construir o caminho completo do arquivo
            caminho_arquivo = os.path.join(diretorio_atual, arquivo)
            # Tentar excluir o arquivo
            try:
                os.remove(caminho_arquivo)
                print(f"Arquivo {arquivo} excluído com sucesso.")
            except Exception as e:
                print(f"Erro ao excluir o arquivo {arquivo}: {e}")

