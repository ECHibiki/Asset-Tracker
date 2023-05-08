# This Python file uses the following encoding: utf-8
import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np
import datetime

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow , QTableWidgetItem
from PySide6.QtGui import QVector3D
from PySide6.QtCore import QDate

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from .ui.ui_main import Ui_Widget
from .ui.ui_symbols import Ui_NewSymbols
from .ui.ui_dates import Ui_Dates
from .ui.ui_query import Ui_Query
from .ui.ui_advanced import Ui_Advanced

# QUERY:  Is this the best way to pass the controller around hmmmm

class WindowManager:
    def __init__(self):
        pass
    def link(self, controller):
        self.controller = controller

    def start(self):
        app = QApplication(sys.argv)
        self.main = MainWidget(controller=self.controller)
        self.main.show()
        app.exec()

    def createSymbolWidget(self):
        self.symbols = SymbolWidget(controller=self.controller)
        self.symbols.show()
    def createDatesWidget(self):
        self.dates = DatesWidget(controller=self.controller)
        self.dates.show()
    def createQueryWidget(self):
        self.q = QueryWidget(controller=self.controller)
        self.q.show()
    def createAdvancedWidget(self):
        self.adv = AdvancedWidget(controller=self.controller)
        self.adv.show()

    def closeSymbolWidget(self):
        self.symbols = None
    def closeDatesWidget(self):
        self.dates = None
    def closeQueryWidget(self):
        self.q = None
    def closeAdvancedWidget(self):
        self.adv = None

    def setAxis(self, axis):
        self.main.setAxis(axis)
    def buildDolarTable(self, dollar_data):
        self.main.setDollarTable(dollar_data)
    def buildDetailsTable(self, advanced_data):
        self.main.setTableDetails(advanced_data)
    def buildPlotData(self, plot_data):
        self.main.plotGraph(plot_data)

class MainWidget(QWidget):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.controller = controller
        self.setFixedSize(self.size())

        self.ui.PercentPerformancePlot.setLimits(xMin=0, xMax=8, minXRange=1, yMin=-100, yMax=100)
        self.ui.PercentPerformancePlot.setRange(xRange=(0,5,) , yRange=(0,100,))
        self.ui.PercentPerformancePlot.showGrid(x = True, y = True, alpha = 0.2)
        
        ticks = [list(zip(range(8), ( '5/9', '5/10', '5/11', '5/12', '5/13','5/14','5/15', '5/16' )))]
#        You can get an existing AxisItem of a PlotWidget like so:
        xax = self.ui.PercentPerformancePlot.getAxis('bottom')
#        And finally set the ticks of the axis like so:
        xax.setTicks(ticks)

        hour = [0, 1,2,3,4,5,6,7,8,9,10]
        temperature = [20, 30,32,34,32,33,31,29,32,35,45]
        # plot data: x, y values
        self.ui.PercentPerformancePlot.plot(hour, temperature)

        hour = [0, 1.5,2.5,3,4.5,5,6.5,7,8,9,10]
        temperature.reverse()
        self.ui.PercentPerformancePlot.plot(hour, temperature)

        
    def closeEvent(self, event):
        self.controller.print("closeEvent")

    def openSettingsItem(self):
        self.controller.openModelItem(self.sender().objectName())

    def plotGraph(self, points):
        # Clear existing plots
        self.ui.PercentPerformancePlot.plotItem.clear()
        print(points)
        if len(points) == 0:
            return
        mini = 100
        maxi = -100
        for symbol, y in points.items():
            x = range(len(y))
            if min(y) < mini:
                mini = min(y)
            if max(y) > maxi:
                maxi = max(y)
            self.ui.PercentPerformancePlot.plot(x, y)
        self.ui.PercentPerformancePlot.setRange( yRange=( mini , maxi, ) )
        pass
    def setAxis(self, axis):
        datalen = len(axis)
        self.ui.PercentPerformancePlot.setLimits(xMin=0, xMax=datalen, minXRange=1, yMin=-100, yMax=100)
        self.ui.PercentPerformancePlot.setRange(xRange=(0,5,) , yRange=(0,100,))

        ticks = [list(zip(range(datalen), axis))]
#        You can get an existing AxisItem of a PlotWidget like so:
        xax = self.ui.PercentPerformancePlot.getAxis('bottom')
