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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QHeaderView,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTableWidget, QTableWidgetItem, QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(544, 522)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(100, 0))
        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(0, 0, 541, 41))
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
        self.horizontalLayoutWidget.setGeometry(QRect(0, 3, 531, 30))
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

        self.RangeButton = QPushButton(self.horizontalLayoutWidget)
        self.RangeButton.setObjectName(u"RangeButton")
        icon1 = QIcon()
        iconThemeName = u"x-office-calendar"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.RangeButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.RangeButton)

        self.RequestsButton = QPushButton(self.horizontalLayoutWidget)
        self.RequestsButton.setObjectName(u"RequestsButton")
        self.RequestsButton.setEnabled(True)
        icon2 = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.RequestsButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.RequestsButton)

        self.ThreeDButton = QPushButton(self.horizontalLayoutWidget)
        self.ThreeDButton.setObjectName(u"ThreeDButton")
        icon3 = QIcon()
        iconThemeName = u"image-x-generic"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.ThreeDButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.ThreeDButton)

        self.MapButton = QPushButton(self.horizontalLayoutWidget)
        self.MapButton.setObjectName(u"MapButton")
        icon4 = QIcon(QIcon.fromTheme(u"emblem-photos"))
        self.MapButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.MapButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(0, 355, 545, 167))
        self.AdvancedTable = QTableWidget(self.groupBox_2)
        self.AdvancedTable.setObjectName(u"AdvancedTable")
        self.AdvancedTable.setGeometry(QRect(0, 20, 545, 148))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.AdvancedTable.sizePolicy().hasHeightForWidth())
        self.AdvancedTable.setSizePolicy(sizePolicy2)
        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(373, 42, 171, 309))
        self.SimpleTable = QTableWidget(self.groupBox_3)
        self.SimpleTable.setObjectName(u"SimpleTable")
        self.SimpleTable.setGeometry(QRect(0, 18, 172, 291))
        self.SimpleTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.SimpleTable.horizontalHeader().setVisible(True)
        self.SimpleTable.horizontalHeader().setDefaultSectionSize(83)
        self.SimpleTable.verticalHeader().setVisible(False)
        self.SimpleTable.verticalHeader().setHighlightSections(True)
        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(0, 41, 371, 311))
        self.PercentPerformancePlot = PlotWidget(self.groupBox_4)
        self.PercentPerformancePlot.setObjectName(u"PercentPerformancePlot")
        self.PercentPerformancePlot.setGeometry(QRect(0, 19, 371, 291))
        self.pushButton = QPushButton(self.groupBox_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(130, 3, 54, 14))
        icon5 = QIcon(QIcon.fromTheme(u"application-x-executable"))
        self.pushButton.setIcon(icon5)

        self.retranslateUi(Widget)
        self.SymbolButton.clicked.connect(Widget.openSettingsItem)
        self.RequestsButton.clicked.connect(Widget.openSettingsItem)
        self.RangeButton.clicked.connect(Widget.openSettingsItem)
        self.ThreeDButton.clicked.connect(Widget.openSettingsItem)

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
        self.RangeButton.setToolTip(QCoreApplication.translate("Widget", u"Dates", None))
#endif // QT_CONFIG(tooltip)
        self.RangeButton.setText("")
#if QT_CONFIG(tooltip)
        self.RequestsButton.setToolTip(QCoreApplication.translate("Widget", u"Time Interval", None))
#endif // QT_CONFIG(tooltip)
        self.RequestsButton.setText("")
#if QT_CONFIG(tooltip)
        self.ThreeDButton.setToolTip(QCoreApplication.translate("Widget", u"3D Chart", None))
#endif // QT_CONFIG(tooltip)
        self.ThreeDButton.setText("")
#if QT_CONFIG(tooltip)
        self.MapButton.setToolTip(QCoreApplication.translate("Widget", u"Map View", None))
#endif // QT_CONFIG(tooltip)
        self.MapButton.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Symbol Details", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Todays $ Value", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"Daily % Performance", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"Mode", None))
    # retranslateUi

