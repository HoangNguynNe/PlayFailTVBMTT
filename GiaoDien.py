# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import ThuatToan


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(845, 598)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 0, 761, 81))
        font = QtGui.QFont()
        font.setFamily("UVN Van Chuong Nang")
        font.setPointSize(24)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 80, 741, 181))
        self.groupBox.setStyleSheet('QGroupBox  {color: green;}')
        font = QtGui.QFont()
        font.setFamily("UVN Bai Sau")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(30, 30, 55, 31))
        font = QtGui.QFont()
        font.setFamily("UVN Thay Giao Nang")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Key_TT = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Key_TT.setGeometry(QtCore.QRect(90, 40, 241, 22))
        font = QtGui.QFont()
        font.setFamily("UVN Van Chuong Nang")
        self.Key_TT.setFont(font)
        self.Key_TT.setObjectName("Key_TT")
        self.label_3 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(380, 30, 61, 31))
        font = QtGui.QFont()
        font.setFamily("UVN Thay Giao Nang")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.Ma_TT = QtWidgets.QLineEdit(parent=self.groupBox)
        self.Ma_TT.setGeometry(QtCore.QRect(460, 40, 241, 22))
        font = QtGui.QFont()
        font.setFamily("UVN Van Chuong Nang")
        self.Ma_TT.setFont(font)
        self.Ma_TT.setObjectName("Ma_TT")
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(220, 70, 181, 31))
        font = QtGui.QFont()
        font.setFamily("UVN Thay Giao Nang")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.LuaChon_TT = QtWidgets.QComboBox(parent=self.groupBox)
        self.LuaChon_TT.setGeometry(QtCore.QRect(380, 70, 121, 31))
        font = QtGui.QFont()
        font.setFamily("UVN Nhan Nang")
        font.setPointSize(10)
        self.LuaChon_TT.setFont(font)
        self.LuaChon_TT.setObjectName("LuaChon_TT")
        self.LuaChon_TT.addItem("")
        self.LuaChon_TT.addItem("")
        self.KetQua_TT = QtWidgets.QPushButton(parent=self.groupBox)
        self.KetQua_TT.setGeometry(QtCore.QRect(290, 120, 121, 41))
        font = QtGui.QFont()
        font.setFamily("UVN Bai Sau")
        self.KetQua_TT.setFont(font)
        self.KetQua_TT.setObjectName("KetQua_TT")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(50, 280, 331, 231))
        font = QtGui.QFont()
        font.setFamily("UVN Bai Sau")
        font.setPointSize(14)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Key_DaXuLy = QtWidgets.QLabel(parent=self.groupBox_2)
        self.Key_DaXuLy.setGeometry(QtCore.QRect(20, 40, 301, 181))
        font = QtGui.QFont()
        font.setFamily("UVN Van Chuong Nang")
        self.Key_DaXuLy.setFont(font)
        self.Key_DaXuLy.setText("")
        self.Key_DaXuLy.setObjectName("Key_DaXuLy")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 280, 341, 231))
        font = QtGui.QFont()
        font.setFamily("UVN Bai Sau")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.KetQua_DaXuLy = QtWidgets.QLabel(parent=self.groupBox_3)
        self.KetQua_DaXuLy.setGeometry(QtCore.QRect(20, 40, 311, 181))
        font = QtGui.QFont()
        font.setFamily("UVN Van Chuong Nang")
        self.KetQua_DaXuLy.setFont(font)
        self.KetQua_DaXuLy.setText("")
        self.KetQua_DaXuLy.setObjectName("KetQua_DaXuLy")
        self.label_5 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(50, 510, 171, 21))
        font = QtGui.QFont()
        font.setFamily("UVN Bach Dang Nang")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.KetQua_TT.clicked.connect(self.ClickKetQua)
        
    def ClickKetQua(self):
        MaThuatToan = self.Ma_TT.text()
        KeyThuatToan = self.Key_TT.text()
        a = ThuatToan.TaoMaTran(KeyThuatToan)
        if self.Ma_TT.text().__len__() == 0:
            msgBox = QMessageBox()
            msgBox.setText("Vui lòng nhập Mã !")
            msgBox.exec()
        elif self.Key_TT.text().__len__() == 0:
            msgBox = QMessageBox()
            msgBox.setText("Vui lòng nhập key !")
            msgBox.exec()
        else:
            if self.LuaChon_TT.currentIndex() == 0:
                b = ThuatToan.LapMa(a,MaThuatToan)
                self.KetQua_DaXuLy.setText(b)
                self.Key_DaXuLy.setText('\n'.join(' '.join(map(str, row[:5])) for row in a))
            else:
                c = ThuatToan.GiaiMa(a,MaThuatToan)
                self.KetQua_DaXuLy.setText(c)
                self.Key_DaXuLy.setText('\n'.join(' '.join(map(str, row[:5])) for row in a))
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "HỆ THỐNG LẬP VÀ GIẢI MÃ PLAYFAIL"))
        self.groupBox.setTitle(_translate("MainWindow", "Thông Tin"))
        self.label_2.setText(_translate("MainWindow", "Key:"))
        self.label_3.setText(_translate("MainWindow", "Bản tin:"))
        self.label_4.setText(_translate("MainWindow", "Lựa chọn: "))
        self.LuaChon_TT.setItemText(0, _translate("MainWindow", "Lập mã"))
        self.LuaChon_TT.setItemText(1, _translate("MainWindow", "Giải mã"))
        self.KetQua_TT.setText(_translate("MainWindow", "Kết quả"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Key"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Kết quả"))
        self.label_5.setText(_translate("MainWindow", "Create by Hoang Nguyen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
