# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\app\resource\ui\calendar.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(544, 488)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        Frame.setFont(font)
        self.gridLayout_3 = QtWidgets.QGridLayout(Frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.BodyLabel = BodyLabel(Frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel.setFont(font)
        self.BodyLabel.setStyleSheet("BodyLabel{\n"
"    color: #6750a4;\n"
"\n"
" \n"
"    background-color: transparent;\n"
"}")
        self.BodyLabel.setObjectName("BodyLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.BodyLabel)
        self.CalendarPicker_begin = CalendarPicker(Frame)
        self.CalendarPicker_begin.setObjectName("CalendarPicker_begin")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.CalendarPicker_begin)
        self.BodyLabel_2 = BodyLabel(Frame)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel_2.setFont(font)
        self.BodyLabel_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.BodyLabel_2.setStyleSheet("BodyLabel{\n"
"    color: #6750a4;\n"
"\n"
" \n"
"    background-color: transparent;\n"
"}")
        self.BodyLabel_2.setObjectName("BodyLabel_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.BodyLabel_2)
        self.CalendarPicker_end = CalendarPicker(Frame)
        self.CalendarPicker_end.setObjectName("CalendarPicker_end")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.CalendarPicker_end)
        self.button_ac = ElevatedPushButton(Frame)
        self.button_ac.setBorderRadius(10)
        self.button_ac.setObjectName("button_ac")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.button_ac)
        self.button_cal = ElevatedPushButton(Frame)
        self.button_cal.setBorderRadius(10)
        self.button_cal.setObjectName("button_cal")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.button_cal)
        self.label = BodyLabel(Frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 169))
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(19)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("BodyLabel{\n"
"    color: #6750a4;\n"
"\n"
"    padding: 8px 24px 9px 24px;\n"
"    outline: none;\n"
"    border: 3px outset #6750a4;\n"
"    border-radius: 10px;\n"
"    background-color: transparent;\n"
"}")
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.label)
        self.gridLayout_3.addLayout(self.formLayout, 0, 1, 1, 1)

        self.retranslateUi(Frame)
        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.BodyLabel.setText(_translate("Frame", "起始日期"))
        self.BodyLabel_2.setText(_translate("Frame", "结束日期"))
        self.button_ac.setText(_translate("Frame", "清空"))
        self.button_cal.setText(_translate("Frame", "计算"))
        self.label.setText(_translate("Frame", "Body label"))
from qmaterialwidgets import BodyLabel, CalendarPicker, ElevatedPushButton
