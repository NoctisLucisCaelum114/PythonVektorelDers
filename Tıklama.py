from PyQt6.QtWidgets import *
app = QApplication([])

class Login(QMainWindow):
    def tiklama(self):
        # print("Tıklandı")
        kullanici = self.ka.text()
        sifre     = self.sf.text()

        mesaj = QMessageBox()
        # mesaj.setText("Tıklandı")
        mesaj.setText(f"Kullanici adi:{kullanici}, Sifre:{sifre}")
        mesaj.exec()

    def __init__(self):
        super().__init__()

        icerik = QVBoxLayout
        icerik.addWidget(QLabel("Kullanici adi"))
        self.ka = QLineEdit()
        icerik.addWidget(self.ka)
        icerik.addWidget(QLabel("Sifre"))
        self.sf = QLineEdit()
        icerik.addWidget(self.sf)
        bt = QPushButton("Giriş yap")
        icerik.addWidget(bt)

        bt.clicked.connect(self.tiklama)

        pencere = QWidget()
        pencere.setLayout(icerik)
        self.setCentralWidget(pencere)

ekran = Login()
ekran.show()
app.exec()
