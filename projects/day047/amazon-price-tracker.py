from bs4 import BeautifulSoup

import requests
import smtplib

EMAIL = "YOUR SENDER EMAIL"
PASSWORD = "YOUR PASSWORD"
SMTP_SERVER = "smtp.gmail.com"

url = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
headers = {
    "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:86.0) Gecko/20100101 Firefox/86.0"
}

desired_price = 200

amazon_product_page = requests.get(
    url=url,
    headers=headers
)

soup = BeautifulSoup(amazon_product_page.text, "lxml")

price = float(soup.select_one("#priceblock_ourprice").getText()[1:])
product = soup.select_one("#productTitle").getText().strip()

if price <= desired_price:
    with smtplib.SMTP(SMTP_SERVER) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs="YOUR DESTINATION EMAIL",
            msg=f"Subject:Amazon Price Alert!\n\n{product} is now ${price}\n{url}".encode('utf-8')
        )
