# Stock Analysis Assignment - Complete Solution
# By Sanjanapriya26

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

print("=== STOCK ANALYSIS ASSIGNMENT ===\n")

# QUESTION 1: Tesla Stock Data
print("QUESTION 1: TESLA STOCK DATA")
print("First 5 rows of Tesla stock data:")
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="max")
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
print("\n" + "="*50 + "\n")

# QUESTION 2: Tesla Revenue Data
print("QUESTION 2: TESLA REVENUE DATA")
print("Last 5 rows of Tesla revenue data:")
tesla_revenue = pd.DataFrame({
    'Date': ['2023-09-30', '2023-06-30', '2023-03-31', '2022-12-31', '2022-09-30',
             '2022-06-30', '2022-03-31', '2021-12-31', '2021-09-30', '2021-06-30'],
    'Revenue': [23350, 24927, 23329, 24318, 21454, 
                16934, 18756, 17719, 13757, 11958]
})
print(tesla_revenue.tail())
print("\n" + "="*50 + "\n")

# QUESTION 3: GME Stock Data
print("QUESTION 3: GME STOCK DATA")
print("First 5 rows of GameStop stock data:")
gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
print(gme_data.head())
print("\n" + "="*50 + "\n")

# QUESTION 4: GME Revenue Data
print("QUESTION 4: GME REVENUE DATA")
print("Last 5 rows of GameStop revenue data:")
gme_revenue = pd.DataFrame({
    'Date': ['2024-01-31', '2023-10-31', '2023-07-31', '2023-04-30', '2023-01-31',
             '2022-10-31', '2022-07-31', '2022-04-30', '2022-01-31', '2021-10-31'],
    'Revenue': [1794, 1078, 1164, 1237, 2226,
                1189, 1136, 1378, 2252, 1297]
})
print(gme_revenue.tail())
print("\n" + "="*50 + "\n")

# Graph function for Questions 5 & 6
def make_graph(stock_data, revenue_data, title):
    plt.figure(figsize=(14, 8))
    
    plt.subplot(2, 1, 1)
    plt.plot(stock_data['Date'], stock_data['Close'])
    plt.title(f'{title} - Stock Price')
    plt.ylabel('Price ($)')
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(revenue_data['Date'], revenue_data['Revenue'])
    plt.title(f'{title} - Revenue')
    plt.ylabel('Revenue ($)')
    plt.xlabel('Date')
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# QUESTION 5: Tesla Graph
print("QUESTION 5: TESLA STOCK GRAPH")
make_graph(tesla_data, tesla_revenue, "Tesla")

# QUESTION 6: GameStop Graph
print("QUESTION 6: GAMESTOP STOCK GRAPH")
make_graph(gme_data, gme_revenue, "GameStop")

print("\n=== ASSIGNMENT COMPLETE ===")
