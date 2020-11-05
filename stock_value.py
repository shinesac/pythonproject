import math
import yfinance as yf

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

    # risk_free_rate = float(input ('Enter the current risk free rate. Use the rate of current treasury bills:  '))
    for k,v in info:
        if k == "regularMarketPrice":
            risk_free_rate = v
    growth_rate = float(input ('Enter the anticipated growth rate:  '))
    last_dividend = float(stock.dividends[-1])
    market_cap_rate = risk_free_rate + beta*(expected_return - risk_free_rate)
    valuation = last_dividend/(market_cap_rate - growth_rate)
    judge_stock()
    print(stock.recommendations)

    