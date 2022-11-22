import requests
import datetime
from twilio.rest import Client



stock_api = "YEPBUF6EWR8DF2I3"
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
parameters = {"function": "TIME_SERIES_DAILY",
              "symbol": STOCK,
              "outputsize": "compact",
              "datatype": "json",
              "apikey": stock_api}
today = datetime.datetime.now().day
yesterday = str(today - 1)
day_before = str(today - 2)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

first_title = ""
first_description = ""
first_url = ""

second_title = ""
second_description = ""
second_url = ""

third_title = ""
third_description = ""
third_url = ""

def get_news():

    news_api = "a2915ea20d8349f2a43a24e6eb9acf00"
    news_parameters = {"q": COMPANY_NAME,
                       "from":"2022-10-14",
                       "sortBy": "publishedAT",
                       "language": "en",
                       "PageSize": 3,
                       "apiKey": news_api}

    news_response = requests.get(url="https://newsapi.org/v2/everything", params=news_parameters)
    news_response.raise_for_status()
    news = news_response.json()

    first_title = news["articles"][0]["title"]
    first_description = news["articles"][0]["description"]
    first_url = news["articles"][0]["url"]

    second_title = news["articles"][1]["title"]
    second_description = news["articles"][1]["description"]
    second_url = news["articles"][1]["url"]

    third_title = news["articles"][2]["title"]
    third_description = news["articles"][2]["description"]
    third_url = news["articles"][2]["url"]



## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
data = response.json()
response.raise_for_status()


# More efficiency ---------------
# data_list = [value for (key, value) in data.items()]
# yesterday_data = data_list[0]
# yesterday_data_closing_price = yesterday_data["4. close"]
# day_before_yesterday = data_list[1]
# day_before_yesterday.closing_price = day_before_yesterday_data["4. close"]






stock_in_close_yest = float(data["Time Series (Daily)"]["2022-10-" + yesterday]["4. close"])
stock_in_close_day_bf = float(data["Time Series (Daily)"]["2022-10-" + day_before]["4. close"])

max_difference = stock_in_close_day_bf / 20
one_percent = stock_in_close_day_bf / 100

if stock_in_close_day_bf > stock_in_close_yest:
    difference = stock_in_close_day_bf - stock_in_close_yest
    percentige = difference / one_percent
    message = f"TSLA: 🔻 by {percentige}%\nHeadline: {first_title}\nBrief:{first_description}\n{first_url}"

else:
    difference = stock_in_close_yest - stock_in_close_day_bf
    percentige = difference / one_percent
    message = f"TSLA: 🔺 by {percentige}%\nHeadline: {first_title}\nBrief:{first_description}\n{first_url}"

if difference >= max_difference:
    get_news()
else:
    print("its ok")




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number.

account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
client = Client(account_sid, auth_token)

message = client.messages.create(
    body=message,
    from=xxxxxxx,
    to='xxxxxxxx'
)
print(message.sid)

# Optional: Format the SMS message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
