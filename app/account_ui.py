# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'account.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QHeaderView,
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(440, 441)
        self.action_addRow = QAction(Dialog)
        self.action_addRow.setObjectName(u"action_addRow")
        self.action_addRow.setMenuRole(QAction.MenuRole.NoRole)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(0, 0, 441, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 0, 5)
        self.accounts = QTableView(self.horizontalLayoutWidget)
        self.accounts.setObjectName(u"accounts")

        self.verticalLayout.addWidget(self.accounts)

        self.horizontalSpacer = QSpacerItem(300, 1, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.verticalLayout.addItem(self.horizontalSpacer)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_1 = QVBoxLayout()
        self.verticalLayout_1.setSpacing(5)
        self.verticalLayout_1.setObjectName(u"verticalLayout_1")
        self.verticalLayout_1.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_1.setContentsMargins(5, 5, 10, 10)
        self.button_Add = QPushButton(self.horizontalLayoutWidget)
        self.button_Add.setObjectName(u"button_Add")

        self.verticalLayout_1.addWidget(self.button_Add)

        self.button_Edit = QPushButton(self.horizontalLayoutWidget)
        self.button_Edit.setObjectName(u"button_Edit")

        self.verticalLayout_1.addWidget(self.button_Edit)

        self.button_Remove = QPushButton(self.horizontalLayoutWidget)
        self.button_Remove.setObjectName(u"button_Remove")

        self.verticalLayout_1.addWidget(self.button_Remove)

        self.verticalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer_4)

        self.button_up = QPushButton(self.horizontalLayoutWidget)
        self.button_up.setObjectName(u"button_up")

        self.verticalLayout_1.addWidget(self.button_up)

        self.button_down = QPushButton(self.horizontalLayoutWidget)
        self.button_down.setObjectName(u"button_down")

        self.verticalLayout_1.addWidget(self.button_down)

        self.verticalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_1.addItem(self.verticalSpacer_6)

        self.botton_close = QPushButton(self.horizontalLayoutWidget)
        self.botton_close.setObjectName(u"botton_close")

        self.verticalLayout_1.addWidget(self.botton_close)

        self.horizontalSpacer_2 = QSpacerItem(100, 1, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.verticalLayout_1.addItem(self.horizontalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout_1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.action_addRow.setText(QCoreApplication.translate("Dialog", u"AddRow", None))
        self.button_Add.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.button_Edit.setText(QCoreApplication.translate("Dialog", u"Edit", None))
        self.button_Remove.setText(QCoreApplication.translate("Dialog", u"Remove", None))
        self.button_up.setText(QCoreApplication.translate("Dialog", u"Up", None))
        self.button_down.setText(QCoreApplication.translate("Dialog", u"Down", None))
        self.botton_close.setText(QCoreApplication.translate("Dialog", u"Close", None))
    # retranslateUi

