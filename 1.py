import sys

from math import factorial, sqrt

from PyQt5.QtWidgets import QApplication, QMainWindow
from calc import Ui_Dialog


class Calculator(QMainWindow, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.button_0.clicked.connect(lambda: self.nbt(0))
        self.button_1.clicked.connect(lambda: self.nbt(1))
        self.button_2.clicked.connect(lambda: self.nbt(2))
        self.button_3.clicked.connect(lambda: self.nbt(3))
        self.button_4.clicked.connect(lambda: self.nbt(4))
        self.button_5.clicked.connect(lambda: self.nbt(5))
        self.button_6.clicked.connect(lambda: self.nbt(6))
        self.button_7.clicked.connect(lambda: self.nbt(7))
        self.button_8.clicked.connect(lambda: self.nbt(8))
        self.button_9.clicked.connect(lambda: self.nbt(9))
        self.button_c.clicked.connect(lambda: self.lcdNumber.display(0))
        self.button_equal.clicked.connect(lambda: self.equal())
        self.button_plus.clicked.connect(lambda: self.operation_now('+'))
        self.button_minus.clicked.connect(lambda: self.operation_now('-'))
        self.button_mul.clicked.connect(lambda: self.operation_now('*'))
        self.button_div.clicked.connect(lambda: self.operation_now('/'))
        self.button_deg.clicked.connect(lambda: self.operation_now('**'))
        self.button_root.clicked.connect(lambda: self.root())
        self.button_factorial.clicked.connect(lambda: self.operation_now('fact'))

    def nbt(self, num):
        if self.lcdNumber.value() != 0:
            x = int(str(int(self.lcdNumber.value())) + str(num))
            self.lcdNumber.display(x)
        else:
            self.lcdNumber.display(num)

    def operation_now(self, oper):
        self.firs_value = self.lcdNumber.value()
        self.lcdNumber.display(0)
        self.oper = oper

    def equal(self):
        second_value = self.lcdNumber.value()
        if self.oper == '+':
            self.lcdNumber.display(self.firs_value + second_value)
        elif self.oper == '-':
            self.lcdNumber.display(self.firs_value - second_value)
        elif self.oper == '/':
            self.lcdNumber.display(self.firs_value / second_value)
        elif self.oper == '*':
            self.lcdNumber.display(self.firs_value * second_value)
        elif self.oper == '**':
            self.lcdNumber.display(self.firs_value ** second_value)

    def root(self):
        self.lcdNumber.display(sqrt(self.lcdNumber.value()))

    def fact(self):
        self.lcdNumber.display(factorial(int(self.lcdNumber.value())))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())