# This Python file uses the following encoding: utf-8
import sys
import pyqtgraph as pg
import pyqtgraph.opengl as gl

import numpy as np
import random
import scipy

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.io.shapereader as shrp
import cartopy



from PySide6.QtWidgets import QApplication, QWidget, QDialog, QMainWindow , QTableWidgetItem, QVBoxLayout
from PySide6.QtGui import QVector3D, QPainter
from PySide6.QtCore import QDate, Qt

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
        pg.setConfigOptions(antialias=True)
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
    def createMapWidget(self, dataset):
        self.map = MapForm(controller=self.controller)
        self.map.show()
        self.map.plotMap(dataset)
    def createDollarWidget(self, dataset):
        self.dlr = DollarForm(controller=self.controller)
        self.dlr.show()
        self.dlr.plotCandles(dataset)
        pass

    def closeSymbolWidget(self):
        self.symbols = None
    def closeDatesWidget(self):
        self.dates = None
    def closeQueryWidget(self):
        self.q = None
    def closeAdvancedWidget(self):
        self.adv = None
    def closeMapWidget(self):
        pass
    def closeDollarWidget(self):
        pass

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
        xax.setTicks(ticks)
        xax.setLabel("Month/Day")

        yax = self.ui.PercentPerformancePlot.getAxis('left')
        yax.setLabel("Percent Value Change")
        
        self.p1 = self.ui.PercentPerformancePlot.plotItem
        self.volume_plot = pg.ViewBox()
        self.p1.showAxis('right')
        self.p1.scene().addItem(self.volume_plot)
        self.p1.getAxis('right').linkToView(self.volume_plot)
        self.volume_plot.setXLink(self.p1)
        self.p1.getAxis('right').setLabel('Percent Volume Change')

        self.volume_plot.setRange(xRange=(0,5,) , yRange=(-10,10,))

        self.updateViews()
        self.p1.vb.sigResized.connect(self.updateViews)


        hour = [0, 1,2,3,4,5,6,7,8,9,10]
        temperature = [0, 20,12,34,12,33,11,29,12,35,25]
        # plot data: x, y values

        scatter = pg.ScatterPlotItem(hour , temperature , symbol="t", size=15, brush='blue')
        self.ui.PercentPerformancePlot.addItem(scatter)

        ppol = scipy.interpolate.CubicSpline( hour , temperature )
        pt = []
        for i in range(100):
            pt.append(i / 10)
        self.ui.PercentPerformancePlot.plot(pt, ppol(pt) , brush="blue")

        

        hour = [0, 1.5,2.5,3,4.5,5,6.5,7,8,9,10]
        temperature = [40, 50,42,44,42,43,41,39,42,45,55]
        temperature.reverse()
        l =self.ui.PercentPerformancePlot.plot(hour, temperature,symbol='s', pen=pg.mkPen(width=2))
        l.setCurveClickable(True, width=10)
        l.sigClicked.connect(self.labelPoint)
        # l.setZValue(10)
        # print(l.childItems()[0].clickable)
        # l.childItems()[0].sigClicked.connect(self.labelPoint)

        # object_methods = [method_name for method_name in dir(l)
        #           if callable(getattr(l, method_name))]
        # print(object_methods)
        
        bg = pg.BarGraphItem(x=range(5), height=[1,5,2,4,3], width=0.5)
        self.volume_plot.addItem(bg)

        proxy = self.p1.scene().sigMouseClicked.connect(self.drawLine)
        # proxy = self.p1.scene().sigPointsHovered.connect(self.labelPoint)
        self.sp = []

    def toggleInterpolation(self):
        self.controller.setInterpolation()

    def labelPoint(self , pt, mclk):
        print(self, pt, mclk)
        if not mclk.double():
            if hasattr(self, "value_label"):
                self.ui.PercentPerformancePlot.removeItem(self.value_label)
            mousePoint = self.p1.vb.mapSceneToView(mclk.scenePos())
            print (mousePoint.x() , mousePoint.y())
            # print (pt.setClipToView(False) , pt.setClipToView(True))
            self.value_label = pg.TextItem( "({:,.2f},{:,.2f})".format((mousePoint.x()), (mousePoint.y()) ) , color="red", fill="#00000033") 
            self.ui.PercentPerformancePlot.addItem(self.value_label)
            self.value_label.setPos(mousePoint.x() , mousePoint.y())

    def clearValueLabel(self):
        if hasattr(self, "value_label"):
            self.ui.PercentPerformancePlot.removeItem(self.value_label)
        pass

    def drawLine(self, mclk):
        try:
            if mclk.double():
                self.clearValueLabel()

                mousePoint = self.p1.vb.mapSceneToView(mclk.scenePos())
                angle = 0
                pt_pos = ( mousePoint.x() , mousePoint.y() ,)
                
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)

                # Combine the values into a hex color code
                color_code = "#{:02x}{:02x}{:02x}".format(r, g, b)
                pi = pg.ScatterPlotItem([pt_pos[0]], [pt_pos[1]] , symbol='o', brush=color_code)
                self.sp.append(pi)
                if len(self.sp) > 2:
                    self.ui.PercentPerformancePlot.removeItem(self.sp[0])
                    del self.sp[0]    
                self.ui.PercentPerformancePlot.addItem(pi)
                

                if hasattr(self, "line_p1" ):
                    x = mousePoint.x() - self.line_p1[0]
                    y = mousePoint.y() - self.line_p1[1]
                    h = np.sqrt( x*x + y*y )
                    angle = np.degrees( np.arcsin( y / h) )
                    if x < 0 :
                        angle = angle * -1
                else:
                    self.line_p1 = ( mousePoint.x() , mousePoint.y() ,)


                if mousePoint.x()+1 < self.line_p1[0]:
                    pt_pos = self.line_p1
                
                self.line_p1 = ( mousePoint.x() , mousePoint.y() ,)

                
                if hasattr(self, "inf_line" ):
                    self.p1.vb.removeItem(self.inf_line)
                self.inf_line = pg.InfiniteLine(pt_pos , angle=angle)
                self.p1.vb.addItem(self.inf_line)
        except Exception as e:
            print("Draw line err" , e)
        
    def updateViews(self):
        self.volume_plot.setGeometry(self.p1.vb.sceneBoundingRect())
        
        ## need to re-update linked axes since this was called
        ## incorrectly while views had different shapes.
        ## (probably this should be handled in ViewBox.resizeEvent)
        self.volume_plot.linkedViewChanged(self.p1.vb, self.volume_plot.XAxis)
            
    def closeEvent(self, event):
        self.controller.print("closeEvent")

    def openSettingsItem(self):
        self.controller.openModelItem(self.sender().objectName())

    def plotGraph(self, points):
        # Clear existing plots
        self.ui.PercentPerformancePlot.plotItem.clear()
        self.volume_plot.clear()
        print(points)
        if len(points) == 0:
            return
        mini = 100
        maxi = -100
        vol_mini = 100
        vol_maxi = -100
        count = 0
        for symbol, symbol_data in points.items():

            x = range(len(symbol_data["close"]))
            if min(symbol_data["close"]) < mini:
                mini = min(symbol_data["close"])
            if max(symbol_data["close"]) > maxi:
                maxi = max(symbol_data["close"])
            if min(symbol_data["vol"]) < vol_mini:
                vol_mini = min(symbol_data["vol"])
            if max(symbol_data["vol"]) > vol_maxi:
                vol_maxi = max(symbol_data["vol"])
           
            self.ui.PercentPerformancePlot.addLegend()
            if symbol_data["curve"] == None:
                l = self.ui.PercentPerformancePlot.plot(x, symbol_data["close"], pen=symbol_data["style"], symbol="s" , name=symbol, hoverable=True)
                l.setCurveClickable(True, width=10)
                l.sigClicked.connect(self.labelPoint)
                # l.setZValue(10)
                # l.sigPointsHovered.connect(self.labelPoint)
            else:
                scatter = pg.ScatterPlotItem(x , symbol_data["close"] , symbol="t", pen=symbol_data["style"])
                self.ui.PercentPerformancePlot.addItem(scatter)
                pt = []
                for i in range(len(x) * 10):
                    pt.append( i / 10)    
                self.ui.PercentPerformancePlot.plot(pt, symbol_data["curve"]( pt ) , pen=symbol_data["style"] , name=symbol)
                

            xo = []
            xi = []
            for pos in x:
                xo.append(pos + count)
                xi.append(pos + count + 1 / len(points))
            count = count + 1 / len(points)
            bg = pg.BarGraphItem(x0=xo, x1=xi, height=symbol_data["vol"], pen="black", brush=symbol_data["style"].brush() )
            self.volume_plot.addItem(bg)
      
        self.volume_plot.setRange( yRange=(vol_mini * 2, vol_maxi * 2,))
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
        symb_header = self.ui.SimpleTable.horizontalHeader()
        symb_header.sectionClicked.connect( lambda x : self.ui.SimpleTable.sortByColumn(x, Qt.AscendingOrder) )
