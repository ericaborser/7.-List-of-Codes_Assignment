#Use yfinance to Extract Stock Data
#GameStop
import yfinance as yf
import pandas as pd
import urllib.request

GameStop = yf.Ticker("GME")
GameStop_Data = GameStop.history(period="max")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
urllib.request.urlretrieve(url,"revenue.htm")

print(GameStop.info['longName'])
GameStop_Data.reset_index(inplace=True)
print(GameStop_Data.head())