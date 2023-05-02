# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dates.ui'
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
from PySide6.QtWidgets import (QApplication, QCalendarWidget, QDateEdit, QLabel,
    QMainWindow, QSizePolicy, QWidget)

class Ui_Dates(object):
    def setupUi(self, Dates):
        if not Dates.objectName():
            Dates.setObjectName(u"Dates")
        Dates.resize(529, 179)
        self.centralwidget = QWidget(Dates)
        self.centralwidget.setObjectName(u"centralwidget")
        self.calendarWidget = QCalendarWidget(self.centralwidget)
        self.calendarWidget.setObjectName(u"calendarWidget")
        self.calendarWidget.setGeometry(QRect(10, 20, 401, 149))
        self.calendarWidget.setSelectionMode(QCalendarWidget.SingleSelection)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 221, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(450, 30, 51, 16))
        self.dateEdit = QDateEdit(self.centralwidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setGeometry(QRect(420, 50, 110, 23))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit_2 = QDateEdit(self.centralwidget)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setGeometry(QRect(420, 100, 110, 23))
        self.dateEdit_2.setCalendarPopup(True)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(450, 80, 31, 20))
        Dates.setCentralWidget(self.centralwidget)

        self.retranslateUi(Dates)

        QMetaObject.connectSlotsByName(Dates)
    # setupUi

    def retranslateUi(self, Dates):
        Dates.setWindowTitle(QCoreApplication.translate("Dates", u"Date Picker", None))
        self.label.setText(QCoreApplication.translate("Dates", u"Select a date range (for start)", None))
        self.label_2.setText(QCoreApplication.translate("Dates", u"Start", None))
        self.label_3.setText(QCoreApplication.translate("Dates", u"End", None))
    # retranslateUi

