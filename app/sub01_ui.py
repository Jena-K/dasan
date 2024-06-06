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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QSpacerItem, QTreeWidget, QTreeWidgetItem,
    QVBoxLayout, QWidget)

class Ui_B1_Action(object):
    def setupUi(self, B1_Action):
        if not B1_Action.objectName():
            B1_Action.setObjectName(u"B1_Action")
        B1_Action.resize(450, 300)
        self.verticalLayout_6 = QVBoxLayout(B1_Action)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeWidget = QTreeWidget(B1_Action)
        font = QFont()
        font.setBold(True)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font);
        __qtreewidgetitem.setBackground(2, QColor(255, 223, 221));
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setBackground(1, QColor(255, 223, 221));
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        __qtreewidgetitem.setBackground(0, QColor(255, 223, 221));
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout.addWidget(self.treeWidget)

        self.horizontalSpacer = QSpacerItem(300, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setSpacing(2)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_1.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(B1_Action)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_1.addWidget(self.pushButton)

        self.verticalSpacer_2 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_1.addItem(self.verticalSpacer_2)

        self.pushButton_2 = QPushButton(B1_Action)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_1.addWidget(self.pushButton_2)

        self.verticalSpacer_3 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_1.addItem(self.verticalSpacer_3)

        self.pushButton_3 = QPushButton(B1_Action)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_1.addWidget(self.pushButton_3)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer_4)

        self.pushButton_4 = QPushButton(B1_Action)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_1.addWidget(self.pushButton_4)

        self.verticalSpacer_5 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_1.addItem(self.verticalSpacer_5)

        self.pushButton_5 = QPushButton(B1_Action)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_1.addWidget(self.pushButton_5)

        self.verticalSpacer_6 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer_6)

        self.pushButton_6 = QPushButton(B1_Action)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_1.addWidget(self.pushButton_6)

        self.verticalSpacer_7 = QSpacerItem(20, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_1.addItem(self.verticalSpacer_7)

        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_1.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_1)


        self.verticalLayout_6.addLayout(self.horizontalLayout)


        self.retranslateUi(B1_Action)

        QMetaObject.connectSlotsByName(B1_Action)
    # setupUi

    def retranslateUi(self, B1_Action):
        B1_Action.setWindowTitle(QCoreApplication.translate("B1_Action", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("B1_Action", u"PW", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("B1_Action", u"ID", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("B1_Action", u"Category", None));
        self.pushButton.setText(QCoreApplication.translate("B1_Action", u"Add", None))
        self.pushButton_2.setText(QCoreApplication.translate("B1_Action", u"Edit", None))
        self.pushButton_3.setText(QCoreApplication.translate("B1_Action", u"Remove", None))
        self.pushButton_4.setText(QCoreApplication.translate("B1_Action", u"Up", None))
        self.pushButton_5.setText(QCoreApplication.translate("B1_Action", u"Down", None))
        self.pushButton_6.setText(QCoreApplication.translate("B1_Action", u"Close", None))
    # retranslateUi

