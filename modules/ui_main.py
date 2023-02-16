# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QStackedWidget,
    QTableView, QVBoxLayout, QWidget)

from pyqtgraph import GraphicsLayoutWidget
import modules.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(804, 521)
        MainWindow.setMinimumSize(QSize(700, 500))
        self.styleSheet = QWidget(MainWindow)
        self.styleSheet.setObjectName(u"styleSheet")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        self.styleSheet.setFont(font)
        self.styleSheet.setStyleSheet(u"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"\n"
"SET APP STYLESHEET - FULL STYLES HERE\n"
"DARK THEME - DRACULA COLOR BASED\n"
"\n"
"///////////////////////////////////////////////////////////////////////////////////////////////// */\n"
"\n"
"QWidget{\n"
"	color: rgb(221, 221, 221);\n"
"	font: 10pt \"Segoe UI\";\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Tooltip */\n"
"QToolTip {\n"
"	color: #ffffff;\n"
"	background-color: rgba(33, 37, 43, 180);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	background-image: none;\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 2px solid rgb(255, 121, 198);\n"
"	text-align: left;\n"
"	padding-left: 8px;\n"
"	margin: 0px;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Bg App */\n"
"#bgApp {	\n"
"	background-color: rg"
                        "b(40, 44, 52);\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Left Menu */\n"
"#leftMenuBg {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#topLogo {\n"
"	background-color: rgb(33, 37, 43);\n"
"	background-image: url(:/images/images/images/PyDracula.png);\n"
"	background-position: centered;\n"
"	background-repeat: no-repeat;\n"
"}\n"
"#titleLeftApp { font: 63 12pt \"Segoe UI Semibold\"; }\n"
"/* #titleLeftDescription { font: 8pt \"Segoe UI\"; color: rgb(189, 147, 249); } */\n"
"#titleLeftDescription { font: 8pt \"Segoe UI\"; color: #ff79c6; }\n"
"\n"
"/* MENUS */\n"
"#topMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color: transparent;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"#topMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#"
                        "topMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#bottomMenu .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"}\n"
"#bottomMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#bottomMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"#leftMenuFrame{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Toggle Button */\n"
"#toggleButton {\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 20px solid transparent;\n"
"	background-color: rgb(37, 41, 48);\n"
"	text-align: left;\n"
"	padding-left: 40px;\n"
"	color: rgb(113, 126, 149);\n"
"}\n"
"#toggleButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
""
                        "}\n"
"#toggleButton:pressed {\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"\n"
"/* Title Menu */\n"
"#titleRightInfo { padding-left: 10px; }\n"
"\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Extra Tab */\n"
"#extraLeftBox {	\n"
"	background-color: rgb(44, 49, 58);\n"
"}\n"
"#extraTopBg{	\n"
"	background-color: rgb(189, 147, 249)\n"
"}\n"
"\n"
"/* Icon */\n"
"#extraIcon {\n"
"	background-position: center;\n"
"	background-repeat: no-repeat;\n"
"	background-image: url(:/icons/images/icons/icon_settings.png);\n"
"}\n"
"\n"
"/* Label */\n"
"#extraLabel { color: rgb(255, 255, 255); }\n"
"\n"
"/* Btn Close */\n"
"#extraCloseColumnBtn { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#extraCloseColumnBtn:hover { background-color: rgb(196, 161, 249); border-style: solid; border-radius: 4px; }\n"
"#extraCloseColumnBtn:pressed { background-color: rgb(180, 141, 238); border-style: solid; border-radius: 4px; }\n"
"\n"
""
                        "/* Extra Content */\n"
"#extraContent{\n"
"	border-top: 3px solid rgb(40, 44, 52);\n"
"}\n"
"\n"
"/* Extra Top Menus */\n"
"#extraTopMenu .QPushButton {\n"
"background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#extraTopMenu .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#extraTopMenu .QPushButton:pressed {	\n"
"	background-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////Content App */\n"
"#contentTopBg{	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"#contentBottom{\n"
"	border-top: 3px solid rgb(44, 49, 58);\n"
"}\n"
"\n"
"/* Top Buttons */\n"
"#rightButtons .QPushButton { background-color: rgba(255, 255, 255, 0); border: none;  border-radius: 5px; }\n"
"#rightButtons .QPushButton:hover { "
                        "background-color: rgb(44, 49, 57); border-style: solid; border-radius: 4px; }\n"
"#rightButtons .QPushButton:pressed { background-color: rgb(23, 26, 30); border-style: solid; border-radius: 4px; }\n"
"\n"
"/* Theme Settings */\n"
"#extraRightBox { background-color: rgb(44, 49, 58); }\n"
"#themeSettingsTopDetail { background-color: rgb(189, 147, 249); }\n"
"\n"
"/* Bottom Bar */\n"
"#bottomBar { background-color: rgb(44, 49, 58); }\n"
"#bottomBar QLabel { font-size: 11px; color: rgb(113, 126, 149); padding-left: 10px; padding-right: 10px; padding-bottom: 2px; }\n"
"\n"
"/* CONTENT SETTINGS */\n"
"/* MENUS */\n"
"#contentSettings .QPushButton {	\n"
"	background-position: left center;\n"
"    background-repeat: no-repeat;\n"
"	border: none;\n"
"	border-left: 22px solid transparent;\n"
"	background-color:transparent;\n"
"	text-align: left;\n"
"	padding-left: 44px;\n"
"}\n"
"#contentSettings .QPushButton:hover {\n"
"	background-color: rgb(40, 44, 52);\n"
"}\n"
"#contentSettings .QPushButton:pressed {	\n"
"	backgrou"
                        "nd-color: rgb(189, 147, 249);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////QTableView */\n"
"QTableView {	\n"
"	background-color: transparent;\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(44, 49, 58);\n"
"	padding: 0px;\n"
"}\n"
"QTableView::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	text-align: center;\n"
"}\n"
"QTableView::item:selected{\n"
"	background-color: rgb(189, 147, 249);\n"
"}\n"
"QHeaderView::section{\n"
"	background-color: rgb(33, 37, 43);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(44, 49, 58);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(44, 49, 60);\n"
"    border-right: 1px solid rgb(44, 49, 60);\n"
"    text-align: center;\n"
"}\n"
"QTableView::horizontalHeader {	\n"
"	background-color: rgb(33, 37, 43);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"  "
                        "  border: 1px solid rgb(33, 37, 43);\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 3p, 0px;\n"
"	border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(33, 37, 43);\n"
"	border-top-left-radius: 5px;\n"
"	border-bottom-left-radius: 5px;\n"
"}\n"
"\n"
"QHeaderView .QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 9px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QHeaderView .QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 9px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView .QScrollBar::handle:horizontal {\n"
"	border-radius: 3.5px;\n"
"}\n"
"QHeaderView .QScrollBar:vertical {\n"
"	border-radius: 3.5px;\n"
" }\n"
"QTableView .QTableCornerButton::section {\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////"
                        "////////////////////////////////////////////////////\n"
