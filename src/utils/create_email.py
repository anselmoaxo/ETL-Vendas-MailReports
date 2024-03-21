import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import yaml


class EmailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(email, password)

    def send_email(self, to_email, subject, body, attachment_path=None):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        if attachment_path:
            attachment = open(attachment_path, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f"attachment; filename= {attachment_path}")
            msg.attach(part)

        text = msg.as_string()
        self.server.sendmail(self.email, to_email, text)
        
        
        with open('config/config.yml', 'r') as file:
            config = yaml.safe_load(file)

# Acessa as configurações do Gmail e do banco de dados
        gmail_config = config['gmail']
        email_1 = gmail_config['email']
        senha = gmail_config['password']
        email_sender = EmailSender(email_1, senha)
        destinatario = 'aoliveira@cstecnologia.com.br'
        assunto = 'Analise Ultimas Vendas'
        corpo = 'Segue analise dos cliente com mais de 30 dias sem retornar a compra'

            # Substitua 'caminho/do/anexo' pelo caminho do arquivo que você deseja anexar
        caminho_do_anexo = 'data/output/vendas.xlsx'

        email_sender.send_email(destinatario, assunto, corpo, caminho_do_anexo)