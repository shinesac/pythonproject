import csv
import math
from datetime import datetime

# feature 1: connect to external API and use data in program- import yahoo finance API data, program uses the data from this API to make calclations 
import yfinance as yf


# feature 2: create list, which is used in the program later- favorites list is created and later used to make a csv file 
# with additional api data that is linked to items in the favorites list
favorite_list = []

# datetime is used to get current date and determine what the current year is, current month is, last year was, and what 2 years ago was.
# This is later used in the program to select data and make calculations
current_date = datetime.now().date()
current_year = current_date.year
current_month = current_date.month
last_year = current_year - 1
last_two_year = last_year - 1

# feature 3: create and use at least 3 fuctions, with at least 1 returning a value used later - 4 functions are listed below and judge_stock
# returns a value of either over, under, or fair valued which is displayed to the user. 

# function to display favorites list (used to make things more DRY)
def display_favorite_list():
    print('Favorites: {}'.format(favorite_list))

# function to print valuation (used to make things more DRY)
def print_valuation():
     print (ticker + ' valuation is {}'.format(valuation))

# function used to determine and display if stock is overvalued, undervalued, or at fair value
def judge_stock(): 
    if valuation < current_stock_price:
        print (ticker + ' Stock is OVERVALUED')
        print_valuation()
        is_growth_stock()
    elif valuation > current_stock_price:
        print (ticker + ' Stock is UNDERVALUED')
        print_valuation()
    else:
        print (ticker + ' Stock is at FAIR VALUE')
        print_valuation()

# function to determine if overvalued stock is could be a high growth stock and not truly overvalued
def is_growth_stock():
    if valuation < 0:
        print(ticker + ' valuation is negative and may be a high growth stock. As such, this valuation method is not usable.')
    else:
        pass

# used to determine risk free rate using the 10yr treasury bond data provided from yfinance stock ticker data for 10yr t-bills.
t_bond = yf.Ticker('^TNX')
bond_info = sorted([[a,b] for a,b in t_bond.info.items()])
for a,b in bond_info:
    if a == "regularMarketPrice":
        risk_free_rate = float(b/100)

# feature 4: create master loop with way to exit - master loop created with while true and breaks (ends) by entering exit
# This takes the stock ticker info, grabs data from the api related to that stock, and makes calculations with the data to determine a final value.
while True:    
    ticker = input ('Enter your stock ticker symbol or type "exit" to exit the program:  ' ) 
    if ticker == "exit":
        break
    stock = yf.Ticker(ticker)
    try:
        info = sorted([[k,v] for k,v in stock.info.items()])
        for k,v in info:
            if k == "beta":
                beta = v
    except KeyError:
        print("Sorry, that ticker does not exist. Please try again.")
    except ImportError:
        print("Sorry, that ticker does not exist. Please try again.")
    else:    
        current_stock_price = float(input('Enter current stock price:  '))
        expected_return = 0.08
        market_cap_rate = risk_free_rate + beta*(expected_return - risk_free_rate)
    try:
        growth_rate = (sum(stock.dividends[str(last_year)]) - sum(stock.dividends[str(last_two_year)]))/sum(stock.dividends[str(last_two_year)])
        last_dividend = float(stock.dividends[-1])
        valuation = last_dividend/(market_cap_rate - growth_rate)
    except ZeroDivisionError:
        print("Sorry, this stock does not have a history of providing dividends. As such, this valuation model cannot be used.")  
    except TypeError:
        print("Sorry, this stock does not have a history of providing dividends. As such, this valuation model cannot be used.")
    else:      
        judge_stock()

# feature 5: calculate and store data based on an external factor such as current date - the current date is grabbed earlier 
# in the program and is used here to sift through API recommendation data to only display the data relevant to the current month and year.
    try:  
        print(stock.recommendations[str(current_date.strftime('%Y-%m'))])
    except KeyError:
        print("Sorry, this stock does not have any recommendations within the current month.")
    except ImportError:
        print("Sorry, there is nothing existing for " + ticker + ".")
    else:    
        display_favorite_list()

# feature 6: other feature - opens and writes data to external csv file. This only occurs if ticker is not already in the favorite list.
# The data is sorted alphabetically and formated before being written to the file for "user-friendliness."
        if ticker not in favorite_list:
            favorite = input('Would you like to add ' + ticker + ' to your favorites list? y/n  ')
            
            if favorite == 'y':
                favorite_list.append(ticker)
                display_favorite_list()
                file = open('favorites.csv', 'a')
                info = sorted([[k,v] for k,v in stock.info.items()])
                file.write("\n" + ticker + "\n")
                for k,v in info:
                    file.write(f'{k} : {v}' + "\n")
                file.close()
            elif favorite == 'n':
                pass