# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Convert.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import assets.icons_rc

class Ui_MainConvert(object):
    def setupUi(self, MainConvert):
        if not MainConvert.objectName():
            MainConvert.setObjectName(u"MainConvert")
        MainConvert.resize(350, 268)
        MainConvert.setMinimumSize(QSize(350, 268))
        MainConvert.setMaximumSize(QSize(350, 268))
        MainConvert.setStyleSheet(u"#centralwidget{	\n"
"	border-style: ridge;\n"
"    border-width: 5px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color:rgb(225, 225, 225);\n"
"}\n"
"QLabel{	\n"
"	border-style: solid;\n"
"	border-width: 0px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	text-align: center;\n"
"    font: bold 16px;\n"
"}\n"
"QLineEdit{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: inset;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QComboBox{		\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-style: inset;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QPlainTextEdit{		\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-style: inset;\n"
"	border-width: 3px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QPushButton{	\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: outset;\n"
"    border-width: 2px;\n"
"   "
                        " border-radius: 5px; \n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 181, 181);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 181, 181);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.centralwidget = QWidget(MainConvert)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(6, 6, 6, 6)
        self.fr_select_item = QFrame(self.centralwidget)
        self.fr_select_item.setObjectName(u"fr_select_item")
        self.fr_select_item.setFrameShape(QFrame.StyledPanel)
        self.fr_select_item.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_select_item)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame = QFrame(self.fr_select_item)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.cmb_st_rev = QComboBox(self.frame)
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.setObjectName(u"cmb_st_rev")
        self.cmb_st_rev.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.cmb_st_rev)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(50, 30))
        self.btn_search.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/icons8-transferir-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_search)

        self.btn_close = QPushButton(self.frame)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(50, 30))
        self.btn_close.setMaximumSize(QSize(50, 16777215))
        self.btn_close.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 0, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(202, 0, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(202, 0, 0);\n"
"    border-style: inset;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/cancelar-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon1)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame)

        self.fr_in = QFrame(self.fr_select_item)
        self.fr_in.setObjectName(u"fr_in")
        sizePolicy.setHeightForWidth(self.fr_in.sizePolicy().hasHeightForWidth())
        self.fr_in.setSizePolicy(sizePolicy)
        self.fr_in.setFrameShape(QFrame.StyledPanel)
        self.fr_in.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.fr_in)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.txt_dig_in = QLineEdit(self.fr_in)
        self.txt_dig_in.setObjectName(u"txt_dig_in")
        self.txt_dig_in.setMinimumSize(QSize(0, 30))
        self.txt_dig_in.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_dig_in.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.txt_dig_in)

        self.txt_dig_in_un = QLineEdit(self.fr_in)
        self.txt_dig_in_un.setObjectName(u"txt_dig_in_un")
        self.txt_dig_in_un.setMinimumSize(QSize(35, 30))
        self.txt_dig_in_un.setMaximumSize(QSize(35, 16777215))
        self.txt_dig_in_un.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.txt_dig_in_un.setAlignment(Qt.AlignCenter)
        self.txt_dig_in_un.setReadOnly(True)

        self.horizontalLayout_5.addWidget(self.txt_dig_in_un)


        self.verticalLayout.addWidget(self.fr_in)

        self.fr_mm = QFrame(self.fr_select_item)
        self.fr_mm.setObjectName(u"fr_mm")
        sizePolicy.setHeightForWidth(self.fr_mm.sizePolicy().hasHeightForWidth())
        self.fr_mm.setSizePolicy(sizePolicy)
        self.fr_mm.setFrameShape(QFrame.StyledPanel)
        self.fr_mm.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.fr_mm)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.txt_dig_mm = QLineEdit(self.fr_mm)
        self.txt_dig_mm.setObjectName(u"txt_dig_mm")
        self.txt_dig_mm.setMinimumSize(QSize(0, 30))
        self.txt_dig_mm.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_dig_mm.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.txt_dig_mm)

        self.txt_dig_mm_un = QLineEdit(self.fr_mm)
        self.txt_dig_mm_un.setObjectName(u"txt_dig_mm_un")
        self.txt_dig_mm_un.setMinimumSize(QSize(35, 30))
        self.txt_dig_mm_un.setMaximumSize(QSize(35, 16777215))
        self.txt_dig_mm_un.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.txt_dig_mm_un.setAlignment(Qt.AlignCenter)
        self.txt_dig_mm_un.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.txt_dig_mm_un)


        self.verticalLayout.addWidget(self.fr_mm)

        self.fr_plg = QFrame(self.fr_select_item)
        self.fr_plg.setObjectName(u"fr_plg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.fr_plg.sizePolicy().hasHeightForWidth())
        self.fr_plg.setSizePolicy(sizePolicy1)
        self.fr_plg.setFrameShape(QFrame.StyledPanel)
        self.fr_plg.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.fr_plg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.txt_dig_plg1 = QLineEdit(self.fr_plg)
        self.txt_dig_plg1.setObjectName(u"txt_dig_plg1")
        self.txt_dig_plg1.setMinimumSize(QSize(0, 30))
        self.txt_dig_plg1.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_dig_plg1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_dig_plg1)

        self.label = QLabel(self.fr_plg)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)

        self.txt_dig_plg2 = QLineEdit(self.fr_plg)
        self.txt_dig_plg2.setObjectName(u"txt_dig_plg2")
        self.txt_dig_plg2.setMinimumSize(QSize(0, 30))
        self.txt_dig_plg2.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_dig_plg2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_dig_plg2)

        self.label_2 = QLabel(self.fr_plg)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_3.addWidget(self.label_2)

        self.txt_dig_plg3 = QLineEdit(self.fr_plg)
        self.txt_dig_plg3.setObjectName(u"txt_dig_plg3")
        self.txt_dig_plg3.setMinimumSize(QSize(0, 30))
        self.txt_dig_plg3.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_dig_plg3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.txt_dig_plg3)

        self.txt_dig_plg_un = QLineEdit(self.fr_plg)
        self.txt_dig_plg_un.setObjectName(u"txt_dig_plg_un")
        self.txt_dig_plg_un.setMinimumSize(QSize(35, 30))
        self.txt_dig_plg_un.setMaximumSize(QSize(35, 16777215))
        self.txt_dig_plg_un.setStyleSheet(u"background-color: rgb(220, 220, 220);")
        self.txt_dig_plg_un.setAlignment(Qt.AlignCenter)
        self.txt_dig_plg_un.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_dig_plg_un)


        self.verticalLayout.addWidget(self.fr_plg)

        self.frame_5 = QFrame(self.fr_select_item)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setStyleSheet(u"QLineEdit{		\n"
"	background-color:rgb(220, 220, 220);\n"
"	border-style: ridge;\n"
"	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_5)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(4)
        self.gridLayout.setContentsMargins(0, 4, 0, 4)
        self.txt_result_plg_un = QLineEdit(self.frame_5)
        self.txt_result_plg_un.setObjectName(u"txt_result_plg_un")
        self.txt_result_plg_un.setMinimumSize(QSize(35, 30))
        self.txt_result_plg_un.setMaximumSize(QSize(35, 16777215))
        self.txt_result_plg_un.setAlignment(Qt.AlignCenter)
        self.txt_result_plg_un.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_plg_un, 2, 2, 1, 1)

        self.txt_result_in_un = QLineEdit(self.frame_5)
        self.txt_result_in_un.setObjectName(u"txt_result_in_un")
        self.txt_result_in_un.setMinimumSize(QSize(35, 30))
        self.txt_result_in_un.setMaximumSize(QSize(35, 16777215))
        self.txt_result_in_un.setAlignment(Qt.AlignCenter)
        self.txt_result_in_un.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_in_un, 1, 2, 1, 1)

        self.txt_result_plg = QLineEdit(self.frame_5)
        self.txt_result_plg.setObjectName(u"txt_result_plg")
        self.txt_result_plg.setMinimumSize(QSize(0, 30))
        self.txt_result_plg.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_result_plg.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_plg, 2, 1, 1, 1)

        self.txt_result_in = QLineEdit(self.frame_5)
        self.txt_result_in.setObjectName(u"txt_result_in")
        self.txt_result_in.setMinimumSize(QSize(0, 30))
        self.txt_result_in.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_result_in.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_in, 1, 1, 1, 1)

        self.txt_result_mm = QLineEdit(self.frame_5)
        self.txt_result_mm.setObjectName(u"txt_result_mm")
        self.txt_result_mm.setMinimumSize(QSize(0, 30))
        self.txt_result_mm.setStyleSheet(u"font: bold 12pt \"Segoe UI\";")
        self.txt_result_mm.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_mm, 0, 1, 1, 1)

        self.txt_result_mm_un = QLineEdit(self.frame_5)
        self.txt_result_mm_un.setObjectName(u"txt_result_mm_un")
        self.txt_result_mm_un.setMinimumSize(QSize(35, 30))
        self.txt_result_mm_un.setMaximumSize(QSize(35, 16777215))
        self.txt_result_mm_un.setAlignment(Qt.AlignCenter)
        self.txt_result_mm_un.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_result_mm_un, 0, 2, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_2.addWidget(self.fr_select_item)

        MainConvert.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainConvert)

        QMetaObject.connectSlotsByName(MainConvert)
    # setupUi

    def retranslateUi(self, MainConvert):
        MainConvert.setWindowTitle(QCoreApplication.translate("MainConvert", u"MainWindow", None))
        self.cmb_st_rev.setItemText(0, QCoreApplication.translate("MainConvert", u"Tipo convers\u00e3o", None))
        self.cmb_st_rev.setItemText(1, QCoreApplication.translate("MainConvert", u"Polegada", None))
        self.cmb_st_rev.setItemText(2, QCoreApplication.translate("MainConvert", u"Polegada Imperial", None))
        self.cmb_st_rev.setItemText(3, QCoreApplication.translate("MainConvert", u"Milimetro", None))

#if QT_CONFIG(tooltip)
        self.btn_search.setToolTip(QCoreApplication.translate("MainConvert", u"<html><head/><body><p><span style=\" font-weight:700;\">Pesquisar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_search.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainConvert", u"<html><head/><body><p><span style=\" font-weight:700;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.txt_dig_in_un.setText(QCoreApplication.translate("MainConvert", u"IN", None))
        self.txt_dig_mm_un.setText(QCoreApplication.translate("MainConvert", u"MM", None))
        self.label.setText(QCoreApplication.translate("MainConvert", u".", None))
        self.label_2.setText(QCoreApplication.translate("MainConvert", u"/", None))
        self.txt_dig_plg_un.setText(QCoreApplication.translate("MainConvert", u"\"", None))
        self.txt_result_plg_un.setText(QCoreApplication.translate("MainConvert", u"\"", None))
        self.txt_result_in_un.setText(QCoreApplication.translate("MainConvert", u"IN", None))
        self.txt_result_mm_un.setText(QCoreApplication.translate("MainConvert", u"MM", None))
    # retranslateUi

