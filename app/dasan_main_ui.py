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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QFrame,
    QHeaderView, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(837, 634)
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
        self.actionNaver_Blog = QAction(MainWindow)
        self.actionNaver_Blog.setObjectName(u"actionNaver_Blog")
        self.actionNaver_blog = QAction(MainWindow)
        self.actionNaver_blog.setObjectName(u"actionNaver_blog")
        self.actionNaver_cafe = QAction(MainWindow)
        self.actionNaver_cafe.setObjectName(u"actionNaver_cafe")
        self.actionBill_Management = QAction(MainWindow)
        self.actionBill_Management.setObjectName(u"actionBill_Management")
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
        self.button_popup_accnt = QPushButton(self.tab)
        self.button_popup_accnt.setObjectName(u"button_popup_accnt")
        self.button_popup_accnt.setGeometry(QRect(360, 230, 75, 24))
        self.treeWidget = QTreeWidget(self.tab)
        font = QFont()
        font.setBold(True)
        font1 = QFont()
        font1.setBold(True)
        font1.setHintingPreference(QFont.PreferFullHinting)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setTextAlignment(2, Qt.AlignCenter);
        __qtreewidgetitem.setFont(2, font1);
        __qtreewidgetitem.setBackground(2, QColor(255, 223, 221));
        __qtreewidgetitem.setTextAlignment(1, Qt.AlignCenter);
        __qtreewidgetitem.setFont(1, font);
        __qtreewidgetitem.setBackground(1, QColor(255, 223, 221));
        __qtreewidgetitem.setTextAlignment(0, Qt.AlignCenter);
        __qtreewidgetitem.setFont(0, font);
        __qtreewidgetitem.setBackground(0, QColor(255, 223, 221));
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        self.treeWidget.setGeometry(QRect(470, 60, 313, 422))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeWidget.sizePolicy().hasHeightForWidth())
        self.treeWidget.setSizePolicy(sizePolicy)
        self.treeWidget.setMaximumSize(QSize(16777212, 16777215))
        self.treeWidget.setBaseSize(QSize(0, 0))
        self.treeWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.treeWidget.setFrameShape(QFrame.Shape.StyledPanel)
        self.treeWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.treeWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.treeWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.treeWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setTabKeyNavigation(True)
        self.treeWidget.setSelectionMode(QAbstractItemView.SelectionMode.ContiguousSelection)
        self.treeWidget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectItems)
        self.treeWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerItem)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.header().setCascadingSectionResizes(False)
        self.tableWidget = QTableWidget(self.tab)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 80, 313, 422))
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
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
        self.menuAccount.addAction(self.actionBill_Management)
        self.menuPlatform.addAction(self.actionNaver_cafe)
        self.menuPlatform.addAction(self.actionNaver_blog)
        self.menuPlatform.addSeparator()
        self.menuPlatform.addAction(self.actionInstafgram)
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
        self.actionNaver_Blog.setText(QCoreApplication.translate("MainWindow", u"Naver Blog", None))
        self.actionNaver_blog.setText(QCoreApplication.translate("MainWindow", u"Naver blog", None))
        self.actionNaver_cafe.setText(QCoreApplication.translate("MainWindow", u"Naver cafe", None))
        self.actionBill_Management.setText(QCoreApplication.translate("MainWindow", u"Bill Management", None))
        self.button_popup_accnt.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(2, QCoreApplication.translate("MainWindow", u"PW", None));
        ___qtreewidgetitem.setText(1, QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"PW", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Tab 1", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Tab 2", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAccount.setTitle(QCoreApplication.translate("MainWindow", u"Bill", None))
        self.menuPlatform.setTitle(QCoreApplication.translate("MainWindow", u"Platform", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

