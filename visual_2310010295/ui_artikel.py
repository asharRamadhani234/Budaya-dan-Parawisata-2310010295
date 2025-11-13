# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'artikel.ui'
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
        self.formLayoutWidget.setGeometry(QRect(10, 10, 371, 121))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDArtikelLabel = QLabel(self.formLayoutWidget)
        self.iDArtikelLabel.setObjectName(u"iDArtikelLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDArtikelLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.judulLabel = QLabel(self.formLayoutWidget)
        self.judulLabel.setObjectName(u"judulLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.judulLabel)

        self.editJudul = QLineEdit(self.formLayoutWidget)
        self.editJudul.setObjectName(u"editJudul")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editJudul)

        self.keteranganLabel = QLabel(self.formLayoutWidget)
        self.keteranganLabel.setObjectName(u"keteranganLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.keteranganLabel)

        self.editKeterangan = QLineEdit(self.formLayoutWidget)
        self.editKeterangan.setObjectName(u"editKeterangan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editKeterangan)

        self.fotoLabel = QLabel(self.formLayoutWidget)
        self.fotoLabel.setObjectName(u"fotoLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.fotoLabel)

        self.editFoto = QLineEdit(self.formLayoutWidget)
        self.editFoto.setObjectName(u"editFoto")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editFoto)

        self.petaLabel = QLabel(self.formLayoutWidget)
        self.petaLabel.setObjectName(u"petaLabel")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.petaLabel)

        self.editPeta = QLineEdit(self.formLayoutWidget)
        self.editPeta.setObjectName(u"editPeta")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.editPeta)

        self.jenisWisataLabel = QLabel(self.formLayoutWidget)
        self.jenisWisataLabel.setObjectName(u"jenisWisataLabel")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.jenisWisataLabel)

        self.editJenis = QLineEdit(self.formLayoutWidget)
        self.editJenis.setObjectName(u"editJenis")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.editJenis)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(40, 130, 56, 18))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(140, 130, 56, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(240, 130, 56, 18))
        self.tabelArtikel = QTableWidget(Form)
        if (self.tabelArtikel.columnCount() < 6):
            self.tabelArtikel.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabelArtikel.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tabelArtikel.setObjectName(u"tabelArtikel")
        self.tabelArtikel.setGeometry(QRect(0, 160, 361, 121))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDArtikelLabel.setText(QCoreApplication.translate("Form", u"ID Artikel", None))
        self.judulLabel.setText(QCoreApplication.translate("Form", u"Judul", None))
        self.keteranganLabel.setText(QCoreApplication.translate("Form", u"Keterangan", None))
        self.fotoLabel.setText(QCoreApplication.translate("Form", u"Foto", None))
        self.petaLabel.setText(QCoreApplication.translate("Form", u"Peta", None))
        self.jenisWisataLabel.setText(QCoreApplication.translate("Form", u"Jenis Wisata", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelArtikel.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Galeri", None));
        ___qtablewidgetitem1 = self.tabelArtikel.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Judul", None));
        ___qtablewidgetitem2 = self.tabelArtikel.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Keterangan", None));
        ___qtablewidgetitem3 = self.tabelArtikel.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Foto", None));
        ___qtablewidgetitem4 = self.tabelArtikel.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Peta", None));
        ___qtablewidgetitem5 = self.tabelArtikel.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Jenis Wisata", None));
    # retranslateUi

