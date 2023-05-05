# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'symbols.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_NewSymbols(object):
    def setupUi(self, NewSymbols):
        if not NewSymbols.objectName():
            NewSymbols.setObjectName(u"NewSymbols")
        NewSymbols.resize(273, 177)
        self.ConfirmSymbols = QPushButton(NewSymbols)
        self.ConfirmSymbols.setObjectName(u"ConfirmSymbols")
        self.ConfirmSymbols.setGeometry(QRect(0, 150, 271, 23))
        self.SymbolList = QPlainTextEdit(NewSymbols)
        self.SymbolList.setObjectName(u"SymbolList")
        self.SymbolList.setGeometry(QRect(0, 20, 271, 121))
        self.label = QLabel(NewSymbols)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 0, 251, 16))

        self.retranslateUi(NewSymbols)
        self.ConfirmSymbols.clicked.connect(NewSymbols.addSymbols)

        QMetaObject.connectSlotsByName(NewSymbols)
    # setupUi

    def retranslateUi(self, NewSymbols):
        NewSymbols.setWindowTitle(QCoreApplication.translate("NewSymbols", u"New Symbols", None))
        self.ConfirmSymbols.setText(QCoreApplication.translate("NewSymbols", u"Confirm", None))
        self.SymbolList.setPlainText("")
        self.label.setText(QCoreApplication.translate("NewSymbols", u"Comma or new line seperated symbols", None))
    # retranslateUi

