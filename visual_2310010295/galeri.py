# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class galeri(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("galeri.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanGaleri=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilGaleri()
        self.halamanGaleri.btnHapus.clicked.connect(self.doHapusGaleri)
        self.halamanGaleri.btnUbah.clicked.connect(self.doUbahGaleri)
        self.halamanGaleri.btnSimpan.clicked.connect(self.doSimpanGaleri)

    def doSimpanGaleri(self):
        if not self.halamanGaleri.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Galeri  Belum di isi")
            self.halamanGaleri.editID.setFocus()
        elif not self.halamanGaleri.editJenis.text().strip():
            QMessageBox.information(None,"Informasi","Jenis Galeri Belum di isi")
            self.halamanGaleri.editJenis.setFocus()
        elif not self.halamanGaleri.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Galeri Belum di isi")
            self.halamanGaleri.editNama.setFocus()
        elif not self.halamanGaleri.editFoto.text().strip():
            QMessageBox.information(None,"Informasi","Foto Galeri Belum di isi")
            self.halamanGaleri.editFoto.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanGaleri.editID.text()
                tempJenis=self.halamanGaleri.editJenis.text()
                tempNama=self.halamanGaleri.editNama.text()
                tempFoto=self.halamanGaleri.editFoto.text()
                self.aksi.doSimpanGaleri(tempID, tempJenis, tempNama, tempFoto)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilGaleri()

            else:
                pass

    def doUbahGaleri(self):
        tempID=self.halamanGaleri.editID.text()
        tempJenis=self.halamanGaleri.editJenis.text()
        tempNama=self.halamanGaleri.editNama.text()
        tempFoto=self.halamanGaleri.editFoto.text()
        self.aksi.doUbahGaleri(tempID, tempJenis, tempNama, tempFoto)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilGaleri()

    def doHapusGaleri(self):
        tempID=self.halamanGaleri.editID.text()
        self.aksi.doHapusGaleri(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilGaleri()


    def tampilGaleri(self):
        self.halamanGaleri.tabelGaleri.setRowCount(0)
        data=self.aksi.dataGaleri()
        for i, r in enumerate(data):
            self.halamanGaleri.tabelGaleri.insertRow(i)
            self.halamanGaleri.tabelGaleri.setItem(i, 0, QTableWidgetItem(str(r["id"])))
            self.halamanGaleri.tabelGaleri.setItem(i, 1, QTableWidgetItem(str(r["jenis_wisata"])))
            self.halamanGaleri.tabelGaleri.setItem(i, 2, QTableWidgetItem(str(r["nama_tempat"])))
            self.halamanGaleri.tabelGaleri.setItem(i, 3, QTableWidgetItem(str(r["foto"])))
