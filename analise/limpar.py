import os

extensions_to_keep = ['.py', '.exe', '.zip','useremail.txt']
for filename in os.listdir('.'):
    if os.path.isfile(filename) and not any(filename.endswith(ext) for ext in extensions_to_keep):
        os.remove(filename)

import os
import shutil
import datetime

# Obter a data e hora atuais
agora = datetime.datetime.now()

# Formatar a data e hora para o formato desejado
data_atual = agora.strftime('%d-%m-%Y')
hora_atual = agora.strftime('%H-%M-%S')

# Definir o nome atual e o novo nome do arquivo
nome_atual = 'Final.zip'
novo_nome = f'Final_{data_atual}_{hora_atual}.zip'

# Renomear o arquivo
os.rename(nome_atual, novo_nome)

# Mover o arquivo para a pasta "Feitos"
pasta_destino = 'Feitos'
if not os.path.exists(pasta_destino):
    os.mkdir(pasta_destino)


import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
with open("useremail.txt","r") as email:
    email_content = email.read()
    print(email_content)
# Definir informações do e-mail
de = "d201910872@uftm.edu.br"
para = email_content
assunto = "VaxG"
mensagem = "VaxG Results\nThanks for using!"

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
parte_anexo.set_payload((arquivo_anexo).read())
encoders.encode_base64(parte_anexo)
parte_anexo.add_header('Content-Disposition', "attachment; filename= %s" % nome_anexo)
msg.attach(parte_anexo)

# Enviar e-mail
senha = "bolinho22"
smtp = smtplib.SMTP('smtp.gmail.com', 587)
smtp.starttls()
smtp.login(de, senha)
texto = msg.as_string()
smtp.sendmail(de, para, texto)
smtp.quit()
shutil.move(novo_nome, pasta_destino)

extensions_to_keep = ['.py', '.exe', '.zip']
for filename in os.listdir('.'):
    if os.path.isfile(filename) and not any(filename.endswith(ext) for ext in extensions_to_keep):
        os.remove(filename)
