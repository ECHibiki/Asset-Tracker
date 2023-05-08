import asyncio
import aiohttp

class Controller:
    def __init__(self):
        self.loop = asyncio.get_event_loop()
        pass
    
    def link(self, view, model):
        self.view = view
        self.model = model
        pass

    def print(self, str):
        print(str)

    """
    ------- V -> C -> M -------  
    """

    def openModelItem(self, obj_name):
        if obj_name == "SymbolButton":
            self.model.openSymbols()
        elif obj_name == "RangeButton":
            self.model.openDates()
        elif obj_name == "RequestsButton":
            self.model.openQuery()
        elif obj_name == "ThreeDButton":
            self.model.openAdvanced()
        else:
            print("undefined" , obj_name)
    
    def symbolWidgetClosed(self):
        self.model.clearSymbolVars()
        print("Window Closed")
    def datesWidgetClosed(self):
        self.model.clearDatesVars()
        print("Window Closed")
    def queryWidgetClosed(self):
        self.model.clearQueryVars()
        print("Window Closed")
    def symbolAdvancedClosed(self):
        self.model.clearAdvancedVars()
        print("Window Closed")

    def replaceSymbolList(self, items):
        self.model.newSymbolList(items)
    
    def addDateItem(self, date):
        self.model.addDateItem(date)

    def alterDates(self, start_date, end_date):
        self.model.setDateRange(start_date, end_date)

    def makeRequest(self, url):
        asyncio.run(self.model.sendRequest(url))

    """
    ------- M -> C -> V -------  
    """

    def openViewItem(self, obj_name):
        if obj_name == "SymbolButton":
            self.view.createSymbolWidget()
        elif obj_name == "RangeButton":
            self.view.createDatesWidget()
        elif obj_name == "RequestsButton":
            self.view.createQueryWidget()
        elif obj_name == "ThreeDButton":
            self.view.createAdvancedWidget()
        else:
            print("undefined" , obj_name)
    
    def closeViewItem(self, obj_name):
        if obj_name == "SymbolButton":
            self.view.closeSymbolWidget()
        elif obj_name == "RangeButton":
            self.view.closeDatesWidget()
        elif obj_name == "RequestsButton":
            self.view.closeQueryWidget()
        elif obj_name == "ThreeDButton":
            self.view.closeAdvancedWidget()
        else:
            print("undefined" , obj_name)

    def setViewFirstDate(self, date):
        self.view.dates.setFirstDate(date)
    def setViewSecondDate(self, date):
        self.view.dates.setSecondDate(date)
    
    def setRequestData(self, data):
        self.view.q.setRequestData(data)

    def setMainData(self, plot_data, dollar_data , advanced_data, date_range ):
        self.view.setAxis( date_range)
        self.view.buildDolarTable(dollar_data)
        self.view.buildDetailsTable(advanced_data)
        self.view.buildPlotData(plot_data)
        pass