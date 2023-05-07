# This Python file uses the following encoding: utf-8
import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
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
        widget = MainWidget(controller=self.controller)
        widget.show()
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

class MainWidget(QWidget):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.controller = controller
        self.setFixedSize(self.size())

        self.ui.PercentPerformancePlot.setLimits(xMin=0, xMax=8, minXRange=1, yMin=0, yMax=100)
        self.ui.PercentPerformancePlot.setRange(xRange=(0,5,) , yRange=(0,100,))
        self.ui.PercentPerformancePlot.showGrid(x = True, y = True, alpha = 0.2)

        ticks = [list(zip(range(8), ( '00:00', '01:00', '02:00', '03:00', '04:00','05:00','06:00', '07:00' )))]
#        You can get an existing AxisItem of a PlotWidget like so:
        xax = self.ui.PercentPerformancePlot.getAxis('bottom')
#        And finally set the ticks of the axis like so:
        xax.setTicks(ticks)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature = [30,32,34,32,33,31,29,32,35,45]
        # plot data: x, y values
        self.ui.PercentPerformancePlot.plot(hour, temperature)

        hour = [1,2,3,4,5,6,7,8,9,10]
        temperature.reverse()
        self.ui.PercentPerformancePlot.plot(hour, temperature)

        
    def closeEvent(self, event):
        self.controller.print("closeEvent")

    def openSettingsItem(self):
        self.controller.openModelItem(self.sender().objectName())

    def plotGraph(self, points):
        # Clear existing plots
        # set axis
        # for each symbol
            # set X
            # set Y
            # self.ui.PercentPerformancePlot.plot
        pass
    def graphPercents(self, perc):
        # clear graph
        # for each symbol
            # set percent
            # asign to index position
        pass
    def tableDetails(self, details):
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
        pass
    def setSecondDate(self, date):
        pass

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
        self.controller.makeRequest(self.ui.URL.text)
    
    def setRequestData(self, data):
        pass

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

        