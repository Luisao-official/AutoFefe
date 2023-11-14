import os
import email
import imaplib

def get_reg_value(*reg_key):
    py_key_values, extracted_list = {}, os.environ['PYTHON_DB'].split(';')
    reg_value = None
    for item in extracted_list:
        key, value = item.split(':')
        py_key_values[key] = value
    try:
        reg_values = []
        for key in reg_key:
            reg_values.append(py_key_values[key])
    except KeyError:
        print('The environment variables are not set correctly')
        printing = [print(f'{key} = {value}') for key, value in py_key_values.items()]
        del printing
        reg_values = None
    finally:
        return reg_values

try:
    email_address, email_password = get_reg_value('EMAIL_ADDRESS', 'EMAIL_PASSWORD')
except TypeError:
    print('The environment variables for email and password are not set correctly. Check README.txt for more information')
    input('Press any key to exit...')
    exit()

SERVER = 'imap.gmail.com'
PORT = 993

mail = imaplib.IMAP4_SSL(SERVER)
mail.login(email_address, email_password)

mail.select("inbox")

status, data = mail.search(None, 'ALL')
print(status)
print(data)

for num in data[0].split():
    status, data = mail.fetch(num, '(RFC822)')
    print(status)
    email_message = email.message_from_bytes(data[0][1])
    print(email_message['From'])
    print(email_message['Subject'])
    print(f"BCC: {email_message['BCC']}")
    print(f"CC: {email_message['CC']}")
    print(f"Date: {email_message['Date']}")
    print(f"Delivered-To: {email_message['Delivered-To']}")
    print("COntent:")

    for piece in email_message.walk():
        if piece.get_content_type() == 'text/plain':
            print(piece.as_string())
    input()
    # break

mail.close()