# This Python file uses the following encoding: utf-8
import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl

from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow
from PySide6.QtGui import QVector3D

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

class View:
    def __init__(self):
        pass
    def link(self, controller):
        self.controller = controller

    def start(self):
        app = QApplication(sys.argv)
        widget = MainWidget(controller=self.controller)
        # symbols = Ui_NewSymbols.SymbolWidget(controller=self.controller)
        # dates = Ui_Dates.DatesWidget(controller=self.controller)
        # q = Ui_Query.QueryWidget(controller=self.controller)
        # adv = Ui_Advanced.AdvancedWidget(controller=self.controller)

        widget.show()

        # symbols.show()
        # dates.show()
        # q.show()
        # adv.show()
        app.exec()

class MainWidget(QWidget):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.controller = controller

        self.ui.PercentPerformancePlot.setLimits(xMin=-0.1, xMax=8, minXRange=1, yMin=0, yMax=100)
        self.ui.PercentPerformancePlot.setRange(xRange=(0,5,) , yRange=(0,5,))
        self.ui.PercentPerformancePlot.showGrid(x = True, y = True, alpha = 0.2)

        ticks = [list(zip(range(8), ( 'a', 'b', 'c', 'd', 'e','f','g', 'h' )))]
#        You can get an existing AxisItem of a PlotWidget like so:
        xax = self.ui.PercentPerformancePlot.getAxis('bottom')
#        And finally set the ticks of the axis like so:
        xax.setTicks(ticks)

    def closeEvent(self, event):
        print("closeEvent")

    def openSettingsItem(self):
        self.controller.print(self.sender().objectName())


class SymbolWidget(QDialog):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_NewSymbols()
        self.ui.setupUi(self)
        self.controller = controller

    def addSymbols(self):
        self.controller.print(self.ui.SymbolList.toPlainText())

class DatesWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Dates()
        self.ui.setupUi(self)
        self.controller = controller

        self.is_start = True

    def dateEffector(self, date):
        # Set in the perscribed position
        # If selected dates before other then swap, next action will be an end setters
        # Else set in true location
        self.controller.print(date)

    def submitDate(self):
        self.controller.print(self.ui.StartDate.date(), self.ui.EndDate.date())

class QueryWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Query()
        self.ui.setupUi(self)
        self.controller = controller

    def sendRequest(self):
        self.controller.print(self.sender())

class AdvancedWidget(QMainWindow):
    def __init__(self, parent=None, controller=None):
        super().__init__(parent)
        self.ui = Ui_Advanced()
        self.ui.setupUi(self)
        self.controller = controller
        ## create three grids, add each to the view
        xgrid = gl.GLGridItem()
        axe = gl.GLAxisItem(QVector3D(20,20,20))
        self.ui.graphicsView.addItem(xgrid)
        self.ui.graphicsView.addItem(axe)
