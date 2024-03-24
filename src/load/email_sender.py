from src.utils.create_email import EmailSender


def enviar_email(email, senha, destino, assunto, corpo, caminho_anexo):
    email_sender = EmailSender(email, senha)
    email_sender.send_email(destino, assunto, corpo, caminho_anexo)
    return print('Email enviado com sucesso')
