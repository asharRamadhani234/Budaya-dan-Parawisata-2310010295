# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'testi.ui'
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
        self.formLayoutWidget.setGeometry(QRect(20, 20, 331, 67))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.iDTestiLabel = QLabel(self.formLayoutWidget)
        self.iDTestiLabel.setObjectName(u"iDTestiLabel")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.iDTestiLabel)

        self.editID = QLineEdit(self.formLayoutWidget)
        self.editID.setObjectName(u"editID")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.editID)

        self.namaLabel = QLabel(self.formLayoutWidget)
        self.namaLabel.setObjectName(u"namaLabel")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.namaLabel)

        self.editNama = QLineEdit(self.formLayoutWidget)
        self.editNama.setObjectName(u"editNama")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.editNama)

        self.saranLabel = QLabel(self.formLayoutWidget)
        self.saranLabel.setObjectName(u"saranLabel")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.saranLabel)

        self.editSaran = QLineEdit(self.formLayoutWidget)
        self.editSaran.setObjectName(u"editSaran")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.editSaran)

        self.btnSimpan = QPushButton(Form)
        self.btnSimpan.setObjectName(u"btnSimpan")
        self.btnSimpan.setGeometry(QRect(40, 100, 56, 18))
        self.btnUbah = QPushButton(Form)
        self.btnUbah.setObjectName(u"btnUbah")
        self.btnUbah.setGeometry(QRect(140, 100, 56, 18))
        self.btnHapus = QPushButton(Form)
        self.btnHapus.setObjectName(u"btnHapus")
        self.btnHapus.setGeometry(QRect(250, 100, 56, 18))
        self.tabelTesti = QTableWidget(Form)
        if (self.tabelTesti.columnCount() < 3):
            self.tabelTesti.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabelTesti.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabelTesti.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabelTesti.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tabelTesti.setObjectName(u"tabelTesti")
        self.tabelTesti.setGeometry(QRect(60, 140, 231, 111))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.iDTestiLabel.setText(QCoreApplication.translate("Form", u"ID Testi", None))
        self.namaLabel.setText(QCoreApplication.translate("Form", u"Nama", None))
        self.saranLabel.setText(QCoreApplication.translate("Form", u"Saran", None))
        self.btnSimpan.setText(QCoreApplication.translate("Form", u"SIMPAN", None))
        self.btnUbah.setText(QCoreApplication.translate("Form", u"UBAH", None))
        self.btnHapus.setText(QCoreApplication.translate("Form", u"HAPUS", None))
        ___qtablewidgetitem = self.tabelTesti.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID Testi", None));
        ___qtablewidgetitem1 = self.tabelTesti.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nama", None));
        ___qtablewidgetitem2 = self.tabelTesti.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Saran", None));
    # retranslateUi

