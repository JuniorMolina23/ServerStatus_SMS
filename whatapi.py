from twilio.rest import Client

account_sid = 'sid'
auth_token = 'token'

client = Client(account_sid, auth_token)

def send_sms(m):
    message = client.messages.create(
    from_='+numero',
    body=m,
    to='+numero destino'
    )

def validator(text):
    with open("status_message.txt", "w") as archivo_estado:
                archivo_estado.write(text)