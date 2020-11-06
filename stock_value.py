import csv
import math
from datetime import datetime
import yfinance as yf

favorite_list = []


current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month
last_year = current_year - 1
last_two_year = last_year - 1

def print_valuation():
     print (ticker + ' valuation is {}'.format(valuation))

def judge_stock(): 
    if valuation < current_stock_price:
        print (ticker + ' Stock is OVERVALUED')
        print_valuation()
    elif valuation > current_stock_price:
        print (ticker + ' Stock is UNDERVALUED')
        print_valuation()
    else:
        print (ticker + ' Stock is at FAIR VALUE')
        print_valuation()


t_bond = yf.Ticker('^TNX')
bond_info = sorted([[a,b] for a,b in t_bond.info.items()])
for a,b in bond_info:
    if a == "regularMarketPrice":
        risk_free_rate = float(b/100)


while True:    
    ticker = input ('Enter your stock ticker symbol or type "exit" to exit the program:  ' )
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
   
    growth_rate = (sum(stock.dividends[str(last_year)]) - sum(stock.dividends[str(last_two_year)]))/sum(stock.dividends[str(last_two_year)])
    last_dividend = float(stock.dividends[-1])
    market_cap_rate = risk_free_rate + beta*(expected_return - risk_free_rate)
    valuation = last_dividend/(market_cap_rate - growth_rate)
    judge_stock()
    print(stock.recommendations[str(current_date.strftime('%Y-%m'))])
    favorite = input('Would you like to add ' + ticker + ' to your favorites list? y/n  ')

    if favorite == 'y':
        favorite_list.append(ticker)
    elif favorite == 'n':
        pass

    print('Favorites: {}'.format(favorite_list))

    view_csv = input('To view in-depth stock data for items in your favorites list, enter "view", otherwise enter "pass":  ')
    if view_csv == "view":
        open('favorites.csv', 'a')
    elif view_csv == "pass":
        pass

    # with open(favorites.csv, newline='') as csvfile:
    #     stockreader = csv.reader(csvfie, delimeter= ':')
