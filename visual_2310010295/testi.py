# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class testi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("testi.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanTesti=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilTesti()
        self.halamanTesti.btnHapus.clicked.connect(self.doHapusTesti)
        self.halamanTesti.btnUbah.clicked.connect(self.doUbahTesti)
        self.halamanTesti.btnSimpan.clicked.connect(self.doSimpanTesti)

    def doSimpanTesti(self):
        if not self.halamanTesti.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Testi  Belum di isi")
            self.halamanTesti.editID.setFocus()
        elif not self.halamanTesti.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Testi Belum di isi")
            self.halamanTesti.editNama.setFocus()
        elif not self.halamanTesti.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Saran Testi Belum di isi")
            self.halamanTesti.editSaran.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanTesti.editID.text()
                tempNama=self.halamanTesti.editNama.text()
                tempSaran=self.halamanTesti.editSaran.text()
                self.aksi.doSimpanTesti(tempID, tempNama, tempSaran)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilTesti()

            else:
                pass

    def doUbahTesti(self):
        tempID=self.halamanTesti.editID.text()
        tempNama=self.halamanTesti.editNama.text()
        tempSaran=self.halamanTesti.editSaran.text()
        self.aksi.doUbahTesti(tempID, tempNama, tempSaran)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilTesti()

    def doHapusTesti(self):
        tempID=self.halamanTesti.editID.text()
        self.aksi.doHapusTesti(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilTesti()


    def tampilTesti(self):
        self.halamanTesti.tabelTesti.setRowCount(0)
        data=self.aksi.dataTesti()
        for i, r in enumerate(data):
            self.halamanTesti.tabelTesti.insertRow(i)
            self.halamanTesti.tabelTesti.setItem(i, 0, QTableWidgetItem(str(r["id"])))
            self.halamanTesti.tabelTesti.setItem(i, 1, QTableWidgetItem(str(r["nama"])))
            self.halamanTesti.tabelTesti.setItem(i, 2, QTableWidgetItem(str(r["saran"])))

