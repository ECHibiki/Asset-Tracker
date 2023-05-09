# matplotlib == easy and flexible, lots of docs
# pyqtgraph == performant and animations, lots of flexibility

## Mon
# T1: Acquire the data from sources
# T1: Alter the view with the data
# T1: table.sortByColumn(0, Qt.AscendingOrder)
# T1: Graph labels

## Tue
# T2: Add volume data to plot as overlapping bar graph
    # MultiplePlotAxes.py
    # https://stackoverflow.com/questions/70435112/pyqtgraph-stacked-bar-graph
# T2: Add a tangent mode when right clicking on the plot 
    # InfiniteLine 
    # https://stackoverflow.com/questions/64564469/how-to-get-mouse-cursor-coordinates-on-a-pyqtgraph-widget
# T2: Hover over datapoints or bar for raw info 
    # https://pyqtgraph.readthedocs.io/en/latest/api_reference/graphicsItems/plotdataitem.html
    # setCurveClickable
    # PlotCurveItem

## Wed
# T3: Bezier spline or linear interpolation toggle
# T3: Candlestick mode
# T3: matplotlib-basemap HQ map window with price as positions

## Thu
# T4: matplotlib $ plot interactive mode
# T4: Graph Lables
# T4: Curve hover 
# T4: Line
 
import aiohttp
import asyncio
import threading
import datetime
import re
import random
import numpy as np
import yfinance as yf
import pyqtgraph as pg

from PySide6.QtCore import QDate

