from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton
import sys


class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.my_input = []
        self.operand_1 = []
        self.operand_2 = []

    def initUI(self):
        self.setGeometry(300, 300, 300, 500)
        self.setWindowTitle("Калькулятор")

        self.label = QLabel(self)
        self.label.setText('0')
        self.label.resize(225, 95)
        self.move(0, 0)

        self.num_1 = QPushButton('1', self)
        self.num_1.resize(60, 60)
        self.num_1.move(12, 70)

        self.num_2 = QPushButton('2', self)
        self.num_2.resize(60, 60)
        self.num_2.move(84, 70)

        self.num_3 = QPushButton('3', self)
        self.num_3.resize(60, 60)
        self.num_3.move(156, 70)

        self.div = QPushButton('/', self)
        self.div.resize(60, 60)
        self.div.move(228, 70)

        self.num_4 = QPushButton('4', self)
        self.num_4.resize(60, 60)
        self.num_4.move(12, 140)

        self.num_5 = QPushButton('5', self)
        self.num_5.resize(60, 60)
        self.num_5.move(84, 140)

        self.num_6 = QPushButton('6', self)
        self.num_6.resize(60, 60)
        self.num_6.move(156, 140)

        self.mul = QPushButton('*', self)
        self.mul.resize(60, 60)
        self.mul.move(228, 140)

        self.num_7 = QPushButton('7', self)
        self.num_7.resize(60, 60)
        self.num_7.move(12, 210)

        self.num_8 = QPushButton('8', self)
        self.num_8.resize(60, 60)
        self.num_8.move(84, 210)

        self.num_9 = QPushButton('9', self)
        self.num_9.resize(60, 60)
        self.num_9.move(156, 210)

        self.plus = QPushButton('+', self)
        self.plus.resize(60, 60)
        self.plus.move(228, 210)

        self.num_0 = QPushButton('0', self)
        self.num_0.resize(60, 60)
        self.num_0.move(12, 280)

        self.minus = QPushButton('-', self)
        self.minus.resize(60, 60)
        self.minus.move(84, 280)

        self.step = QPushButton('^', self)
        self.step.resize(60, 60)
        self.step.move(156, 280)

        self.sqrt = QPushButton('√', self)
        self.sqrt.resize(60, 60)
        self.sqrt.move(228, 280)

        self.delen = QPushButton('%', self)
        self.delen.resize(60, 60)
        self.delen.move(12, 350)

        self.delenie = QPushButton('//', self)
        self.delenie.resize(60, 60)
        self.delenie.move(84, 350)

        self.kvadrat = QPushButton('x²', self)
        self.kvadrat.resize(60, 60)
        self.kvadrat.move(156, 350)

        self.ravn = QPushButton('=', self)
        self.ravn.resize(160, 60)
        self.ravn.move(70, 420)

        self.c = QPushButton('C', self)
        self.c.resize(60, 60)
        self.c.move(228, 350)

        self.num_1.clicked.connect(self.one)
        self.num_2.clicked.connect(self.two)
        self.num_3.clicked.connect(self.three)
        self.num_4.clicked.connect(self.four)
        self.num_5.clicked.connect(self.five)
        self.num_6.clicked.connect(self.six)
        self.num_7.clicked.connect(self.seven)
        self.num_8.clicked.connect(self.eight)
        self.num_9.clicked.connect(self.nine)
        self.num_0.clicked.connect(self.zero)
        self.plus.clicked.connect(self.plus_1)
        self.minus.clicked.connect(self.minus_1)
        self.mul.clicked.connect(self.mul_1)
        self.div.clicked.connect(self.div_1)
        self.step.clicked.connect(self.step_1)
        self.sqrt.clicked.connect(self.sqrt_1)
        self.ravn.clicked.connect(self.ravno)
        self.c.clicked.connect(self.clean)
        self.delen.clicked.connect(self.delen_1)
        self.delenie.clicked.connect(self.delenie_1)
        self.kvadrat.clicked.connect(self.kvadrat_1)

    def enterValue(self):
        if self.label.text() == '0':
            self.label.setText('')
        self.label.setText(self.label.text() + self.my_input)

    def one(self):
        self.my_input = '1'
        self.enterValue()

    def two(self):
        self.my_input = '2'
        self.enterValue()

    def three(self):
        self.my_input = '3'
        self.enterValue()

    def four(self):
        self.my_input = '4'
        self.enterValue()

    def five(self):
        self.my_input = '5'
        self.enterValue()

    def six(self):
        self.my_input = '6'
        self.enterValue()

    def seven(self):
        self.my_input = '7'
        self.enterValue()

    def eight(self):
        self.my_input = '8'
        self.enterValue()

    def nine(self):
        self.my_input = '9'
        self.enterValue()

    def zero(self):
        self.my_input = '0'
        self.enterValue()

    def plus_1(self):
        self.operation = '+'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def minus_1(self):
        self.operation = '-'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def mul_1(self):
        self.operation = '*'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def div_1(self):
        self.operation = '/'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def step_1(self):
        self.operation = '^'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def sqrt_1(self):
        self.operation = '√'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def delen_1(self):
        self.operation = '%'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def delenie_1(self):
        self.operation = '//'
        self.operand_1 = float(self.label.text())
        self.label.setText('')

    def kvadrat_1(self):
        self.operation = 'x²'
        self.operand_1 = float(self.label.text())
        self.label.setText('')
        self.rezult = self.operand_1 ** 2
        self.label.setText(str(self.rezult))

    def ravno(self):
        self.operand_2 = float(self.label.text())
        if self.operation == '+':
            self.rezult = self.operand_1 + self.operand_2
        elif self.operation == '-':
            self.rezult = self.operand_1 - self.operand_2
        elif self.operation == '*':
            self.rezult = self.operand_1 * self.operand_2
        elif self.operation == '/':
            if self.operand_2 == 0:
                self.rezult = 'error'
            else:
                self.rezult = self.operand_1 / self.operand_2
        elif self.operation == '^':
            self.rezult = self.operand_1 ** self.operand_2
        elif self.operation == '√':
            self.rezult = self.operand_1 ** (1 / self.operand_2)
        elif self.operation == '%':
            self.rezult = self.operand_1 % self.operand_2
        elif self.operation == '//':
            self.rezult = self.operand_1 // self.operand_2
        self.label.setText(str(self.rezult))

    def clean(self):
        self.label.setText('')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())