# 
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



class MapForm(QMainWindow):
    def __init__(self,controller=None, *args, **kwargs):
        super(MapForm, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.sc = MapWidget(self, width=10, height=10, dpi=100)

        toolbar = NavigationToolbar(self.sc, self)

        layout = QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(self.sc)
        
        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)
        self.controller = controller
        self.show()

    def plotMap(self, dataset):
        resolution = '10m'
        category = 'cultural'
        name = 'admin_0_countries'
        shpfilename = shrp.natural_earth(resolution, category, name)
        reader = shrp.Reader(shpfilename)
        countries = reader.records()

        
        country_power = dict()
        for _, data in dataset.items():
            cn = "ATA"
            if data["advanced"]["country"] == "Canada":
                cn = "CAN"
            elif data["advanced"]["country"] == "United States":
                cn = "USA"    
            print(data["advanced"]["country"])
            if country_power.get(cn) == None:
                country_power[cn] = 0
            country_power[cn] = country_power[cn] + data["close"][-1]
        maxi = max(country_power.values())
    
        print(country_power, maxi)
        weights = dict()
        for count, data in country_power.items():
            weights[count] = (0,0, data / maxi)
        print(weights)
        for country in countries:
            if country.attributes['ADM0_A3'] in weights:

                self.sc.axes.add_geometries(country.geometry, ccrs.PlateCarree(),
                                facecolor=weights[country.attributes['ADM0_A3']],
                                label=country.attributes['ADM0_A3'])
            else:
                self.sc.axes.add_geometries(country.geometry, ccrs.PlateCarree(),
                                facecolor=(0, 1, 0),
                                label=country.attributes['ADM0_A3'])
        pass

