# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Summary.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_Summary(object):
    def setupUi(self, Summary):
        if not Summary.objectName():
            Summary.setObjectName(u"Summary")
        Summary.resize(800, 600)
        Summary.setStyleSheet(u"background-color: #e4e4e4;\n"
"	color: #000;\n"
"	selection-background-color: #46a2da;\n"
"	selection-color: #fff;")
        self.centralwidget = QWidget(Summary)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 30, 751, 121))
        self.frame.setFrameShape(QFrame.WinPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 731, 101))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lblSumNetto = QLabel(self.gridLayoutWidget)
        self.lblSumNetto.setObjectName(u"lblSumNetto")
        font = QFont()
        font.setPointSize(12)
        self.lblSumNetto.setFont(font)
        self.lblSumNetto.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblSumNetto.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblSumNetto, 1, 4, 1, 1)

        self.lblDiffEarned = QLabel(self.gridLayoutWidget)
        self.lblDiffEarned.setObjectName(u"lblDiffEarned")
        self.lblDiffEarned.setFont(font)
        self.lblDiffEarned.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblDiffEarned.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblDiffEarned, 1, 2, 1, 1)

        self.lblDiffTax = QLabel(self.gridLayoutWidget)
        self.lblDiffTax.setObjectName(u"lblDiffTax")
        self.lblDiffTax.setFont(font)
        self.lblDiffTax.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblDiffTax.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblDiffTax, 1, 3, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 0, 2, 1, 1)

        self.lblSumProducts = QLabel(self.gridLayoutWidget)
        self.lblSumProducts.setObjectName(u"lblSumProducts")
        self.lblSumProducts.setFont(font)
        self.lblSumProducts.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblSumProducts.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblSumProducts, 1, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label.setFrameShadow(QFrame.Raised)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 4, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.lblTotalSum = QLabel(self.gridLayoutWidget)
        self.lblTotalSum.setObjectName(u"lblTotalSum")
        self.lblTotalSum.setFont(font)
        self.lblTotalSum.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblTotalSum.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.lblTotalSum, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_5.setFrameShape(QFrame.Box)
        self.label_5.setFrameShadow(QFrame.Raised)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)

        self.gridLayout.setRowStretch(0, 1)
        self.gridLayout.setRowStretch(1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(10, 180, 771, 211))
        self.frame_2.setFrameShape(QFrame.WinPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(10, 10, 751, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lblWithdraw1 = QLabel(self.gridLayoutWidget_2)
        self.lblWithdraw1.setObjectName(u"lblWithdraw1")
        self.lblWithdraw1.setFont(font)
        self.lblWithdraw1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblWithdraw1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblWithdraw1, 1, 2, 1, 1)

        self.lblNotes1 = QLabel(self.gridLayoutWidget_2)
        self.lblNotes1.setObjectName(u"lblNotes1")
        self.lblNotes1.setFont(font)
        self.lblNotes1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblNotes1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblNotes1, 1, 0, 1, 1)

        self.lblNetto1 = QLabel(self.gridLayoutWidget_2)
        self.lblNetto1.setObjectName(u"lblNetto1")
        self.lblNetto1.setFont(font)
        self.lblNetto1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblNetto1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblNetto1, 1, 3, 1, 1)

        self.label_11 = QLabel(self.gridLayoutWidget_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_11.setFrameShadow(QFrame.Raised)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_11, 1, 4, 1, 1)

        self.label_6 = QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_6, 0, 2, 1, 1)

        self.lblSUM1 = QLabel(self.gridLayoutWidget_2)
        self.lblSUM1.setObjectName(u"lblSUM1")
        self.lblSUM1.setFont(font)
        self.lblSUM1.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblSUM1.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblSUM1, 1, 1, 1, 1)

        self.label_10 = QLabel(self.gridLayoutWidget_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_10.setFrameShape(QFrame.Box)
        self.label_10.setFrameShadow(QFrame.Raised)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 1)

        self.label_8 = QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_8.setFrameShadow(QFrame.Raised)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_8, 0, 4, 1, 1)

        self.label_7 = QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_7, 0, 1, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_9, 0, 3, 1, 1)

        self.label_12 = QLabel(self.gridLayoutWidget_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_12.setFrameShadow(QFrame.Raised)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_12, 2, 4, 1, 1)

        self.lblNetto2 = QLabel(self.gridLayoutWidget_2)
        self.lblNetto2.setObjectName(u"lblNetto2")
        self.lblNetto2.setFont(font)
        self.lblNetto2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblNetto2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblNetto2, 2, 3, 1, 1)

        self.lblWithdraw2 = QLabel(self.gridLayoutWidget_2)
        self.lblWithdraw2.setObjectName(u"lblWithdraw2")
        self.lblWithdraw2.setFont(font)
        self.lblWithdraw2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblWithdraw2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblWithdraw2, 2, 2, 1, 1)

        self.lblSUM2 = QLabel(self.gridLayoutWidget_2)
        self.lblSUM2.setObjectName(u"lblSUM2")
        self.lblSUM2.setFont(font)
        self.lblSUM2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblSUM2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblSUM2, 2, 1, 1, 1)

        self.lblNotes2 = QLabel(self.gridLayoutWidget_2)
        self.lblNotes2.setObjectName(u"lblNotes2")
        self.lblNotes2.setFont(font)
        self.lblNotes2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblNotes2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.lblNotes2, 2, 0, 1, 1)

        self.gridLayout_2.setRowStretch(0, 1)
        self.gridLayout_2.setRowStretch(1, 1)
        self.gridLayout_2.setRowStretch(2, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 1)
        self.gridLayout_2.setColumnStretch(2, 1)
        self.gridLayout_2.setColumnStretch(3, 1)
        self.gridLayout_2.setColumnStretch(4, 1)
        self.gridLayoutWidget_3 = QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(510, 430, 261, 80))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_13.setFrameShadow(QFrame.Raised)
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_13, 0, 1, 1, 1)

        self.lblMutual = QLabel(self.gridLayoutWidget_3)
        self.lblMutual.setObjectName(u"lblMutual")
        self.lblMutual.setFont(font)
        self.lblMutual.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblMutual.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblMutual, 0, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_3)
        self.label_14.setObjectName(u"label_14")
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(True)
        self.label_14.setFont(font2)
        self.label_14.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_14.setFrameShadow(QFrame.Raised)
        self.label_14.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_14, 1, 1, 1, 1)

        self.lblMutualD = QLabel(self.gridLayoutWidget_3)
        self.lblMutualD.setObjectName(u"lblMutualD")
        self.lblMutualD.setFont(font)
        self.lblMutualD.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblMutualD.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.lblMutualD, 1, 0, 1, 1)

        self.gridLayout_3.setColumnStretch(0, 1)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(320, 430, 160, 80))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_15 = QLabel(self.verticalLayoutWidget)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"border: 1px solid gray;\n"
