# This Python file uses the following encoding: utf-8
import mysql.connector

class crud:
    def __init__(self):
       self.koneksiDB=mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='pbo2_2310010295'
       )

    # ----------------GALERI----------------
    def doSimpanGaleri(self, ID, JENIS, NAMA, FOTO):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into galeri(id, jenis_wisata, nama_tempat, foto) VALUE(%s,%s,%s,%s)",
        (ID, JENIS, NAMA, FOTO))
        self.koneksiDB.commit()
        alamat.close()

    def doUbahGaleri(self, ID, JENIS, NAMA, FOTO):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update galeri set jenis_wisata=%s, nama_tempat=%s, foto=%s where id=%s",
        (JENIS, NAMA, FOTO, ID))
        self.koneksiDB.commit()
        alamat.close()

    def dataGaleri(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM galeri order by id asc")
        return alamat.fetchall()


    def doHapusGaleri(self, ID):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from galeri where id=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()

    # ----------------TESTI----------------
    def doSimpanTesti(self, ID, NAMA, SARAN):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into testi(id, nama, saran) VALUE(%s,%s,%s)",
        (ID, NAMA, SARAN))
        self.koneksiDB.commit()
        alamat.close()

    def doUbahTesti(self, ID, NAMA, SARAN):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update testi set nama=%s, saran=%s where id=%s",
        (NAMA, SARAN, ID))
        self.koneksiDB.commit()
        alamat.close()

    def dataTesti(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM testi order by id asc")
        return alamat.fetchall()


    def doHapusTesti(self, ID):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from testi where id=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()

    # ----------------ARTIKEL----------------
    def doSimpanArtikel(self, ID, JUDUL, KETERANGAN, FOTO, PETA, JENIS):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into artikel(id, judul, keterangan, foto, peta, jenis_wisata) VALUE(%s,%s,%s,%s,%s,%s)",
        (ID, JUDUL, KETERANGAN, FOTO, PETA, JENIS))
        self.koneksiDB.commit()
        alamat.close()

    def doUbahArtikel(self, ID, JUDUL, KETERANGAN, FOTO, PETA, JENIS):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update artikel set judul=%s, keterangan=%s, foto=%s, peta=%s, jenis_wisata=%s where id=%s",
        (JUDUL, KETERANGAN, FOTO, PETA, JENIS, ID))
        self.koneksiDB.commit()
        alamat.close()

    def dataArtikel(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM artikel order by id asc")
        return alamat.fetchall()


    def doHapusArtikel(self, ID):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from artikel where id=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()

     # ----------------DISKUSI----------------
    def doSimpanDiskusi(self, ID, NAMA, PESAN, TIME):
        alamat=self.koneksiDB.cursor()
        alamat.execute("insert into diskusi(id, nama, pesan, time) VALUE(%s,%s,%s,%s)",
        (ID, NAMA, PESAN, TIME))
        self.koneksiDB.commit()
        alamat.close()

    def doUbahDiskusi(self, ID, NAMA, PESAN, TIME):
        alamat=self.koneksiDB.cursor()
        alamat.execute("update diskusi set nama=%s, pesan=%s, time=%s where id=%s",
        (NAMA, PESAN, TIME, ID))
        self.koneksiDB.commit()
        alamat.close()

    def dataDiskusi(self):
        alamat=self.koneksiDB.cursor(dictionary=True)
        alamat.execute("SELECT*FROM diskusi order by id asc")
        return alamat.fetchall()


    def doHapusDiskusi(self, ID):
        alamat=self.koneksiDB.cursor()
        alamat.execute("delete from diskusi where id=%s", (ID,))
        self.koneksiDB.commit()
        alamat.close()

