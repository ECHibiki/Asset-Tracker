# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'advanced.ui'
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

from pyqtgraph.opengl import GLViewWidget

class Ui_Advanced(object):
    def setupUi(self, Advanced):
        if not Advanced.objectName():
            Advanced.setObjectName(u"Advanced")
        Advanced.resize(460, 374)
        self.graphicsView = GLViewWidget(Advanced)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(0, 0, 461, 371))

        self.retranslateUi(Advanced)

        QMetaObject.connectSlotsByName(Advanced)
    # setupUi

    def retranslateUi(self, Advanced):
        Advanced.setWindowTitle(QCoreApplication.translate("Advanced", u"PyQtGraph Demo", None))
    # retranslateUi

