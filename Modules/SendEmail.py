import os
import smtplib
# import imghdr
from email.message import EmailMessage


def read_environment_variables():
    print("Searching for the keys")
    py_key_values, extracted_list = {}, os.environ.get("PYTHON_DB", "").split(";")

    for item in extracted_list:
        key, value = item.split(":")
        py_key_values[key] = value

    try:
        email_address = py_key_values["EMAIL_ADDRESS"]
        email_password = py_key_values["EMAIL_PASSWORD"]
        print("Found the keys")
        return email_address, email_password
    except KeyError:
        print("The environment variables are not set correctly")
        printing = [print(f"{key} = {value}") for key, value in py_key_values.items()]
        del printing
        input("Press any key to exit...")
        exit()


def send_email(sender_email, sender_password, target_email):
    # with open("test.jpg", "rb") as img_file:
    #     img_data = img_file.read()
    #     img_type = imghdr.what(img_file.name)
    #     img_name = img_file.name

    subject = "Python Email Test"
    body = "Se voce esta lendo isso, o email foi enviado com sucesso!"
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = target_email
    msg.set_content(body)
    # msg.add_attachment(img_data, maintype="image", subtype=img_type, filename=img_name)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp_connection:
        print("Sending email.... guenta ai")
        smtp_connection.login(sender_email, sender_password)
        smtp_connection.send_message(msg)
        print("Email sent")


if __name__ == "__main__":
    EMAIL_ADDRESS, EMAIL_PASSWORD = read_environment_variables()
    TARGET_EMAIL = "test@gmail.com"
    send_email(EMAIL_ADDRESS, EMAIL_PASSWORD, TARGET_EMAIL)
