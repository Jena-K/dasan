# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dasan_main.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QTabWidget, QToolBar,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 632)
        MainWindow.setMaximumSize(QSize(837, 643))
        self.actionBackup = QAction(MainWindow)
        self.actionBackup.setObjectName(u"actionBackup")
        self.actionLogout = QAction(MainWindow)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionInstafgram = QAction(MainWindow)
        self.actionInstafgram.setObjectName(u"actionInstafgram")
        icon = QIcon()
        icon.addFile(u"../../../../Users/Jena/.designer/backup/images/Instagram_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionInstafgram.setIcon(icon)
        self.actionCafe = QAction(MainWindow)
        self.actionCafe.setObjectName(u"actionCafe")
        icon1 = QIcon()
        icon1.addFile(u"../../../../Users/Jena/.designer/backup/images/naver_cafe_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCafe.setIcon(icon1)
        self.actionBlog = QAction(MainWindow)
        self.actionBlog.setObjectName(u"actionBlog")
        icon2 = QIcon()
        icon2.addFile(u"../../../../Users/Jena/.designer/backup/images/naver_blog_logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionBlog.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 0, 821, 561))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.verticalLayoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 837, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAccount = QMenu(self.menubar)
        self.menuAccount.setObjectName(u"menuAccount")
        self.menuPlatform = QMenu(self.menubar)
        self.menuPlatform.setObjectName(u"menuPlatform")
        self.menuNaver = QMenu(self.menuPlatform)
        self.menuNaver.setObjectName(u"menuNaver")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.ToolBarArea.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAccount.menuAction())
        self.menubar.addAction(self.menuPlatform.menuAction())
        self.menuFile.addAction(self.actionLogout)
        self.menuFile.addAction(self.actionBackup)
        self.menuPlatform.addAction(self.menuNaver.menuAction())
        self.menuPlatform.addAction(self.actionInstafgram)
        self.menuNaver.addAction(self.actionBlog)
        self.menuNaver.addAction(self.actionCafe)
        self.toolBar.addAction(self.actionBlog)
        self.toolBar.addAction(self.actionCafe)
        self.toolBar.addAction(self.actionInstafgram)
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionBackup.setText(QCoreApplication.translate("MainWindow", u"Backup", None))
        self.actionLogout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.actionInstafgram.setText(QCoreApplication.translate("MainWindow", u"Instafgram", None))
        self.actionCafe.setText(QCoreApplication.translate("MainWindow", u"Cafe", None))
        self.actionBlog.setText(QCoreApplication.translate("MainWindow", u"Blog", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Account", None))
        self.menuPlatform.setTitle(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.menuNaver.setTitle(QCoreApplication.translate("MainWindow", u"Naver", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

