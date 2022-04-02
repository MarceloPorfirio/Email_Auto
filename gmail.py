import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Olá Bom dia, Estamos com algumas promoções.</p>

    bla,bla,bla,bla

    """
    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = "marcelobrys20@gmail.com"
    msg['To'] = "marcelobrys31@gmail.com; marcelobrys20@hotmail.com"
    password = "leonardo21"
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending Email
    s.login(msg['From'],password)
    s.sendmail(msg['From'],[msg['To']],msg.as_string().encode('utf-8'))
    print('email enviado !')

enviar_email()