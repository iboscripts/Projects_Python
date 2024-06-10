import datetime as dt
import smtplib
import random
import pandas
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(sender_email, sender_password, recipient_email, subject, message):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    msg.attach(MIMEText(message, 'plain'))

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=sender_email, password=sender_password)
        connection.send_message(msg)


my_email = "furkan.cinko2312@gmail.com"
password = "hsnizlbvwfpyotpd"

current_date = dt.datetime.now()
day = current_date.day
month = current_date.month

data = pandas.read_csv("birthdays.csv")

for index, row in data.iterrows():
    birthday_day = row["day"]
    birthday_month = row["month"]
    birthday_mail = row["email"]
    birthday_name = row["name"]

    if day == birthday_day and month == birthday_month:
        file_path = f"letter_templates/letter_{random.randint(1, 7)}.txt"

        with open(file_path, 'r', encoding='utf-8') as file:
            letter = file.read()

        letter = letter.replace("[NAME]", birthday_name)

        send_email(sender_email=my_email,
                   sender_password=password,
                   recipient_email=birthday_mail,
                   subject="Mutlu Yıllar!",
                   message=letter)
