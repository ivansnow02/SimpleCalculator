import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import cal_mainwindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = cal_mainwindow.CalculatorMainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
