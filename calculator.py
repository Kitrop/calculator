import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout, QVBoxLayout, QPushButton

formatNumber = lambda n: n \
    if n % 1 \
    else int(n)


def do_not_run_twice(f, prev_args=[]):
    def wrapper(*args, **kwargs):
        if prev_args and args == prev_args[-1]:
            return None

        prev_args.append(args)

        return f(*args, **kwargs)

    return wrapper


def isNum(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


class Calculator(QWidget):
    def __init__(self):
        super(Calculator, self).__init__()

        # Vertical axis
        self.vbox = QVBoxLayout(self)
        self.hbox_input = QHBoxLayout()
        self.hbox_first = QHBoxLayout()
        self.hbox_result = QHBoxLayout()

        # Tie horizontal axis
        self.vbox.addLayout(self.hbox_input)
        self.vbox.addLayout(self.hbox_first)
        self.vbox.addLayout(self.hbox_result)

        # Create widgets
        self.input = QLineEdit(self)
        self.hbox_input.addWidget(self.input)

        self.b_1 = QPushButton("1", self)
        self.hbox_first.addWidget(self.b_1)

        self.b_2 = QPushButton("2", self)
        self.hbox_first.addWidget(self.b_2)

        self.b_3 = QPushButton("3", self)
        self.hbox_first.addWidget(self.b_3)

        self.b_plus = QPushButton("+", self)
        self.hbox_first.addWidget(self.b_plus)

        self.b_minus = QPushButton("-", self)
        self.hbox_first.addWidget(self.b_minus)

        self.b_mult = QPushButton("*", self)
        self.hbox_first.addWidget(self.b_mult)

        self.b_div = QPushButton("/", self)
        self.hbox_first.addWidget(self.b_div)

        self.b_dot = QPushButton(".", self)
        self.hbox_first.addWidget(self.b_dot)

        self.b_result = QPushButton("=", self)
        self.hbox_result.addWidget(self.b_result)
        ########################################

        # Widget handler
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

    def _button(self, param):
        line = self.input.text()
        count = self.input.text().count('.')
        self.input.setText(line + param)

    # @do_not_run_twice
    def _operation(self, op):
        self.num_1 = formatNumber(float(self.input.text()))
        self.op = op
        self.input.setText("")

    # Func calculations
    def _result(self):
        self.num_2 = formatNumber(float(self.input.text()))
        if self.op == "+" and isNum(self.num_2) == True and isNum(self.num_1) == True:
            self.input.setText(str(self.num_1 + self.num_2))

        if self.op == "-" and isNum(self.num_2) == True and isNum(self.num_1) == True:
            self.input.setText(str(self.num_1 - self.num_2))

        if self.op == "*" and isNum(self.num_2) and isNum(self.num_1):
            self.input.setText(str(self.num_1 * self.num_2))

        if self.op == "/" and self.num_1 != 0 and self.num_2 != 0 and isNum(self.num_2) == True and isNum(
                self.num_1) == True:
            self.input.setText(str(self.num_1 / self.num_2))


def application():
    app = QApplication(sys.argv)
    win = Calculator()
    win.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
