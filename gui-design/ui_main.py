# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QGroupBox, QHBoxLayout,
    QHeaderView, QLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QTableView, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(541, 490)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(100, 0))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 541, 51))
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy1)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush4 = QBrush(QColor(255, 255, 220, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush5 = QBrush(QColor(0, 0, 0, 127))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        brush6 = QBrush(QColor(239, 239, 239, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        brush7 = QBrush(QColor(202, 202, 202, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        brush8 = QBrush(QColor(159, 159, 159, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        brush9 = QBrush(QColor(184, 184, 184, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        brush10 = QBrush(QColor(118, 118, 118, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        brush11 = QBrush(QColor(247, 247, 247, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        brush13 = QBrush(QColor(177, 177, 177, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.groupBox.setPalette(palette)
        self.groupBox.setAutoFillBackground(True)
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 10, 531, 31))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.SymbolButton = QPushButton(self.horizontalLayoutWidget)
        self.SymbolButton.setObjectName(u"SymbolButton")
        icon = QIcon()
        iconThemeName = u"emblem-symbolic-link"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.SymbolButton.setIcon(icon)

        self.horizontalLayout.addWidget(self.SymbolButton)

        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        iconThemeName = u"x-office-calendar"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        icon2 = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_2.setIcon(icon2)

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon3 = QIcon()
        iconThemeName = u"image-x-generic"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.pushButton_3.setIcon(icon3)

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.graphicsView = PlotWidget(Widget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 50, 361, 291))
        self.scrollArea = QScrollArea(Widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(0, 350, 541, 141))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush14 = QBrush(QColor(222, 221, 218, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush15 = QBrush(QColor(238, 238, 236, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush15)
        brush16 = QBrush(QColor(111, 110, 109, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush16)
        brush17 = QBrush(QColor(148, 147, 145, 255))
        brush17.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush17)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush14)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush15)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush8)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush10)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush15)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush17)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush16)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush14)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush11)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush12)
#endif
        self.scrollArea.setPalette(palette1)
        self.scrollArea.setAutoFillBackground(True)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 525, 125))
        self.tableView = QTableView(self.scrollAreaWidgetContents)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(0, 0, 531, 192))
        self.tableView.setAutoFillBackground(False)
        self.tableView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.tableView.setGridStyle(Qt.SolidLine)
        self.tableView.setSortingEnabled(False)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollArea_2 = QScrollArea(Widget)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setGeometry(QRect(370, 50, 171, 291))
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 155, 289))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Asset Tracker Prototype", None))
        self.groupBox.setTitle("")
#if QT_CONFIG(tooltip)
        self.SymbolButton.setToolTip(QCoreApplication.translate("Widget", u"Symbols", None))
#endif // QT_CONFIG(tooltip)
        self.SymbolButton.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate("Widget", u"Dates", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("Widget", u"Time Interval", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText("")
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("Widget", u"3D Chart", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText("")
    # retranslateUi

