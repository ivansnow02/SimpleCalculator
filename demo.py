import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import setThemeColor
from qmaterialwidgets import setThemeColor as setThemeColor2

from app.view.main_window import Calculator

QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
app = QApplication(sys.argv)
ui = Calculator()
setThemeColor("#6750a4")
setThemeColor2("#6750a4")
ui.show()
sys.exit(app.exec_())
