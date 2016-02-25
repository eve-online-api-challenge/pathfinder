# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources\ui\gui_main.ui'
#
# Created: Thu Feb 25 22:15:33 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(636, 670)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.graphicsView_banner = QtGui.QGraphicsView(self.centralwidget)
        self.graphicsView_banner.setMinimumSize(QtCore.QSize(420, 132))
        self.graphicsView_banner.setMaximumSize(QtCore.QSize(16777215, 132))
        self.graphicsView_banner.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_banner.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView_banner.setObjectName("graphicsView_banner")
        self.verticalLayout.addWidget(self.graphicsView_banner)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(330, 0))
        self.groupBox.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit_source = QtGui.QLineEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_source.sizePolicy().hasHeightForWidth())
        self.lineEdit_source.setSizePolicy(sizePolicy)
        self.lineEdit_source.setMaxLength(32)
        self.lineEdit_source.setObjectName("lineEdit_source")
        self.gridLayout.addWidget(self.lineEdit_source, 1, 1, 1, 1)
        self.label_destination = QtGui.QLabel(self.groupBox)
        self.label_destination.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_destination.setObjectName("label_destination")
        self.gridLayout.addWidget(self.label_destination, 3, 0, 1, 1)
        self.lineEdit_destination = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_destination.setMaxLength(32)
        self.lineEdit_destination.setPlaceholderText("")
        self.lineEdit_destination.setObjectName("lineEdit_destination")
        self.gridLayout.addWidget(self.lineEdit_destination, 3, 1, 1, 1)
        self.label_source = QtGui.QLabel(self.groupBox)
        self.label_source.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_source.setObjectName("label_source")
        self.gridLayout.addWidget(self.label_source, 1, 0, 1, 1)
        self.pushButton_player_location = QtGui.QPushButton(self.groupBox)
        self.pushButton_player_location.setEnabled(False)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/crest_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_player_location.setIcon(icon)
        self.pushButton_player_location.setObjectName("pushButton_player_location")
        self.gridLayout.addWidget(self.pushButton_player_location, 1, 2, 1, 1)
        self.pushButton_find_path = QtGui.QPushButton(self.groupBox)
        self.pushButton_find_path.setObjectName("pushButton_find_path")
        self.gridLayout.addWidget(self.pushButton_find_path, 3, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 1)
        self.label_status = QtGui.QLabel(self.groupBox)
        self.label_status.setObjectName("label_status")
        self.gridLayout.addWidget(self.label_status, 4, 1, 1, 2)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.tableWidget_path = QtGui.QTableWidget(self.groupBox)
        self.tableWidget_path.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget_path.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget_path.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget_path.setRowCount(0)
        self.tableWidget_path.setColumnCount(0)
        self.tableWidget_path.setObjectName("tableWidget_path")
        self.tableWidget_path.setColumnCount(0)
        self.tableWidget_path.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget_path)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_set_dest = QtGui.QPushButton(self.groupBox)
        self.pushButton_set_dest.setEnabled(False)
        self.pushButton_set_dest.setIcon(icon)
        self.pushButton_set_dest.setObjectName("pushButton_set_dest")
        self.horizontalLayout_6.addWidget(self.pushButton_set_dest)
        self.lineEdit_set_dest = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_set_dest.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.lineEdit_set_dest.setMaxLength(32)
        self.lineEdit_set_dest.setObjectName("lineEdit_set_dest")
        self.horizontalLayout_6.addWidget(self.lineEdit_set_dest)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addWidget(self.groupBox)
        self.groupBox__options = QtGui.QGroupBox(self.centralwidget)
        self.groupBox__options.setMinimumSize(QtCore.QSize(280, 0))
        self.groupBox__options.setMaximumSize(QtCore.QSize(280, 16777215))
        self.groupBox__options.setObjectName("groupBox__options")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox__options)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_eve_login = QtGui.QPushButton(self.groupBox__options)
        self.pushButton_eve_login.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_eve_login.sizePolicy().hasHeightForWidth())
        self.pushButton_eve_login.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/eve_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_eve_login.setIcon(icon1)
        self.pushButton_eve_login.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_eve_login.setObjectName("pushButton_eve_login")
        self.verticalLayout_3.addWidget(self.pushButton_eve_login)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_trip_get = QtGui.QPushButton(self.groupBox__options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_trip_get.sizePolicy().hasHeightForWidth())
        self.pushButton_trip_get.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/tripwire_logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_trip_get.setIcon(icon2)
        self.pushButton_trip_get.setIconSize(QtCore.QSize(24, 24))
        self.pushButton_trip_get.setObjectName("pushButton_trip_get")
        self.horizontalLayout_4.addWidget(self.pushButton_trip_get)
        self.pushButton_trip_config = QtGui.QPushButton(self.groupBox__options)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_trip_config.sizePolicy().hasHeightForWidth())
        self.pushButton_trip_config.setSizePolicy(sizePolicy)
        self.pushButton_trip_config.setMinimumSize(QtCore.QSize(0, 0))
        self.pushButton_trip_config.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/config_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_trip_config.setIcon(icon3)
        self.pushButton_trip_config.setObjectName("pushButton_trip_config")
        self.horizontalLayout_4.addWidget(self.pushButton_trip_config)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.label_trip_status = QtGui.QLabel(self.groupBox__options)
        self.label_trip_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_trip_status.setObjectName("label_trip_status")
        self.verticalLayout_3.addWidget(self.label_trip_status)
        self.groupBox_restrictions = QtGui.QGroupBox(self.groupBox__options)
        self.groupBox_restrictions.setObjectName("groupBox_restrictions")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_restrictions)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox_whsize_small = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_whsize_small.setEnabled(False)
        self.checkBox_whsize_small.setChecked(True)
        self.checkBox_whsize_small.setObjectName("checkBox_whsize_small")
        self.gridLayout_2.addWidget(self.checkBox_whsize_small, 1, 0, 1, 1)
        self.checkBox_whsize_medium = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_whsize_medium.setEnabled(False)
        self.checkBox_whsize_medium.setChecked(True)
        self.checkBox_whsize_medium.setObjectName("checkBox_whsize_medium")
        self.gridLayout_2.addWidget(self.checkBox_whsize_medium, 2, 0, 1, 1)
        self.checkBox_whsize_xl = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_whsize_xl.setEnabled(False)
        self.checkBox_whsize_xl.setChecked(True)
        self.checkBox_whsize_xl.setObjectName("checkBox_whsize_xl")
        self.gridLayout_2.addWidget(self.checkBox_whsize_xl, 2, 1, 1, 1)
        self.checkBox_whsize_large = QtGui.QCheckBox(self.groupBox_restrictions)
        self.checkBox_whsize_large.setEnabled(False)
        self.checkBox_whsize_large.setChecked(True)
        self.checkBox_whsize_large.setObjectName("checkBox_whsize_large")
        self.gridLayout_2.addWidget(self.checkBox_whsize_large, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox_restrictions)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 2)
        self.verticalLayout_5.addLayout(self.gridLayout_2)
        self.verticalLayout_3.addWidget(self.groupBox_restrictions)
        self.groupBox_avoidance = QtGui.QGroupBox(self.groupBox__options)
        self.groupBox_avoidance.setObjectName("groupBox_avoidance")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_avoidance)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.checkBox_avoid_enabled = QtGui.QCheckBox(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_avoid_enabled.sizePolicy().hasHeightForWidth())
        self.checkBox_avoid_enabled.setSizePolicy(sizePolicy)
        self.checkBox_avoid_enabled.setObjectName("checkBox_avoid_enabled")
        self.horizontalLayout_5.addWidget(self.checkBox_avoid_enabled)
        self.label_avoid_status = QtGui.QLabel(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_avoid_status.sizePolicy().hasHeightForWidth())
        self.label_avoid_status.setSizePolicy(sizePolicy)
        self.label_avoid_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_avoid_status.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_avoid_status.setObjectName("label_avoid_status")
        self.horizontalLayout_5.addWidget(self.label_avoid_status)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtGui.QLabel(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_avoid_name = QtGui.QLineEdit(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_avoid_name.sizePolicy().hasHeightForWidth())
        self.lineEdit_avoid_name.setSizePolicy(sizePolicy)
        self.lineEdit_avoid_name.setMaxLength(32)
        self.lineEdit_avoid_name.setObjectName("lineEdit_avoid_name")
        self.horizontalLayout_2.addWidget(self.lineEdit_avoid_name)
        self.pushButton_avoid_add = QtGui.QPushButton(self.groupBox_avoidance)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_avoid_add.sizePolicy().hasHeightForWidth())
        self.pushButton_avoid_add.setSizePolicy(sizePolicy)
        self.pushButton_avoid_add.setMinimumSize(QtCore.QSize(32, 0))
        self.pushButton_avoid_add.setMaximumSize(QtCore.QSize(32, 16777215))
        self.pushButton_avoid_add.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_avoid_add.setObjectName("pushButton_avoid_add")
        self.horizontalLayout_2.addWidget(self.pushButton_avoid_add)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.line_2 = QtGui.QFrame(self.groupBox_avoidance)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_4.addWidget(self.line_2)
        self.listWidget_avoid = QtGui.QListWidget(self.groupBox_avoidance)
        self.listWidget_avoid.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listWidget_avoid.setObjectName("listWidget_avoid")
        self.verticalLayout_4.addWidget(self.listWidget_avoid)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.pushButton_avoid_delete = QtGui.QPushButton(self.groupBox_avoidance)
        self.pushButton_avoid_delete.setObjectName("pushButton_avoid_delete")
        self.horizontalLayout_3.addWidget(self.pushButton_avoid_delete)
        self.pushButton_avoid_clear = QtGui.QPushButton(self.groupBox_avoidance)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/delete_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_avoid_clear.setIcon(icon4)
        self.pushButton_avoid_clear.setObjectName("pushButton_avoid_clear")
        self.horizontalLayout_3.addWidget(self.pushButton_avoid_clear)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_3.addWidget(self.groupBox_avoidance)
        self.horizontalLayout.addWidget(self.groupBox__options)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 636, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Route planner", None, QtGui.QApplication.UnicodeUTF8))
        self.label_destination.setText(QtGui.QApplication.translate("MainWindow", "Destination:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_source.setText(QtGui.QApplication.translate("MainWindow", "Source:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_player_location.setText(QtGui.QApplication.translate("MainWindow", "Player location", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_find_path.setText(QtGui.QApplication.translate("MainWindow", "Find path", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Result:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_status.setText(QtGui.QApplication.translate("MainWindow", "Path status", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_set_dest.setText(QtGui.QApplication.translate("MainWindow", "Set in-game destination", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox__options.setTitle(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_eve_login.setText(QtGui.QApplication.translate("MainWindow", "Log in with EvE", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_trip_get.setText(QtGui.QApplication.translate("MainWindow", "Get Tripwire Chain", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_trip_config.setText(QtGui.QApplication.translate("MainWindow", "Config", None, QtGui.QApplication.UnicodeUTF8))
        self.label_trip_status.setText(QtGui.QApplication.translate("MainWindow", "Not connected to Tripwire, yet", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_restrictions.setTitle(QtGui.QApplication.translate("MainWindow", "Restrictions", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_whsize_small.setText(QtGui.QApplication.translate("MainWindow", "Small", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_whsize_medium.setText(QtGui.QApplication.translate("MainWindow", "Medium", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_whsize_xl.setText(QtGui.QApplication.translate("MainWindow", "Very large", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_whsize_large.setText(QtGui.QApplication.translate("MainWindow", "Large", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Wormhole size:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_avoidance.setTitle(QtGui.QApplication.translate("MainWindow", "Avoidance list", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBox_avoid_enabled.setText(QtGui.QApplication.translate("MainWindow", "Enabled", None, QtGui.QApplication.UnicodeUTF8))
        self.label_avoid_status.setText(QtGui.QApplication.translate("MainWindow", "Addition status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "System:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_add.setText(QtGui.QApplication.translate("MainWindow", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_delete.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_avoid_clear.setText(QtGui.QApplication.translate("MainWindow", "Clear all", None, QtGui.QApplication.UnicodeUTF8))

import resources_rc
