'''
@File  :test.py
@Author:Zhiwei Zheng
@Date  :6/21/2021 6:27 PM
@Desc  :
'''
import copy
import sys
from PyQt5 import QtWidgets
from GUI import Ui_Form
import functions as fc
import time


class MyPyQT_Form(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQT_Form, self).__init__()
        self.display_flag = False
        self.setupUi(self)
        self.procedure = None
        self.mode_flag = True
        self.step = 0
        # self.inputEight = [[], [], [], 0, 0]
        # self.expectedEight = [[], [], [], 0, 0]
        self.pushButton.clicked.connect(self.start_button)
        self.pushButton_2.clicked.connect(self.change_button)

    def change_display(self, procedure):
        first = procedure[0]
        second = procedure[1]
        third = procedure[2]
        change = []
        for i in first:
            if i == 0:
                change.append('')
            else:
                change.append(str(i))
        for i in second:
            if i == 0:
                change.append('')
            else:
                change.append(str(i))
        for i in third:
            if i == 0:
                change.append('')
            else:
                change.append(str(i))
        self.textEdit.setText(change[0])
        self.textEdit_2.setText(change[1])
        self.textEdit_3.setText(change[2])
        self.textEdit_4.setText(change[3])
        self.textEdit_6.setText(change[4])
        self.textEdit_5.setText(change[5])
        self.textEdit_7.setText(change[6])
        self.textEdit_9.setText(change[7])
        self.textEdit_8.setText(change[8])

    def start_button(self):
        self.procedure = None
        self.step = 0
        self.display_flag = False
        inputEight = [[], [], [], 0, 0]
        expectedEight = [[], [], [], 0, 0]
        judge = []
        if self.textEdit.toPlainText() == '':
            inputEight[0].append(0)
        else:
            judge.append(int(self.textEdit.toPlainText()))
            inputEight[0].append(int(self.textEdit.toPlainText()))

        if self.textEdit_2.toPlainText() == '':
            inputEight[0].append(0)
        else:
            judge.append(int(self.textEdit_2.toPlainText()))
            inputEight[0].append(int(self.textEdit_2.toPlainText()))

        if self.textEdit_3.toPlainText() == '':
            inputEight[0].append(0)
        else:
            judge.append(int(self.textEdit_3.toPlainText()))
            inputEight[0].append(int(self.textEdit_3.toPlainText()))

        if self.textEdit_4.toPlainText() == '':
            inputEight[1].append(0)
        else:
            judge.append(int(self.textEdit_4.toPlainText()))
            inputEight[1].append(int(self.textEdit_4.toPlainText()))

        if self.textEdit_6.toPlainText() == '':
            inputEight[1].append(0)
        else:
            judge.append(int(self.textEdit_6.toPlainText()))
            inputEight[1].append(int(self.textEdit_6.toPlainText()))

        if self.textEdit_5.toPlainText() == '':
            inputEight[1].append(0)
        else:
            judge.append(int(self.textEdit_5.toPlainText()))
            inputEight[1].append(int(self.textEdit_5.toPlainText()))

        if self.textEdit_7.toPlainText() == '':
            inputEight[2].append(0)
        else:
            judge.append(int(self.textEdit_7.toPlainText()))
            inputEight[2].append(int(self.textEdit_7.toPlainText()))

        if self.textEdit_9.toPlainText() == '':
            inputEight[2].append(0)
        else:
            judge.append(int(self.textEdit_9.toPlainText()))
            inputEight[2].append(int(self.textEdit_9.toPlainText()))

        if self.textEdit_8.toPlainText() == '':
            inputEight[2].append(0)
        else:
            judge.append(int(self.textEdit_8.toPlainText()))
            inputEight[2].append(int(self.textEdit_8.toPlainText()))

        flag_1 = True
        temp = set(judge)
        if len(temp) != 8:
            flag_1 = False
        else:
            for i in judge:
                if i > 8 or i < 0:
                    flag_1 = False
                    break

        judge = []
        if self.textEdit_10.toPlainText() == '':
            expectedEight[0].append(0)
        else:
            judge.append(int(self.textEdit_10.toPlainText()))
            expectedEight[0].append(int(self.textEdit_10.toPlainText()))

        if self.textEdit_18.toPlainText() == '':
            expectedEight[0].append(0)
        else:
            judge.append(int(self.textEdit_18.toPlainText()))
            expectedEight[0].append(int(self.textEdit_18.toPlainText()))

        if self.textEdit_13.toPlainText() == '':
            expectedEight[0].append(0)
        else:
            judge.append(int(self.textEdit_13.toPlainText()))
            expectedEight[0].append(int(self.textEdit_13.toPlainText()))

        if self.textEdit_11.toPlainText() == '':
            expectedEight[1].append(0)
        else:
            judge.append(int(self.textEdit_11.toPlainText()))
            expectedEight[1].append(int(self.textEdit_11.toPlainText()))

        if self.textEdit_12.toPlainText() == '':
            expectedEight[1].append(0)
        else:
            judge.append(int(self.textEdit_12.toPlainText()))
            expectedEight[1].append(int(self.textEdit_12.toPlainText()))

        if self.textEdit_17.toPlainText() == '':
            expectedEight[1].append(0)
        else:
            judge.append(int(self.textEdit_17.toPlainText()))
            expectedEight[1].append(int(self.textEdit_17.toPlainText()))

        if self.textEdit_14.toPlainText() == '':
            expectedEight[2].append(0)
        else:
            judge.append(int(self.textEdit_14.toPlainText()))
            expectedEight[2].append(int(self.textEdit_14.toPlainText()))

        if self.textEdit_16.toPlainText() == '':
            expectedEight[2].append(0)
        else:
            judge.append(int(self.textEdit_16.toPlainText()))
            expectedEight[2].append(int(self.textEdit_16.toPlainText()))

        if self.textEdit_15.toPlainText() == '':
            expectedEight[2].append(0)
        else:
            judge.append(int(self.textEdit_15.toPlainText()))
            expectedEight[2].append(int(self.textEdit_15.toPlainText()))

        flag_2 = True
        temp = set(judge)
        if len(temp) != 8:
            flag_2 = False
        else:
            for i in judge:
                if i > 8 or i < 0:
                    flag_2 = False
                    break
        self.mode_flag = True
        if self.checkBox.isChecked():
            mode = '1'
        elif self.checkBox_2.isChecked():
            mode = '2'
        elif self.checkBox_3.isChecked():
            mode = '3'
        elif self.checkBox_4.isChecked():
            mode = '4'
        elif self.checkBox_5.isChecked():
            mode = '5'
        else:
            self.mode_flag = False
        if expectedEight != inputEight:
            if flag_1 and flag_2:
                if self.mode_flag:
                    if fc.judge(inputEight, expectedEight):
                        # mode choice
                        openTable = [expectedEight]
                        closeTable = []
                        valueTable = [fc.aStarOne(inputEight, expectedEight)]

                        while 1:
                            flag, index1 = fc.overCondition(inputEight, openTable)
                            if flag:
                                print("results:")
                                temp_closeTable = copy.deepcopy(closeTable)
                                self.procedure = []
                                self.flashBack(openTable[index1], temp_closeTable)
                                print('1', self.procedure)
                                break
                            minIndex = valueTable.index(min(valueTable))
                            temp_list = [openTable[minIndex]]

                            for i in range(len(temp_list)):
                                index2 = openTable.index(temp_list[i])
                                fc.extend(temp_list[i], inputEight, openTable, valueTable, closeTable, mode, index2)

                        print("扩展的节点个数{}".format(len(openTable) + len(closeTable)))
                        self.textBrowser_3.setText('点击Next Step进行演示'+'\n'+'method' + mode +'   '
                                                   "扩展的节点个数{}".format(len(openTable) + len(closeTable)))
                        self.display_flag = True

                        # display
                    else:
                        self.textBrowser_3.setText("Cannot be solved.")
                else:
                    self.textBrowser_3.setText("Method not allowed.")

            else:
                self.textBrowser_3.setText("Only numbers from 0 to 8 are allowed.")
        else:
            self.textBrowser_3.setText("Two matrix are the same.")

    def change_button(self):
        if self.display_flag:
            print('0')
            length = len(self.procedure)
            print(length)
            if self.step < length:
                print('1')
                self.change_display(self.procedure[self.step])
                self.step += 1
            else:
                self.textBrowser_3.setText("Done.")

        else:
            self.textBrowser_3.setText("Processing. Please wait.")

    def flashBack(self, data, temp_closeTable):
        '''从初始八数码回溯至目标八数码'''

        self.procedure.append(data)
        print(data)
        tempTable = []
        '''将上一层的八数码移入tempTable'''
        for item in temp_closeTable:
            if item[3] == data[3] - 1:
                tempTable.append(item)

        for item in tempTable:
            if abs(fc.errorNum(item, data)) == 1:
                break
        if item[3] == 0:
            self.procedure.append(item)
            print(item)

        else:
            self.flashBack(item, temp_closeTable)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    my_pyqt_form = MyPyQT_Form()
    my_pyqt_form.show()
    sys.exit(app.exec_())
