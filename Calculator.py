import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qframelesswindow.windows import WindowsWindowEffect
from qframelesswindow import AcrylicWindow

from calendar import CalendarCal
from home import Home
from qfluentwidgets import FluentWindow
from qfluentwidgets import FluentIcon as FIF


class Calculator(FluentWindow, AcrylicWindow):
    def __init__(self):
        super().__init__()
        self.windowEffect = WindowsWindowEffect(self)
        self.homeInterface = Home.HomeWidget(self)
        self.calendarInterface = CalendarCal.Calendar(self)
        self.setupUi()

    def setupUi(self):
        self.addSubInterface(self.homeInterface, icon=FIF.HOME, text="首页")
        self.addSubInterface(self.calendarInterface, icon=FIF.CALENDAR, text="日期计算")
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background:transparent")
        self.windowEffect.setAcrylicEffect(int(self.winId()), enableShadow=False)


if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    ui = Calculator()

    ui.show()
    sys.exit(app.exec_())
