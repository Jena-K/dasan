# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sub01.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
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
from PySide6.QtWidgets import (QApplication, QPushButton, QSizePolicy, QWidget)

class Ui_B1_Action(object):
    def setupUi(self, B1_Action):
        if not B1_Action.objectName():
            B1_Action.setObjectName(u"B1_Action")
        B1_Action.resize(400, 300)
        self.pushButton = QPushButton(B1_Action)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(90, 70, 75, 24))

        self.retranslateUi(B1_Action)

        QMetaObject.connectSlotsByName(B1_Action)
    # setupUi

    def retranslateUi(self, B1_Action):
        B1_Action.setWindowTitle(QCoreApplication.translate("B1_Action", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("B1_Action", u"Clear", None))
    # retranslateUi

