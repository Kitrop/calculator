import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

formatNumber = lambda n: n \
    if n % 1 \
    else int(n)


class Calculator(QWidget):

    # Check for num. Return boolean
    def isnum(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def __init__(self):
        super(Calculator, self).__init__()

        # Vertical axis
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        # 7 8 9 *
        self.hbox_first = QHBoxLayout()
        # 4 5 6 -
        self.hbox_two = QHBoxLayout()
        # 1 2 3 +
        self.hbox_three = QHBoxLayout()
        #  . 0 /
        self.hbox_thour = QHBoxLayout()
        # =
        self.hbox_result = QHBoxLayout()

        # Tie horizontal axis
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_two)
        self.vbox.addLayout(self.hbox_three)
        self.vbox.addLayout(self.hbox_thour)
        self.vbox.addLayout(self.hbox_result)

        # Create widgets
        ## Input
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_three.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_three.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_three.addWidget(self.b_3)

        self.b_4 = QPushButton("4", self)
        self.hbox_two.addWidget(self.b_4)

        self.b_5 = QPushButton("5", self)
        self.hbox_two.addWidget(self.b_5)

        self.b_6 = QPushButton("6", self)
        self.hbox_two.addWidget(self.b_6)

        self.b_7 = QPushButton("7", self)
        self.hbox_first.addWidget(self.b_7)

        self.b_8 = QPushButton("8", self)
        self.hbox_first.addWidget(self.b_8)

        self.b_9 = QPushButton("9", self)
        self.hbox_first.addWidget(self.b_9)

        self.b_0 = QPushButton("0", self)
        self.hbox_thour.addWidget(self.b_0)

        self.b_plus = QPushButton("+", self)
        self.hbox_three.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_two.addWidget(self.b_minus)

        self.b_mult = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_mult)

        self.b_div = QPushButton("/", self)
        self.hbox_thour.addWidget(self.b_div)

        self.b_dot = QPushButton(".", self)
        self.hbox_thour.addWidget(self.b_dot)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        ########################################

        # Connects
        self.b_plus.clicked.connect(lambda: self._operation("+"))
        self.b_minus.clicked.connect(lambda: self._operation("-"))
        self.b_mult.clicked.connect(lambda: self._operation("*"))
        self.b_div.clicked.connect(lambda: self._operation("/"))
        self.b_dot.clicked.connect(lambda: self._button("."))

        # Result
        self.b_result.clicked.connect(self._result)

        # Int numbers
        self.b_1.clicked.connect(lambda: self._button("1"))
        self.b_2.clicked.connect(lambda: self._button("2"))
        self.b_3.clicked.connect(lambda: self._button("3"))
        self.b_4.clicked.connect(lambda: self._button("4"))
        self.b_5.clicked.connect(lambda: self._button("5"))
        self.b_6.clicked.connect(lambda: self._button("6"))
        self.b_7.clicked.connect(lambda: self._button("7"))
        self.b_8.clicked.connect(lambda: self._button("8"))
        self.b_9.clicked.connect(lambda: self._button("9"))
        self.b_0.clicked.connect(lambda: self._button("0"))

    # Button handler
    def _button(self, param):
        line = self.input.text()
        self.input.setText(line + param)

    # Math sign handler
    def _operation(self, op):
        if not self.isnum(self.input.text()):
            return self.input.setText("Ошибка")
        else:
            self.num_1 = formatNumber(float(self.input.text()))
            self.op = op
            self.input.setText("")

    # Func calculations
    def _result(self):
        if not self.isnum(self.input.text()):
            return self.input.setText("Ошибка")
        if self.input.text() and self.op:

            self.num_2 = formatNumber(float(self.input.text()))

            if self.op == "+":
                self.input.setText(str(self.num_1 + self.num_2))

            if self.op == "-":
                self.input.setText(str(self.num_1 - self.num_2))

            if self.op == "*":
                self.input.setText(str(self.num_1 * self.num_2))

            if self.op == "/" and self.num_1 != 0 and self.num_2 != 0:
                self.input.setText(str(self.num_1 / self.num_2))
            else:
                return self.input.setText("Нельзя делить на ноль")

def application():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
