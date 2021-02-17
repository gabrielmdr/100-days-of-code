import smtplib

MY_EMAIL = "gabriel76242@gmail.com"
MY_PASSWORD = "MY_PASSWORD"
SMTP_SERVER = "smtp.gmail.com"


def send_emails(emails, message, google_flight_link):
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        for email in emails:
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
            )
