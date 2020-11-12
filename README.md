# pythonproject
2020 Python Class Project for Code Louisville

Overview

This project is an "app" that can be used to determine if a stock is overvalued, undervalued, or at fair value using the Dividend Growth Model and CAPM model.
It also provides the user with the latest recommendations from the current month for purchasing the stock. 
The user has the ability to save the stock to their "favorites list."  The favorites list is displayed to the user before and after being prompted. 
If the stock is saved, additional comprehensive data is written into the favorites.csv file.


How it works   

Stock data that is used to make the relevant calcuations is retrieved from the yahoo finance API, yfinance.

Datetime is used to grab the current date, which is used to ensure only relevant data (recommendations) is displayed to the user and that
the calcuations (dividend growth calculation) is accurate. 

A while loop is used to allow the program to continue to run, so the user can continue to evaluate stocks and add to their favorites list. 
The user can choose to break out of the loop, by keying in "exit".

The "app" takes 2 inputs from the user (the stock ticker and current stock price) and then automatically makes the calcuations by grabbing the data needed
from the Yahoo Finance API, yfinance.  

The app has a series of error-handling checks to prevent adding of invalid stocks to the favorite list, to handle invalid stock ticker entries by informing
the user of the error and prompting the user to retry, and notifying the user if the model used cannot be used/inaccurate (which occurs if the stock does
not pay out dividends or is a high growth stock).  However, the high growth stock (negative valuation), continues the valuation but displays the disclaimer.
Another error-handling check is used to notify the user if there are no recent recommendations within the current month.  
If an ticker entry is invalid, the user will be prompted to enter in the stock ticker again (or they can exit). 

Only if the stock is a valid stock, the app will ask the user if they would like to add the stock to their favorites list.  If the user types "y", 
the ticker symbol is added to the favorites list and significant data (taken from the API) about the stock is alphabetized, formatted, and written into
the favorites csv file.  If the user enters "n", then nothing will be written and the user will continue on to enter the next stock they would like to evaluate or exit. 


Features included

1. "Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program" :
	This is done by the while True loop and the break if the user enters "exit".

2. "Create a dictionary or list, populate it with several values, retrieve at least one value, and use it in your program":
	This is done by the creation of the favorites list.  If any stock tickers are already in the list, the program will not ask to add it.  
	Items (and related data )in the list are written into the csv file. 

3. "Create and call at least 3 functions, at least one of which must return a value that is used":
	There are 4 functions used. The judge_stock function returns value (overvalue, undervalue, fair value ) which is displayed to the user. 

4. "Connect to an external/3rd party API and read data into your app":
	The yfinance API is used. Data is extracted from this API and used to make calculations, display relevant inforamtion, 
	and organized and formatted into the csv file if added to the favorites list.  

5. "Calculate and display data based on an external factor (ex: get the current date, and display how many days remaining until some event)"
	Datetime is used to get the current date. The current date is used to calculate what was the prior year and what was the year 2 years ago.
	These years are used to pull information from the API regarding dividends to make the dividend growth rate calculation. 
	Datetime is also used to extract and display only recommendations that are within the current month to the user if available. 

6. "Other features can be added to this list - just ask if your project needs something specific and as long as it’s a good demonstration of your programming skills, 
   it almost certainly will count!":
	The data taken from the API is sorted and formatted and written to the favorites.csv file for easy viewing. 


Suggestions on how to run

*Program requires Python 3.8 or numpy 1.19.3 - Python 3.9.0 or numpy 1.19.4 will result in an error*

1. pip install yfinance
2. Download the python file and the csv file.
3. Run the program in your console/terminal.
4. Suggestions for stocks: CLX, MSFT, T, DIS (these will produce different results based on error-handling and calculations).
5. Follow the prompts (enter any number for current stock price).
6. Add to favorites list by following prompt and view favorities.csv file.
7. Try entering an invalid stock ticker to test error handling (ie. FJFKLH)
8. Try not entering a stock in the favorites list by typing "n" and then check the favorites.csv file to see that it did NOT add data. 
9. Try exiting the program by entering "exit" when prompted.

	
Thank you!, 

Shinesa Chowdhury




