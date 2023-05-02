# This Python file uses the following encoding: utf-8
import sys
import pyqtgraph
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

class SymbolWidget(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_symbols.Ui_NewSymbols()
        self.ui.setupUi(self)

class DatesWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_dates.Ui_Dates()
        self.ui.setupUi(self)

class QueryWidget(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = ui_query.Ui_Query()
        self.ui.setupUi(self)

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
