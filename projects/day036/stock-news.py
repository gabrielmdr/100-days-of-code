from twilio.rest import Client

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

ALPHA_VANTAGE_ENDPOINT = "https://www.alphavantage.co/query"
ALPHA_VANTAGE_API_KEY = "ALPHA_VANTAGE_API_KEY"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "NEWS_API_KEY"
TWILIO_ACCOUNT_SID = "TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA",
    "apikey": ALPHA_VANTAGE_API_KEY
}

stock_response = requests.get(url=ALPHA_VANTAGE_ENDPOINT, params=stock_params)
stock_response.raise_for_status()

timeseries_array = [value for (key, value) in stock_response.json()["Time Series (Daily)"].items()]

yesterday = timeseries_array[0]
yesterdayclose = float(yesterday["4. close"])

twodaysago = timeseries_array[1]
twodaysagoclose = float(twodaysago["4. close"])

difference = yesterdayclose - twodaysagoclose
updown = None
if difference > 0:
    updown = "🔺"
else:
    updown = "🔻"

diffpercent = round((abs(difference) / yesterdayclose) * 100)

if diffpercent > 1:
    news_params = {
        "qInTitle": "Tesla",
        "apiKey": NEWS_API_KEY
    }

    newsresponse = requests.get(url=NEWS_ENDPOINT, params=news_params)
    newsresponse.raise_for_status()

    articles = newsresponse.json()["articles"][:3]


    def sendsms(article):
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        message = client.messages \
            .create(
                body=f"{STOCK_NAME}: {updown}{diffpercent}%\n{article}",
                from_="YOUR TWILIO PHONE NUMBER",
                to="YOUR PHONE NUMBER"
            )

        print(message.status)


    formattedarticles = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in articles]

    for article in formattedarticles:
        sendsms(article)