class Model:
    def __init__(self):
        self.data_list = dict()
        # Set or create a default of 7 days
        self.end_date = self.createWorkDay( self.datetimeTuple( datetime.date.today() ) )
        self.start_date = self.createWorkDay( self.datetimeTuple( datetime.date.today() + datetime.timedelta(days= -7 )  ) )
        self.first_day_unset = True

    def link(self, controller):
        self.controller = controller

    def datetimeTuple(self, base):
        return (base.year, base.month, base.day)
    def tupleToQDate(self, t):
        q = QDate()
        q.setDate(*t)
        return q

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
        date = date.toPython()
        potential_date = self.tupleToQDate(self.createWorkDay( self.datetimeTuple( date ) ))
        if self.first_day_unset :
            self.controller.setViewFirstDate( potential_date )
        else:
            self.controller.setViewSecondDate( potential_date )
        self.first_day_unset = not self.first_day_unset

    def setDateRange(self, start_date: QDate, end_date: QDate):
        # this function should effect the main window in showing new date ranges on relevant data
        # Use a general reference to a dict item
        # Shouldn't extend past today
        # for demo purposes do not alter data on call, but change the plot view and range
        start_date = start_date.getDate()
        end_date = end_date.getDate()
        print(start_date , end_date)
        if end_date < start_date:
            start_date , end_date = end_date , start_date
        self.start_date = self.createWorkDay(  start_date  )
        self.end_date = self.createWorkDay(  end_date   )
        self.setMainData()   
        self.controller.closeViewItem("RangeButton")

    def openSymbols(self):
        self.controller.openViewItem("SymbolButton")
    def openDates(self):
        self.controller.openViewItem("RangeButton")
        self.controller.setViewFirstDate( self.tupleToQDate(self.start_date) )
        self.controller.setViewSecondDate( self.tupleToQDate(self.end_date) )
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
        symbol_list = re.split("\s|," , symbols)
        thread_list = []
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

                thread_list.append(threading.Thread(target=self.buildData,args=(symbol,)))
        for thread in thread_list:
            thread.start()
        for thread in thread_list:
            thread.join()
        self.setMainData()
        self.controller.closeViewItem("SymbolButton")

    async def sendRequest(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get( url ) as response:
                self.controller.setRequestData( str(response.status) )

    def buildData(self, symbol):
        try:
            print( symbol)
            ticker = yf.Ticker(symbol) 
            i = ticker.info
            for key, info in i.items() :
                if isinstance(info , dict) or isinstance(info , list):
                    pass
                else:
                    self.data_list[symbol]["advanced"][key] = info
            h = ticker.history(period="3mo") # gets 3 months of daily data with weekends excluded
            for _, history in h.iterrows():
                self.data_list[symbol]["day"].append( self.dateToAxisString(history.name.to_pydatetime()) )
                self.data_list[symbol]["open"].append(history.Open)
                self.data_list[symbol]["high"].append(history.High)
                self.data_list[symbol]["low"].append(history.Low)
                self.data_list[symbol]["close"].append(history.Close)
                self.data_list[symbol]["volume"].append(history.Volume)
            
            r = random.randint(0, 255)
            g = random.randint(0, 255)
            b = random.randint(0, 255)

            # Combine the values into a hex color code
            color_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
            self.data_list[symbol]["color"] = pg.mkPen(width=2,color=color_code,foreground=color_code,background=color_code,brush=color_code)
        except:
            del self.data_list[symbol]
            print("Symbol err", symbol)

    # 2023-05-04 00:00:00-04:00
    def dateToAxisString(self, date):
        return str(date.month) + "/" + str(date.day)


# TIME INTERVAL NOT SET

    def buildPlotData(self):
        # from the dataset return a new set of plot points over the time interval
        plot_data = dict()
        yesterday = dict()
        for symbol, data in self.data_list.items( ):
            plot_data[symbol] =  {"close": [] , "open": [] , "high": [] , "low": [] , "vol": [], "style": data["color"] }
            c = 0
            for i , close in enumerate(data["close"]):
                if len(yesterday) == 0:
                    yesterday["close"] = close 
                    yesterday["open"] =  data["open"][i] 
                    yesterday["high"] =  data["high"][i] 
                    yesterday["low"] =  data["low"][i] 
                    yesterday["volume"] =  data["volume"][i] 
                elif not self.inTimeRange(data["day"][i]):
                    yesterday["close"] = close
                    yesterday["open"] =  data["open"][i] 
                    yesterday["high"] =  data["high"][i] 
                    yesterday["low"] =  data["low"][i] 
                    yesterday["volume"] =  data["volume"][i] 
                else:
                    plot_data[symbol]["close"].append( self.percentDifference( close , yesterday["close"] ) * 100 )
                    plot_data[symbol]["open"].append( self.percentDifference( data["open"][i]  , yesterday["open"] ) * 100 )
                    plot_data[symbol]["high"].append( self.percentDifference( data["high"][i]  , yesterday["high"] ) * 100 )
                    plot_data[symbol]["low"].append( self.percentDifference( data["low"][i]  , yesterday["low"] ) * 100 )
                    plot_data[symbol]["vol"].append( self.percentDifference( data["volume"][i] , yesterday["volume"] ) * 100 )
                    
                    yesterday["close"] = close
                    yesterday["open"] =  data["open"][i] 
                    yesterday["high"] =  data["high"][i] 
                    yesterday["low"] =  data["low"][i] 
                    yesterday["volume"] =  data["volume"][i] 
                    c  = c  + 1
        return plot_data
    def buildDollarData(self):
        percent_list = dict()
        for symbol, data in self.data_list.items( ):
            percent_list[symbol] = "${:,.2f}".format(data["close"][-1])
        return percent_list 
    def buildAdvancedData(self):
        adv_list = dict()
        for symbol, data in self.data_list.items( ):
            adv_list[symbol] = data["advanced"]
        return adv_list

    def buildXAxis(self):
        s = datetime.date(*self.start_date)
        e = datetime.date(*self.end_date)
        axis = []
        while s <= e:
            i = s
            if i.weekday() < 5:
                axis.append( str(i.month) + "/" + str(i.day) )
            s = s + datetime.timedelta( days=+1 )
        return axis 

    def setMainData(self):
        self.controller.setMainData(self.buildPlotData() , self.buildDollarData() , self.buildAdvancedData() , self.buildXAxis() )

    def percentDifference(self, a , b):
        return (a - b) / b
    
    def inTimeRange(self, time):
        # MM/DD
        
        start = datetime.date(*self.start_date)
        end = datetime.date(*self.end_date)

        time = time.split("/")
        time = datetime.date(2023, int(time[0]), int(time[1]))
        return start <= time <= end