# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
from galeri import galeri
from testi import testi
from artikel import artikel
from diskusi import diskusi




class main(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        filenya=QFile("main.ui")
        filenya.open(QFile.ReadOnly)

        unggahfile=QUiLoader()
        self.halamanUtama=unggahfile.load(filenya,self)
        self.setMenuBar(self.halamanUtama.menuBar())
        self.resize(self.halamanUtama.size())
        self.halamanUtama.actionGaleri.triggered.connect(self.bukaGaleri)
        self.halamanUtama.actionTesti.triggered.connect(self.bukaTesti)
        self.halamanUtama.actionArtikel.triggered.connect(self.bukaArtikel)
        self.halamanUtama.actionDiskusi.triggered.connect(self.bukaDiskusi)



    def bukaGaleri(self):
        self.formGaleri=galeri()
        self.formGaleri.show()

    def bukaTesti(self):
        self.formTesti=testi()
        self.formTesti.show()

    def bukaArtikel(self):
        self.formArtikel=artikel()
        self.formArtikel.show()

    def bukaDiskusi(self):
        self.formDiskusi=diskusi()
        self.formDiskusi.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    aplikasi = main()
    aplikasi.show()
    sys.exit(app.exec())
