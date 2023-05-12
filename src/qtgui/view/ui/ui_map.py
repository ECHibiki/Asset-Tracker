# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'map.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QWidget)

class Ui_MapForm(object):
    def setupUi(self, MapForm):
        if not MapForm.objectName():
            MapForm.setObjectName(u"MapForm")
        MapForm.resize(470, 447)
        self.MapItem = QWidget(MapForm)
        self.MapItem.setObjectName(u"MapItem")
        self.MapItem.setGeometry(QRect(-1, 0, 471, 441))

        self.retranslateUi(MapForm)

        QMetaObject.connectSlotsByName(MapForm)
    # setupUi

    def retranslateUi(self, MapForm):
        MapForm.setWindowTitle(QCoreApplication.translate("MapForm", u"Form", None))
    # retranslateUi

