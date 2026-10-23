# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_autoinput.ui'
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
from PySide6.QtWidgets import (QApplication, QMainWindow, QSizePolicy, QStackedWidget,
    QVBoxLayout, QWidget)

from views.pages.page_input_technopro import PageInputTechnopro
from views.pages.page_kontrol_otk import PageKontrolOtk
from views.pages.page_markirovanie import PageMarkirovanie
from views.pages.page_normirovanie import PageNormirovanie
from views.pages.page_razmetka import PageRazmetka
from views.pages.page_sborka import PageSborka
from views.pages.page_select_operation import PageSelectOperation
from views.pages.page_shlifovanie import PageShlifovanie
from views.pages.page_shlifovanie_osnovnoe import PageShlifovanieOsnovnoe
from views.pages.page_shlifovanie_start import PageShlifovanieStart
from views.pages.page_sverlilnaya import PageSverlilnaya
from views.pages.page_tehno_iot import PageTehnoIot
from views.pages.page_tokarnaya import PageTokarnaya
from views.pages.page_tokarnaya_angle import PageTokarnayaAngle
from views.pages.page_tokarnaya_faska import PageTokarnayaFaska
from views.pages.page_tokarnaya_podrezka import PageTokarnayaPodrezka
from views.pages.page_tokarnaya_rastachivanie import PageTokarnayaRastachivanie
from views.pages.page_tokarnaya_rezba import PageTokarnayaRezba
from views.pages.page_tokarnaya_start import PageTokarnayaStart
from views.pages.page_tokarnaya_sverlenie import PageTokarnayaSverlenie
from views.pages.page_tokarnaya_tochenie import PageTokarnayaTochenie
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 900)
        MainWindow.setMinimumSize(QSize(1200, 0))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        font = QFont()
        font.setFamilies([u"Rage"])
        font.setPointSize(9)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/icons/logo_cut.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setStyleSheet(u"color: white;\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgb(0, 57, 95), stop:1 rgb(0, 83, 122));\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"")
        self.page_select_operation = PageSelectOperation()
        self.page_select_operation.setObjectName(u"page_select_operation")
        self.page_select_operation.setMaximumSize(QSize(16777215, 1080))
        self.verticalLayout_3 = QVBoxLayout(self.page_select_operation)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget.addWidget(self.page_select_operation)
        self.page_tokarnaya = PageTokarnaya()
        self.page_tokarnaya.setObjectName(u"page_tokarnaya")
        self.page_tokarnaya.setMaximumSize(QSize(16777215, 1080))
        self.verticalLayout_4 = QVBoxLayout(self.page_tokarnaya)
        self.verticalLayout_4.setSpacing(15)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.stackedWidget.addWidget(self.page_tokarnaya)
        self.page_tokarnaya_start = PageTokarnayaStart()
        self.page_tokarnaya_start.setObjectName(u"page_tokarnaya_start")
        self.page_tokarnaya_start.setMaximumSize(QSize(16777215, 1080))
        self.verticalLayout_17 = QVBoxLayout(self.page_tokarnaya_start)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stackedWidget.addWidget(self.page_tokarnaya_start)
        self.page_tokarnaya_podrezka = PageTokarnayaPodrezka()
        self.page_tokarnaya_podrezka.setObjectName(u"page_tokarnaya_podrezka")
        self.page_tokarnaya_podrezka.setMaximumSize(QSize(16777215, 1080))
        self.verticalLayout_8 = QVBoxLayout(self.page_tokarnaya_podrezka)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.stackedWidget.addWidget(self.page_tokarnaya_podrezka)
        self.page_tokarnaya_tochenie = PageTokarnayaTochenie()
        self.page_tokarnaya_tochenie.setObjectName(u"page_tokarnaya_tochenie")
        self.page_tokarnaya_tochenie.setMaximumSize(QSize(16777215, 1080))
        self.stackedWidget.addWidget(self.page_tokarnaya_tochenie)
        self.page_tokarnaya_sverlenie = PageTokarnayaSverlenie()
        self.page_tokarnaya_sverlenie.setObjectName(u"page_tokarnaya_sverlenie")
        self.page_tokarnaya_sverlenie.setMaximumSize(QSize(16777215, 1080))
        self.stackedWidget.addWidget(self.page_tokarnaya_sverlenie)
        self.page_input_technopro = PageInputTechnopro()
        self.page_input_technopro.setObjectName(u"page_input_technopro")
        self.page_input_technopro.setMaximumSize(QSize(16777215, 1080))
        self.stackedWidget.addWidget(self.page_input_technopro)
        self.page_tokarnaya_rastachivanie = PageTokarnayaRastachivanie()
        self.page_tokarnaya_rastachivanie.setObjectName(u"page_tokarnaya_rastachivanie")
        self.stackedWidget.addWidget(self.page_tokarnaya_rastachivanie)
        self.page_tokarnaya_rezba = PageTokarnayaRezba()
        self.page_tokarnaya_rezba.setObjectName(u"page_tokarnaya_rezba")
        self.stackedWidget.addWidget(self.page_tokarnaya_rezba)
        self.page_tokarnaya_faska = PageTokarnayaFaska()
        self.page_tokarnaya_faska.setObjectName(u"page_tokarnaya_faska")
        self.stackedWidget.addWidget(self.page_tokarnaya_faska)
        self.page_tokarnaya_angle = PageTokarnayaAngle()
        self.page_tokarnaya_angle.setObjectName(u"page_tokarnaya_angle")
        self.stackedWidget.addWidget(self.page_tokarnaya_angle)
        self.page_razmetka = PageRazmetka()
        self.page_razmetka.setObjectName(u"page_razmetka")
        self.stackedWidget.addWidget(self.page_razmetka)
        self.page_sverlilnaya = PageSverlilnaya()
        self.page_sverlilnaya.setObjectName(u"page_sverlilnaya")
        self.page_sverlilnaya.setMinimumSize(QSize(0, 900))
        self.stackedWidget.addWidget(self.page_sverlilnaya)
        self.page_tehno_iot = PageTehnoIot()
        self.page_tehno_iot.setObjectName(u"page_tehno_iot")
        self.stackedWidget.addWidget(self.page_tehno_iot)
        self.page_sborka = PageSborka()
        self.page_sborka.setObjectName(u"page_sborka")
        self.page_sborka.setMinimumSize(QSize(1200, 0))
        self.stackedWidget.addWidget(self.page_sborka)
        self.page_normirovanie = PageNormirovanie()
        self.page_normirovanie.setObjectName(u"page_normirovanie")
        self.stackedWidget.addWidget(self.page_normirovanie)
        self.page_kontrol_otk = PageKontrolOtk()
        self.page_kontrol_otk.setObjectName(u"page_kontrol_otk")
        self.stackedWidget.addWidget(self.page_kontrol_otk)
        self.page_markirovanie = PageMarkirovanie()
        self.page_markirovanie.setObjectName(u"page_markirovanie")
        self.stackedWidget.addWidget(self.page_markirovanie)
        self.page_shlifovanie = PageShlifovanie()
        self.page_shlifovanie.setObjectName(u"page_shlifovanie")
        self.stackedWidget.addWidget(self.page_shlifovanie)
        self.page_shlifovanie_start = PageShlifovanieStart()
        self.page_shlifovanie_start.setObjectName(u"page_shlifovanie_start")
        self.stackedWidget.addWidget(self.page_shlifovanie_start)
        self.page_shlifovanie_osnovnoe = PageShlifovanieOsnovnoe()
        self.page_shlifovanie_osnovnoe.setObjectName(u"page_shlifovanie_osnovnoe")
        self.stackedWidget.addWidget(self.page_shlifovanie_osnovnoe)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(20)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0422\u0435\u0445\u043d\u043e\u041f\u043e\u043c\u043e\u0449\u043d\u0438\u043a", None))
    # retranslateUi

