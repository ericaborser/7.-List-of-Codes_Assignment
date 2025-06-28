#Use Webscraping to Extract GME Revenue Data
import pandas as pd
import requests
from bs4 import BeautifulSoup
import warnings

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html"
html_data_2 = requests.get(url).text
print(html_data_2)

soup = BeautifulSoup(html_data_2, 'html.parser')

#Create an Empty DataFrame
gme_revenue = pd.DataFrame(columns=["Date","Revenue"])
#Find the Relevant Table
#Check for the GameStop Quarterly Revenue Table
#Iterate Through Rows in the Table Body
for row in soup.find("tbody").find_all("tr"):
    col = row.find_all('td')
    date = col[0].text
    revenue = col[1].text

    #Append Data to the DataFrame
    gme_revenue=pd.concat([gme_revenue,pd.DataFrame({'Date':[date],'Revenue':[revenue]})], ignore_index=True)

#Remove the comma and dollar sign from the revenue column
gme_revenue["Revenue"] = gme_revenue['Revenue'].str.replace(',|\$',"",regex=True)

#remove null or empty strings in the revenue column
gme_revenue.dropna(inplace=True)
gme_revenue = gme_revenue[gme_revenue['Revenue'] != ""]

print("GameStop, Corp.")
#Print Extracted Data
print(gme_revenue.head())