#        And finally set the ticks of the axis like so:
        xax.setTicks(ticks)
        
    def setDollarTable(self, dollars):
        self.ui.SimpleTable.setRowCount(0)
        self.ui.SimpleTable.setColumnCount(0)

        self.ui.SimpleTable.setRowCount(len(dollars))
        self.ui.SimpleTable.setColumnCount(2)

        self.ui.SimpleTable.setHorizontalHeaderLabels(["Symbol" , "Value"])
        r = 0
        for symbol, value in dollars.items():
            self.ui.SimpleTable.setItem(r , 0 , QTableWidgetItem(symbol))
            self.ui.SimpleTable.setItem(r , 1 , QTableWidgetItem(value))
            r = r + 1
    def setTableDetails(self, details):
        self.ui.AdvancedTable.setRowCount(0)
        self.ui.AdvancedTable.setColumnCount(0)

        labels = []
        keys = []
        for symbol, data in details.items():
            labels.append(symbol)
            for key, _ in data.items():
                if key not in keys:
                    keys.append(key)

        keys = sorted(keys)
        self.ui.AdvancedTable.setRowCount(len(keys))
        self.ui.AdvancedTable.setColumnCount(len(labels))

        self.ui.AdvancedTable.setVerticalHeaderLabels(keys)
        self.ui.AdvancedTable.setHorizontalHeaderLabels(labels)

        r = 0
        col = 0
        for _, data in details.items():
            r = 0
            for k , detail in sorted(data.items()):
                while len(keys) > r and k != keys[r]:
                    self.ui.AdvancedTable.setItem(r , col , QTableWidgetItem(str("X")))
                    r = r + 1
                    continue
                self.ui.AdvancedTable.setItem(r , col , QTableWidgetItem(str(detail)))
                r = r + 1
            col = col + 1 
        pass


class SymbolWidget(QDialog):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_NewSymbols()
        self.ui.setupUi(self)
        self.controller = controller
        self.setFixedSize(self.size())

    def closeEvent(self, event):
        self.controller.symbolWidgetClosed()

    def addSymbols(self):
        self.controller.replaceSymbolList(self.ui.SymbolList.toPlainText())

class DatesWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Dates()
        self.ui.setupUi(self)
        self.controller = controller
        self.setFixedSize(self.size())

    def closeEvent(self, event):
        self.controller.datesWidgetClosed()

    def dateEffector(self, date: QDate):
        self.controller.addDateItem(date)

    def submitDate(self):
        self.controller.alterDates(self.ui.StartDate.date(), self.ui.EndDate.date())

    def setFirstDate(self, date):
        self.ui.StartDate.setDate(date)
    def setSecondDate(self, date):
        self.ui.EndDate.setDate(date)

class QueryWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Query()
        self.ui.setupUi(self)
        self.controller = controller
        self.setFixedSize(self.size())

    def closeEvent(self, event):
        self.controller.queryWidgetClosed()

    def sendRequest(self):
        self.controller.makeRequest(self.ui.URL.text())
    
    def setRequestData(self, data):
        self.ui.ResponseCode.setText(data)

class AdvancedWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Advanced()
        self.ui.setupUi(self)
        self.controller = controller
        ## create three grids, add each to the view
        # xgrid = gl.GLGridItem()
        # axe = gl.GLAxisItem(QVector3D(20,20,20))
        # self.ui.graphicsView.addItem(xgrid)
        # self.ui.graphicsView.addItem(axe)
        # self.setFixedSize(self.size())

        ## Generate random points
        #https://gist.github.com/markjay4k/da2f55e28514be7160a7c5fbf95bd243
 # create the background grids
        self.traces = dict()
        gx = gl.GLGridItem()
        gx.rotate(90, 0, 1, 0)
        gx.translate(-10, 0, 0)
        self.ui.graphicsView.addItem(gx)
        gy = gl.GLGridItem()
        gy.rotate(90, 1, 0, 0)
        gy.translate(0, -10, 0)
        self.ui.graphicsView.addItem(gy)
        gz = gl.GLGridItem()
        gz.translate(0, 0, -10)
        self.ui.graphicsView.addItem(gz)

        self.n = 50
        self.m = 1000
        self.y = np.linspace(-10, 10, self.n)
        self.x = np.linspace(-10, 10, self.m)
        self.phase = 0

        for i in range(self.n):
            yi = np.array([self.y[i]] * self.m)
            d = np.sqrt(self.x ** 2 + yi ** 2)
            z = 10 * np.cos(d + self.phase) / (d + 1)
            pts = np.vstack([self.x, yi, z]).transpose()
            self.traces[i] = gl.GLLinePlotItem(pos=pts, color=pg.glColor(
                (i, self.n * 1.3)), width=(i + 1) / 10, antialias=True)
            self.ui.graphicsView.addItem(self.traces[i])


    def advancedEvent(self, event):
        self.controller.advancedWidgetClosed()

        