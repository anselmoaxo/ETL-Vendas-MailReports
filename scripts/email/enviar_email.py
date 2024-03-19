import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv
import os

load_dotenv()
senha = os.getenv("SENHA")
email_1 = os.getenv("EMAIL")


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


if __name__ == "__main__":
    email_sender = EmailSender(email_1, senha)
    destinatario = 'aoliveira@cstecnologia.com.br'
    assunto = 'Teste de e-mail com anexo'
    corpo = 'Este é um e-mail de teste com anexo.'

    # Substitua 'caminho/do/anexo' pelo caminho do arquivo que você deseja anexar
    caminho_do_anexo = 'data/teste.pdf'

    email_sender.send_email(destinatario, assunto, corpo, caminho_do_anexo)
