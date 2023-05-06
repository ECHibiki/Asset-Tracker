class Controller:
    def __init__(self):
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
    def datesWidgetClosed(self):
        self.model.clearDatesVars()
    def queryWidgetClosed(self):
        self.model.clearQueryVars()
    def symbolAdvancedClosed(self):
        self.model.clearAdvancedVars()

    def replaceSymbolList(self, items):
        self.model.newSymbolList(items)
    
    def addDateItem(self, date):
        self.model.addDateItem(date)

    def alterDates(self, start_date, end_date):
        self.model.setDateRange(start_date, end_date)

    def makeRequest(self, url):
        self.model.sendRequest(url)

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