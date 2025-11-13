# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from databasequery import crud

class diskusi(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("diskusi.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanDiskusi=unggahfile.load(filenya,self)
        #self.resize(self.halamanAnggota.size())
        self.aksi=crud()
        self.tampilDiskusi()
        self.halamanDiskusi.btnHapus.clicked.connect(self.doHapusDiskusi)
        self.halamanDiskusi.btnUbah.clicked.connect(self.doUbahDiskusi)
        self.halamanDiskusi.btnSimpan.clicked.connect(self.doSimpanDiskusi)

    def doSimpanDiskusi(self):
        if not self.halamanDiskusi.editID.text().strip():
            QMessageBox.information(None,"Informasi","ID Diskusi  Belum di isi")
            self.halamanDiskusi.editID.setFocus()
        elif not self.halamanDiskusi.editNama.text().strip():
            QMessageBox.information(None,"Informasi","Nama Diskusi Belum di isi")
            self.halamanDiskusi.editNama.setFocus()
        elif not self.halamanDiskusi.editPesan.text().strip():
            QMessageBox.information(None,"Informasi","Pesan Diskusi Belum di isi")
            self.halamanDiskusi.editPesan.setFocus()
        elif not self.halamanDiskusi.editTime.text().strip():
            QMessageBox.information(None,"Informasi","Time Diskusi Belum di isi")
            self.halamanDiskusi.editTime.setFocus()
        else:
            validasi=QMessageBox.information(None,"Informasi","Apakah anda yakin menyimpan data ini?",
            QMessageBox.Yes | QMessageBox.No)

            if validasi==QMessageBox.Yes:

                tempID=self.halamanDiskusi.editID.text()
                tempNama=self.halamanDiskusi.editNama.text()
                tempPesan=self.halamanDiskusi.editPesan.text()
                tempTime=self.halamanDiskusi.editTime.text()
                self.aksi.doSimpanDiskusi(tempID, tempNama, tempPesan, tempTime)
                QMessageBox.information(None,"Informasi","Data Berhasil di simpan")
                self.tampilDiskusi()

            else:
                pass

    def doUbahDiskusi(self):
        tempID=self.halamanDiskusi.editID.text()
        tempNama=self.halamanDiskusi.editNama.text()
        tempPesan=self.halamanDiskusi.editPesan.text()
        tempTime=self.halamanDiskusi.editTime.text()
        self.aksi.doUbahDiskusi(tempID, tempNama, tempPesan, tempTime)
        QMessageBox.information(None,"Informasi","Data Berhasil di ubah")
        self.tampilDiskusi()

    def doHapusDiskusi(self):
        tempID=self.halamanDiskusi.editID.text()
        self.aksi.doHapusDiskusi(tempID)
        QMessageBox.information(None,"Informasi","Data Berhasil di Hapus")
        self.tampilDiskusi()


    def tampilDiskusi(self):
        self.halamanDiskusi.tabelDiskusi.setRowCount(0)
        data=self.aksi.dataDiskusi()
        for i, r in enumerate(data):
            self.halamanDiskusi.tabelDiskusi.insertRow(i)
            self.halamanDiskusi.tabelDiskusi.setItem(i, 0, QTableWidgetItem(str(r["id"])))
            self.halamanDiskusi.tabelDiskusi.setItem(i, 1, QTableWidgetItem(str(r["nama"])))
            self.halamanDiskusi.tabelDiskusi.setItem(i, 2, QTableWidgetItem(str(r["pesan"])))
            self.halamanDiskusi.tabelDiskusi.setItem(i, 3, QTableWidgetItem(str(r["time"])))
