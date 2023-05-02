# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'query.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Query(object):
    def setupUi(self, Query):
        if not Query.objectName():
            Query.setObjectName(u"Query")
        Query.resize(221, 138)
        self.lineEdit = QLineEdit(Query)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 40, 181, 21))
        self.label = QLabel(Query)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 181, 16))
        self.pushButton = QPushButton(Query)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(70, 100, 80, 23))
        self.label_2 = QLabel(Query)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 70, 101, 16))

        self.retranslateUi(Query)

        QMetaObject.connectSlotsByName(Query)
    # setupUi

    def retranslateUi(self, Query):
        Query.setWindowTitle(QCoreApplication.translate("Query", u"Query", None))
        self.lineEdit.setText(QCoreApplication.translate("Query", u"https://google.com/", None))
        self.label.setText(QCoreApplication.translate("Query", u"Make a request to a URL", None))
        self.pushButton.setText(QCoreApplication.translate("Query", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("Query", u"Response: ", None))
    # retranslateUi

