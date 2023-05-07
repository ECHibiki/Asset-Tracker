# T1: Acquire the data from sources
# T1: Alter the view with the data
# T1: Bar chart labels

# T2: Add a tangent mode when right clicking on the plot
# T2: Add volume data to plot as overlapping bar graph
# T2: Hover over datapoints or bar for raw info

# T3: Candlestick and/or line
# T3: Bezier spline or linear interpolation toggle
# T3: HQ map window with price as positions

# T4: Resize issues
# T4: .exe
 
# data structures numpy
# asyncio/aiohttp to yahoo and update view on timer

import aiohttp
import asyncio
import re
import numpy as np
import yfinance as yf

class Model:
    def __init__(self):
        self.data_list = dict()
        # Set or create a default of 1 week
        self.start_date = ""
        self.end_date = ""
        pass
    def link(self, controller):
        self.controller = controller
        pass

    # When data fetching is needed create an asyncio action    
    # if a window is closed then related functions should not execute. 
    # Class needs these handlers

    def openSymbols(self):
        self.controller.openViewItem("SymbolButton")
    def openDates(self):
        self.controller.openViewItem("RangeButton")
        self.controller.setViewFirstDate( self.start_date )
        self.controller.setViewSecondDate( self.end_date )
    def openQuery(self):
        self.controller.openViewItem("RequestsButton")
    def openAdvanced(self):
        self.controller.openViewItem("ThreeDButton")

    def clearSymbolVars(self):
        pass
    def clearDatesVars(self):
        pass
    def clearQueryVars(self):
        pass
    def clearAdvancedVars(self):
        pass

    def newSymbolList(self, symbols:str):
        # this function should effect the main window in showing new symbols to display
        # Use a general reference to a dict item
        symbol_list = re.split("(\s|,)" , symbols)
        for symbol in symbol_list:
            if symbol not in self.data_list:
                self.data_list[symbol] = dict({
                    "day": [], # datestamp
                    "open": [], 
                    "high": [], 
                    "low": [], 
                    "close": [], 
                    "volume": [], 
                    "advanced": dict(), # a long list of company data, trimmed to only non-array/dict data of 100char in len
                })
                self.buildData(symbol)

    def addDateItem(self, date):
        # check where the date should be opened
        # deny if past relevant date
        pass

    def setDateRange(self, start_date, end_date):
        # this function should effect the main window in showing new date ranges on relevant data
        # Use a general reference to a dict item
        # Shouldn't extend past today
        # for demo purposes do not alter data on call, but change the plot view and range
        pass

    def sendRequest(self, url):
        pass

    def buildData(self, symbol):
        # msft = yf.Ticker("MSFT") gets microsoft
        # msft.info gets a ton of stuff
        # msft.history(period="3mo") gets 3 months of daily data with weekends excluded
        # chart will only use a week
        pass