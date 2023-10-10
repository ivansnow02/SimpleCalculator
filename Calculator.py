import string
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from cal_mainwindow import Ui_MainWindow


def is_number(num):
    if num == '0b' or '0o' or '0x' or num.isdigit():
        return True
    else:
        return False


class Calculator(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.display = '0'

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        btn_string = 'button_'
        btn_id = [str(i) for i in range(10)] + [chr(i) for i in range(ord('a'), ord('f'))] + ['dot', 'plus', 'minus',
                                                                                              'mult',
                                                                                              'div', 'lb', 'rb', 'pow',
                                                                                              'mod',
                                                                                              '0b', '0o', '0x']
        for id in btn_id:
            btn = getattr(self, btn_string + id)
            btn.clicked.connect(self.deal_btn)
        self.button_ac.clicked.connect(self.clean_display)
        self.button_del.clicked.connect(self.del_num)
        self.button_equal.clicked.connect(self.calculate)
        self.button_bin.clicked.connect(self.change_to_bin)
        self.button_oct.clicked.connect(self.change_to_oct)
        self.button_hex.clicked.connect(self.change_to_hex)

    def deal_btn(self):
        sender = self.sender()
        input = sender.text()
        if self.is_display_not_ok() and is_number(input):
            self.display = input
        elif is_number(input):
            self.display += input
        else:
            self.display += ' ' + input + ' '
        self.display = self.display.lower()
        self.label.setText(self.display)

    def clean_display(self):
        self.display = '0'
        self.label.setText(self.display)

    def del_num(self):
        if self.is_display_not_ok():
            pass
        else:
            if self.display[-3] == '0b' or self.display[-1] == '0o' or self.display[-1] == '0x':
                self.display = self.display[:-2]
            elif self.display[-1] == ' ':
                self.display = self.display[:-3]
            else:
                self.display = self.display[:-1]
                if self.display == ' ':
                    self.display = '0'
        self.label.setText(self.display)

    def calculate(self):
        try:
            self.display = str(eval(self.display))
        except:
            self.display = 'Error'
        self.label.setText(self.display)

    def is_display_not_ok(self):
        if self.display == 'Error' or self.display == '0':
            return True
        else:
            return False

    def change_to_bin(self):
        try:
            self.display = bin(int(self.display))
        except:
            self.display = 'Error'
        self.label.setText(self.display)

    def change_to_oct(self):
        try:
            self.display = oct(int(self.display))
        except:
            self.display = 'Error'
        self.label.setText(self.display)

    def change_to_hex(self):
        try:
            self.display = hex(int(self.display))
        except:
            self.display = 'Error'
        self.label.setText(self.display)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Calculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
