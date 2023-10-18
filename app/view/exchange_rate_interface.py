import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QFrame, QApplication

from app.common import rate_spider
from app.resource.ui.rate import Ui_Frame


class ExchangeRate(Ui_Frame, QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.rate_data = rate_spider.get_rate()
        self.setupUi(self)

    def setupUi(self, Frame):
        items = []
        super().setupUi(Frame)
        self.setObjectName("rate")
        self.button_cal.clicked.connect(self.calculate)
        self.button_ac.clicked.connect(self.clean)
        items = self.rate_data.keys()
        # self.ComboBox.setLabel("币种")
        self.ComboBox.addItems(items)
        self.ComboBox.setCurrentIndex(0)
        self.LineEdit.setPlaceholderText("请输入金额")

    def calculate(self):
        current_text = self.ComboBox.currentText()

        rate = self.rate_data[current_text]
        try:
            input = float(self.LineEdit.text())
            output = input * rate
            self.LineEdit_2.setText(str(output))
        except:
            self.LineEdit_2.setText("输入错误")

    def clean(self):
        self.LineEdit.setText("")
        self.LineEdit_2.setText("")


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    ui = ExchangeRate()

    ui.show()
    sys.exit(app.exec_())
