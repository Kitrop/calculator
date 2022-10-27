import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton, QMainWindow


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Калькулятор")
        self.setGeometry(300, 250, 350, 200)

        self.new_text = QtWidgets.QLabel(self)


        main_text = QtWidgets.QLabel(self)
        main_text.setText("Это стандратный текст")
        main_text.move(100, 100)
        main_text.adjustSize()

        btn = QtWidgets.QPushButton(self)
        btn.move(70, 150)
        btn.setText("нажми на меня")
        btn.adjustSize()
        btn.clicked.connect(self.add_label)

    def add_label(self):
        self.new_text.setText("Вторая надпись")
        self.new_text.move(100, 50)
        self.adjustSize()





def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
