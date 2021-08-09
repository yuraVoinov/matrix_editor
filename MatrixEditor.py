from PyQt5 import QtCore, QtGui, QtWidgets
from matrix_class import MatrixClass
from math import nan

class Ui_MainWindow(object):

    def __init__(self):
        self.matrix = MatrixClass()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(656, 353)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowser_matrix = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_matrix.setGeometry(QtCore.QRect(10, 20, 311, 311))
        self.textBrowser_matrix.setObjectName("textBrowser_matrix")
        self.pushButton_openFile = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_openFile.setGeometry(QtCore.QRect(340, 20, 93, 91))
        self.pushButton_openFile.setObjectName("pushButton_openFile")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(440, 20, 199, 96))
        self.widget.setObjectName("widget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.spinBox_rows_randomFill = QtWidgets.QSpinBox(self.widget)
        self.spinBox_rows_randomFill.setObjectName("spinBox_rows_randomFill")
        self.gridLayout.addWidget(self.spinBox_rows_randomFill, 1, 1, 1, 1)
        self.spinBox_columns_randomFill = QtWidgets.QSpinBox(self.widget)
        self.spinBox_columns_randomFill.setObjectName("spinBox_columns_randomFill")
        self.gridLayout.addWidget(self.spinBox_columns_randomFill, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.pushButton_randomFill = QtWidgets.QPushButton(self.widget)
        self.pushButton_randomFill.setObjectName("pushButton_randomFill")
        self.gridLayout.addWidget(self.pushButton_randomFill, 0, 0, 1, 2)
        self.gridLayout_5.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.pushButton_swapColumns = QtWidgets.QPushButton(self.widget)
        self.pushButton_swapColumns.setObjectName("pushButton_swapColumns")
        self.gridLayout_3.addWidget(self.pushButton_swapColumns, 0, 0, 1, 2)
        self.pushButton_swapRows = QtWidgets.QPushButton(self.widget)
        self.pushButton_swapRows.setObjectName("pushButton_swapRows")
        self.gridLayout_3.addWidget(self.pushButton_swapRows, 1, 0, 1, 2)
        self.spinBox_swap_first = QtWidgets.QSpinBox(self.widget)
        self.spinBox_swap_first.setObjectName("spinBox_swap_first")
        self.gridLayout_3.addWidget(self.spinBox_swap_first, 2, 0, 1, 1)
        self.spinBox_swap_second = QtWidgets.QSpinBox(self.widget)
        self.spinBox_swap_second.setObjectName("spinBox_swap_second")
        self.gridLayout_3.addWidget(self.spinBox_swap_second, 2, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 0, 1, 1, 1)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(341, 124, 301, 141))
        self.widget1.setObjectName("widget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.textBrowser_printInfo = QtWidgets.QTextBrowser(self.widget1)
        self.textBrowser_printInfo.setObjectName("textBrowser_printInfo")
        self.gridLayout_2.addWidget(self.textBrowser_printInfo, 0, 0, 1, 1)
        self.pushButton_maxElement = QtWidgets.QPushButton(self.widget1)
        self.pushButton_maxElement.setObjectName("pushButton_maxElement")
        self.gridLayout_2.addWidget(self.pushButton_maxElement, 1, 0, 1, 1)
        self.pushButton_maxRow = QtWidgets.QPushButton(self.widget1)
        self.pushButton_maxRow.setObjectName("pushButton_maxRow")
        self.gridLayout_2.addWidget(self.pushButton_maxRow, 2, 0, 1, 1)
        self.pushButton_maxColumn = QtWidgets.QPushButton(self.widget1)
        self.pushButton_maxColumn.setObjectName("pushButton_maxColumn")
        self.gridLayout_2.addWidget(self.pushButton_maxColumn, 3, 0, 1, 1)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(340, 270, 301, 65))
        self.widget2.setObjectName("widget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.pushButton_printRow = QtWidgets.QPushButton(self.widget2)
        self.pushButton_printRow.setObjectName("pushButton_printRow")
        self.gridLayout_4.addWidget(self.pushButton_printRow, 0, 0, 1, 1)
        self.spinBox_printRowColumn = QtWidgets.QSpinBox(self.widget2)
        self.spinBox_printRowColumn.setObjectName("spinBox_printRowColumn")
        self.gridLayout_4.addWidget(self.spinBox_printRowColumn, 0, 1, 2, 1)
        self.pushButton_printColumn = QtWidgets.QPushButton(self.widget2)
        self.pushButton_printColumn.setObjectName("pushButton_printColumn")
        self.gridLayout_4.addWidget(self.pushButton_printColumn, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_randomFill.clicked.connect(self.pushButton_random_fill_clicked)

        self.pushButton_swapRows.clicked.connect(self.pushButton_swap_rows_clicked)

        self.pushButton_swapColumns.clicked.connect(self.pushButton_swap_columns_clicked)

        self.pushButton_maxElement.clicked.connect(self.pushButton_max_element_clicked)

        self.pushButton_maxRow.clicked.connect(self.pushButton_max_row_clicked)

        self.pushButton_maxColumn.clicked.connect(self.pushButton_max_column_clicked)

        self.pushButton_printRow.clicked.connect(self.pushButton_print_row)

        self.pushButton_printColumn.clicked.connect(self.pushButton_print_column)

        self.pushButton_openFile.clicked.connect(self.pushButton_open_file_clicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MatrixEditor"))
        self.pushButton_openFile.setText(_translate("MainWindow", "Open file"))
        self.label_2.setText(_translate("MainWindow", "columns"))
        self.label.setText(_translate("MainWindow", "rows"))
        self.pushButton_randomFill.setText(_translate("MainWindow", "Random fill"))
        self.pushButton_swapColumns.setText(_translate("MainWindow", "Swap columns"))
        self.pushButton_swapRows.setText(_translate("MainWindow", "Swap rows"))
        self.pushButton_maxElement.setText(_translate("MainWindow", "Max element"))
        self.pushButton_maxRow.setText(_translate("MainWindow", "Max row (sum)"))
        self.pushButton_maxColumn.setText(_translate("MainWindow", "Max column (sum)"))
        self.pushButton_printRow.setText(_translate("MainWindow", "Print row"))
        self.pushButton_printColumn.setText(_translate("MainWindow", "Print column"))


    def pushButton_random_fill_clicked(self):

        rows = self.spinBox_rows_randomFill.value()
        columns = self.spinBox_columns_randomFill.value()

        self.matrix.random_fill(rows, columns)
        self.textBrowser_matrix.setText(self.matrix.to_string())

    def pushButton_swap_rows_clicked(self):

        first = self.spinBox_swap_first.value()
        second = self.spinBox_swap_second.value()

        if not self.matrix.matrix:
            return self.textBrowser_matrix.setText(str(self.matrix.swap_rows(first, second)))

        self.matrix.swap_rows(first, second)
        self.textBrowser_matrix.setText(self.matrix.to_string())

    def pushButton_swap_columns_clicked(self):

        first = self.spinBox_swap_first.value()
        second = self.spinBox_swap_second.value()

        if not self.matrix.matrix:
            return self.textBrowser_matrix.setText(str(self.matrix.swap_columns(first, second)))

        self.matrix.swap_columns(first, second)
        self.textBrowser_matrix.setText(self.matrix.to_string())

    def pushButton_max_element_clicked(self):
        if not self.matrix.matrix:
            return self.textBrowser_printInfo.setText(str(self.matrix.find_max_element()))
        max_element, max_row_index, max_column_index = self.matrix.find_max_element()
        self.textBrowser_printInfo.setText(f"Max element is : {max_element}, {max_row_index+1} row, {max_column_index+1} column")

    def pushButton_max_row_clicked(self):
        if not self.matrix.matrix:
            return self.textBrowser_printInfo.setText(str(self.matrix.max_row()))
        max_row_index, max_row_sum = self.matrix.max_row()
        self.textBrowser_printInfo.setText(f"Index of max row is {max_row_index + 1}, sum: {max_row_sum}")

    def pushButton_max_column_clicked(self):
        if not self.matrix.matrix:
            return self.textBrowser_printInfo.setText(str(self.matrix.max_column()))
        max_column_index, max_column_sum = self.matrix.max_column()
        self.textBrowser_printInfo.setText(f"Index of max column is {max_column_index+1}, sum: {max_column_sum}")

    def pushButton_print_row(self):
        row_index = self.spinBox_printRowColumn.value()
        if not self.matrix.matrix:
            return self.textBrowser_printInfo.setText(str(self.matrix.row_print(row_index)))
        self.textBrowser_printInfo.setText(str(self.matrix.row_print(row_index)))

    def pushButton_print_column(self):
        column_index = self.spinBox_printRowColumn.value()
        if not self.matrix.matrix:
            return self.textBrowser_printInfo.setText(str(self.matrix.column_print(column_index)))
        self.textBrowser_printInfo.setText(str(self.matrix.column_print(column_index)))

    def pushButton_open_file_clicked(self):
        self.matrix.read_file()
        self.textBrowser_matrix.setText(self.matrix.to_string())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

