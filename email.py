import win32com.client as win32

# Criar integração do python com outlook
outlook = win32.Dispatch('outlook.application')

# Criar um email
email = outlook.CreateItem(0)

# Configurar as informações do seu e-mail
email.To = "marcelobrys20@gmail.com"
email.Subject = "assunto"
email.HTMLBody = """ 
<p>Olá Bom dia, Estamos com algumas promoções.</p>

bla,bla,bla,bla
Olá Bom dia, Estamos com algumas promoções.

bla,bla,bla,bla


"""

email.Send()