# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diskusi.ui'
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
        self.formLayoutWidget.setGeometry(QRect(0, 10, 391, 101))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDDiskusiLabel = QLabel(self.formLayoutWidget)
        self.iDDiskusiLabel.setObjectName(u"iDDiskusiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDDiskusiLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaLabel = QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName(u"namaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.pesanLabel = QLabel(self.formLayoutWidget)
        self.pesanLabel.setObjectName(u"pesanLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.pesanLabel)

        self.editPesan = QLineEdit(self.formLayoutWidget)
        self.editPesan.setObjectName(u"editPesan")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editPesan)

        self.timeLabel = QLabel(self.formLayoutWidget)
        self.timeLabel.setObjectName(u"timeLabel")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.timeLabel)

        self.editTime = QLineEdit(self.formLayoutWidget)
        self.editTime.setObjectName(u"editTime")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.editTime)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(60, 120, 56, 18))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(170, 120, 56, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(270, 120, 56, 18))
        self.tabelDiskusi = QTableWidget(Form)
        if (self.tabelDiskusi.columnCount() < 4):
            self.tabelDiskusi.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelDiskusi.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelDiskusi.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelDiskusi.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabelDiskusi.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.tabelDiskusi.setObjectName(u"tabelDiskusi")
        self.tabelDiskusi.setGeometry(QRect(10, 140, 381, 141))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDDiskusiLabel.setText(QCoreApplication.translate("Form", u"ID Diskusi", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.pesanLabel.setText(QCoreApplication.translate("Form", u"Pesan", None))
        self.timeLabel.setText(QCoreApplication.translate("Form", u"Time", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelDiskusi.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Diskusi", None));
        ___qtablewidgetitem1 = self.tabelDiskusi.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelDiskusi.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Pesan", None));
        ___qtablewidgetitem3 = self.tabelDiskusi.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Time", None));
    # retranslateUi