class DollarForm(QMainWindow):
    def __init__(self,controller=None, *args, **kwargs):
        super(DollarForm, self).__init__(*args, **kwargs)

        # Create the maptlotlib FigureCanvas object,
        # which defines a single set of axes as self.axes.
        self.sc = PlotWidget(self, width=5, height=4, dpi=100)
        self.sc.axes.plot([0,1,2,3,4], [10,1,20,3,40])

        self.toolbar = NavigationToolbar(self.sc, self)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.toolbar)
        self.layout.addWidget(self.sc)
        
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        self.setCentralWidget(self.widget)
        self.controller = controller
        self.show()

    def plotCandles(self, dataset):
        pass

class MapWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=10):
        fig = Figure(figsize=(width,height), dpi=dpi)
        ax = plt.axes(projection=ccrs.PlateCarree())
        
        self.axes = fig.add_subplot(111, projection=ccrs.PlateCarree())
        # Add map features
        print(type(self.axes))
        self.axes.coastlines()
        self.axes.gridlines()
        self.axes.add_feature(cartopy.cartopy.feature.BORDERS)
        
        

        super(MapWidget, self).__init__(fig)


        # ax = 

        # fig = plt.figure()
        # ax.coastlines()
        # ax.figure.canvas.draw()
        # renderer = fig.canvas.renderer
        # painter = QPainter(self)
        # painter.drawPixmap(0, 0, renderer.toPixmap())

class PlotWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=10):
        fig = Figure()
        self.axes = fig.add_subplot(111)
        super(PlotWidget, self).__init__(fig)

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

        