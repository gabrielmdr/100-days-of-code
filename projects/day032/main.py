import datetime
import pandas
import random
import smtplib

birthdayperson = None
letters = []

senderemail = "example@mail.com"  # Your email here
senderpassword = "password"  # Your password here

smtpserver = "smtp.example.com"  # SMTP server here (e.g. Gmail: smtp.gmail.com)

for n in range(1, 4):
    with open(f"./letter_templates/letter_{n}.txt") as letterfile:
        letters.append(letterfile.read())

birthdays_dataframe = pandas.read_csv("birthdays.csv")
birthdays = birthdays_dataframe.to_dict(orient="records")

now = datetime.datetime.now()
for index in range(len(birthdays)):
    birthday = birthdays[index]
    if now.date() == datetime.date(birthday["year"], birthday["month"], birthday["day"]):
        birthdayperson = birthday

        if birthdayperson:
            letter = random.choice(letters)
            letter = letter.replace("[NAME]", birthdayperson["name"])

            with smtplib.SMTP(smtpserver) as connection:
                connection.starttls()
                connection.login(user=senderemail, password=senderpassword)
                connection.sendmail(
                    from_addr=senderemail,
                    to_addrs=birthdayperson["email"],
                    msg=f"Subject:Happy Birthday!\n\n{letter}"
                )
    birthdayperson = None
