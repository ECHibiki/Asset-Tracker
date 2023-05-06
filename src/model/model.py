# T1: Acquire the data from sources
# T2: Alter the view with the data
# T3: Add a tangent mode when right clicking on the plot
# T4: Add volume data to plot
# T5: Hover over datapoints for raw info
# T6: Bezier spline or linear interpolation toggle
# T7: Candlestick or line
# T8: HQ map window with price as positions
# T9: Resize issues
 
# data structures numpy
# asyncio/aiohttp to yahoo and update view on timer

import aiohttp
import asyncio

class Model:
    def __init__(self):
        pass
    def link(self, controller):
        self.controller = controller
        pass

    # When data fetching is needed create an asyncio action    
    # if a window is closed then related functions should not execute. 
    # Class needs these handlers

    def openSymbols(self):
        pass
    def openDates(self):
        pass
    def openQuery(self):
        pass
    def openAdvanced(self):
        pass

    def clearSymbolVars(self):
        pass
    def clearDatesVars(self):
        pass
    def clearQueryVars(self):
        pass
    def clearAdvancedVars(self):
        pass

    def newSymbolList(self, symbols):
        # this function should effect the main window in showing new symbols to display
        # Use a general reference to a dict item
        pass

    def addDateItem(self, date):
        # check where the date should be opened
        pass

    def setDateRange(self, start_date, end_date):
        # this function should effect the main window in showing new date ranges on relevant data
        # Use a general reference to a dict item
        pass

    def sendRequest(self, url):
        pass