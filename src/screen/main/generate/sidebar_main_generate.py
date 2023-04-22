import resource_pyqt5.resource_rc

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sidebar_main_2.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 684)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setObjectName("widget_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_3)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.widget = QtWidgets.QWidget(self.widget_3)
        self.widget.setObjectName("widget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.change_btn = QtWidgets.QPushButton(self.widget)
        self.change_btn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/menu2.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_btn.setIcon(icon)
        self.change_btn.setIconSize(QtCore.QSize(20, 20))
        self.change_btn.setCheckable(True)
        self.change_btn.setObjectName("change_btn")
        self.horizontalLayout_3.addWidget(self.change_btn)
        spacerItem = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.search_input = QtWidgets.QLineEdit(self.widget)
        self.search_input.setObjectName("search_input")
        self.horizontalLayout_3.addWidget(self.search_input)
        self.search_btn = QtWidgets.QPushButton(self.widget)
        self.search_btn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/search.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QtCore.QSize(18, 18))
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_3.addWidget(self.search_btn)
        spacerItem1 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.user_btn = QtWidgets.QPushButton(self.widget)
        self.user_btn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/exit.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_btn.setIcon(icon2)
        self.user_btn.setObjectName("user_btn")
        self.horizontalLayout_3.addWidget(self.user_btn)
        self.verticalLayout_5.addWidget(self.widget)
        self.stackedWidget = QtWidgets.QStackedWidget(self.widget_3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.page_1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_2 = QtWidgets.QWidget(self.page_1)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.widget_2)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(19, 10, 941, 601))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.widget_5 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 20))
        self.widget_5.setMaximumSize(QtCore.QSize(16777215, 35))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget_5)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 941, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_4.setContentsMargins(150, 0, 130, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.checkBox_vehicledetection = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_vehicledetection.setObjectName("checkBox_vehicledetection")
        self.horizontalLayout_4.addWidget(self.checkBox_vehicledetection)
        self.checkBox_platedetection = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_platedetection.setObjectName("checkBox_platedetection")
        self.horizontalLayout_4.addWidget(self.checkBox_platedetection)
        self.checkBox_speeddetection = QtWidgets.QCheckBox(self.horizontalLayoutWidget)
        self.checkBox_speeddetection.setMaximumSize(QtCore.QSize(150, 30))
        self.checkBox_speeddetection.setObjectName("checkBox_speeddetection")
        self.horizontalLayout_4.addWidget(self.checkBox_speeddetection)
        self.comboBox_model = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox_model.setMaximumSize(QtCore.QSize(130, 16777215))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.comboBox_model.setFont(font)
        self.comboBox_model.setObjectName("comboBox_model")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.comboBox_model.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_model)
        self.verticalLayout_6.addWidget(self.widget_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem2)
        self.label_page1_video = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_page1_video.setText("")
        self.label_page1_video.setObjectName("label_page1_video")
        self.verticalLayout_6.addWidget(self.label_page1_video)
        spacerItem3 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_6.addItem(spacerItem3)
        self.widget_6 = QtWidgets.QWidget(self.verticalLayoutWidget)
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 40))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget_6)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(-1, 0, 941, 42))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.select_video_pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.select_video_pushButton.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.select_video_pushButton.setFont(font)
        self.select_video_pushButton.setObjectName("select_video_pushButton")
        self.horizontalLayout_6.addWidget(self.select_video_pushButton)
        self.pushButton_close = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_close.setMinimumSize(QtCore.QSize(0, 40))
        self.pushButton_close.setMaximumSize(QtCore.QSize(200, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_close.setFont(font)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout_6.addWidget(self.pushButton_close)
        self.verticalLayout_6.addWidget(self.widget_6)
        self.gridLayout_3.addWidget(self.widget_2, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_6 = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.page_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.frame = QtWidgets.QFrame(self.page_3)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 10, 956, 621))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.left_frame = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.left_frame.setMinimumSize(QtCore.QSize(700, 0))
        self.left_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.left_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.left_frame.setObjectName("left_frame")
        self.frame_2 = QtWidgets.QFrame(self.left_frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 681, 171))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.profil_photo = QtWidgets.QLabel(self.frame_2)
        self.profil_photo.setGeometry(QtCore.QRect(10, 10, 221, 151))
        self.profil_photo.setText("")
        self.profil_photo.setObjectName("profil_photo")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 0, 271, 171))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_name = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.verticalLayout_7.addWidget(self.label_name)
        self.label_surname = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_surname.setFont(font)
        self.label_surname.setObjectName("label_surname")
        self.verticalLayout_7.addWidget(self.label_surname)
        self.label_age = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_age.setFont(font)
        self.label_age.setObjectName("label_age")
        self.verticalLayout_7.addWidget(self.label_age)
        self.label_gender = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_gender.setFont(font)
        self.label_gender.setObjectName("label_gender")
        self.verticalLayout_7.addWidget(self.label_gender)
        self.label_tc = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_tc.setFont(font)
        self.label_tc.setObjectName("label_tc")
        self.verticalLayout_7.addWidget(self.label_tc)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.frame_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(280, 0, 117, 171))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_8.addWidget(self.label_4)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_8.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_8.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_8.addWidget(self.label_10)
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_8.addWidget(self.label_5)
        self.frame_3 = QtWidgets.QFrame(self.left_frame)
        self.frame_3.setGeometry(QtCore.QRect(10, 190, 681, 81))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_plate_detection_image = QtWidgets.QLabel(self.frame_3)
        self.label_plate_detection_image.setGeometry(QtCore.QRect(0, 10, 281, 71))
        self.label_plate_detection_image.setText("")
        self.label_plate_detection_image.setObjectName("label_plate_detection_image")
        self.label_plate_write = QtWidgets.QLabel(self.frame_3)
        self.label_plate_write.setGeometry(QtCore.QRect(300, 0, 371, 91))
        font = QtGui.QFont()
        font.setPointSize(21)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_plate_write.setFont(font)
        self.label_plate_write.setAlignment(QtCore.Qt.AlignCenter)
        self.label_plate_write.setObjectName("label_plate_write")
        self.frame_4 = QtWidgets.QFrame(self.left_frame)
        self.frame_4.setGeometry(QtCore.QRect(10, 270, 681, 321))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.label_camera_vehicle_image = QtWidgets.QLabel(self.frame_4)
        self.label_camera_vehicle_image.setGeometry(QtCore.QRect(0, 20, 681, 341))
        self.label_camera_vehicle_image.setText("")
        self.label_camera_vehicle_image.setObjectName("label_camera_vehicle_image")
        self.line = QtWidgets.QFrame(self.left_frame)
        self.line.setGeometry(QtCore.QRect(10, 270, 681, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.left_frame)
        self.line_2.setGeometry(QtCore.QRect(10, 180, 681, 20))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.left_frame)
        self.right_frame = QtWidgets.QFrame(self.horizontalLayoutWidget_3)
        self.right_frame.setMinimumSize(QtCore.QSize(200, 0))
        self.right_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.right_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.right_frame.setObjectName("right_frame")
        self.tableWidget_plate = QtWidgets.QTableWidget(self.right_frame)
        self.tableWidget_plate.setGeometry(QtCore.QRect(0, 10, 201, 521))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.tableWidget_plate.setFont(font)
        self.tableWidget_plate.setColumnCount(0)
        self.tableWidget_plate.setObjectName("tableWidget_plate")
        self.tableWidget_plate.setRowCount(0)
        self.pushButton = QtWidgets.QPushButton(self.right_frame)
        self.pushButton.setGeometry(QtCore.QRect(0, 540, 201, 71))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.right_frame)
        self.gridLayout_2.addWidget(self.frame, 0, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.page_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_7 = QtWidgets.QLabel(self.page_4)
        font = QtGui.QFont()
        font.setPointSize(50)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_5.addWidget(self.label_7, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_4)
        self.verticalLayout_5.addWidget(self.stackedWidget)
        self.gridLayout.addWidget(self.widget_3, 0, 2, 1, 1)
        self.icon_only_widget = QtWidgets.QWidget(self.centralwidget)
        self.icon_only_widget.setMinimumSize(QtCore.QSize(70, 0))
        self.icon_only_widget.setBaseSize(QtCore.QSize(0, 0))
        self.icon_only_widget.setObjectName("icon_only_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.icon_only_widget)
        self.label.setMinimumSize(QtCore.QSize(50, 50))
        self.label.setMaximumSize(QtCore.QSize(50, 50))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/icons/icons/h.ico"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem5 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem5)
        self.home_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.home_btn_1.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/home.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_btn_1.setIcon(icon3)
        self.home_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.home_btn_1.setCheckable(True)
        self.home_btn_1.setAutoExclusive(True)
        self.home_btn_1.setObjectName("home_btn_1")
        self.verticalLayout.addWidget(self.home_btn_1)
        self.statistic_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.statistic_btn_1.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/graph.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.statistic_btn_1.setIcon(icon4)
        self.statistic_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.statistic_btn_1.setCheckable(True)
        self.statistic_btn_1.setAutoExclusive(True)
        self.statistic_btn_1.setObjectName("statistic_btn_1")
        self.verticalLayout.addWidget(self.statistic_btn_1)
        self.settings_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.settings_btn_1.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/settings.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settings_btn_1.setIcon(icon5)
        self.settings_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.settings_btn_1.setCheckable(True)
        self.settings_btn_1.setAutoExclusive(True)
        self.settings_btn_1.setObjectName("settings_btn_1")
        self.verticalLayout.addWidget(self.settings_btn_1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 452, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem6)
        self.exit_btn_1 = QtWidgets.QPushButton(self.icon_only_widget)
        self.exit_btn_1.setText("")
        self.exit_btn_1.setIcon(icon2)
        self.exit_btn_1.setIconSize(QtCore.QSize(30, 30))
        self.exit_btn_1.setCheckable(True)
        self.exit_btn_1.setAutoExclusive(True)
        self.exit_btn_1.setObjectName("exit_btn_1")
        self.verticalLayout_3.addWidget(self.exit_btn_1)
        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)
        self.full_menu_widget = QtWidgets.QWidget(self.centralwidget)
        self.full_menu_widget.setMinimumSize(QtCore.QSize(150, 0))
        self.full_menu_widget.setObjectName("full_menu_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.full_menu_widget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.full_menu_widget)
        self.label_2.setMaximumSize(QtCore.QSize(40, 40))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/icons/icons/h.ico"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.full_menu_widget)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.widget_4 = QtWidgets.QWidget(self.full_menu_widget)
        self.widget_4.setMinimumSize(QtCore.QSize(30, 0))
        self.widget_4.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_2.addWidget(self.widget_4)
        spacerItem7 = QtWidgets.QSpacerItem(20, 70, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem7)
        self.home_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.home_btn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.home_btn_2.setIcon(icon3)
        self.home_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.home_btn_2.setCheckable(True)
        self.home_btn_2.setAutoExclusive(True)
        self.home_btn_2.setObjectName("home_btn_2")
        self.verticalLayout_2.addWidget(self.home_btn_2)
        self.statistic_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.statistic_btn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.statistic_btn_2.setIcon(icon4)
        self.statistic_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.statistic_btn_2.setCheckable(True)
        self.statistic_btn_2.setAutoExclusive(True)
        self.statistic_btn_2.setObjectName("statistic_btn_2")
        self.verticalLayout_2.addWidget(self.statistic_btn_2)
        self.settings_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.settings_btn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.settings_btn_2.setIcon(icon5)
        self.settings_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.settings_btn_2.setCheckable(True)
        self.settings_btn_2.setAutoExclusive(True)
        self.settings_btn_2.setObjectName("settings_btn_2")
        self.verticalLayout_2.addWidget(self.settings_btn_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_2)
        spacerItem8 = QtWidgets.QSpacerItem(20, 467, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem8)
        self.exit_btn_2 = QtWidgets.QPushButton(self.full_menu_widget)
        self.exit_btn_2.setMinimumSize(QtCore.QSize(0, 35))
        self.exit_btn_2.setIcon(icon2)
        self.exit_btn_2.setIconSize(QtCore.QSize(20, 20))
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.verticalLayout_4.addWidget(self.exit_btn_2)
        self.gridLayout.addWidget(self.full_menu_widget, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.change_btn.toggled['bool'].connect(self.icon_only_widget.setVisible) # type: ignore
        self.change_btn.toggled['bool'].connect(self.full_menu_widget.setHidden) # type: ignore
        self.home_btn_1.toggled['bool'].connect(self.home_btn_2.setChecked) # type: ignore
        self.statistic_btn_1.toggled['bool'].connect(self.statistic_btn_2.setChecked) # type: ignore
        self.settings_btn_1.toggled['bool'].connect(self.settings_btn_2.setChecked) # type: ignore
        self.exit_btn_1.toggled['bool'].connect(self.exit_btn_2.setChecked) # type: ignore
        self.home_btn_2.toggled['bool'].connect(self.home_btn_1.setChecked) # type: ignore
        self.statistic_btn_2.toggled['bool'].connect(self.statistic_btn_1.setChecked) # type: ignore
        self.settings_btn_2.toggled['bool'].connect(self.settings_btn_1.setChecked) # type: ignore
        self.exit_btn_2.toggled['bool'].connect(self.exit_btn_1.setChecked) # type: ignore
        self.exit_btn_2.clicked.connect(MainWindow.close) # type: ignore
        self.exit_btn_1.clicked.connect(MainWindow.close) # type: ignore
        self.user_btn.clicked.connect(MainWindow.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.search_input.setPlaceholderText(_translate("MainWindow", "search"))
        self.checkBox_vehicledetection.setText(_translate("MainWindow", "Vehicle Counting"))
        self.checkBox_platedetection.setText(_translate("MainWindow", "Plate Detection"))
        self.checkBox_speeddetection.setText(_translate("MainWindow", "Speed"))
        self.comboBox_model.setItemText(0, _translate("MainWindow", "Yolov8n"))
        self.comboBox_model.setItemText(1, _translate("MainWindow", "Yolov8s"))
        self.comboBox_model.setItemText(2, _translate("MainWindow", "Yolov8l"))
        self.comboBox_model.setItemText(3, _translate("MainWindow", "Yolov8sCustom"))
        self.select_video_pushButton.setText(_translate("MainWindow", "Select Video"))
        self.pushButton_close.setText(_translate("MainWindow", "Close"))
        self.label_6.setText(_translate("MainWindow", "Statistic"))
        self.label_name.setText(_translate("MainWindow", "TextLabel"))
        self.label_surname.setText(_translate("MainWindow", "TextLabel"))
        self.label_age.setText(_translate("MainWindow", "TextLabel"))
        self.label_gender.setText(_translate("MainWindow", "TextLabel"))
        self.label_tc.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Name           :"))
        self.label_8.setText(_translate("MainWindow", "Surname      :"))
        self.label_9.setText(_translate("MainWindow", "Age               :"))
        self.label_10.setText(_translate("MainWindow", "Gender         :"))
        self.label_5.setText(_translate("MainWindow", "Tc                  :"))
        self.label_plate_write.setText(_translate("MainWindow", "34ab ."))
        self.pushButton.setText(_translate("MainWindow", "Update"))
        self.label_7.setText(_translate("MainWindow", "PAGE 4"))
        self.label_3.setText(_translate("MainWindow", "Vehicle Counting"))
        self.home_btn_2.setText(_translate("MainWindow", "Home"))
        self.statistic_btn_2.setText(_translate("MainWindow", "Statistic"))
        self.settings_btn_2.setText(_translate("MainWindow", "Settings"))
        self.exit_btn_2.setText(_translate("MainWindow", "Exit"))










