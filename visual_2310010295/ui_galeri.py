# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'galeri.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 331, 90))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDLabel = QLabel(self.formLayoutWidget)
        self.iDLabel.setObjectName(u"iDLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.jenisWisataLabel = QLabel(self.formLayoutWidget)
        self.jenisWisataLabel.setObjectName(u"jenisWisataLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.jenisWisataLabel)

        self.editJenis = QLineEdit(self.formLayoutWidget)
        self.editJenis.setObjectName(u"editJenis")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editJenis)

        self.namaTempatLabel = QLabel(self.formLayoutWidget)
        self.namaTempatLabel.setObjectName(u"namaTempatLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.namaTempatLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.fotoLabel = QLabel(self.formLayoutWidget)
        self.fotoLabel.setObjectName(u"fotoLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.fotoLabel)

        self.editFoto = QLineEdit(self.formLayoutWidget)
        self.editFoto.setObjectName(u"editFoto")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editFoto)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 140, 56, 18))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(140, 140, 56, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(230, 140, 56, 18))
        self.tabelGaleri = QTableWidget(Form)
        if (self.tabelGaleri.columnCount() < 4):
            self.tabelGaleri.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelGaleri.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelGaleri.setObjectName(u"tabelGaleri")
        self.tabelGaleri.setGeometry(QRect(20, 171, 321, 111))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDLabel.setText(QCoreApplication.translate("Form", u"ID Galeri", None))
        self.jenisWisataLabel.setText(QCoreApplication.translate("Form", u"Jenis Wisata", None))
        self.namaTempatLabel.setText(QCoreApplication.translate("Form", u"Nama Tempat", None))
        self.fotoLabel.setText(QCoreApplication.translate("Form", u"Foto", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelGaleri.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Galeri", None));
        ___qtablewidgetitem1 = self.tabelGaleri.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Jenis Wisata", None));
        ___qtablewidgetitem2 = self.tabelGaleri.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nama Tempat", None));
        ___qtablewidgetitem3 = self.tabelGaleri.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Foto", None));
    # retranslateUi