"LineEdit */\n"
"QLineEdit {\n"
"	background-color: rgb(33, 37, 43);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding-left: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QLineEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"PlainTextEdit */\n"
"QPlainTextEdit {\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	padding: 10px;\n"
"	selection-color: rgb(255, 255, 255);\n"
"	selection-background-color: rgb(255, 121, 198);\n"
"}\n"
"QPlainTextEdit  QScrollBar:vertical {\n"
"    width: 8px;\n"
" }\n"
"QPlainTextEdit  QScrollBar:horizontal {\n"
"    height: 8px;\n"
" }\n"
"QPlainTextEdit:hover {\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QPlainTextEdit:"
                        "focus {\n"
"	border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ScrollBars */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 8px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(189, 147, 249);\n"
"    min-width: 25px;\n"
"	border-radius: 4px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-right-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-bottom-left-radius: 4px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}"
                        "\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 8px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {	\n"
"	background: rgb(189, 147, 249);\n"
"    min-height: 25px;\n"
"	border-radius: 4px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-bottom-left-radius: 4px;\n"
"    border-bottom-right-radius: 4px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"	border-top-left-radius: 4px;\n"
"    border-top-right-radius: 4px;\n"
"     subcontrol-position: top;\n"
"    "
                        " subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CheckBox */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"	background-image: url(:/icons/images/icons/cil-check-alt.png);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"RadioButton */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 7"
                        "2);\n"
"	width: 15px;\n"
"	height: 15px;\n"
"	border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"	border: 3px solid rgb(52, 59, 72);	\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"ComboBox */\n"
"QComboBox{\n"
"	background-color: rgb(27, 29, 35);\n"
"	border-radius: 5px;\n"
"	border: 2px solid rgb(33, 37, 43);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"	subcontrol-origin: padding;\n"
"	subcontrol-position: top right;\n"
"	width: 25px; \n"
"	border-left-width: 3px;\n"
"	border-left-color: rgba(39, 44, 54, 150);\n"
"	border-left-style: solid;\n"
"	border-top-right-radius: 3px;\n"
"	border-bottom-right-radius: 3px;	\n"
"	background-image: url(:/icons/i"
                        "mages/icons/cil-arrow-bottom.png);\n"
"	background-position: center;\n"
"	background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 121, 198);	\n"
"	background-color: rgb(33, 37, 43);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Sliders */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 5px;\n"
"    height: 10px;\n"
"	margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(189, 147, 249);\n"
"    border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(255, 121, 198);"
                        "\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 5px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"	background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(189, 147, 249);\n"
"	border: none;\n"
"    height: 10px;\n"
"    width: 10px;\n"
"    margin: 0px;\n"
"	border-radius: 5px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(195, 155, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(255, 121, 198);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"CommandLinkButton */\n"
"QCommandLinkButton {	\n"
"	color: rgb(255, 121, 198);\n"
"	border-radius: 5px;\n"
"	padding: 5px;\n"
"	color: rgb(255, 170, 255);\n"
"}\n"
"QCommandLinkButton:hover {	\n"
"	color: rgb(255, 170, 255);\n"
"	background-color: rgb(44, 49, 60);\n"
"}\n"
"QCommandLinkButton:pres"
                        "sed {	\n"
