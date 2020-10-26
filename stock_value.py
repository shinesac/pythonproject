stock = input ('Enter your stock ticker symbol:  ')
current_stock_price = float(input('Enter current stock price:  '))
expected_return = float(input ('Enter the expected return on the S&P 500:  '))
beta = float (input ('Enter the beta value:  '))
risk_free_rate = float(input ('Enter the current risk free rate. Use the rate of current treasury bills:  '))
growth_rate = float(input ('Enter the anticipated growth rate:  '))
last_dividend = float((input ('Enter the dividend payout for the company:  ')))
market_cap_rate = risk_free_rate + beta*(expected_return - risk_free_rate)
valuation = last_dividend/(market_cap_rate - growth_rate)

def judge_stock(): 
    if valuation < current_stock_price:
        print (stock + ' Stock is OVERVALUED')
        print (valuation)
    elif valuation > current_stock_price:
            print (stock + ' Stock is UNDERVALUED')
            print (valuation)
    else:
            print (stock + ' Stock is at fair value')
            print (valuation)

judge_stock()

