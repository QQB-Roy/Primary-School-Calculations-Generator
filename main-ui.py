# -*- coding: utf-8 -*-
#小学计算题生成器
#Primary School Calculation Generator

import random,os,time
from PyQt5 import QtCore, QtGui, QtWidgets

# 获取当前时间
t = time.strftime("%m月%d日 %H时%M分%S秒")

# 定义运算符号和对应的操作
operations = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    'x': lambda x, y: x * y,
    '÷': lambda x, y: x / y
}

#公因数计算
def factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(400, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(400, 300))
        Form.setMaximumSize(QtCore.QSize(400, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./QQB.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.checkBox_4 = QtWidgets.QCheckBox(Form)
        self.checkBox_4.setGeometry(QtCore.QRect(270, 160, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setKerning(False)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setInputMethodHints(QtCore.Qt.ImhNone)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(270, 120, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setKerning(False)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(270, 140, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setKerning(False)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setInputMethodHints(QtCore.Qt.ImhNone)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(270, 100, 51, 20))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setKerning(False)
        self.checkBox.setFont(font)
        self.checkBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.checkBox.setObjectName("checkBox")
        self.spinBox = QtWidgets.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(110, 100, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(Form)
        self.spinBox_2.setGeometry(QtCore.QRect(110, 130, 42, 22))
        self.spinBox_2.setObjectName("spinBox_2")
        self.spinBox_3 = QtWidgets.QSpinBox(Form)
        self.spinBox_3.setGeometry(QtCore.QRect(110, 160, 42, 22))
        self.spinBox_3.setObjectName("spinBox_3")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(140, 220, 100, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(40, 100, 60, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setKerning(True)
        self.textBrowser.setFont(font)
        self.textBrowser.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser.setMouseTracking(False)
        self.textBrowser.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser.setAcceptDrops(True)
        self.textBrowser.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textBrowser.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser.setLineWidth(1)
        self.textBrowser.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser.setTabChangesFocus(False)
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(40, 130, 60, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setKerning(True)
        self.textBrowser_2.setFont(font)
        self.textBrowser_2.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser_2.setMouseTracking(False)
        self.textBrowser_2.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_2.setAcceptDrops(True)
        self.textBrowser_2.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser_2.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textBrowser_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_2.setLineWidth(1)
        self.textBrowser_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_2.setTabChangesFocus(False)
        self.textBrowser_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(40, 160, 60, 30))
        font = QtGui.QFont()
        font.setFamily("宋体")
        font.setKerning(True)
        self.textBrowser_3.setFont(font)
        self.textBrowser_3.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textBrowser_3.setMouseTracking(False)
        self.textBrowser_3.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.textBrowser_3.setAcceptDrops(True)
        self.textBrowser_3.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.textBrowser_3.setInputMethodHints(QtCore.Qt.ImhMultiLine)
        self.textBrowser_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textBrowser_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textBrowser_3.setLineWidth(1)
        self.textBrowser_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textBrowser_3.setTabChangesFocus(False)
        self.textBrowser_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # 将生成按钮的 clicked 信号连接到函数
        self.pushButton.clicked.connect(self.question_output)
    

    def question_output(self):
        maxnum = int(self.spinBox.value())
        minnum = int(self.spinBox_2.value())
        total = int(self.spinBox_3.value())
        symbols = []

        if self.checkBox.isChecked() == True:
             symbols.append("+")
        if self.checkBox_2.isChecked() == True:
             symbols.append("-")
        if self.checkBox_3.isChecked() == True:
             symbols.append("x")
        if self.checkBox_4.isChecked() == True:
             symbols.append("÷")


        if maxnum == minnum or total <= 0:
            print ("认真的？")
            reply = QtWidgets.QMessageBox.warning(
                Form, "警告", "认真的？", QtWidgets.QMessageBox.Yes
            )
        elif maxnum == minnum == 0:
             print ("这还要算吗？")
             reply = QtWidgets.QMessageBox.warning(
                Form, "警告", "这还要算吗？", QtWidgets.QMessageBox.Yes
            )
        elif maxnum < minnum :
             print ("大小搞反了哦！")
             reply = QtWidgets.QMessageBox.warning(
                Form, "警告", "大小搞反了哦！", QtWidgets.QMessageBox.Yes
            )
        elif symbols == [] :
             print ("没有符号怎么算？")
             reply = QtWidgets.QMessageBox.warning(
                Form, "警告", "没有符号怎么算？", QtWidgets.QMessageBox.Yes
            )
        else:
             #运算
             while total >= 0 :
                num1 = random.randint(minnum,maxnum)
                num2 = random.randint(minnum,maxnum)

             # 从列表中抽取一个符号 
                chosen_symbol = random.choice(symbols)


                if chosen_symbol in ('-','÷') and num1 < num2:
                        num1,num2 = num2,num1       
                        #print ("-")
                        pass
                elif chosen_symbol == '÷' and (num1 == 0 or num2 == 0):
                        #print ("÷")
                        continue
                if chosen_symbol == '÷':
                        num1_factors = factors(num1)
                        num2 = random.choice(num1_factors)
                        pass

                result = operations[chosen_symbol](num1, num2)
                
                #新建文件夹
                if self.pushButton.clicked:
                    folder_name = './' + t
                    if not os.path.exists(folder_name):
                        os.makedirs(folder_name)

                    question_file = folder_name + '/题目.txt'
                    answer_file = folder_name + '/答案.txt'


                #输出部分
                with open(question_file, 'a', encoding='utf-8') as qf:
                        qf.write(f"{num1} {chosen_symbol} {num2} = \n")

                with open(answer_file, 'a', encoding='utf-8') as af:
                        af.write(f"{num1} {chosen_symbol} {num2} = {result}\n")

                print(f"{num1} {chosen_symbol} {num2} = ")
                print(f"{num1} {chosen_symbol} {num2} = {result}")

                total = total - 1
                if total == 0:
                     reply = QtWidgets.QMessageBox.information(
                          Form, 
                          "小学计算题生成器", f"生成完毕,结果也保存到{t}", 
                          QtWidgets.QMessageBox.Yes
                          )




    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "小学计算题生成器"))
        self.checkBox_4.setText(_translate("Form", "÷"))
        self.checkBox_2.setText(_translate("Form", "-"))
        self.checkBox_3.setText(_translate("Form", "x"))
        self.checkBox.setText(_translate("Form", "+"))
        self.pushButton.setText(_translate("Form", "生成"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">最大值</span><span style=\" font-family:\'SimSun\';\"> </span></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">最小值</span><span style=\" font-family:\'SimSun\';\"> </span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'SimSun\'; font-size:12pt;\">总数</span><span style=\" font-family:\'SimSun\';\"> </span></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
