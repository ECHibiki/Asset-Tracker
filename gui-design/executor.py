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
import ui_main
import ui_symbols
import ui_dates
import ui_query
import ui_advanced

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_main.Ui_Widget()
        self.ui.setupUi(self)

        self.ui.PercentPerformancePlot.setLimits(xMin=-0.1, xMax=8, minXRange=1, yMin=0, yMax=100)
        self.ui.PercentPerformancePlot.setRange(xRange=(0,5,) , yRange=(0,5,))
        self.ui.PercentPerformancePlot.showGrid(x = True, y = True, alpha = 0.2)

        ticks = [list(zip(range(8), ( 'a', 'b', 'c', 'd', 'e','f','g', 'h' )))]
#        You can get an existing AxisItem of a PlotWidget like so:
        xax = self.ui.PercentPerformancePlot.getAxis('bottom')
#        And finally set the ticks of the axis like so:
        xax.setTicks(ticks)



    def openSettingsItem(self):
        print(self.sender().objectName())


class SymbolWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_symbols.Ui_NewSymbols()
        self.ui.setupUi(self)

    def addSymbols(self):
        print(self.ui.SymbolList.toPlainText())

class DatesWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_dates.Ui_Dates()
        self.ui.setupUi(self)

        self.is_start = True;

    def dateEffector(self, date):
        # Set in the perscribed position
        # If selected dates before other then swap, next action will be an end setters
        # Else set in true location
        print(date)

    def submitDate(self):
        print(self.ui.StartDate.date(), self.ui.EndDate.date())

class QueryWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_query.Ui_Query()
        self.ui.setupUi(self)

    def sendRequest(self):
        print(self.sender())

class AdvancedWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_advanced.Ui_Advanced()
        self.ui.setupUi(self)
        ## create three grids, add each to the view
        xgrid = gl.GLGridItem()
        axe = gl.GLAxisItem(QVector3D(20,20,20))
        self.ui.graphicsView.addItem(xgrid)
        self.ui.graphicsView.addItem(axe)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWidget()
    symbols = SymbolWidget()
    dates = DatesWidget()
    q = QueryWidget()
    adv = AdvancedWidget()

    widget.show()
    symbols.show()
    dates.show()
    q.show()
    adv.show()

    sys.exit(app.exec())
