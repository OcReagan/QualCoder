# Form implementation generated from reading ui file 'ui_dialog_charts.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogCharts(object):
    def setupUi(self, DialogCharts):
        DialogCharts.setObjectName("DialogCharts")
        DialogCharts.resize(1011, 597)
        self.label_info = QtWidgets.QLabel(DialogCharts)
        self.label_info.setGeometry(QtCore.QRect(9, 9, 391, 22))
        self.label_info.setObjectName("label_info")
        self.label_pie = QtWidgets.QLabel(DialogCharts)
        self.label_pie.setGeometry(QtCore.QRect(10, 80, 311, 22))
        self.label_pie.setObjectName("label_pie")
        self.label_bar = QtWidgets.QLabel(DialogCharts)
        self.label_bar.setGeometry(QtCore.QRect(10, 143, 291, 22))
        self.label_bar.setObjectName("label_bar")
        self.comboBox_pie_charts = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_pie_charts.setGeometry(QtCore.QRect(10, 110, 321, 25))
        self.comboBox_pie_charts.setObjectName("comboBox_pie_charts")
        self.comboBox_bar_charts = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_bar_charts.setGeometry(QtCore.QRect(10, 170, 321, 25))
        self.comboBox_bar_charts.setObjectName("comboBox_bar_charts")
        self.comboBox_sunburst_charts = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_sunburst_charts.setGeometry(QtCore.QRect(10, 225, 321, 25))
        self.comboBox_sunburst_charts.setObjectName("comboBox_sunburst_charts")
        self.label_hierarchy = QtWidgets.QLabel(DialogCharts)
        self.label_hierarchy.setGeometry(QtCore.QRect(10, 200, 291, 22))
        self.label_hierarchy.setObjectName("label_hierarchy")
        self.label_coder = QtWidgets.QLabel(DialogCharts)
        self.label_coder.setGeometry(QtCore.QRect(410, 103, 151, 22))
        self.label_coder.setObjectName("label_coder")
        self.comboBox_coders = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_coders.setGeometry(QtCore.QRect(410, 130, 321, 25))
        self.comboBox_coders.setObjectName("comboBox_coders")
        self.comboBox_file = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_file.setGeometry(QtCore.QRect(410, 190, 321, 25))
        self.comboBox_file.setObjectName("comboBox_file")
        self.label_select_file = QtWidgets.QLabel(DialogCharts)
        self.label_select_file.setGeometry(QtCore.QRect(410, 160, 231, 22))
        self.label_select_file.setObjectName("label_select_file")
        self.comboBox_case = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_case.setGeometry(QtCore.QRect(410, 250, 321, 25))
        self.comboBox_case.setObjectName("comboBox_case")
        self.label_select_case = QtWidgets.QLabel(DialogCharts)
        self.label_select_case.setGeometry(QtCore.QRect(410, 220, 211, 22))
        self.label_select_case.setObjectName("label_select_case")
        self.pushButton_attributes = QtWidgets.QPushButton(DialogCharts)
        self.pushButton_attributes.setGeometry(QtCore.QRect(410, 350, 231, 25))
        self.pushButton_attributes.setObjectName("pushButton_attributes")
        self.label_filter = QtWidgets.QLabel(DialogCharts)
        self.label_filter.setGeometry(QtCore.QRect(408, 76, 201, 22))
        self.label_filter.setObjectName("label_filter")
        self.lineEdit_filter = QtWidgets.QLineEdit(DialogCharts)
        self.lineEdit_filter.setGeometry(QtCore.QRect(640, 77, 91, 25))
        self.lineEdit_filter.setText("")
        self.lineEdit_filter.setObjectName("lineEdit_filter")
        self.label_filters = QtWidgets.QLabel(DialogCharts)
        self.label_filters.setGeometry(QtCore.QRect(410, 50, 321, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_filters.setFont(font)
        self.label_filters.setObjectName("label_filters")
        self.label_chart_options = QtWidgets.QLabel(DialogCharts)
        self.label_chart_options.setGeometry(QtCore.QRect(10, 50, 311, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_chart_options.setFont(font)
        self.label_chart_options.setObjectName("label_chart_options")
        self.comboBox_category = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_category.setGeometry(QtCore.QRect(410, 310, 321, 25))
        self.comboBox_category.setObjectName("comboBox_category")
        self.label_category = QtWidgets.QLabel(DialogCharts)
        self.label_category.setGeometry(QtCore.QRect(410, 280, 151, 22))
        self.label_category.setObjectName("label_category")
        self.line = QtWidgets.QFrame(DialogCharts)
        self.line.setGeometry(QtCore.QRect(360, 50, 20, 521))
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.label_chart_attributes = QtWidgets.QLabel(DialogCharts)
        self.label_chart_attributes.setGeometry(QtCore.QRect(10, 390, 261, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_chart_attributes.setFont(font)
        self.label_chart_attributes.setObjectName("label_chart_attributes")
        self.label_num_attr = QtWidgets.QLabel(DialogCharts)
        self.label_num_attr.setGeometry(QtCore.QRect(10, 516, 291, 22))
        self.label_num_attr.setObjectName("label_num_attr")
        self.label_char_attr = QtWidgets.QLabel(DialogCharts)
        self.label_char_attr.setGeometry(QtCore.QRect(10, 457, 291, 22))
        self.label_char_attr.setObjectName("label_char_attr")
        self.comboBox_num_attributes = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_num_attributes.setGeometry(QtCore.QRect(10, 543, 321, 25))
        self.comboBox_num_attributes.setObjectName("comboBox_num_attributes")
        self.comboBox_char_attributes = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_char_attributes.setGeometry(QtCore.QRect(10, 480, 321, 25))
        self.comboBox_char_attributes.setObjectName("comboBox_char_attributes")
        self.line_2 = QtWidgets.QFrame(DialogCharts)
        self.line_2.setGeometry(QtCore.QRect(10, 370, 331, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_2.setObjectName("line_2")
        self.groupBox = QtWidgets.QGroupBox(DialogCharts)
        self.groupBox.setGeometry(QtCore.QRect(10, 391, 321, 61))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.radioButton_file = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_file.setGeometry(QtCore.QRect(0, 30, 112, 23))
        self.radioButton_file.setChecked(True)
        self.radioButton_file.setObjectName("radioButton_file")
        self.radioButton_case = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_case.setGeometry(QtCore.QRect(120, 30, 112, 23))
        self.radioButton_case.setObjectName("radioButton_case")
        self.checkBox_export_html = QtWidgets.QCheckBox(DialogCharts)
        self.checkBox_export_html.setGeometry(QtCore.QRect(430, 10, 301, 23))
        self.checkBox_export_html.setObjectName("checkBox_export_html")
        self.label_chart_options_2 = QtWidgets.QLabel(DialogCharts)
        self.label_chart_options_2.setGeometry(QtCore.QRect(10, 280, 261, 22))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label_chart_options_2.setFont(font)
        self.label_chart_options_2.setObjectName("label_chart_options_2")
        self.line_3 = QtWidgets.QFrame(DialogCharts)
        self.line_3.setGeometry(QtCore.QRect(10, 30, 721, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(DialogCharts)
        self.line_4.setGeometry(QtCore.QRect(10, 260, 331, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line_4.setObjectName("line_4")
        self.comboBox_heatmap = QtWidgets.QComboBox(DialogCharts)
        self.comboBox_heatmap.setGeometry(QtCore.QRect(10, 310, 321, 25))
        self.comboBox_heatmap.setObjectName("comboBox_heatmap")
        self.groupBox.raise_()
        self.label_info.raise_()
        self.label_pie.raise_()
        self.label_bar.raise_()
        self.comboBox_pie_charts.raise_()
        self.comboBox_bar_charts.raise_()
        self.comboBox_sunburst_charts.raise_()
        self.label_hierarchy.raise_()
        self.label_coder.raise_()
        self.comboBox_coders.raise_()
        self.comboBox_file.raise_()
        self.label_select_file.raise_()
        self.comboBox_case.raise_()
        self.label_select_case.raise_()
        self.pushButton_attributes.raise_()
        self.label_filter.raise_()
        self.lineEdit_filter.raise_()
        self.label_filters.raise_()
        self.label_chart_options.raise_()
        self.comboBox_category.raise_()
        self.label_category.raise_()
        self.line.raise_()
        self.label_chart_attributes.raise_()
        self.label_num_attr.raise_()
        self.label_char_attr.raise_()
        self.comboBox_num_attributes.raise_()
        self.comboBox_char_attributes.raise_()
        self.line_2.raise_()
        self.checkBox_export_html.raise_()
        self.label_chart_options_2.raise_()
        self.line_3.raise_()
        self.line_4.raise_()
        self.comboBox_heatmap.raise_()

        self.retranslateUi(DialogCharts)
        QtCore.QMetaObject.connectSlotsByName(DialogCharts)

    def retranslateUi(self, DialogCharts):
        _translate = QtCore.QCoreApplication.translate
        DialogCharts.setWindowTitle(_translate("DialogCharts", "Charts"))
        self.label_info.setText(_translate("DialogCharts", "Charts displayed in the default web browser"))
        self.label_pie.setText(_translate("DialogCharts", "Pie charts"))
        self.label_bar.setText(_translate("DialogCharts", "Bar charts"))
        self.label_hierarchy.setText(_translate("DialogCharts", "Sunburst and treemap charts"))
        self.label_coder.setText(_translate("DialogCharts", "Select coder"))
        self.label_select_file.setText(_translate("DialogCharts", "Select file"))
        self.comboBox_case.setToolTip(_translate("DialogCharts", "If portions of a text file are assigned to a case, the code frequency and total text characters may be incorrect.\n"
"Codings from the entire text file are used for the calculations."))
        self.label_select_case.setToolTip(_translate("DialogCharts", "If portions of a text file are assigned to a case, the code frequency and total text characters may be incorrect.\n"
"Codings from the entire text file are used for the calculations."))
        self.label_select_case.setText(_translate("DialogCharts", "Select case"))
        self.pushButton_attributes.setText(_translate("DialogCharts", "Select attributes"))
        self.label_filter.setText(_translate("DialogCharts", "Filter out values below:"))
        self.lineEdit_filter.setToolTip(_translate("DialogCharts", "Enter number for filter cut off"))
        self.label_filters.setText(_translate("DialogCharts", "<b>Data filters</b>"))
        self.label_chart_options.setText(_translate("DialogCharts", "<b>Coding charts</b>"))
        self.label_category.setText(_translate("DialogCharts", "Select category"))
        self.label_chart_attributes.setText(_translate("DialogCharts", "<b>Attribute charts</b>"))
        self.label_num_attr.setText(_translate("DialogCharts", "Numeric attributes"))
        self.label_char_attr.setText(_translate("DialogCharts", "Character attributes"))
        self.radioButton_file.setText(_translate("DialogCharts", "File"))
        self.radioButton_case.setText(_translate("DialogCharts", "Case"))
        self.checkBox_export_html.setText(_translate("DialogCharts", "Export HTML file"))
        self.label_chart_options_2.setText(_translate("DialogCharts", "<b>Heatmap charts</b>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogCharts = QtWidgets.QDialog()
    ui = Ui_DialogCharts()
    ui.setupUi(DialogCharts)
    DialogCharts.show()
    sys.exit(app.exec())
