# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class artikel(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("artikel.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanArtikel=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilArtikel()
        self.halamanArtikel.btnHapus.clicked.connect(self.doHapusArtikel)
        self.halamanArtikel.btnUbah.clicked.connect(self.doUbahArtikel)
        self.halamanArtikel.btnSimpan.clicked.connect(self.doSimpanArtikel)

    def doSimpanArtikel(self):
        if not self.halamanArtikel.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Artikel  Belum di isi")
            self.halamanArtikel.editID.setFocus()
        elif not self.halamanArtikel.editJudul.text().strip():
            QMessageBox.information(None,"Informasi","Judul Artikel Belum di isi")
            self.halamanArtikel.editJudul.setFocus()
        elif not self.halamanArtikel.editKeterangan.text().strip():
            QMessageBox.information(None,"Informasi","Keterangan Artikel Belum di isi")
            self.halamanArtikel.editKeterangan.setFocus()
        elif not self.halamanArtikel.editKeterangan.text().strip():
            QMessageBox.information(None,"Informasi","Foto Artikel Belum di isi")
            self.halamanArtikel.editFoto.setFocus()
        elif not self.halamanArtikel.editPeta.text().strip():
            QMessageBox.information(None,"Informasi","Peta Artikel Belum di isi")
            self.halamanArtikel.editPeta.setFocus()
        elif not self.halamanArtikel.editJenis.text().strip():
            QMessageBox.information(None,"Informasi","Jenis Artikel Belum di isi")
            self.halamanArtikel.editJenis.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanArtikel.editID.text()
                tempJudul=self.halamanArtikel.editJudul.text()
                tempKeterangan=self.halamanArtikel.editKeterangan.text()
                tempFoto=self.halamanArtikel.editFoto.text()
                tempPeta=self.halamanArtikel.editPeta.text()
                tempJenis=self.halamanArtikel.editJenis.text()
                self.aksi.doSimpanArtikel(tempID, tempJudul, tempKeterangan, tempFoto, tempPeta, tempJenis)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilArtikel()

            else:
                pass

    def doUbahArtikel(self):
        tempID=self.halamanArtikel.editID.text()
        tempJudul=self.halamanArtikel.editJudul.text()
        tempKeterangan=self.halamanArtikel.editKeterangan.text()
        tempFoto=self.halamanArtikel.editFoto.text()
        tempPeta=self.halamanArtikel.editPeta.text()
        tempJenis=self.halamanArtikel.editJenis.text()
        self.aksi.doUbahArtikel(tempID, tempJudul, tempKeterangan, tempFoto, tempPeta, tempJenis)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilArtikel()

    def doHapusArtikel(self):
        tempID=self.halamanArtikel.editID.text()
        self.aksi.doHapusArtikel(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilArtikel()


    def tampilArtikel(self):
        self.halamanArtikel.tabelArtikel.setRowCount(0)
        data=self.aksi.dataArtikel()
        for i, r in enumerate(data):
            self.halamanArtikel.tabelArtikel.insertRow(i)
            self.halamanArtikel.tabelArtikel.setItem(i, 0, QTableWidgetItem(str(r["id"])))
            self.halamanArtikel.tabelArtikel.setItem(i, 1, QTableWidgetItem(str(r["judul"])))
            self.halamanArtikel.tabelArtikel.setItem(i, 2, QTableWidgetItem(str(r["keterangan"])))
            self.halamanArtikel.tabelArtikel.setItem(i, 3, QTableWidgetItem(str(r["foto"])))
            self.halamanArtikel.tabelArtikel.setItem(i, 4, QTableWidgetItem(str(r["peta"])))
            self.halamanArtikel.tabelArtikel.setItem(i, 5, QTableWidgetItem(str(r["jenis_wisata"])))