"border-radius: 10px;")
        self.label_15.setFrameShadow(QFrame.Raised)
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_15)

        self.lblMutualD_2 = QLabel(self.verticalLayoutWidget)
        self.lblMutualD_2.setObjectName(u"lblMutualD_2")
        self.lblMutualD_2.setFont(font)
        self.lblMutualD_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.lblMutualD_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblMutualD_2)

        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(40, 480, 92, 31))
        self.btnBack.setStyleSheet(u"QPushButton {\n"
"  background-color: qlineargradient(spread:repeat, x1:1, y1:0, x2:1, y2:1, stop:0 rgba(184, 184,      184, 255),stop:1 rgba(159, 159, 159, 255));\n"
"	color: #000;\n"
"	min-width: 80px;\n"
"	border-style: solid;\n"
"	border-width: 1px;\n"
"	border-color: #051a39;\n"
"	padding: 5px;\n"
"}\n"
"QPushButton#btnBack:hover\n"
"{\n"
"	background-color: rgba(70,162,218,50%);\n"
"	border: 1px solid #46a2da;\n"
"\n"
"}\n"
"\n"
"QPushButton#btnBack:pressed {\n"
"    background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,\n"
"                                      stop: 0 #dadbde, stop: 1 #f6f7fa);\n"
"}")
        Summary.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Summary)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        Summary.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Summary)
        self.statusbar.setObjectName(u"statusbar")
        Summary.setStatusBar(self.statusbar)

        self.retranslateUi(Summary)

        QMetaObject.connectSlotsByName(Summary)
    # setupUi

    def retranslateUi(self, Summary):
        Summary.setWindowTitle(QCoreApplication.translate("Summary", u"MainWindow", None))
        self.lblSumNetto.setText("")
        self.lblDiffEarned.setText("")
        self.lblDiffTax.setText("")
        self.label_4.setText(QCoreApplication.translate("Summary", u"\u0645\u062c\u0645\u0648\u0639 \u0641\u0631\u0642 \u0645\u0643\u062a\u0633\u0628", None))
        self.lblSumProducts.setText("")
        self.label_3.setText(QCoreApplication.translate("Summary", u"\u0645\u062c\u0645\u0648\u0639 \u0633\u0639\u0631 \u0627\u0644\u0628\u0636\u0627\u0639\u0629", None))
        self.label.setText(QCoreApplication.translate("Summary", u"\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0635\u0627\u0641\u064a", None))
        self.label_2.setText(QCoreApplication.translate("Summary", u"\u0645\u062c\u0645\u0648\u0639 \u0641\u0631\u0642 \u0627\u0644\u0631\u0633\u0648\u0645", None))
        self.lblTotalSum.setText("")
        self.label_5.setText(QCoreApplication.translate("Summary", u"\u0627\u0644\u0645\u062c\u0645\u0648\u0639 \u0627\u0644\u0639\u0627\u0645", None))
        self.lblWithdraw1.setText("")
        self.lblNotes1.setText("")
        self.lblNetto1.setText("")
        self.label_11.setText(QCoreApplication.translate("Summary", u"\u062d\u0627\u0632\u0645", None))
        self.label_6.setText(QCoreApplication.translate("Summary", u"\u0627\u062c\u0645\u0627\u0644\u064a \u0627\u0644\u0633\u062d\u0648\u0628\u0627\u062a", None))
        self.lblSUM1.setText("")
        self.label_10.setText(QCoreApplication.translate("Summary", u"\u0645\u0644\u0627\u062d\u0638\u0627\u062a", None))
        self.label_8.setText(QCoreApplication.translate("Summary", u"\u0627\u0644\u0645\u0645\u0648\u0644", None))
        self.label_7.setText(QCoreApplication.translate("Summary", u"\u0627\u0644\u0645\u062d\u0635\u0644\u0629", None))
        self.label_9.setText(QCoreApplication.translate("Summary", u"\u0635\u0627\u0641\u064a \u0627\u0644\u0640\u0623\u0631\u0628\u0627\u062d", None))
        self.label_12.setText(QCoreApplication.translate("Summary", u"\u062d\u0633\u0627\u0645", None))
        self.lblNetto2.setText("")
        self.lblWithdraw2.setText("")
        self.lblSUM2.setText("")
        self.lblNotes2.setText("")
        self.label_13.setText(QCoreApplication.translate("Summary", u"\u0627\u0644\u0645\u0634\u062a\u0631\u0643", None))
        self.lblMutual.setText("")
        self.label_14.setText(QCoreApplication.translate("Summary", u"/ 2", None))
        self.lblMutualD.setText("")
        self.label_15.setText(QCoreApplication.translate("Summary", u"\u0645\u062c\u0645\u0648\u0639 \u062a\u0639\u0648\u064a\u0636 \u0627\u0644\u0634\u062d\u0646", None))
        self.lblMutualD_2.setText("")
        self.btnBack.setText(QCoreApplication.translate("Summary", u"\u0639\u0648\u062f\u0629", None))
    # retranslateUi