"	color: rgb(189, 147, 249);\n"
"	background-color: rgb(52, 58, 71);\n"
"}\n"
"\n"
"/* /////////////////////////////////////////////////////////////////////////////////////////////////\n"
"Button */\n"
"#pagesContainer QPushButton {\n"
"	border: 2px solid rgb(52, 59, 72);\n"
"	border-radius: 5px;	\n"
"	background-color: rgb(52, 59, 72);\n"
"}\n"
"#pagesContainer QPushButton:hover {\n"
"	background-color: rgb(57, 65, 80);\n"
"	border: 2px solid rgb(61, 70, 86);\n"
"}\n"
"#pagesContainer QPushButton:pressed {	\n"
"	background-color: rgb(35, 40, 49);\n"
"	border: 2px solid rgb(43, 50, 61);\n"
"}\n"
"\n"
"")
        self.appMargins = QVBoxLayout(self.styleSheet)
        self.appMargins.setSpacing(0)
        self.appMargins.setObjectName(u"appMargins")
        self.appMargins.setContentsMargins(10, 10, 10, 10)
        self.bgApp = QFrame(self.styleSheet)
        self.bgApp.setObjectName(u"bgApp")
        self.bgApp.setStyleSheet(u"")
        self.bgApp.setFrameShape(QFrame.NoFrame)
        self.bgApp.setFrameShadow(QFrame.Raised)
        self.appLayout = QHBoxLayout(self.bgApp)
        self.appLayout.setSpacing(0)
        self.appLayout.setObjectName(u"appLayout")
        self.appLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuBg = QFrame(self.bgApp)
        self.leftMenuBg.setObjectName(u"leftMenuBg")
        self.leftMenuBg.setMinimumSize(QSize(60, 0))
        self.leftMenuBg.setMaximumSize(QSize(60, 16777215))
        self.leftMenuBg.setFrameShape(QFrame.NoFrame)
        self.leftMenuBg.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.leftMenuBg)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.topLogoInfo = QFrame(self.leftMenuBg)
        self.topLogoInfo.setObjectName(u"topLogoInfo")
        self.topLogoInfo.setMinimumSize(QSize(0, 50))
        self.topLogoInfo.setMaximumSize(QSize(16777215, 50))
        self.topLogoInfo.setFrameShape(QFrame.NoFrame)
        self.topLogoInfo.setFrameShadow(QFrame.Raised)
        self.topLogo = QFrame(self.topLogoInfo)
        self.topLogo.setObjectName(u"topLogo")
        self.topLogo.setGeometry(QRect(10, 5, 42, 42))
        self.topLogo.setMinimumSize(QSize(42, 42))
        self.topLogo.setMaximumSize(QSize(42, 42))
        self.topLogo.setFrameShape(QFrame.NoFrame)
        self.topLogo.setFrameShadow(QFrame.Raised)
        self.titleLeftApp = QLabel(self.topLogoInfo)
        self.titleLeftApp.setObjectName(u"titleLeftApp")
        self.titleLeftApp.setGeometry(QRect(70, 8, 160, 20))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.titleLeftApp.setFont(font1)
        self.titleLeftApp.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.titleLeftDescription = QLabel(self.topLogoInfo)
        self.titleLeftDescription.setObjectName(u"titleLeftDescription")
        self.titleLeftDescription.setGeometry(QRect(70, 27, 160, 16))
        self.titleLeftDescription.setMaximumSize(QSize(16777215, 16))
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(8)
        font2.setBold(False)
        font2.setItalic(False)
        self.titleLeftDescription.setFont(font2)
        self.titleLeftDescription.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.verticalLayout_3.addWidget(self.topLogoInfo)

        self.leftMenuFrame = QFrame(self.leftMenuBg)
        self.leftMenuFrame.setObjectName(u"leftMenuFrame")
        self.leftMenuFrame.setFrameShape(QFrame.NoFrame)
        self.leftMenuFrame.setFrameShadow(QFrame.Raised)
        self.verticalMenuLayout = QVBoxLayout(self.leftMenuFrame)
        self.verticalMenuLayout.setSpacing(0)
        self.verticalMenuLayout.setObjectName(u"verticalMenuLayout")
        self.verticalMenuLayout.setContentsMargins(0, 0, 0, 0)
        self.toggleBox = QFrame(self.leftMenuFrame)
        self.toggleBox.setObjectName(u"toggleBox")
        self.toggleBox.setMaximumSize(QSize(16777215, 45))
        self.toggleBox.setFrameShape(QFrame.NoFrame)
        self.toggleBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.toggleBox)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.toggleButton = QPushButton(self.toggleBox)
        self.toggleButton.setObjectName(u"toggleButton")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toggleButton.sizePolicy().hasHeightForWidth())
        self.toggleButton.setSizePolicy(sizePolicy)
        self.toggleButton.setMinimumSize(QSize(0, 45))
        self.toggleButton.setFont(font)
        self.toggleButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.toggleButton.setLayoutDirection(Qt.LeftToRight)
        self.toggleButton.setStyleSheet(u"background-image: url(:/icons/images/icons/icon_menu.png);")

        self.verticalLayout_4.addWidget(self.toggleButton)


        self.verticalMenuLayout.addWidget(self.toggleBox)

        self.topMenu = QFrame(self.leftMenuFrame)
        self.topMenu.setObjectName(u"topMenu")
        self.topMenu.setFrameShape(QFrame.NoFrame)
        self.topMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.topMenu)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.topMenu)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy)
        self.btn_home.setMinimumSize(QSize(0, 45))
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_home.setLayoutDirection(Qt.LeftToRight)
        self.btn_home.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-home.png);")

        self.verticalLayout_8.addWidget(self.btn_home)

        self.btn_settings = QPushButton(self.topMenu)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_settings.sizePolicy().hasHeightForWidth())
        self.btn_settings.setSizePolicy(sizePolicy)
        self.btn_settings.setMinimumSize(QSize(0, 45))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_settings.setLayoutDirection(Qt.LeftToRight)
        self.btn_settings.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-equalizer.png);")

        self.verticalLayout_8.addWidget(self.btn_settings)

        self.btn_chart = QPushButton(self.topMenu)
        self.btn_chart.setObjectName(u"btn_chart")
        self.btn_chart.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_chart.sizePolicy().hasHeightForWidth())
        self.btn_chart.setSizePolicy(sizePolicy)
        self.btn_chart.setMinimumSize(QSize(0, 45))
        self.btn_chart.setFont(font)
        self.btn_chart.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_chart.setLayoutDirection(Qt.LeftToRight)
        self.btn_chart.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-chart-line.png);")

        self.verticalLayout_8.addWidget(self.btn_chart)

        self.btn_table = QPushButton(self.topMenu)
        self.btn_table.setObjectName(u"btn_table")
        self.btn_table.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_table.sizePolicy().hasHeightForWidth())
        self.btn_table.setSizePolicy(sizePolicy)
        self.btn_table.setMinimumSize(QSize(0, 45))
        self.btn_table.setFont(font)
        self.btn_table.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_table.setLayoutDirection(Qt.LeftToRight)
        self.btn_table.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-view-module.png);")

        self.verticalLayout_8.addWidget(self.btn_table)

        self.btn_exit = QPushButton(self.topMenu)
        self.btn_exit.setObjectName(u"btn_exit")
        sizePolicy.setHeightForWidth(self.btn_exit.sizePolicy().hasHeightForWidth())
        self.btn_exit.setSizePolicy(sizePolicy)
        self.btn_exit.setMinimumSize(QSize(0, 45))
        self.btn_exit.setFont(font)
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exit.setLayoutDirection(Qt.LeftToRight)
        self.btn_exit.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_8.addWidget(self.btn_exit)


        self.verticalMenuLayout.addWidget(self.topMenu, 0, Qt.AlignTop)

        self.bottomMenu = QFrame(self.leftMenuFrame)
        self.bottomMenu.setObjectName(u"bottomMenu")
        self.bottomMenu.setFrameShape(QFrame.NoFrame)
        self.bottomMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.bottomMenu)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_start = QPushButton(self.bottomMenu)
        self.btn_start.setObjectName(u"btn_start")
        self.btn_start.setEnabled(False)
        sizePolicy.setHeightForWidth(self.btn_start.sizePolicy().hasHeightForWidth())
        self.btn_start.setSizePolicy(sizePolicy)
        self.btn_start.setMinimumSize(QSize(0, 45))
        self.btn_start.setFont(font)
        self.btn_start.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_start.setLayoutDirection(Qt.LeftToRight)
        self.btn_start.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-media-play.png);")

        self.verticalLayout_9.addWidget(self.btn_start)


        self.verticalMenuLayout.addWidget(self.bottomMenu, 0, Qt.AlignBottom)


        self.verticalLayout_3.addWidget(self.leftMenuFrame)


        self.appLayout.addWidget(self.leftMenuBg)

        self.contentBox = QFrame(self.bgApp)
        self.contentBox.setObjectName(u"contentBox")
        self.contentBox.setFrameShape(QFrame.NoFrame)
        self.contentBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contentBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.contentTopBg = QFrame(self.contentBox)
        self.contentTopBg.setObjectName(u"contentTopBg")
        self.contentTopBg.setMinimumSize(QSize(0, 50))
        self.contentTopBg.setMaximumSize(QSize(16777215, 50))
        self.contentTopBg.setFrameShape(QFrame.NoFrame)
        self.contentTopBg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.contentTopBg)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 10, 0)
        self.leftBox = QFrame(self.contentTopBg)
        self.leftBox.setObjectName(u"leftBox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.leftBox.sizePolicy().hasHeightForWidth())
        self.leftBox.setSizePolicy(sizePolicy1)
        self.leftBox.setFrameShape(QFrame.NoFrame)
        self.leftBox.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.leftBox)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.titleRightInfo = QLabel(self.leftBox)
        self.titleRightInfo.setObjectName(u"titleRightInfo")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.titleRightInfo.sizePolicy().hasHeightForWidth())
        self.titleRightInfo.setSizePolicy(sizePolicy2)
        self.titleRightInfo.setMaximumSize(QSize(16777215, 45))
        self.titleRightInfo.setFont(font)
        self.titleRightInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.titleRightInfo)


        self.horizontalLayout.addWidget(self.leftBox)

        self.rightButtons = QFrame(self.contentTopBg)
        self.rightButtons.setObjectName(u"rightButtons")
        self.rightButtons.setMinimumSize(QSize(0, 28))
        self.rightButtons.setFrameShape(QFrame.NoFrame)
        self.rightButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.rightButtons)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.settingsTopBtn = QPushButton(self.rightButtons)
        self.settingsTopBtn.setObjectName(u"settingsTopBtn")
        self.settingsTopBtn.setMinimumSize(QSize(28, 28))
        self.settingsTopBtn.setMaximumSize(QSize(28, 28))
        self.settingsTopBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/images/icons/cil-comment-square.png", QSize(), QIcon.Normal, QIcon.Off)
        self.settingsTopBtn.setIcon(icon)
        self.settingsTopBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.settingsTopBtn)

        self.minimizeAppBtn = QPushButton(self.rightButtons)
        self.minimizeAppBtn.setObjectName(u"minimizeAppBtn")
        self.minimizeAppBtn.setMinimumSize(QSize(28, 28))
        self.minimizeAppBtn.setMaximumSize(QSize(28, 28))
        self.minimizeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/images/icons/icon_minimize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeAppBtn.setIcon(icon1)
        self.minimizeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.minimizeAppBtn)

        self.maximizeRestoreAppBtn = QPushButton(self.rightButtons)
        self.maximizeRestoreAppBtn.setObjectName(u"maximizeRestoreAppBtn")
        self.maximizeRestoreAppBtn.setMinimumSize(QSize(28, 28))
        self.maximizeRestoreAppBtn.setMaximumSize(QSize(28, 28))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setStyleStrategy(QFont.PreferDefault)
        self.maximizeRestoreAppBtn.setFont(font3)
        self.maximizeRestoreAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/images/icons/icon_maximize.png", QSize(), QIcon.Normal, QIcon.Off)
        self.maximizeRestoreAppBtn.setIcon(icon2)
        self.maximizeRestoreAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.maximizeRestoreAppBtn)

        self.closeAppBtn = QPushButton(self.rightButtons)
        self.closeAppBtn.setObjectName(u"closeAppBtn")
        self.closeAppBtn.setMinimumSize(QSize(28, 28))
        self.closeAppBtn.setMaximumSize(QSize(28, 28))
        self.closeAppBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/images/icons/icon_close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.closeAppBtn.setIcon(icon3)
        self.closeAppBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.closeAppBtn)


        self.horizontalLayout.addWidget(self.rightButtons, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.contentTopBg)

        self.contentBottom = QFrame(self.contentBox)
        self.contentBottom.setObjectName(u"contentBottom")
        self.contentBottom.setFrameShape(QFrame.NoFrame)
        self.contentBottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.contentBottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.content = QFrame(self.contentBottom)
        self.content.setObjectName(u"content")
        self.content.setFrameShape(QFrame.NoFrame)
        self.content.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.content)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pagesContainer = QFrame(self.content)
        self.pagesContainer.setObjectName(u"pagesContainer")
        self.pagesContainer.setFrameShape(QFrame.NoFrame)
        self.pagesContainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.pagesContainer)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(10, 10, 10, 10)
        self.stackedWidget = QStackedWidget(self.pagesContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background: transparent;")
        self.home = QWidget()
        self.home.setObjectName(u"home")
        self.home.setStyleSheet(u"background-image: url(:/images/images/images/PyDracula_vertical.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;")
        self.stackedWidget.addWidget(self.home)
        self.page_setting = QWidget()
        self.page_setting.setObjectName(u"page_setting")
        self.page_setting.setStyleSheet(u"b")
        self.verticalLayout = QVBoxLayout(self.page_setting)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 5, 10, 10)
        self.row_1 = QFrame(self.page_setting)
        self.row_1.setObjectName(u"row_1")
        self.row_1.setFrameShape(QFrame.StyledPanel)
        self.row_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.row_1)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_div_content_1 = QFrame(self.row_1)
        self.frame_div_content_1.setObjectName(u"frame_div_content_1")
        self.frame_div_content_1.setMinimumSize(QSize(0, 110))
        self.frame_div_content_1.setMaximumSize(QSize(16777215, 110))
        self.frame_div_content_1.setFrameShape(QFrame.NoFrame)
        self.frame_div_content_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_div_content_1)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_title_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_title_wid_1.setObjectName(u"frame_title_wid_1")
        self.frame_title_wid_1.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_1.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_title_wid_1)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.labelBoxBlenderInstalation = QLabel(self.frame_title_wid_1)
        self.labelBoxBlenderInstalation.setObjectName(u"labelBoxBlenderInstalation")
        self.labelBoxBlenderInstalation.setFont(font)
        self.labelBoxBlenderInstalation.setStyleSheet(u"")

        self.verticalLayout_18.addWidget(self.labelBoxBlenderInstalation)


        self.verticalLayout_17.addWidget(self.frame_title_wid_1)

        self.frame_content_wid_1 = QFrame(self.frame_div_content_1)
        self.frame_content_wid_1.setObjectName(u"frame_content_wid_1")
        self.frame_content_wid_1.setFrameShape(QFrame.NoFrame)
        self.frame_content_wid_1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_content_wid_1)
        self.verticalLayout_28.setSpacing(3)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.le_profile_file = QLineEdit(self.frame_content_wid_1)
        self.le_profile_file.setObjectName(u"le_profile_file")
        self.le_profile_file.setMinimumSize(QSize(0, 30))
        self.le_profile_file.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_profile_file.setReadOnly(True)

        self.horizontalLayout_9.addWidget(self.le_profile_file)

        self.pb_load_profile = QPushButton(self.frame_content_wid_1)
        self.pb_load_profile.setObjectName(u"pb_load_profile")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pb_load_profile.sizePolicy().hasHeightForWidth())
        self.pb_load_profile.setSizePolicy(sizePolicy3)
        self.pb_load_profile.setMinimumSize(QSize(75, 30))
        self.pb_load_profile.setFont(font)
        self.pb_load_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_load_profile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon4 = QIcon()
        icon4.addFile(u":/icons/images/icons/cil-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_load_profile.setIcon(icon4)

        self.horizontalLayout_9.addWidget(self.pb_load_profile)

        self.pb_save_profile = QPushButton(self.frame_content_wid_1)
        self.pb_save_profile.setObjectName(u"pb_save_profile")
        sizePolicy3.setHeightForWidth(self.pb_save_profile.sizePolicy().hasHeightForWidth())
        self.pb_save_profile.setSizePolicy(sizePolicy3)
        self.pb_save_profile.setMinimumSize(QSize(75, 30))
        self.pb_save_profile.setFont(font)
        self.pb_save_profile.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_save_profile.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        icon5 = QIcon()
        icon5.addFile(u":/icons/images/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_profile.setIcon(icon5)

        self.horizontalLayout_9.addWidget(self.pb_save_profile)


        self.verticalLayout_28.addLayout(self.horizontalLayout_9)

        self.labelVersion_4 = QLabel(self.frame_content_wid_1)
        self.labelVersion_4.setObjectName(u"labelVersion_4")
        sizePolicy3.setHeightForWidth(self.labelVersion_4.sizePolicy().hasHeightForWidth())
        self.labelVersion_4.setSizePolicy(sizePolicy3)
        self.labelVersion_4.setMinimumSize(QSize(0, 15))
        self.labelVersion_4.setMaximumSize(QSize(16777215, 15))
        self.labelVersion_4.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_4.setLineWidth(1)
        self.labelVersion_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_28.addWidget(self.labelVersion_4)


        self.verticalLayout_17.addWidget(self.frame_content_wid_1)


        self.verticalLayout_16.addWidget(self.frame_div_content_1)


        self.verticalLayout.addWidget(self.row_1)

        self.frame_title_wid_2 = QFrame(self.page_setting)
        self.frame_title_wid_2.setObjectName(u"frame_title_wid_2")
        self.frame_title_wid_2.setMaximumSize(QSize(16777215, 35))
        self.frame_title_wid_2.setFrameShape(QFrame.StyledPanel)
        self.frame_title_wid_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_title_wid_2)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.labelBoxBlenderInstalation_3 = QLabel(self.frame_title_wid_2)
        self.labelBoxBlenderInstalation_3.setObjectName(u"labelBoxBlenderInstalation_3")
        self.labelBoxBlenderInstalation_3.setFont(font)
        self.labelBoxBlenderInstalation_3.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.labelBoxBlenderInstalation_3)


        self.verticalLayout.addWidget(self.frame_title_wid_2)

        self.row_2 = QFrame(self.page_setting)
        self.row_2.setObjectName(u"row_2")
        self.row_2.setFrameShape(QFrame.StyledPanel)
        self.row_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.row_2)
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setSpacing(10)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.labelVersion_12 = QLabel(self.row_2)
        self.labelVersion_12.setObjectName(u"labelVersion_12")
        sizePolicy3.setHeightForWidth(self.labelVersion_12.sizePolicy().hasHeightForWidth())
        self.labelVersion_12.setSizePolicy(sizePolicy3)
        self.labelVersion_12.setMinimumSize(QSize(0, 26))
        self.labelVersion_12.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_12.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_12.setLineWidth(1)
        self.labelVersion_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.labelVersion_12)

        self.cb_range = QComboBox(self.row_2)
        self.cb_range.addItem("")
        self.cb_range.addItem("")
        self.cb_range.setObjectName(u"cb_range")
        self.cb_range.setEnabled(True)
        sizePolicy3.setHeightForWidth(self.cb_range.sizePolicy().hasHeightForWidth())
        self.cb_range.setSizePolicy(sizePolicy3)
        self.cb_range.setMinimumSize(QSize(0, 34))
        self.cb_range.setMaximumSize(QSize(16777215, 34))
        self.cb_range.setFont(font)
        self.cb_range.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_range.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_range.setIconSize(QSize(16, 16))

        self.verticalLayout_26.addWidget(self.cb_range)

        self.labelVersion_6 = QLabel(self.row_2)
        self.labelVersion_6.setObjectName(u"labelVersion_6")
        sizePolicy3.setHeightForWidth(self.labelVersion_6.sizePolicy().hasHeightForWidth())
        self.labelVersion_6.setSizePolicy(sizePolicy3)
        self.labelVersion_6.setMinimumSize(QSize(0, 26))
        self.labelVersion_6.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_6.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_6.setLineWidth(1)
        self.labelVersion_6.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_26.addWidget(self.labelVersion_6)

        self.cb_trig_mode = QComboBox(self.row_2)
        self.cb_trig_mode.addItem("")
        self.cb_trig_mode.addItem("")
        self.cb_trig_mode.setObjectName(u"cb_trig_mode")
        self.cb_trig_mode.setMinimumSize(QSize(0, 34))
        self.cb_trig_mode.setMaximumSize(QSize(16777215, 34))
        self.cb_trig_mode.setFont(font)
        self.cb_trig_mode.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_trig_mode.setAutoFillBackground(False)
        self.cb_trig_mode.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_trig_mode.setIconSize(QSize(16, 16))
        self.cb_trig_mode.setFrame(True)

        self.verticalLayout_26.addWidget(self.cb_trig_mode)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_3)


        self.horizontalLayout_10.addLayout(self.verticalLayout_26)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setSpacing(10)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.labelVersion_5 = QLabel(self.row_2)
        self.labelVersion_5.setObjectName(u"labelVersion_5")
        sizePolicy3.setHeightForWidth(self.labelVersion_5.sizePolicy().hasHeightForWidth())
        self.labelVersion_5.setSizePolicy(sizePolicy3)
        self.labelVersion_5.setMinimumSize(QSize(0, 26))
        self.labelVersion_5.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_5.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_5.setLineWidth(1)
        self.labelVersion_5.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.labelVersion_5)

        self.cb_trig_dir = QComboBox(self.row_2)
        self.cb_trig_dir.addItem("")
        self.cb_trig_dir.addItem("")
        self.cb_trig_dir.addItem("")
        self.cb_trig_dir.setObjectName(u"cb_trig_dir")
        self.cb_trig_dir.setMinimumSize(QSize(0, 34))
        self.cb_trig_dir.setMaximumSize(QSize(16777215, 34))
        self.cb_trig_dir.setFont(font)
        self.cb_trig_dir.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_trig_dir.setAutoFillBackground(False)
        self.cb_trig_dir.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_trig_dir.setIconSize(QSize(16, 16))
        self.cb_trig_dir.setFrame(True)

        self.verticalLayout_25.addWidget(self.cb_trig_dir)

        self.labelVersion_7 = QLabel(self.row_2)
        self.labelVersion_7.setObjectName(u"labelVersion_7")
        sizePolicy3.setHeightForWidth(self.labelVersion_7.sizePolicy().hasHeightForWidth())
        self.labelVersion_7.setSizePolicy(sizePolicy3)
        self.labelVersion_7.setMinimumSize(QSize(0, 26))
        self.labelVersion_7.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_7.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_7.setLineWidth(1)
        self.labelVersion_7.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_25.addWidget(self.labelVersion_7)

        self.cb_os = QComboBox(self.row_2)
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.addItem("")
        self.cb_os.setObjectName(u"cb_os")
        self.cb_os.setMinimumSize(QSize(0, 34))
        self.cb_os.setMaximumSize(QSize(16777215, 34))
        self.cb_os.setFont(font)
        self.cb_os.setCursor(QCursor(Qt.PointingHandCursor))
        self.cb_os.setAutoFillBackground(False)
        self.cb_os.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.cb_os.setIconSize(QSize(16, 16))
        self.cb_os.setFrame(True)

        self.verticalLayout_25.addWidget(self.cb_os)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_4)


        self.horizontalLayout_10.addLayout(self.verticalLayout_25)

        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setSpacing(10)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.labelVersion_8 = QLabel(self.row_2)
        self.labelVersion_8.setObjectName(u"labelVersion_8")
        sizePolicy3.setHeightForWidth(self.labelVersion_8.sizePolicy().hasHeightForWidth())
        self.labelVersion_8.setSizePolicy(sizePolicy3)
        self.labelVersion_8.setMinimumSize(QSize(0, 26))
        self.labelVersion_8.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_8.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_8.setLineWidth(1)
        self.labelVersion_8.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_24.addWidget(self.labelVersion_8)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_12.setContentsMargins(5, -1, 17, -1)
        self.slider_period = QSlider(self.row_2)
        self.slider_period.setObjectName(u"slider_period")
        sizePolicy3.setHeightForWidth(self.slider_period.sizePolicy().hasHeightForWidth())
        self.slider_period.setSizePolicy(sizePolicy3)
        self.slider_period.setStyleSheet(u"")
        self.slider_period.setMinimum(10)
        self.slider_period.setMaximum(5000)
        self.slider_period.setPageStep(1)
        self.slider_period.setOrientation(Qt.Horizontal)
        self.slider_period.setTickPosition(QSlider.NoTicks)

        self.horizontalLayout_12.addWidget(self.slider_period)


        self.verticalLayout_24.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setSizeConstraint(QLayout.SetMinimumSize)
        self.le_period = QLineEdit(self.row_2)
        self.le_period.setObjectName(u"le_period")
        self.le_period.setMinimumSize(QSize(0, 34))
        self.le_period.setMaximumSize(QSize(16777215, 34))
        self.le_period.setCursor(QCursor(Qt.PointingHandCursor))
        self.le_period.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_period.setReadOnly(False)

        self.horizontalLayout_8.addWidget(self.le_period)

        self.labelVersion_9 = QLabel(self.row_2)
        self.labelVersion_9.setObjectName(u"labelVersion_9")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.labelVersion_9.sizePolicy().hasHeightForWidth())
        self.labelVersion_9.setSizePolicy(sizePolicy4)
        self.labelVersion_9.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_9.setLineWidth(1)
        self.labelVersion_9.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.labelVersion_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.le_frequency = QLineEdit(self.row_2)
        self.le_frequency.setObjectName(u"le_frequency")
        self.le_frequency.setMinimumSize(QSize(0, 34))
        self.le_frequency.setMaximumSize(QSize(16777215, 34))
        self.le_frequency.setCursor(QCursor(Qt.PointingHandCursor))
        self.le_frequency.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_frequency.setReadOnly(False)

        self.horizontalLayout_8.addWidget(self.le_frequency)

        self.labelVersion_10 = QLabel(self.row_2)
        self.labelVersion_10.setObjectName(u"labelVersion_10")
        sizePolicy4.setHeightForWidth(self.labelVersion_10.sizePolicy().hasHeightForWidth())
        self.labelVersion_10.setSizePolicy(sizePolicy4)
        self.labelVersion_10.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_10.setLineWidth(1)
        self.labelVersion_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.labelVersion_10)


        self.verticalLayout_24.addLayout(self.horizontalLayout_8)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_5)


        self.horizontalLayout_10.addLayout(self.verticalLayout_24)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setSpacing(10)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.labelVersion_11 = QLabel(self.row_2)
        self.labelVersion_11.setObjectName(u"labelVersion_11")
        sizePolicy3.setHeightForWidth(self.labelVersion_11.sizePolicy().hasHeightForWidth())
        self.labelVersion_11.setSizePolicy(sizePolicy3)
        self.labelVersion_11.setMinimumSize(QSize(0, 26))
        self.labelVersion_11.setMaximumSize(QSize(16777215, 26))
        self.labelVersion_11.setStyleSheet(u"color: rgb(113, 126, 149);")
        self.labelVersion_11.setLineWidth(1)
        self.labelVersion_11.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_27.addWidget(self.labelVersion_11)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(5, -1, 10, -1)
        self.slider_cycles = QSlider(self.row_2)
        self.slider_cycles.setObjectName(u"slider_cycles")
        sizePolicy3.setHeightForWidth(self.slider_cycles.sizePolicy().hasHeightForWidth())
        self.slider_cycles.setSizePolicy(sizePolicy3)
        self.slider_cycles.setStyleSheet(u"")
        self.slider_cycles.setMinimum(10)
        self.slider_cycles.setMaximum(2097152)
        self.slider_cycles.setPageStep(1)
        self.slider_cycles.setOrientation(Qt.Horizontal)

        self.horizontalLayout_13.addWidget(self.slider_cycles)


        self.verticalLayout_27.addLayout(self.horizontalLayout_13)

        self.le_cycles = QLineEdit(self.row_2)
        self.le_cycles.setObjectName(u"le_cycles")
        self.le_cycles.setMinimumSize(QSize(0, 34))
        self.le_cycles.setMaximumSize(QSize(16777215, 34))
        self.le_cycles.setCursor(QCursor(Qt.PointingHandCursor))
        self.le_cycles.setStyleSheet(u"background-color: rgb(33, 37, 43);")
        self.le_cycles.setReadOnly(False)

        self.verticalLayout_27.addWidget(self.le_cycles)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_27.addItem(self.verticalSpacer_2)


        self.horizontalLayout_10.addLayout(self.verticalLayout_27)

        self.horizontalLayout_10.setStretch(0, 2)
        self.horizontalLayout_10.setStretch(1, 2)
        self.horizontalLayout_10.setStretch(2, 3)
        self.horizontalLayout_10.setStretch(3, 2)

        self.verticalLayout.addWidget(self.row_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.stackedWidget.addWidget(self.page_setting)
        self.page_plot = QWidget()
        self.page_plot.setObjectName(u"page_plot")
        self.verticalLayout_5 = QVBoxLayout(self.page_plot)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(10, 5, 10, 10)
        self.glw_detail = GraphicsLayoutWidget(self.page_plot)
        self.glw_detail.setObjectName(u"glw_detail")
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.glw_detail.sizePolicy().hasHeightForWidth())
        self.glw_detail.setSizePolicy(sizePolicy5)

        self.verticalLayout_5.addWidget(self.glw_detail)

        self.glw_overall = GraphicsLayoutWidget(self.page_plot)
        self.glw_overall.setObjectName(u"glw_overall")
        sizePolicy4.setHeightForWidth(self.glw_overall.sizePolicy().hasHeightForWidth())
        self.glw_overall.setSizePolicy(sizePolicy4)

        self.verticalLayout_5.addWidget(self.glw_overall)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 6, -1, -1)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.gridLayout.setHorizontalSpacing(20)
        self.gridLayout.setVerticalSpacing(10)
        self.cb_ch7 = QCheckBox(self.page_plot)
        self.cb_ch7.setObjectName(u"cb_ch7")
        sizePolicy3.setHeightForWidth(self.cb_ch7.sizePolicy().hasHeightForWidth())
        self.cb_ch7.setSizePolicy(sizePolicy3)
        self.cb_ch7.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch7, 0, 3, 1, 1)

        self.cb_ch5 = QCheckBox(self.page_plot)
        self.cb_ch5.setObjectName(u"cb_ch5")
        sizePolicy3.setHeightForWidth(self.cb_ch5.sizePolicy().hasHeightForWidth())
        self.cb_ch5.setSizePolicy(sizePolicy3)
        self.cb_ch5.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch5, 0, 2, 1, 1)

        self.cb_ch2 = QCheckBox(self.page_plot)
        self.cb_ch2.setObjectName(u"cb_ch2")
        sizePolicy3.setHeightForWidth(self.cb_ch2.sizePolicy().hasHeightForWidth())
        self.cb_ch2.setSizePolicy(sizePolicy3)
        self.cb_ch2.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch2, 1, 0, 1, 1)

        self.cb_ch1 = QCheckBox(self.page_plot)
        self.cb_ch1.setObjectName(u"cb_ch1")
        sizePolicy3.setHeightForWidth(self.cb_ch1.sizePolicy().hasHeightForWidth())
        self.cb_ch1.setSizePolicy(sizePolicy3)
        self.cb_ch1.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch1, 0, 0, 1, 1)

        self.cb_ch8 = QCheckBox(self.page_plot)
        self.cb_ch8.setObjectName(u"cb_ch8")
        sizePolicy3.setHeightForWidth(self.cb_ch8.sizePolicy().hasHeightForWidth())
        self.cb_ch8.setSizePolicy(sizePolicy3)
        self.cb_ch8.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch8, 1, 3, 1, 1)

        self.cb_ch6 = QCheckBox(self.page_plot)
        self.cb_ch6.setObjectName(u"cb_ch6")
        sizePolicy3.setHeightForWidth(self.cb_ch6.sizePolicy().hasHeightForWidth())
        self.cb_ch6.setSizePolicy(sizePolicy3)
        self.cb_ch6.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch6, 1, 2, 1, 1)

        self.cb_ch3 = QCheckBox(self.page_plot)
        self.cb_ch3.setObjectName(u"cb_ch3")
        sizePolicy3.setHeightForWidth(self.cb_ch3.sizePolicy().hasHeightForWidth())
        self.cb_ch3.setSizePolicy(sizePolicy3)
        self.cb_ch3.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch3, 0, 1, 1, 1)

        self.cb_ch4 = QCheckBox(self.page_plot)
        self.cb_ch4.setObjectName(u"cb_ch4")
        sizePolicy3.setHeightForWidth(self.cb_ch4.sizePolicy().hasHeightForWidth())
        self.cb_ch4.setSizePolicy(sizePolicy3)
        self.cb_ch4.setChecked(True)

        self.gridLayout.addWidget(self.cb_ch4, 1, 1, 1, 1)

        self.pb_save_plot = QPushButton(self.page_plot)
        self.pb_save_plot.setObjectName(u"pb_save_plot")
        sizePolicy1.setHeightForWidth(self.pb_save_plot.sizePolicy().hasHeightForWidth())
        self.pb_save_plot.setSizePolicy(sizePolicy1)
        self.pb_save_plot.setMinimumSize(QSize(75, 30))
        self.pb_save_plot.setFont(font)
        self.pb_save_plot.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_save_plot.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pb_save_plot.setIcon(icon5)

        self.gridLayout.addWidget(self.pb_save_plot, 1, 4, 1, 1)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)

        self.horizontalLayout_6.addLayout(self.gridLayout)

        self.horizontalLayout_6.setStretch(0, 5)

        self.verticalLayout_5.addLayout(self.horizontalLayout_6)

        self.verticalLayout_5.setStretch(0, 30)
        self.verticalLayout_5.setStretch(1, 3)
        self.verticalLayout_5.setStretch(2, 5)
        self.stackedWidget.addWidget(self.page_plot)
        self.page_table = QWidget()
        self.page_table.setObjectName(u"page_table")
        self.verticalLayout_10 = QVBoxLayout(self.page_table)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(10, 5, 10, 10)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.labelBoxBlenderInstalation_2 = QLabel(self.page_table)
        self.labelBoxBlenderInstalation_2.setObjectName(u"labelBoxBlenderInstalation_2")
        self.labelBoxBlenderInstalation_2.setFont(font)
        self.labelBoxBlenderInstalation_2.setStyleSheet(u"")

        self.horizontalLayout_7.addWidget(self.labelBoxBlenderInstalation_2)

        self.pb_export_table = QPushButton(self.page_table)
        self.pb_export_table.setObjectName(u"pb_export_table")
        sizePolicy4.setHeightForWidth(self.pb_export_table.sizePolicy().hasHeightForWidth())
        self.pb_export_table.setSizePolicy(sizePolicy4)
        self.pb_export_table.setMinimumSize(QSize(75, 30))
        self.pb_export_table.setMaximumSize(QSize(100, 16777215))
        self.pb_export_table.setFont(font)
        self.pb_export_table.setCursor(QCursor(Qt.PointingHandCursor))
        self.pb_export_table.setStyleSheet(u"background-color: rgb(52, 59, 72);")
        self.pb_export_table.setIcon(icon5)

        self.horizontalLayout_7.addWidget(self.pb_export_table)


        self.verticalLayout_10.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.page_table)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_10.addWidget(self.tableView)

        self.stackedWidget.addWidget(self.page_table)

        self.verticalLayout_15.addWidget(self.stackedWidget)


        self.horizontalLayout_4.addWidget(self.pagesContainer)

        self.extraRightBox = QFrame(self.content)
        self.extraRightBox.setObjectName(u"extraRightBox")
        self.extraRightBox.setMinimumSize(QSize(0, 0))
        self.extraRightBox.setMaximumSize(QSize(0, 16777215))
        self.extraRightBox.setFrameShape(QFrame.NoFrame)
        self.extraRightBox.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.extraRightBox)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.themeSettingsTopDetail = QFrame(self.extraRightBox)
        self.themeSettingsTopDetail.setObjectName(u"themeSettingsTopDetail")
        self.themeSettingsTopDetail.setMaximumSize(QSize(16777215, 3))
        self.themeSettingsTopDetail.setFrameShape(QFrame.NoFrame)
        self.themeSettingsTopDetail.setFrameShadow(QFrame.Raised)

        self.verticalLayout_7.addWidget(self.themeSettingsTopDetail)

        self.contentSettings = QFrame(self.extraRightBox)
        self.contentSettings.setObjectName(u"contentSettings")
        self.contentSettings.setFrameShape(QFrame.NoFrame)
        self.contentSettings.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.contentSettings)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.topMenus = QFrame(self.contentSettings)
        self.topMenus.setObjectName(u"topMenus")
        self.topMenus.setFrameShape(QFrame.NoFrame)
        self.topMenus.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.topMenus)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.btn_message = QPushButton(self.topMenus)
        self.btn_message.setObjectName(u"btn_message")
        sizePolicy.setHeightForWidth(self.btn_message.sizePolicy().hasHeightForWidth())
        self.btn_message.setSizePolicy(sizePolicy)
        self.btn_message.setMinimumSize(QSize(0, 45))
        self.btn_message.setFont(font)
        self.btn_message.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_message.setLayoutDirection(Qt.LeftToRight)
        self.btn_message.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-envelope-open.png);")

        self.verticalLayout_14.addWidget(self.btn_message)

        self.btn_print = QPushButton(self.topMenus)
        self.btn_print.setObjectName(u"btn_print")
        sizePolicy.setHeightForWidth(self.btn_print.sizePolicy().hasHeightForWidth())
        self.btn_print.setSizePolicy(sizePolicy)
        self.btn_print.setMinimumSize(QSize(0, 45))
        self.btn_print.setFont(font)
        self.btn_print.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_print.setLayoutDirection(Qt.LeftToRight)
        self.btn_print.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-print.png);")

        self.verticalLayout_14.addWidget(self.btn_print)

        self.btn_logout = QPushButton(self.topMenus)
        self.btn_logout.setObjectName(u"btn_logout")
        sizePolicy.setHeightForWidth(self.btn_logout.sizePolicy().hasHeightForWidth())
        self.btn_logout.setSizePolicy(sizePolicy)
        self.btn_logout.setMinimumSize(QSize(0, 45))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_logout.setLayoutDirection(Qt.LeftToRight)
        self.btn_logout.setStyleSheet(u"background-image: url(:/icons/images/icons/cil-account-logout.png);")

        self.verticalLayout_14.addWidget(self.btn_logout)


        self.verticalLayout_13.addWidget(self.topMenus, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.contentSettings)


        self.horizontalLayout_4.addWidget(self.extraRightBox)


        self.verticalLayout_6.addWidget(self.content)

        self.bottomBar = QFrame(self.contentBottom)
        self.bottomBar.setObjectName(u"bottomBar")
        self.bottomBar.setMinimumSize(QSize(0, 22))
        self.bottomBar.setMaximumSize(QSize(16777215, 22))
        self.bottomBar.setFrameShape(QFrame.NoFrame)
        self.bottomBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.bottomBar)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.connection_status_label = QLabel(self.bottomBar)
        self.connection_status_label.setObjectName(u"connection_status_label")
        self.connection_status_label.setMaximumSize(QSize(16777215, 16))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setBold(False)
        font4.setItalic(False)
        self.connection_status_label.setFont(font4)
        self.connection_status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.connection_status_label)

        self.running_status_label = QLabel(self.bottomBar)
        self.running_status_label.setObjectName(u"running_status_label")
        self.running_status_label.setMaximumSize(QSize(16777215, 16))
        self.running_status_label.setFont(font4)
        self.running_status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.running_status_label)

        self.time_status_label = QLabel(self.bottomBar)
        self.time_status_label.setObjectName(u"time_status_label")
        self.time_status_label.setMaximumSize(QSize(16777215, 16))
        self.time_status_label.setFont(font4)
        self.time_status_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.time_status_label)

        self.version = QLabel(self.bottomBar)
        self.version.setObjectName(u"version")
        self.version.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.version)

        self.frame_size_grip = QFrame(self.bottomBar)
        self.frame_size_grip.setObjectName(u"frame_size_grip")
        self.frame_size_grip.setMinimumSize(QSize(20, 0))
        self.frame_size_grip.setMaximumSize(QSize(20, 16777215))
        self.frame_size_grip.setFrameShape(QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_size_grip)


        self.verticalLayout_6.addWidget(self.bottomBar)


        self.verticalLayout_2.addWidget(self.contentBottom)


        self.appLayout.addWidget(self.contentBox)


        self.appMargins.addWidget(self.bgApp)

        MainWindow.setCentralWidget(self.styleSheet)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MiaowDaq - ULM7606 Data Acquisition Application", None))
        self.titleLeftApp.setText(QCoreApplication.translate("MainWindow", u"MiaowDaq", None))
        self.titleLeftDescription.setText(QCoreApplication.translate("MainWindow", u"Data acquisition demo", None))
        self.toggleButton.setText(QCoreApplication.translate("MainWindow", u"Hide", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_chart.setText(QCoreApplication.translate("MainWindow", u"Chart", None))
        self.btn_table.setText(QCoreApplication.translate("MainWindow", u"Table", None))
        self.btn_exit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.btn_start.setText(QCoreApplication.translate("MainWindow", u"Start Sampling", None))
        self.titleRightInfo.setText(QCoreApplication.translate("MainWindow", u"MiaowDaq - ULM7606 Data Acquisition Application", None))
#if QT_CONFIG(tooltip)
        self.settingsTopBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsTopBtn.setText("")
#if QT_CONFIG(tooltip)
        self.minimizeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maximizeRestoreAppBtn.setText("")
#if QT_CONFIG(tooltip)
        self.closeAppBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.closeAppBtn.setText("")
        self.labelBoxBlenderInstalation.setText(QCoreApplication.translate("MainWindow", u"PROFILE", None))
        self.le_profile_file.setText("")
        self.le_profile_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Default to ./profile.json", None))
        self.pb_load_profile.setText(QCoreApplication.translate("MainWindow", u"Load...", None))
        self.pb_save_profile.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.labelVersion_4.setText(QCoreApplication.translate("MainWindow", u"Load or save the specification", None))
        self.labelBoxBlenderInstalation_3.setText(QCoreApplication.translate("MainWindow", u"SPECIFICATION", None))
        self.labelVersion_12.setText(QCoreApplication.translate("MainWindow", u"Range", None))
        self.cb_range.setItemText(0, QCoreApplication.translate("MainWindow", u"-10V ~ +10V", None))
        self.cb_range.setItemText(1, QCoreApplication.translate("MainWindow", u"-5V ~ +5V", None))

        self.labelVersion_6.setText(QCoreApplication.translate("MainWindow", u"Triggle Mode", None))
        self.cb_trig_mode.setItemText(0, QCoreApplication.translate("MainWindow", u"Internal", None))
        self.cb_trig_mode.setItemText(1, QCoreApplication.translate("MainWindow", u"Switch & Internal", None))

        self.labelVersion_5.setText(QCoreApplication.translate("MainWindow", u"Triggle", None))
        self.cb_trig_dir.setItemText(0, QCoreApplication.translate("MainWindow", u"Rising Edge", None))
        self.cb_trig_dir.setItemText(1, QCoreApplication.translate("MainWindow", u"Falling Edge", None))
        self.cb_trig_dir.setItemText(2, QCoreApplication.translate("MainWindow", u"Both", None))

        self.labelVersion_7.setText(QCoreApplication.translate("MainWindow", u"Upsampling", None))
        self.cb_os.setItemText(0, QCoreApplication.translate("MainWindow", u"None - 1x", None))
        self.cb_os.setItemText(1, QCoreApplication.translate("MainWindow", u"Up - 2x", None))
        self.cb_os.setItemText(2, QCoreApplication.translate("MainWindow", u"Up - 4x", None))
        self.cb_os.setItemText(3, QCoreApplication.translate("MainWindow", u"Up - 8x", None))
        self.cb_os.setItemText(4, QCoreApplication.translate("MainWindow", u"Up - 16x", None))
        self.cb_os.setItemText(5, QCoreApplication.translate("MainWindow", u"Up - 32x", None))
        self.cb_os.setItemText(6, QCoreApplication.translate("MainWindow", u"Up - 64x", None))

        self.labelVersion_8.setText(QCoreApplication.translate("MainWindow", u"Sample Preiod", None))
        self.le_period.setText(QCoreApplication.translate("MainWindow", u"1000", None))
        self.le_period.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Period", None))
        self.labelVersion_9.setText(QCoreApplication.translate("MainWindow", u"us", None))
        self.le_frequency.setText("")
        self.le_frequency.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Frequency", None))
        self.labelVersion_10.setText(QCoreApplication.translate("MainWindow", u"hz", None))
        self.labelVersion_11.setText(QCoreApplication.translate("MainWindow", u"Sample Cycles", None))
        self.le_cycles.setText(QCoreApplication.translate("MainWindow", u"10000", None))
        self.le_cycles.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cycles", None))
        self.cb_ch7.setText(QCoreApplication.translate("MainWindow", u"Channel 7", None))
        self.cb_ch5.setText(QCoreApplication.translate("MainWindow", u"Channel 5", None))
        self.cb_ch2.setText(QCoreApplication.translate("MainWindow", u"Channel 2", None))
        self.cb_ch1.setText(QCoreApplication.translate("MainWindow", u"Channel 1", None))
        self.cb_ch8.setText(QCoreApplication.translate("MainWindow", u"Channel 8", None))
        self.cb_ch6.setText(QCoreApplication.translate("MainWindow", u"Channel 6", None))
        self.cb_ch3.setText(QCoreApplication.translate("MainWindow", u"Channel 3", None))
        self.cb_ch4.setText(QCoreApplication.translate("MainWindow", u"Channel 4", None))
        self.pb_save_plot.setText(QCoreApplication.translate("MainWindow", u"Save...", None))
        self.labelBoxBlenderInstalation_2.setText(QCoreApplication.translate("MainWindow", u"CAPTURED DATA", None))
        self.pb_export_table.setText(QCoreApplication.translate("MainWindow", u"Export...", None))
        self.btn_message.setText(QCoreApplication.translate("MainWindow", u"Message", None))
        self.btn_print.setText(QCoreApplication.translate("MainWindow", u"Print", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.connection_status_label.setText(QCoreApplication.translate("MainWindow", u"Connecting device...", None))
        self.running_status_label.setText(QCoreApplication.translate("MainWindow", u"Not running...", None))
        self.time_status_label.setText(QCoreApplication.translate("MainWindow", u"0/0ms", None))
        self.version.setText(QCoreApplication.translate("MainWindow", u"v1.0.0", None))
    # retranslateUi

