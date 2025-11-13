# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
    QSizePolicy, QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionGaleri = QAction(MainWindow)
        self.actionGaleri.setObjectName(u"actionGaleri")
        self.actionTesti = QAction(MainWindow)
        self.actionTesti.setObjectName(u"actionTesti")
        self.actionArtikel = QAction(MainWindow)
        self.actionArtikel.setObjectName(u"actionArtikel")
        self.actionDiskusi = QAction(MainWindow)
        self.actionDiskusi.setObjectName(u"actionDiskusi")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 18))
        self.menuMenu_Halaman = QMenu(self.menubar)
        self.menuMenu_Halaman.setObjectName(u"menuMenu_Halaman")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu_Halaman.menuAction())
        self.menuMenu_Halaman.addAction(self.actionGaleri)
        self.menuMenu_Halaman.addAction(self.actionTesti)
        self.menuMenu_Halaman.addAction(self.actionArtikel)
        self.menuMenu_Halaman.addAction(self.actionDiskusi)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionGaleri.setText(QCoreApplication.translate("MainWindow", u"Galeri", None))
        self.actionTesti.setText(QCoreApplication.translate("MainWindow", u"Testi", None))
        self.actionArtikel.setText(QCoreApplication.translate("MainWindow", u"Artikel", None))
        self.actionDiskusi.setText(QCoreApplication.translate("MainWindow", u"Diskusi", None))
        self.menuMenu_Halaman.setTitle(QCoreApplication.translate("MainWindow", u"Menu Halaman", None))
    # retranslateUi

