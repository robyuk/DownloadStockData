# Downloads stock data from Yahoo Finance
import requests
from datetime import datetime
import time

ticker=input("Enter ticker symbol: ")
start_date=input('Enter start date as yyyy/mm/dd : ')
end_date=input('Enter end date as yyyy/mm/dd : ')

# Convert input dates to datetime format
start_dt=datetime.strptime(start_date,'%Y/%m/%d')
end_dt=datetime.strptime(end_date,'%Y/%m/%d')

#Convert dates to seconds from epoch
start_secs=int(time.mktime(start_dt.timetuple()))
end_secs=int(time.mktime(end_dt.timetuple()))

#Contruct the URL query
url=f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={start_secs}&period2={end_secs}&interval=1d&events=history&includeAdjustedClose=true"

#Contruct a browser header.  This is required by the Yahoo Finance site
headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content=requests.get(url,headers=headers).content

with open(f"{ticker}.csv", "wb") as file:
    file.write(content)