import math
from datetime import datetime
import yfinance as yf



current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month
last_year = current_year - 1
last_two_year = last_year - 1

def judge_stock(): 
    if valuation < current_stock_price:
        print (ticker + ' Stock is OVERVALUED')
        print (valuation)
    elif valuation > current_stock_price:
            print (ticker + ' Stock is UNDERVALUED')
            print (valuation)
    else:
            print (ticker + ' Stock is at fair value')
            print (valuation)

while True:    
    ticker = input ('Enter your stock ticker symbol or type exit to exit the program:  ' )
    if ticker == "exit":
        break
    stock = yf.Ticker(ticker)
    info = sorted([[k,v] for k,v in stock.info.items()])
    for k,v in info:
        # print(f'{k} : {v}')
        if k == "beta":
            beta = v
    current_stock_price = float(input('Enter current stock price:  '))
    expected_return = 0.08
    for k,v in info:
        if k == "regularMarketPrice":
            risk_free_rate = v
    growth_rate = (sum(stock.dividends[str(last_year)]) - sum(stock.dividends[str(last_two_year)]))/sum(stock.dividends[str(last_two_year)])
    print (growth_rate)
    last_dividend = float(stock.dividends[-1])
    market_cap_rate = risk_free_rate + beta*(expected_return - risk_free_rate)
    valuation = last_dividend/(market_cap_rate - growth_rate)
    judge_stock()
    print(stock.recommendations[str(current_date.strftime('%Y-%m'))])

    