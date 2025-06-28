#Use yfinance to Extract Stock Data
#TESLA
import yfinance as yf
import pandas as pd
import urllib.request

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
urllib.request.urlretrieve(url,"revenue.htm")

print(tesla.info['longName'])
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
