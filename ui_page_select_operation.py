# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_page_select_operation.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)
import res_rc

class Ui_PageSelectOperation(object):
    def setupUi(self, PageSelectOperation):
        if not PageSelectOperation.objectName():
            PageSelectOperation.setObjectName(u"PageSelectOperation")
        PageSelectOperation.resize(1000, 839)
        PageSelectOperation.setMinimumSize(QSize(1000, 0))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        PageSelectOperation.setFont(font)
        PageSelectOperation.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_3 = QVBoxLayout(PageSelectOperation)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalWidget_2 = QWidget(PageSelectOperation)
        self.verticalWidget_2.setObjectName(u"verticalWidget_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalWidget_2.sizePolicy().hasHeightForWidth())
        self.verticalWidget_2.setSizePolicy(sizePolicy)
        self.verticalWidget_2.setMaximumSize(QSize(16777215, 16777215))
        self.verticalWidget_2.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:1, y2:0, stop:0 rgba(20, 40, 80, 255), stop:1 rgba(39, 73, 109, 255));\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.verticalWidget_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, 10, -1)
        self.pushButton = QPushButton(self.verticalWidget_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        icon = QIcon()
        icon.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))

        self.horizontalLayout.addWidget(self.pushButton, 0, Qt.AlignmentFlag.AlignLeft)

        self.btn_predlog = QPushButton(self.verticalWidget_2)
        self.btn_predlog.setObjectName(u"btn_predlog")
        self.btn_predlog.setEnabled(True)
        self.btn_predlog.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_predlog.setStyleSheet(u"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 30px;	\n"
"	width: 250px;\n"
"	font-size: 17px;\n"
"	padding: 5 0 5 0;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")

        self.horizontalLayout.addWidget(self.btn_predlog, 0, Qt.AlignmentFlag.AlignRight)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label = QLabel(self.verticalWidget_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setBaseSize(QSize(3, 0))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Black"])
        font1.setWeight(QFont.DemiBold)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: none;\n"
"color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"font-size: 28px;\n"
"font-weight: 600;\n"
"border: none;\n"
"width: 300px;\n"
"\n"
"")

        self.verticalLayout_5.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter)

        self.label_select = QLabel(self.verticalWidget_2)
        self.label_select.setObjectName(u"label_select")
        font2 = QFont()
        font2.setFamilies([u"Onyx"])
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.label_select.setFont(font2)
        self.label_select.setStyleSheet(u"background-color: none;\n"
"color: rgb(203, 203, 203);\n"
"font-size: 15px;\n"
"font-weight: 400;\n"
"border: none")

        self.verticalLayout_5.addWidget(self.label_select, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_5)

        self.label_3 = QLabel(self.verticalWidget_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"background: none;")

        self.verticalLayout_2.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, 20)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(40, -1, 40, 0)
        self.widget_2 = QWidget(self.verticalWidget_2)
        self.widget_2.setObjectName(u"widget_2")

        self.horizontalLayout_2.addWidget(self.widget_2)

        self.scrollArea = QScrollArea(self.verticalWidget_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"	background: rgba(0, 0, 0, 0);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 912, 557))
        self.scrollAreaWidgetContents.setStyleSheet(u"background: rgba(0, 0, 0, 0);")
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.scrollAreaWidgetContents)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 30px;	\n"
"	width: 300px;\n"
"	font-size: 17px;\n"
"	padding: 5 0 5 40;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"	text-align: left;\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}\n"
"QPushButton:disabled {\n"
"	background:qradialgradien"
                        "t(spread:pad, cx:0.5, cy:0.5, radius:0.851, fx:0.5, fy:0.5, stop:0 rgba(60, 60, 60, 255), stop:1 rgba(89, 89, 89, 255));\n"
