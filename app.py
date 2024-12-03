# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/app.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 380)
        MainWindow.setStyleSheet("background-color: #8ff0a4;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 20, 572, 284))
        self.layoutWidget.setMinimumSize(QtCore.QSize(138, 90))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.card_1 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_1.sizePolicy().hasHeightForWidth())
        self.card_1.setSizePolicy(sizePolicy)
        self.card_1.setMinimumSize(QtCore.QSize(138, 90))
        self.card_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_1.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/questions.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.card_1.setIcon(icon)
        self.card_1.setIconSize(QtCore.QSize(180, 160))
        self.card_1.setObjectName("card_1")
        self.gridLayout.addWidget(self.card_1, 0, 0, 1, 1)
        self.card_2 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_2.sizePolicy().hasHeightForWidth())
        self.card_2.setSizePolicy(sizePolicy)
        self.card_2.setMinimumSize(QtCore.QSize(138, 90))
        self.card_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_2.setText("")
        self.card_2.setIcon(icon)
        self.card_2.setIconSize(QtCore.QSize(180, 160))
        self.card_2.setObjectName("card_2")
        self.gridLayout.addWidget(self.card_2, 0, 1, 1, 1)
        self.card_3 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_3.sizePolicy().hasHeightForWidth())
        self.card_3.setSizePolicy(sizePolicy)
        self.card_3.setMinimumSize(QtCore.QSize(138, 90))
        self.card_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_3.setText("")
        self.card_3.setIcon(icon)
        self.card_3.setIconSize(QtCore.QSize(180, 160))
        self.card_3.setObjectName("card_3")
        self.gridLayout.addWidget(self.card_3, 0, 2, 1, 1)
        self.card_4 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_4.sizePolicy().hasHeightForWidth())
        self.card_4.setSizePolicy(sizePolicy)
        self.card_4.setMinimumSize(QtCore.QSize(138, 90))
        self.card_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_4.setText("")
        self.card_4.setIcon(icon)
        self.card_4.setIconSize(QtCore.QSize(180, 160))
        self.card_4.setObjectName("card_4")
        self.gridLayout.addWidget(self.card_4, 0, 3, 1, 1)
        self.card_5 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_5.sizePolicy().hasHeightForWidth())
        self.card_5.setSizePolicy(sizePolicy)
        self.card_5.setMinimumSize(QtCore.QSize(138, 90))
        self.card_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_5.setText("")
        self.card_5.setIcon(icon)
        self.card_5.setIconSize(QtCore.QSize(180, 160))
        self.card_5.setObjectName("card_5")
        self.gridLayout.addWidget(self.card_5, 1, 0, 1, 1)
        self.card_6 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_6.sizePolicy().hasHeightForWidth())
        self.card_6.setSizePolicy(sizePolicy)
        self.card_6.setMinimumSize(QtCore.QSize(138, 90))
        self.card_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_6.setText("")
        self.card_6.setIcon(icon)
        self.card_6.setIconSize(QtCore.QSize(180, 160))
        self.card_6.setObjectName("card_6")
        self.gridLayout.addWidget(self.card_6, 1, 1, 1, 1)
        self.card_7 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_7.sizePolicy().hasHeightForWidth())
        self.card_7.setSizePolicy(sizePolicy)
        self.card_7.setMinimumSize(QtCore.QSize(138, 90))
        self.card_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_7.setText("")
        self.card_7.setIcon(icon)
        self.card_7.setIconSize(QtCore.QSize(180, 160))
        self.card_7.setObjectName("card_7")
        self.gridLayout.addWidget(self.card_7, 1, 2, 1, 1)
        self.card_8 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_8.sizePolicy().hasHeightForWidth())
        self.card_8.setSizePolicy(sizePolicy)
        self.card_8.setMinimumSize(QtCore.QSize(138, 90))
        self.card_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_8.setText("")
        self.card_8.setIcon(icon)
        self.card_8.setIconSize(QtCore.QSize(180, 160))
        self.card_8.setObjectName("card_8")
        self.gridLayout.addWidget(self.card_8, 1, 3, 1, 1)
        self.card_9 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_9.sizePolicy().hasHeightForWidth())
        self.card_9.setSizePolicy(sizePolicy)
        self.card_9.setMinimumSize(QtCore.QSize(138, 90))
        self.card_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_9.setText("")
        self.card_9.setIcon(icon)
        self.card_9.setIconSize(QtCore.QSize(180, 160))
        self.card_9.setObjectName("card_9")
        self.gridLayout.addWidget(self.card_9, 2, 0, 1, 1)
        self.card_10 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_10.sizePolicy().hasHeightForWidth())
        self.card_10.setSizePolicy(sizePolicy)
        self.card_10.setMinimumSize(QtCore.QSize(138, 90))
        self.card_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_10.setText("")
        self.card_10.setIcon(icon)
        self.card_10.setIconSize(QtCore.QSize(180, 160))
        self.card_10.setObjectName("card_10")
        self.gridLayout.addWidget(self.card_10, 2, 1, 1, 1)
        self.card_11 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_11.sizePolicy().hasHeightForWidth())
        self.card_11.setSizePolicy(sizePolicy)
        self.card_11.setMinimumSize(QtCore.QSize(138, 90))
        self.card_11.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_11.setText("")
        self.card_11.setIcon(icon)
        self.card_11.setIconSize(QtCore.QSize(180, 160))
        self.card_11.setObjectName("card_11")
        self.gridLayout.addWidget(self.card_11, 2, 2, 1, 1)
        self.card_12 = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.card_12.sizePolicy().hasHeightForWidth())
        self.card_12.setSizePolicy(sizePolicy)
        self.card_12.setMinimumSize(QtCore.QSize(138, 90))
        self.card_12.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.card_12.setText("")
        self.card_12.setIcon(icon)
        self.card_12.setIconSize(QtCore.QSize(180, 160))
        self.card_12.setObjectName("card_12")
        self.gridLayout.addWidget(self.card_12, 2, 3, 1, 1)
        self.timeResultat = QtWidgets.QLabel(self.centralwidget)
        self.timeResultat.setGeometry(QtCore.QRect(370, 320, 231, 20))
        self.timeResultat.setText("")
        self.timeResultat.setObjectName("timeResultat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 23))
        self.menubar.setStyleSheet("background-color: rgb(197, 228, 255);")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionReset.setIcon(icon1)
        self.actionReset.setObjectName("actionReset")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon2)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionReset)
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionReset.setText(_translate("MainWindow", "Reset"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())