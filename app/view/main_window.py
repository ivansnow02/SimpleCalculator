import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qframelesswindow.windows import WindowsWindowEffect
from qframelesswindow import AcrylicWindow


from app.view import home_interface, calendar_interface, exchange_rate_interface
from qfluentwidgets import FluentWindow, NavigationItemPosition
from qfluentwidgets import FluentIcon as FIF
from qfluentwidgets import setThemeColor
from qmaterialwidgets import setThemeColor as setThemeColor2



class Calculator(FluentWindow, AcrylicWindow):
    def __init__(self):
        super().__init__()
        self.windowEffect = WindowsWindowEffect(self)
        self.homeInterface = home_interface.HomeWidget(self)
        self.calendarInterface = calendar_interface.Calendar(self)
        self.exchangeRateInterface = exchange_rate_interface.ExchangeRate(self)
        self.setupUi()

    def setupUi(self):
        self.addSubInterface(self.homeInterface, icon=FIF.HOME, text="首页")
        self.addSubInterface(self.calendarInterface, icon=FIF.CALENDAR, text="日期计算")
        self.addSubInterface(self.exchangeRateInterface, icon=FIF.MARKET, text="汇率计算")
        self.setWindowTitle("Calculator")
        self.setStyleSheet("background:transparent")
        self.windowEffect.setAcrylicEffect(int(self.winId()), enableShadow=False)



if __name__ == '__main__':
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    app = QApplication(sys.argv)
    ui = Calculator()
    setThemeColor("#6750a4")
    setThemeColor2("#6750a4")
    ui.show()
    sys.exit(app.exec_())
