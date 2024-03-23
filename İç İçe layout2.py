from PyQt6.QtWidgets import *

class AnaPencere(QMainWindow):
    def __init__(self):
        super().__init__()

        dikeyicerik3 = QVBoxLayout()
        dikeyicerik3.addWidget(QLabel("Adı"))
        dikeyicerik3.addWidget(QLabel("Soyadı"))

        dikeyicerik4 = QVBoxLayout()
        dikeyicerik4.addWidget(QLineEdit())
        dikeyicerik4.addWidget(QLineEdit())

        yatayicerik1 = QHBoxLayout()
        yatayicerik1.addLayout(dikeyicerik3)
        yatayicerik1.addLayout(dikeyicerik4)

    
