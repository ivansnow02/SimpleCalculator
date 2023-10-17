import sys

from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QFrame, QApplication

from ui.calendar import Ui_Frame


class Calendar(Ui_Frame, QFrame):
    def __init__(self, parent=None):
        super().__init__(parent=parent)


        self.display = "中间经过0天"
        self.setupUi(self)


    def setupUi(self, Frame):
        super().setupUi(Frame)
        self.setObjectName("calendar")
        self.button_cal.clicked.connect(self.calculate)
        self.button_ac.clicked.connect(self.clean)
        self.CalendarPicker_begin.date = self.CalendarPicker_end.date = QDate.currentDate()
        self.label.setText(self.display)

    def calculate(self):
        try:
            begin_date = self.CalendarPicker_begin.date
            end_date = self.CalendarPicker_end.date
            begin_date = begin_date.toPyDate()
            end_date = end_date.toPyDate()
            days = (end_date - begin_date).days
            self.display = "中间经过" + str(days) + "天"
            self.label.setText(self.display)
        except:
            self.display = "输入错误"
            self.label.setText(self.display)

    def clean(self):
        self.CalendarPicker_begin.date = self.CalendarPicker_end.date = QDate.currentDate()
        self.display = "中间经过0天"
        self.label.setText(self.display)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    ui = Calendar()

    ui.show()
    sys.exit(app.exec_())