"	border: 1px solid qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(89, 89, 89, 255), stop:1 rgba(111, 111, 111, 255))\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, -1)
        self.btn_sborka = QPushButton(self.frame)
        self.btn_sborka.setObjectName(u"btn_sborka")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Light"])
        self.btn_sborka.setFont(font3)
        self.btn_sborka.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sborka.setStyleSheet(u"text-align: none;\n"
"padding-left: 0;\n"
"padding-right: 160;")
        icon1 = QIcon()
        icon1.addFile(u":/operations/operations/sborka-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sborka.setIcon(icon1)
        self.btn_sborka.setIconSize(QSize(160, 100))

        self.gridLayout.addWidget(self.btn_sborka, 10, 0, 1, 1)

        self.btn_razmetka_2 = QPushButton(self.frame)
        self.btn_razmetka_2.setObjectName(u"btn_razmetka_2")
        self.btn_razmetka_2.setEnabled(False)
        self.btn_razmetka_2.setFont(font3)
        self.btn_razmetka_2.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_razmetka_2.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/operations/operations/goriz-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_razmetka_2.setIcon(icon2)
        self.btn_razmetka_2.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_razmetka_2, 1, 1, 1, 1)

        self.btn_tokarnaya = QPushButton(self.frame)
        self.btn_tokarnaya.setObjectName(u"btn_tokarnaya")
        self.btn_tokarnaya.setFont(font3)
        self.btn_tokarnaya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tokarnaya.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_tokarnaya.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/operations/operations/tokarnaya-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_tokarnaya.setIcon(icon3)
        self.btn_tokarnaya.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_tokarnaya, 0, 0, 1, 1)

        self.btn_markirovanie = QPushButton(self.frame)
        self.btn_markirovanie.setObjectName(u"btn_markirovanie")
        self.btn_markirovanie.setFont(font3)
        self.btn_markirovanie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_markirovanie.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u":/operations/operations/markirovanie.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_markirovanie.setIcon(icon4)
        self.btn_markirovanie.setIconSize(QSize(55, 55))

        self.gridLayout.addWidget(self.btn_markirovanie, 9, 0, 1, 1)

        self.btn_razmetka = QPushButton(self.frame)
        self.btn_razmetka.setObjectName(u"btn_razmetka")
        self.btn_razmetka.setFont(font3)
        self.btn_razmetka.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_razmetka.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/operations/operations/razmetka-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_razmetka.setIcon(icon5)
        self.btn_razmetka.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_razmetka, 1, 0, 1, 1)

        self.btn_kontrol_otk_11 = QPushButton(self.frame)
        self.btn_kontrol_otk_11.setObjectName(u"btn_kontrol_otk_11")
        self.btn_kontrol_otk_11.setEnabled(False)
        self.btn_kontrol_otk_11.setFont(font3)
        self.btn_kontrol_otk_11.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_11.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/operations/operations/shpatlevanie.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_11.setIcon(icon6)
        self.btn_kontrol_otk_11.setIconSize(QSize(55, 55))

        self.gridLayout.addWidget(self.btn_kontrol_otk_11, 6, 0, 1, 1)

        self.btn_kontrol_otk = QPushButton(self.frame)
        self.btn_kontrol_otk.setObjectName(u"btn_kontrol_otk")
        self.btn_kontrol_otk.setFont(font3)
        self.btn_kontrol_otk.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_kontrol_otk.setStyleSheet(u"")
        icon7 = QIcon()
        icon7.addFile(u":/operations/operations/otk-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk.setIcon(icon7)
        self.btn_kontrol_otk.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btn_kontrol_otk, 2, 0, 1, 1)

        self.btn_kontrol_otk_12 = QPushButton(self.frame)
        self.btn_kontrol_otk_12.setObjectName(u"btn_kontrol_otk_12")
        self.btn_kontrol_otk_12.setEnabled(False)
        self.btn_kontrol_otk_12.setFont(font3)
        self.btn_kontrol_otk_12.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_12.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/operations/operations/slesarnaya.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_12.setIcon(icon8)
        self.btn_kontrol_otk_12.setIconSize(QSize(55, 55))

        self.gridLayout.addWidget(self.btn_kontrol_otk_12, 8, 0, 1, 1)

        self.btn_frezernaya = QPushButton(self.frame)
        self.btn_frezernaya.setObjectName(u"btn_frezernaya")
        self.btn_frezernaya.setEnabled(False)
        font4 = QFont()
        font4.setFamilies([u"Segoe UI Light"])
        font4.setStrikeOut(False)
        self.btn_frezernaya.setFont(font4)
        self.btn_frezernaya.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_frezernaya.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/operations/operations/frezernaya-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_frezernaya.setIcon(icon9)
        self.btn_frezernaya.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_frezernaya, 2, 1, 1, 1)

        self.btn_kontrol_otk_3 = QPushButton(self.frame)
        self.btn_kontrol_otk_3.setObjectName(u"btn_kontrol_otk_3")
        self.btn_kontrol_otk_3.setEnabled(False)
        self.btn_kontrol_otk_3.setFont(font3)
        self.btn_kontrol_otk_3.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_3.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/operations/operations/promivka-no-bg-preview (carve.photos).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_3.setIcon(icon10)
        self.btn_kontrol_otk_3.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btn_kontrol_otk_3, 7, 0, 1, 1)

        self.btn_sverlilnaya = QPushButton(self.frame)
        self.btn_sverlilnaya.setObjectName(u"btn_sverlilnaya")
        self.btn_sverlilnaya.setFont(font3)
        self.btn_sverlilnaya.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_sverlilnaya.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/operations/operations/sverlovka-no-bg.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_sverlilnaya.setIcon(icon11)
        self.btn_sverlilnaya.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_sverlilnaya, 0, 1, 1, 1)

        self.btn_kontrol_otk_9 = QPushButton(self.frame)
        self.btn_kontrol_otk_9.setObjectName(u"btn_kontrol_otk_9")
        self.btn_kontrol_otk_9.setEnabled(False)
        self.btn_kontrol_otk_9.setFont(font3)
        self.btn_kontrol_otk_9.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_9.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/operations/operations/sborka.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_9.setIcon(icon12)
        self.btn_kontrol_otk_9.setIconSize(QSize(50, 35))

        self.gridLayout.addWidget(self.btn_kontrol_otk_9, 5, 0, 1, 1)

        self.btn_kontrol_otk_2 = QPushButton(self.frame)
        self.btn_kontrol_otk_2.setObjectName(u"btn_kontrol_otk_2")
        self.btn_kontrol_otk_2.setEnabled(False)
        self.btn_kontrol_otk_2.setFont(font3)
        self.btn_kontrol_otk_2.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_2.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/operations/operations/hydro_ispit.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_2.setIcon(icon13)
        self.btn_kontrol_otk_2.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btn_kontrol_otk_2, 4, 0, 1, 1)

        self.btn_otreznaya = QPushButton(self.frame)
        self.btn_otreznaya.setObjectName(u"btn_otreznaya")
        self.btn_otreznaya.setEnabled(True)
        self.btn_otreznaya.setFont(font3)
        self.btn_otreznaya.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_otreznaya.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/operations/operations/cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_otreznaya.setIcon(icon14)
        self.btn_otreznaya.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_otreznaya, 3, 0, 1, 1)

        self.btn_shlifovanie = QPushButton(self.frame)
        self.btn_shlifovanie.setObjectName(u"btn_shlifovanie")
        self.btn_shlifovanie.setEnabled(True)
        self.btn_shlifovanie.setFont(font3)
        self.btn_shlifovanie.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_shlifovanie.setStyleSheet(u"")
        icon15 = QIcon()
        icon15.addFile(u":/operations/operations/shlifovka.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_shlifovanie.setIcon(icon15)
        self.btn_shlifovanie.setIconSize(QSize(45, 45))

        self.gridLayout.addWidget(self.btn_shlifovanie, 3, 1, 1, 1)

        self.btn_kontrol_otk_5 = QPushButton(self.frame)
        self.btn_kontrol_otk_5.setObjectName(u"btn_kontrol_otk_5")
        self.btn_kontrol_otk_5.setEnabled(False)
        self.btn_kontrol_otk_5.setFont(font3)
        self.btn_kontrol_otk_5.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_5.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon16 = QIcon()
        icon16.addFile(u":/operations/operations/svarka.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_5.setIcon(icon16)
        self.btn_kontrol_otk_5.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_kontrol_otk_5, 4, 1, 1, 1)

        self.btn_kontrol_otk_7 = QPushButton(self.frame)
        self.btn_kontrol_otk_7.setObjectName(u"btn_kontrol_otk_7")
        self.btn_kontrol_otk_7.setEnabled(False)
        self.btn_kontrol_otk_7.setFont(font3)
        self.btn_kontrol_otk_7.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_7.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon17 = QIcon()
        icon17.addFile(u":/operations/operations/gel_ispit.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_7.setIcon(icon17)
        self.btn_kontrol_otk_7.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_kontrol_otk_7, 5, 1, 1, 1)

        self.btn_kontrol_otk_8 = QPushButton(self.frame)
        self.btn_kontrol_otk_8.setObjectName(u"btn_kontrol_otk_8")
        self.btn_kontrol_otk_8.setEnabled(False)
        self.btn_kontrol_otk_8.setFont(font3)
        self.btn_kontrol_otk_8.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_8.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon18 = QIcon()
        icon18.addFile(u":/operations/operations/elect_ispit.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_8.setIcon(icon18)
        self.btn_kontrol_otk_8.setIconSize(QSize(70, 70))

        self.gridLayout.addWidget(self.btn_kontrol_otk_8, 6, 1, 1, 1)

        self.btn_kontrol_otk_10 = QPushButton(self.frame)
        self.btn_kontrol_otk_10.setObjectName(u"btn_kontrol_otk_10")
        self.btn_kontrol_otk_10.setEnabled(False)
        self.btn_kontrol_otk_10.setFont(font3)
        self.btn_kontrol_otk_10.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_10.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon19 = QIcon()
        icon19.addFile(u":/operations/operations/term_obrabotka.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_10.setIcon(icon19)
        self.btn_kontrol_otk_10.setIconSize(QSize(55, 55))

        self.gridLayout.addWidget(self.btn_kontrol_otk_10, 7, 1, 1, 1)

        self.btn_kontrol_otk_4 = QPushButton(self.frame)
        self.btn_kontrol_otk_4.setObjectName(u"btn_kontrol_otk_4")
        self.btn_kontrol_otk_4.setEnabled(False)
        self.btn_kontrol_otk_4.setFont(font3)
        self.btn_kontrol_otk_4.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_4.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon20 = QIcon()
        icon20.addFile(u":/operations/operations/painting.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_4.setIcon(icon20)
        self.btn_kontrol_otk_4.setIconSize(QSize(50, 50))

        self.gridLayout.addWidget(self.btn_kontrol_otk_4, 8, 1, 1, 1)

        self.btn_kontrol_otk_6 = QPushButton(self.frame)
        self.btn_kontrol_otk_6.setObjectName(u"btn_kontrol_otk_6")
        self.btn_kontrol_otk_6.setEnabled(False)
        self.btn_kontrol_otk_6.setFont(font3)
        self.btn_kontrol_otk_6.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.btn_kontrol_otk_6.setStyleSheet(u"QPushButton:hover {\n"
"	color: rgb(221, 71, 71);\n"
"	border-left: 1px solid rgb(203, 88, 88);\n"
"	border-right: 1px solid rgb(203, 88, 88);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(160, 18, 18, 58), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(160, 17, 17, 58))\n"
"}")
        icon21 = QIcon()
        icon21.addFile(u":/operations/operations/balance.PNG", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_kontrol_otk_6.setIcon(icon21)
        self.btn_kontrol_otk_6.setIconSize(QSize(60, 60))

        self.gridLayout.addWidget(self.btn_kontrol_otk_6, 9, 1, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout)


        self.verticalLayout_7.addWidget(self.frame)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.widget = QWidget(self.verticalWidget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget {\n"
"	background: none;\n"
"}\n"
"QPushButton {\n"
"	background:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(0, 168, 204, 255));\n"
"	border: none;\n"
"	height: 30px;	\n"
"	width: 400px;\n"
"	font-size: 17px;\n"
"	padding: 5 0 5 0;\n"
"	border-bottom-right-radius: 15px;\n"
"	border-top-left-radius: 15px;\n"
"	border: 1px solid qradialgradient(spread:pad, cx:0.506, cy:1, radius:1.147, fx:0.494318, fy:1, stop:0 rgba(12, 123, 147, 255), stop:1 rgba(255, 255, 255, 0));\n"
"}\n"
"QPushButton:hover {\n"
"	color: rgb(0, 168, 204);\n"
"	border-left: 1px solid rgb(10, 169, 255);\n"
"	border-right: 1px solid rgb(10, 169, 255);\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.477, x2:1, y2:0.518, stop:0 rgba(15, 109, 159, 64), stop:0.505682 rgba(15, 111, 149, 0), stop:1 rgba(15, 112, 139, 58));\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(0, 53, 93)\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.widget)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_6.addWidget(self.line)

        self.btn_tehno_iot = QPushButton(self.widget)
        self.btn_tehno_iot.setObjectName(u"btn_tehno_iot")
        self.btn_tehno_iot.setFont(font3)
        self.btn_tehno_iot.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_tehno_iot.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_tehno_iot, 0, Qt.AlignmentFlag.AlignHCenter)

        self.btn_normirovanie = QPushButton(self.widget)
        self.btn_normirovanie.setObjectName(u"btn_normirovanie")
        self.btn_normirovanie.setFont(font3)
        self.btn_normirovanie.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_normirovanie, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.widget)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.verticalLayout_3.addWidget(self.verticalWidget_2)


        self.retranslateUi(PageSelectOperation)

        QMetaObject.connectSlotsByName(PageSelectOperation)
    # setupUi

    def retranslateUi(self, PageSelectOperation):
        PageSelectOperation.setWindowTitle(QCoreApplication.translate("PageSelectOperation", u"Form", None))
        self.pushButton.setText("")
        self.btn_predlog.setText(QCoreApplication.translate("PageSelectOperation", u"\u041f\u0440\u0435\u0434\u043b\u043e\u0436\u0435\u043d\u0438\u044f \u043f\u043e \u0443\u043b\u0443\u0447\u0448\u0435\u043d\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("PageSelectOperation", u"\u0413\u041b\u0410\u0412\u041d\u0410\u042f \u0421\u0422\u0420\u0410\u041d\u0418\u0426\u0410", None))
        self.label_select.setText(QCoreApplication.translate("PageSelectOperation", u"\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u044e \u0434\u043b\u044f \u0437\u0430\u043f\u043e\u043b\u043d\u0435\u043d\u0438\u044f \u043f\u0435\u0440\u0435\u0445\u043e\u0434\u043e\u0432", None))
        self.label_3.setText("")
        self.btn_sborka.setText(QCoreApplication.translate("PageSelectOperation", u"\u041f\u0420\u041e\u0427\u0418\u0415 \u041e\u041f\u0415\u0420\u0410\u0426\u0418\u0418", None))
#if QT_CONFIG(tooltip)
        self.btn_razmetka_2.setToolTip(QCoreApplication.translate("PageSelectOperation", u"<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.btn_razmetka_2.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.btn_razmetka_2.setText(QCoreApplication.translate("PageSelectOperation", u" \u0413\u041e\u0420\u0418\u0417\u041e\u041d\u0422\u0410\u041b\u042c\u041d\u041e-\u0420\u0410\u0421\u0422\u041e\u0427\u041d\u0410\u042f", None))
        self.btn_tokarnaya.setText(QCoreApplication.translate("PageSelectOperation", u" \u0422\u041e\u041a\u0410\u0420\u041d\u0410\u042f", None))
        self.btn_markirovanie.setText(QCoreApplication.translate("PageSelectOperation", u"\u041c\u0410\u0420\u041a\u0418\u0420\u041e\u0412\u0410\u041d\u0418\u0415", None))
        self.btn_razmetka.setText(QCoreApplication.translate("PageSelectOperation", u"  \u0420\u0410\u0417\u041c\u0415\u0422\u041a\u0410", None))
        self.btn_kontrol_otk_11.setText(QCoreApplication.translate("PageSelectOperation", u"     \u0428\u041f\u0410\u0422\u041b\u0415\u0412\u0410\u041d\u0418\u0415", None))
        self.btn_kontrol_otk.setText(QCoreApplication.translate("PageSelectOperation", u"        \u041a\u041e\u041d\u0422\u0420\u041e\u041b\u042c \u041e\u0422\u041a", None))
        self.btn_kontrol_otk_12.setText(QCoreApplication.translate("PageSelectOperation", u"\u0421\u041b\u0415\u0421\u0410\u0420\u041d\u0410\u042f", None))
#if QT_CONFIG(tooltip)
        self.btn_frezernaya.setToolTip(QCoreApplication.translate("PageSelectOperation", u"<html><head/><body><p><span style=\" font-size:8pt; color:#000000;\">\u0412 \u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0435</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_frezernaya.setText(QCoreApplication.translate("PageSelectOperation", u"      \u0424\u0420\u0415\u0417\u0415\u0420\u041d\u0410\u042f", None))
        self.btn_kontrol_otk_3.setText(QCoreApplication.translate("PageSelectOperation", u"     \u041f\u0420\u041e\u041c\u042b\u0412\u041a\u0410", None))
        self.btn_sverlilnaya.setText(QCoreApplication.translate("PageSelectOperation", u"     \u0421\u0412\u0415\u0420\u041b\u0418\u041b\u042c\u041d\u0410\u042f", None))
        self.btn_kontrol_otk_9.setText(QCoreApplication.translate("PageSelectOperation", u"       \u0421\u0411\u041e\u0420\u041a\u0410", None))
        self.btn_kontrol_otk_2.setText(QCoreApplication.translate("PageSelectOperation", u"     \u0413\u0418\u0414\u0420\u0410\u0412\u041b\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0418\u0421\u041f\u042b\u0422\u0410\u041d\u0418\u042f", None))
        self.btn_otreznaya.setText(QCoreApplication.translate("PageSelectOperation", u"   \u041e\u0422\u0420\u0415\u0417\u041d\u0410\u042f", None))
        self.btn_shlifovanie.setText(QCoreApplication.translate("PageSelectOperation", u"\u0428\u041b\u0418\u0424\u041e\u0412\u0410\u041b\u042c\u041d\u0410\u042f", None))
        self.btn_kontrol_otk_5.setText(QCoreApplication.translate("PageSelectOperation", u" \u0421\u0412\u0410\u0420\u041a\u0410", None))
        self.btn_kontrol_otk_7.setText(QCoreApplication.translate("PageSelectOperation", u" \u0418\u0421\u041f\u042b\u0422\u0410\u041d\u0418\u042f \u041d\u0410 \u0413\u0415\u0420\u041c\u0415\u0422\u0418\u0427\u041d\u041e\u0421\u0422\u042c", None))
        self.btn_kontrol_otk_8.setText(QCoreApplication.translate("PageSelectOperation", u" \u042d\u041b\u0415\u041a\u0422\u0420\u0418\u0427\u0415\u0421\u041a\u0418\u0415 \u0418\u0421\u041f\u042b\u0422\u0410\u041d\u0418\u042f", None))
        self.btn_kontrol_otk_10.setText(QCoreApplication.translate("PageSelectOperation", u"    \u0422\u0415\u0420\u041c\u041e\u041e\u0411\u0420\u0410\u0411\u041e\u0422\u041a\u0410", None))
        self.btn_kontrol_otk_4.setText(QCoreApplication.translate("PageSelectOperation", u"     \u041e\u041a\u0420\u0410\u0428\u0418\u0412\u0410\u041d\u0418\u0415", None))
        self.btn_kontrol_otk_6.setText(QCoreApplication.translate("PageSelectOperation", u"     \u0411\u0410\u041b\u0410\u041d\u0421\u0418\u0420\u041e\u0412\u041a\u0410", None))
        self.btn_tehno_iot.setText(QCoreApplication.translate("PageSelectOperation", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043a \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u0438 \u0418\u041e\u0422 \u0438 \u043e\u0431\u043e\u0440\u0443\u0434\u043e\u0432\u0430\u043d\u0438\u0435", None))
        self.btn_normirovanie.setText(QCoreApplication.translate("PageSelectOperation", u"\u041d\u043e\u0440\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435", None))
    # retranslateUi

