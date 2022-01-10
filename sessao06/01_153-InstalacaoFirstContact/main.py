"""
PyQt é um toolkit desenvolvido em c++ utilizado por varios programas para
criação de aplicações GUI(interface grafica). Também inclui diversas
funcionalidades, tais como: acesso a base de dados, threads, comunicação de rede,
etc ...

pip install pyqt5
pip install PyQt5-stubs  ou  pip install PyQt5-stubs==5.15.2.0

--- Codigo inicial para qualquer programa em QT
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout


class Calculadora(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Calculadora')
        self.setFixedSize(400,400)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)



        self.setCentralWidget(self.cw)



if __name__ == '__main__':
    qt = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    qt.exec_()



"""
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QGridLayout


class App(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cw = QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')
        self.btn.setStyleSheet('font-size: 12px; background: yellow')
        # botao, 0, 0, 1, 1(botao, linha=0, coluna=0, rolspan=1, qtsColunasobotaoVaiTer=1) igual grid de html
        self.grid.addWidget(self.btn, 0, 0, 1, 1)
        # self.btn.clicked.connect(lambda: print('Olá mundo'))
        self.btn.clicked.connect(self.acao)

        self.setCentralWidget(self.cw)

    def acao(self):
        print('alguma coisa')


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    app = App()
    app.show()
    qt.exec_()
