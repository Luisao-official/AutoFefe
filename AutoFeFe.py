import serial
import time
from datetime import datetime
from Modules import Get_mails, SendEmail
from Modules.Schedules import Events
from os import system


# def write_read(x):
#     arduino.write(bytes(x,   'utf-8'))
#     time.sleep(0.05)
#     data = arduino.readline()
#     return data


# while True:
#     num = input("Enter a number: ")
#     value = write_read(num)
#     print(value)

# Configure the serial connection
start_port = 2
end_port = 10

# TODO - Fix this implementation
# for i in range(start_port, end_port):
#     try:
#         port = "COM" + str(i)
#         arduino = serial.Serial(port, 115200, timeout=0.1)
#         print("Connected to " + port)
#         break
#     except serial.SerialException:
#         print("Failed to connect on " + port)


def check_events():
    events = Events.from_file("events.txt")
    if len(events) == 0:
        print("Tu ta livre")
        return
    for event in events:
        event_datetime_str = f"{event.date} at {event.time}"
        event_datetime = datetime.strptime(event_datetime_str, "%Y-%m-%d at %H:%M")

        # Calculate time remaining
        current_datetime = datetime.now()
        time_remaining = event_datetime - current_datetime

        # Check if the event has passed or is in the future
        if time_remaining.total_seconds() > 0:
            print(
                f"{event.name}: {event_datetime_str} (Time Remaining: {time_remaining})"
            )
        else:
            Events.erase("events.txt", events.index(event) + 1)
            print(f"{event.name}: {event_datetime_str} (Event has passed)")
    time.sleep(5)


def send_email():
    email_address, email_password = SendEmail.read_environment_variables()
    SendEmail.send_email(email_address, email_password, "test@email.edu.br")


def log(message):
    with open("log.txt", "a") as file:
        file.write(f"{datetime.now()}: {message}\n")


commands = {"checkEvents": check_events, "sendMail": send_email}

actual_entry = "Home"
challenge = {"yes": 1, "no": 0}

arduino = serial.Serial(port="COM3", baudrate=115200, timeout=1)

while True:
    data = arduino.readline().decode().strip()
    time.sleep(0.1)

arduino.close()
