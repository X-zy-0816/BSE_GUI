# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(1214, 674)
        self.label = QtWidgets.QLabel(main_window)
        self.label.setGeometry(QtCore.QRect(220, 0, 771, 31))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(main_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 1191, 621))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_main = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_main.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_main.setObjectName("horizontalLayout_main")
        self.frame_traders = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_traders.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_traders.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_traders.setObjectName("frame_traders")
        self.label_Trader_desc = QtWidgets.QLabel(self.frame_traders)
        self.label_Trader_desc.setGeometry(QtCore.QRect(0, 0, 191, 31))
        self.label_Trader_desc.setObjectName("label_Trader_desc")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.frame_traders)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 80, 271, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_trader_1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_trader_1.setObjectName("label_trader_1")
        self.horizontalLayout_3.addWidget(self.label_trader_1)
        self.comboBox_t1 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_t1.setObjectName("comboBox_t1")
        self.horizontalLayout_3.addWidget(self.comboBox_t1)
        self.spinBox_t1 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_t1.setObjectName("spinBox_t1")
        self.horizontalLayout_3.addWidget(self.spinBox_t1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_trader_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_trader_2.setObjectName("label_trader_2")
        self.horizontalLayout_5.addWidget(self.label_trader_2)
        self.comboBox_t2 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_t2.setObjectName("comboBox_t2")
        self.horizontalLayout_5.addWidget(self.comboBox_t2)
        self.spinBox_t2 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_t2.setObjectName("spinBox_t2")
        self.horizontalLayout_5.addWidget(self.spinBox_t2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_trader_3 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_trader_3.setObjectName("label_trader_3")
        self.horizontalLayout_6.addWidget(self.label_trader_3)
        self.comboBox_t3 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_t3.setObjectName("comboBox_t3")
        self.horizontalLayout_6.addWidget(self.comboBox_t3)
        self.spinBox_t3 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_t3.setObjectName("spinBox_t3")
        self.horizontalLayout_6.addWidget(self.spinBox_t3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_trader_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_trader_4.setObjectName("label_trader_4")
        self.horizontalLayout_7.addWidget(self.label_trader_4)
        self.comboBox_t4 = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_t4.setObjectName("comboBox_t4")
        self.horizontalLayout_7.addWidget(self.comboBox_t4)
        self.spinBox_t4 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_t4.setObjectName("spinBox_t4")
        self.horizontalLayout_7.addWidget(self.spinBox_t4)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.label_Seller_Trader = QtWidgets.QLabel(self.frame_traders)
        self.label_Seller_Trader.setGeometry(QtCore.QRect(0, 50, 181, 31))
        self.label_Seller_Trader.setObjectName("label_Seller_Trader")
        self.label_Buyer_Trader = QtWidgets.QLabel(self.frame_traders)
        self.label_Buyer_Trader.setGeometry(QtCore.QRect(0, 290, 181, 31))
        self.label_Buyer_Trader.setObjectName("label_Buyer_Trader")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame_traders)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(0, 320, 271, 211))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_trader_5 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_trader_5.setObjectName("label_trader_5")
        self.horizontalLayout_8.addWidget(self.label_trader_5)
        self.comboBox_t5 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_t5.setObjectName("comboBox_t5")
        self.horizontalLayout_8.addWidget(self.comboBox_t5)
        self.spinBox_t5 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_t5.setObjectName("spinBox_t5")
        self.horizontalLayout_8.addWidget(self.spinBox_t5)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_trader_6 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_trader_6.setObjectName("label_trader_6")
        self.horizontalLayout_9.addWidget(self.label_trader_6)
        self.comboBox_t6 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_t6.setObjectName("comboBox_t6")
        self.horizontalLayout_9.addWidget(self.comboBox_t6)
        self.spinBox_t6 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_t6.setObjectName("spinBox_t6")
        self.horizontalLayout_9.addWidget(self.spinBox_t6)
        self.verticalLayout_4.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_trader_7 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_trader_7.setObjectName("label_trader_7")
        self.horizontalLayout_10.addWidget(self.label_trader_7)
        self.comboBox_t7 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_t7.setObjectName("comboBox_t7")
        self.horizontalLayout_10.addWidget(self.comboBox_t7)
        self.spinBox_t7 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_t7.setObjectName("spinBox_t7")
        self.horizontalLayout_10.addWidget(self.spinBox_t7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_trader_8 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_trader_8.setObjectName("label_trader_8")
        self.horizontalLayout_11.addWidget(self.label_trader_8)
        self.comboBox_t8 = QtWidgets.QComboBox(self.verticalLayoutWidget_2)
        self.comboBox_t8.setObjectName("comboBox_t8")
        self.horizontalLayout_11.addWidget(self.comboBox_t8)
        self.spinBox_t8 = QtWidgets.QSpinBox(self.verticalLayoutWidget_2)
        self.spinBox_t8.setObjectName("spinBox_t8")
        self.horizontalLayout_11.addWidget(self.spinBox_t8)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.pushButton_CopytoBuyer = QtWidgets.QPushButton(self.frame_traders)
        self.pushButton_CopytoBuyer.setGeometry(QtCore.QRect(180, 50, 111, 31))
        self.pushButton_CopytoBuyer.setObjectName("pushButton_CopytoBuyer")
        self.horizontalLayout_main.addWidget(self.frame_traders)
        self.frame_Basic = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_Basic.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Basic.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Basic.setObjectName("frame_Basic")
        self.layoutWidget = QtWidgets.QWidget(self.frame_Basic)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 291, 621))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_21 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_21.setObjectName("verticalLayout_21")
        self.verticalLayout_Limit_Ranges = QtWidgets.QVBoxLayout()
        self.verticalLayout_Limit_Ranges.setObjectName("verticalLayout_Limit_Ranges")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.spinBox_sellerRange1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_sellerRange1.setMaximum(500)
        self.spinBox_sellerRange1.setObjectName("spinBox_sellerRange1")
        self.horizontalLayout.addWidget(self.spinBox_sellerRange1)
        self.spinBox_sellerRange2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_sellerRange2.setMaximum(500)
        self.spinBox_sellerRange2.setObjectName("spinBox_sellerRange2")
        self.horizontalLayout.addWidget(self.spinBox_sellerRange2)
        self.verticalLayout_Limit_Ranges.addLayout(self.horizontalLayout)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_12.addWidget(self.label_5)
        self.spinBox_sellerRange3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_sellerRange3.setMaximum(500)
        self.spinBox_sellerRange3.setObjectName("spinBox_sellerRange3")
        self.horizontalLayout_12.addWidget(self.spinBox_sellerRange3)
        self.spinBox_sellerRange4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_sellerRange4.setMaximum(500)
        self.spinBox_sellerRange4.setObjectName("spinBox_sellerRange4")
        self.horizontalLayout_12.addWidget(self.spinBox_sellerRange4)
        self.verticalLayout_Limit_Ranges.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_13.addWidget(self.label_6)
        self.spinBox_buyerRange1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_buyerRange1.setMaximum(500)
        self.spinBox_buyerRange1.setObjectName("spinBox_buyerRange1")
        self.horizontalLayout_13.addWidget(self.spinBox_buyerRange1)
        self.spinBox_buyerRange2 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_buyerRange2.setMaximum(500)
        self.spinBox_buyerRange2.setObjectName("spinBox_buyerRange2")
        self.horizontalLayout_13.addWidget(self.spinBox_buyerRange2)
        self.verticalLayout_Limit_Ranges.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox_buyerRange3 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_buyerRange3.setMaximum(500)
        self.spinBox_buyerRange3.setObjectName("spinBox_buyerRange3")
        self.horizontalLayout_2.addWidget(self.spinBox_buyerRange3)
        self.spinBox_buyerRange4 = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_buyerRange4.setMaximum(500)
        self.spinBox_buyerRange4.setObjectName("spinBox_buyerRange4")
        self.horizontalLayout_2.addWidget(self.spinBox_buyerRange4)
        self.verticalLayout_Limit_Ranges.addLayout(self.horizontalLayout_2)
        self.verticalLayout_21.addLayout(self.verticalLayout_Limit_Ranges)
        self.horizontalLayout_Market_Time = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Market_Time.setObjectName("horizontalLayout_Market_Time")
        self.label_StepMode_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_StepMode_5.setObjectName("label_StepMode_5")
        self.horizontalLayout_Market_Time.addWidget(self.label_StepMode_5)
        self.spinBox_marketTime = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_marketTime.setMinimum(1)
        self.spinBox_marketTime.setMaximum(1000)
        self.spinBox_marketTime.setObjectName("spinBox_marketTime")
        self.horizontalLayout_Market_Time.addWidget(self.spinBox_marketTime)
        self.verticalLayout_21.addLayout(self.horizontalLayout_Market_Time)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_change = QtWidgets.QLabel(self.layoutWidget)
        self.label_change.setObjectName("label_change")
        self.verticalLayout.addWidget(self.label_change)
        self.horizontalSlider = QtWidgets.QSlider(self.layoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout.addWidget(self.horizontalSlider)
        self.verticalLayout_21.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem)
        self.horizontalLayout_Order_Interval = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Order_Interval.setObjectName("horizontalLayout_Order_Interval")
        self.label_StepMode_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_StepMode_4.setObjectName("label_StepMode_4")
        self.horizontalLayout_Order_Interval.addWidget(self.label_StepMode_4)
        self.spinBox_orderInterval = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_orderInterval.setMinimum(1)
        self.spinBox_orderInterval.setMaximum(500)
        self.spinBox_orderInterval.setObjectName("spinBox_orderInterval")
        self.horizontalLayout_Order_Interval.addWidget(self.spinBox_orderInterval)
        self.verticalLayout_21.addLayout(self.horizontalLayout_Order_Interval)
        self.horizontalLayout_StepMode = QtWidgets.QHBoxLayout()
        self.horizontalLayout_StepMode.setObjectName("horizontalLayout_StepMode")
        self.label_StepMode = QtWidgets.QLabel(self.layoutWidget)
        self.label_StepMode.setObjectName("label_StepMode")
        self.horizontalLayout_StepMode.addWidget(self.label_StepMode)
        self.comboBox_stepMode = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_stepMode.setObjectName("comboBox_stepMode")
        self.horizontalLayout_StepMode.addWidget(self.comboBox_stepMode)
        self.verticalLayout_21.addLayout(self.horizontalLayout_StepMode)
        self.horizontalLayout_TimeMode = QtWidgets.QHBoxLayout()
        self.horizontalLayout_TimeMode.setObjectName("horizontalLayout_TimeMode")
        self.label_StepMode_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_StepMode_2.setObjectName("label_StepMode_2")
        self.horizontalLayout_TimeMode.addWidget(self.label_StepMode_2)
        self.comboBox_timeMode = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_timeMode.setObjectName("comboBox_timeMode")
        self.horizontalLayout_TimeMode.addWidget(self.comboBox_timeMode)
        self.verticalLayout_21.addLayout(self.horizontalLayout_TimeMode)
        self.horizontalLayout_Total_Trials = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Total_Trials.setObjectName("horizontalLayout_Total_Trials")
        self.label_StepMode_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_StepMode_3.setObjectName("label_StepMode_3")
        self.horizontalLayout_Total_Trials.addWidget(self.label_StepMode_3)
        self.spinBox_totalTrials = QtWidgets.QSpinBox(self.layoutWidget)
        self.spinBox_totalTrials.setMinimum(1)
        self.spinBox_totalTrials.setMaximum(10000)
        self.spinBox_totalTrials.setObjectName("spinBox_totalTrials")
        self.horizontalLayout_Total_Trials.addWidget(self.spinBox_totalTrials)
        self.verticalLayout_21.addLayout(self.horizontalLayout_Total_Trials)
        self.horizontalLayout_Verbose = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Verbose.setObjectName("horizontalLayout_Verbose")
        self.checkBox_verbose = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_verbose.setObjectName("checkBox_verbose")
        self.horizontalLayout_Verbose.addWidget(self.checkBox_verbose)
        self.checkBox_saveImages = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_saveImages.setCheckable(True)
        self.checkBox_saveImages.setChecked(True)
        self.checkBox_saveImages.setObjectName("checkBox_saveImages")
        self.horizontalLayout_Verbose.addWidget(self.checkBox_saveImages)
        self.verticalLayout_21.addLayout(self.horizontalLayout_Verbose)
        spacerItem1 = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_21.addItem(spacerItem1)
        self.pushButton_Start = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_Start.setObjectName("pushButton_Start")
        self.verticalLayout_21.addWidget(self.pushButton_Start)
        self.horizontalLayout_main.addWidget(self.frame_Basic)
        self.frame_Outcome = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_Outcome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Outcome.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Outcome.setObjectName("frame_Outcome")
        self.textEdit_info = QtWidgets.QTextEdit(self.frame_Outcome)
        self.textEdit_info.setGeometry(QtCore.QRect(0, 0, 281, 371))
        self.textEdit_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.textEdit_info.setObjectName("textEdit_info")
        self.label_map1 = QtWidgets.QLabel(self.frame_Outcome)
        self.label_map1.setGeometry(QtCore.QRect(0, 370, 281, 251))
        self.label_map1.setText("")
        self.label_map1.setObjectName("label_map1")
        self.horizontalLayout_main.addWidget(self.frame_Outcome)
        self.frame_Outcome_2 = QtWidgets.QFrame(self.horizontalLayoutWidget)
        self.frame_Outcome_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Outcome_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Outcome_2.setObjectName("frame_Outcome_2")
        self.label_map2 = QtWidgets.QLabel(self.frame_Outcome_2)
        self.label_map2.setGeometry(QtCore.QRect(0, 10, 281, 281))
        self.label_map2.setText("")
        self.label_map2.setObjectName("label_map2")
        self.label_map3 = QtWidgets.QLabel(self.frame_Outcome_2)
        self.label_map3.setGeometry(QtCore.QRect(0, 320, 281, 281))
        self.label_map3.setText("")
        self.label_map3.setObjectName("label_map3")
        self.horizontalLayout_main.addWidget(self.frame_Outcome_2)

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Dialog"))
        self.label.setText(_translate("main_window", "BSE GUI (version 1)"))
        self.label_Trader_desc.setText(_translate("main_window", "Trader: ZIP, ZIC, SHVR, GVWY"))
        self.label_trader_1.setText(_translate("main_window", "Trader 1"))
        self.label_trader_2.setText(_translate("main_window", "Trader 2"))
        self.label_trader_3.setText(_translate("main_window", "Trader 3"))
        self.label_trader_4.setText(_translate("main_window", "Trader 4"))
        self.label_Seller_Trader.setText(_translate("main_window", "Seller_Trader"))
        self.label_Buyer_Trader.setText(_translate("main_window", "Buyer_Trader"))
        self.label_trader_5.setText(_translate("main_window", "Trader 1"))
        self.label_trader_6.setText(_translate("main_window", "Trader 2"))
        self.label_trader_7.setText(_translate("main_window", "Trader 3"))
        self.label_trader_8.setText(_translate("main_window", "Trader 4"))
        self.pushButton_CopytoBuyer.setText(_translate("main_window", "Copy to Buyer"))
        self.label_2.setText(_translate("main_window", "Seller_Range_1"))
        self.label_5.setText(_translate("main_window", "Seller_Range_2"))
        self.label_6.setText(_translate("main_window", "Buyer_Range_1"))
        self.label_3.setText(_translate("main_window", "Buyer_Range_2"))
        self.label_StepMode_5.setText(_translate("main_window", "Market_Time(Minutes)"))
        self.label_change.setText(_translate("main_window", "Stock_change time :    0%"))
        self.label_StepMode_4.setText(_translate("main_window", "Order_Interval(Seconds)"))
        self.label_StepMode.setText(_translate("main_window", "StepMode"))
        self.label_StepMode_2.setText(_translate("main_window", "TimeMode"))
        self.label_StepMode_3.setText(_translate("main_window", "Total_Trials"))
        self.checkBox_verbose.setText(_translate("main_window", "Verbose"))
        self.checkBox_saveImages.setText(_translate("main_window", "Save_Images"))
        self.pushButton_Start.setText(_translate("main_window", "Start"))
        self.textEdit_info.setHtml(_translate("main_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">Market_INFO</span></p></body></html>"))