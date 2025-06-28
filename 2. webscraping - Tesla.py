#Use Webscraping to Extract Tesla Revenue Data
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
print(html_data)

soup = BeautifulSoup(html_data, 'html.parser')

#Create an Empty DataFrame
tesla_revenue = pd.DataFrame(columns=["Date","Revenue"])
#Find the Relevant Table
#Check for the Tesla Quarterly Revenue Table
#Iterate Through Rows in the Table Body
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text

    #Append Data to the DataFrame
    tesla_revenue=pd.concat([tesla_revenue,pd.DataFrame({'Date':[date],'Revenue':[revenue]})], ignore_index=True)

#Remove the comma and dollar sign from the revenue column
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

#remove null or empty strings in the revenue column
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

print("Tesla, Inc")
#Print Extracted Data
print(tesla_revenue.head())