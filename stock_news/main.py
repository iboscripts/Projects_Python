import requests
from datetime import datetime, date, timedelta
import arrow
import pytz

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
alpha_key = "R3JZKVBHQ3R1RRAQ"
news_key = "6e82ba1dc74c44df889137e375a54acd"

us_tz = pytz.timezone("America/New_York")
yesterday = (datetime.now(us_tz) - timedelta(1)).strftime("%Y-%m-%d")
day_before = (datetime.now(us_tz) - timedelta(2)).strftime("%Y-%m-%d")


url_alpha = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=TSLA&apikey=demo=R3JZKVBHQ3R1RRAQ"
r = requests.get(url_alpha)
data = r.json()
closing_price_yesterday = float(data["Time Series (Daily)"][yesterday]["4. close"])
closing_price_day_before = float(data["Time Series (Daily)"][day_before]["4. close"])

difference = abs(closing_price_yesterday - closing_price_day_before)
diff_percent = (difference / closing_price_yesterday) * 100

if diff_percent > 5.00:
    print("Get News")


url_new = f"https://newsapi.org/v2/everything?q=tesla&from=2024-03-13&sortBy=publishedAt&apiKey={news_key}"
r = requests.get(url_new)
data = r.json()

recent_news_titles = [article["title"] for article in data["articles"][:3]]
recent_news_descriptions = [article["description"] for article in data["articles"][:3]]

for title, description in zip(recent_news_titles, recent_news_descriptions):
    print("title:", title)
    print("description", description)
    print()

"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

