import yfinance as yf
import pandas as pd
from bs4 import BeautifulSoup
import requests
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import warnings

pio.renderers.default = "browser"
warnings.filterwarnings("ignore", category = FutureWarning)

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm"
html_data = requests.get(url).text
#print(html_data)

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

tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)

#Define Graphing Function
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()

make_graph(tesla_data, tesla_revenue, "Tesla, Inc.")
