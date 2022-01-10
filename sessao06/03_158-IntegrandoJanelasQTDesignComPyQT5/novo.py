"""
comando para converter um arquivo qt em python
pyuic5.exe design.ui -o design.py
"""

import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap


class Novo(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)  # super do qmainwindow
        super().setupUi(self)  # super do ui_mainwindow
        self.btnEscolherArquivo.clicked.connect(self.abrir_imagem)
        self.inputAltura.setDisabled(True)
        self.btnRedimensionar.clicked.connect(self.redimensionar)
        self.btnSalvar.clicked.connect(self.salvar)

    def abrir_imagem(self):
        imagem, _ = QFileDialog.getOpenFileName(
            self.centralwidget,
            'Abrir imagem',
            r'C:\Users\lrute\Pictures',
            # options=QFileDialog.DontUseNativeDialog
        )

        self.inputAbrirArquivo.setText(imagem)
        self.img_original = QPixmap(imagem)  # cria uma copia da imagem original
        self.labelImg.setPixmap(self.img_original)
        self.inputLargura.setText(str(self.img_original.width()))
        self.inputAltura.setText(str(self.img_original.height()))

    def redimensionar(self):
        largura = int(self.inputLargura.text())
        self.nova_imagem = self.img_original.scaledToWidth(largura)  # calcula a altura pela largura
        self.labelImg.setPixmap(self.nova_imagem)
        self.inputLargura.setText(str(self.nova_imagem.width()))
        self.inputAltura.setText(str(self.nova_imagem.height()))

    def salvar(self):
        imagem, _ = QFileDialog.getSaveFileName(
            self.centralwidget,
            'Salvar imagem',
            r'C:\Users\lrute\Desktop',
            # options=QFileDialog.DontUseNativeDialog
        )
        self.nova_imagem.save(imagem, 'PNG')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    novo = Novo()
    novo.show()
    qt.exec_()