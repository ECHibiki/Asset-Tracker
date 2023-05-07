# T1: Acquire the data from sources
# T1: Alter the view with the data
# T1: Bar chart labels

# T2: Add a tangent mode when right clicking on the plot
# T2: Add volume data to plot as overlapping bar graph
# T2: Hover over datapoints or bar for raw info

# T3: Candlestick and/or line
# T3: Bezier spline or linear interpolation toggle
# T3: HQ map window with price as positions

# T4: Buffering icon
# T4: Resize issues
# T4: .exe
 
# data structures numpy
# asyncio/aiohttp to yahoo and update view on timer

import aiohttp
import asyncio
import datetime
import re
import numpy as np
import yfinance as yf

class Model:
    def __init__(self):
        self.data_list = dict()
        # Set or create a default of 7 days
        self.start_date = self.createWorkDay( self.datetimeTuple( datetime.date.today() ) )
        self.end_date = self.createWorkDay( self.datetimeTuple( datetime.date.today() + datetime.timedelta(days= -7 )  ) )
        self.first_day_unset = True
        
    def link(self, controller):
        self.controller = controller
        

    def datetimeTuple(self, base):
        return (base.year, base.month, base.day)

    def createWorkDay(self, date_tuple):
        if datetime.date(*date_tuple).weekday() < 5:
            return date_tuple
        else:
            date_obj = datetime.date(*date_tuple)
            days_until_workday = (5 - date_obj.weekday()) - 1   # Calculate days until the next Monday
            next_workday_obj = date_obj + datetime.timedelta(days=days_until_workday)  # Calculate the next workday
            next_workday_tuple = (next_workday_obj.year, next_workday_obj.month, next_workday_obj.day)  # Convert the next workday to a tuple
            return next_workday_tuple

    def addDateItem(self, date):
        if self.first_day_unset :
            potential_start_date = self.createWorkDay( self.datetimeTuple( date ) )
            self.controller.setViewFirstDate( potential_start_date )
        else:
            potential_end_date = self.createWorkDay( self.datetimeTuple( date ) )
            self.controller.setViewSecondDate( potential_end_date )
        self.first_day_unset = not self.first_day_unset

    def setDateRange(self, start_date, end_date):
        # this function should effect the main window in showing new date ranges on relevant data
        # Use a general reference to a dict item
        # Shouldn't extend past today
        # for demo purposes do not alter data on call, but change the plot view and range
        self.start_date = self.createWorkDay( self.datetimeTuple( start_date ) )
        self.end_date = self.createWorkDay( self.datetimeTuple( end_date  ) )
        self.setMainData()   

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
            if symbol == "":
                pass
            elif symbol not in self.data_list:
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
        self.setMainData()

    async def sendRequest(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get( url ) as response:
                self.controller.setRequestData( response.status )

    def buildData(self, symbol):
        ticker = yf.Ticker(symbol) 
        i = ticker.info

        for key, info in i.items() :
            if isinstance(info , dict) or isinstance(info , list):
                pass
            else:
                self.buildData[symbol]["advanced"][key] = info

        h = ticker.history(period="3mo") # gets 3 months of daily data with weekends excluded
        for _, history in h.iterrows():
            self.data_list[symbol]["day"].push( self.dateToAxisString(history.name) )
            self.data_list[symbol]["open"].push(history.Open)
            self.data_list[symbol]["high"].push(history.High)
            self.data_list[symbol]["low"].push(history.Low)
            self.data_list[symbol]["close"].push(history.Close)
            self.data_list[symbol]["volume"].push(history.Volume)

    # 2023-05-04 00:00:00-04:00
    def dateToAxisString(datestr):
        d = datestr.split(" ")
        if len(d) < 1 :
            print("Strange date entered def dateToAxisString(datestr)")
            return datetime.date.today().month + "/" + datetime.date.today().day()
        d = d[0].split("-")
        if len(d < 3):
            print("Strange dash split def dateToAxisString(datestr)")
            return datetime.date.today().month + "/" + datetime.date.today().day()
        return d[1] + "/" + d[2]


# TIME INTERVAL NOT SET

    def buildPlotData(self):
        # from the dataset return a new set of plot points over the time interval
        plot_data = dict()
        yesterday = 0
        for symbol, data in self.data_list.items( ):
            plot_data[symbol] = dict()
            for i , close in enumerate(data["close"]):
                if yesterday == 0:
                    yesterday = close 
                elif not self.inTimeRange(data["day"][i]):
                    yesterday = close
                else:
                    plot_data[symbol]["xaxis"].append(data["day"][i])
                    plot_data[symbol]["x"].append( i )
                    plot_data[symbol]["y"].append( self.percentDifference( close , yesterday ) * 100 )
                    yesterday = close
        pass
    def buildPercentData(self):
        percent_list = dict()
        for symbol, data in self.data_list.items( ):
            percent_list[symbol] = ( 100 * self.percentDifference(data["close"][-1] , data["close"][-2]) ) + "%"
        return percent_list 
    def buildAdvancedData(self):
        adv_list = dict()
        for symbol, data in self.data_list.items( ):
            adv_list[symbol] = data["advanced"]
        return adv_list

    def setMainData(self):
        self.controller.setMainData(self.buildPlotData() , self.buildPercentData() , self.buildAdvancedData() )

    def percentDifference(a , b):
        return (a - b) / b
    
    def inTimeRange(self, time):
        # MM/DD
        
        start = datetime.date(*self.start_date)
        end = datetime.date(*self.end_date)

        time = time.split("/")
        time = datetime.date(2023, *time)
        return start <= time <= end