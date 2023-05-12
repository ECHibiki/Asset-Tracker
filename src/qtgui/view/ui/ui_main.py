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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QHeaderView, QLayout, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

from pyqtgraph import PlotWidget

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(731, 647)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Widget.sizePolicy().hasHeightForWidth())
        Widget.setSizePolicy(sizePolicy)
        Widget.setMinimumSize(QSize(100, 0))
        Widget.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(8)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(4, 1, 4, 5)
        self.groupBox_4 = QGroupBox(Widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(117)
        sizePolicy1.setVerticalStretch(59)
        sizePolicy1.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy1)
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.PercentPerformancePlot = PlotWidget(self.groupBox_4)
        self.PercentPerformancePlot.setObjectName(u"PercentPerformancePlot")
        self.PercentPerformancePlot.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(66)
        sizePolicy2.setVerticalStretch(210)
        sizePolicy2.setHeightForWidth(self.PercentPerformancePlot.sizePolicy().hasHeightForWidth())
        self.PercentPerformancePlot.setSizePolicy(sizePolicy2)
        self.PercentPerformancePlot.setMinimumSize(QSize(0, 0))
        self.PercentPerformancePlot.setSizeIncrement(QSize(0, 0))
        self.PercentPerformancePlot.setBaseSize(QSize(0, 53))

        self.verticalLayout.addWidget(self.PercentPerformancePlot)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.InterpolateButton = QPushButton(self.groupBox_4)
        self.InterpolateButton.setObjectName(u"InterpolateButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.InterpolateButton.sizePolicy().hasHeightForWidth())
        self.InterpolateButton.setSizePolicy(sizePolicy3)
        self.InterpolateButton.setMaximumSize(QSize(16777215, 15))
        icon = QIcon()
        iconThemeName = u"application-x-executable"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.InterpolateButton.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.InterpolateButton)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.gridLayout.addWidget(self.groupBox_4, 2, 0, 1, 1)

        self.groupBox_2 = QGroupBox(Widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy4)
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setMaximumSize(QSize(16777215, 160))
        self.gridLayout_4 = QGridLayout(self.groupBox_2)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.AdvancedTable = QTableWidget(self.groupBox_2)
        self.AdvancedTable.setObjectName(u"AdvancedTable")
        sizePolicy.setHeightForWidth(self.AdvancedTable.sizePolicy().hasHeightForWidth())
        self.AdvancedTable.setSizePolicy(sizePolicy)

        self.gridLayout_4.addWidget(self.AdvancedTable, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 3, 0, 1, 2)

        self.groupBox_3 = QGroupBox(Widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(104)
        sizePolicy5.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy5)
        self.groupBox_3.setMaximumSize(QSize(133, 16777215))
        self.gridLayout_3 = QGridLayout(self.groupBox_3)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SimpleTable = QTableWidget(self.groupBox_3)
        if (self.SimpleTable.columnCount() < 2):
            self.SimpleTable.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.SimpleTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.SimpleTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.SimpleTable.setObjectName(u"SimpleTable")
        self.SimpleTable.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.SimpleTable.horizontalHeader().setVisible(True)
        self.SimpleTable.horizontalHeader().setMinimumSectionSize(51)
        self.SimpleTable.horizontalHeader().setDefaultSectionSize(62)
        self.SimpleTable.verticalHeader().setVisible(False)
        self.SimpleTable.verticalHeader().setHighlightSections(True)

        self.gridLayout_3.addWidget(self.SimpleTable, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_3, 2, 1, 1, 1)

        self.groupBox = QGroupBox(Widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(40)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy6)
        self.groupBox.setMinimumSize(QSize(0, 0))
        self.groupBox.setMaximumSize(QSize(16777215, 37))
        self.groupBox.setSizeIncrement(QSize(0, 25))
        self.groupBox.setBaseSize(QSize(0, 0))
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
        self.groupBox.setFlat(False)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(8, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.SymbolButton = QPushButton(self.groupBox)
        self.SymbolButton.setObjectName(u"SymbolButton")
        icon1 = QIcon()
        iconThemeName = u"emblem-symbolic-link"
        if QIcon.hasThemeIcon(iconThemeName):
            icon1 = QIcon.fromTheme(iconThemeName)
        else:
            icon1.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.SymbolButton.setIcon(icon1)

        self.horizontalLayout.addWidget(self.SymbolButton)

        self.RangeButton = QPushButton(self.groupBox)
        self.RangeButton.setObjectName(u"RangeButton")
        icon2 = QIcon()
        iconThemeName = u"x-office-calendar"
        if QIcon.hasThemeIcon(iconThemeName):
            icon2 = QIcon.fromTheme(iconThemeName)
        else:
            icon2.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.RangeButton.setIcon(icon2)

        self.horizontalLayout.addWidget(self.RangeButton)

        self.RequestsButton = QPushButton(self.groupBox)
        self.RequestsButton.setObjectName(u"RequestsButton")
        self.RequestsButton.setEnabled(True)
        icon3 = QIcon()
        iconThemeName = u"list-add"
        if QIcon.hasThemeIcon(iconThemeName):
            icon3 = QIcon.fromTheme(iconThemeName)
        else:
            icon3.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.RequestsButton.setIcon(icon3)

        self.horizontalLayout.addWidget(self.RequestsButton)

        self.ThreeDButton = QPushButton(self.groupBox)
        self.ThreeDButton.setObjectName(u"ThreeDButton")
        icon4 = QIcon()
        iconThemeName = u"image-x-generic"
        if QIcon.hasThemeIcon(iconThemeName):
            icon4 = QIcon.fromTheme(iconThemeName)
        else:
            icon4.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.ThreeDButton.setIcon(icon4)

        self.horizontalLayout.addWidget(self.ThreeDButton)

        self.MapButton = QPushButton(self.groupBox)
        self.MapButton.setObjectName(u"MapButton")
        icon5 = QIcon()
        iconThemeName = u"emblem-photos"
        if QIcon.hasThemeIcon(iconThemeName):
            icon5 = QIcon.fromTheme(iconThemeName)
        else:
            icon5.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.MapButton.setIcon(icon5)

        self.horizontalLayout.addWidget(self.MapButton)

        self.DollarPlot = QPushButton(self.groupBox)
        self.DollarPlot.setObjectName(u"DollarPlot")
        icon6 = QIcon()
        iconThemeName = u"zoom-in"
        if QIcon.hasThemeIcon(iconThemeName):
            icon6 = QIcon.fromTheme(iconThemeName)
        else:
            icon6.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        self.DollarPlot.setIcon(icon6)

        self.horizontalLayout.addWidget(self.DollarPlot)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 2)


        self.retranslateUi(Widget)
        self.SymbolButton.clicked.connect(Widget.openSettingsItem)
        self.DollarPlot.clicked.connect(Widget.openSettingsItem)
        self.MapButton.clicked.connect(Widget.openSettingsItem)
        self.RequestsButton.clicked.connect(Widget.openSettingsItem)
        self.RangeButton.clicked.connect(Widget.openSettingsItem)
        self.ThreeDButton.clicked.connect(Widget.openSettingsItem)
        self.InterpolateButton.clicked.connect(Widget.toggleInterpolation)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Asset Tracker Prototype", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Widget", u"Daily % Performance", None))
        self.InterpolateButton.setText(QCoreApplication.translate("Widget", u"Interpolation", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Widget", u"Symbol Details", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Widget", u"Todays $ Value", None))
        ___qtablewidgetitem = self.SimpleTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Widget", u"Symbol", None));
        ___qtablewidgetitem1 = self.SimpleTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Widget", u"Value", None));
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
        self.DollarPlot.setText("")
    # retranslateUi

