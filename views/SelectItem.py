# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SelectItem.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import assets.icons_rc

class Ui_SelectItem(object):
    def setupUi(self, SelectItem):
        if not SelectItem.objectName():
            SelectItem.setObjectName(u"SelectItem")
        SelectItem.resize(865, 430)
        SelectItem.setStyleSheet(u"#fr_select_item{	\n"
"	border-style: ridge;\n"
"    border-width: 5px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"}\n"
"QTableWidget QLineEdit::focus{\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"	border-width: 2px;\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QTableWidget QWidget {\n"
"	background-color: rgb(126, 126, 126);\n"
"    color: #fffff8;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}\n"
"QTableWidget QHeaderView::section {\n"
"	background-color: rgb(126, 126, 126);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
" 	padding-left: 2px;\n"
"}\n"
"QTableWidget QTableCornerButton::section {\n"
"  	background-color: rgb(126, 126, 126);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
"}\n"
"QLabel{	\n"
"	"
                        "padding: 0px 0px 0px 10px;\n"
"	border-style: solid;\n"
"	border-width: 0px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"	text-align: left;\n"
"    font: bold 12px;\n"
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
"    border-radius: 5px; \n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 181, 181);\n"
"    b"
                        "order-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 181, 181);\n"
"    border-style: inset;\n"
"}\n"
"")
        self.horizontalLayout_2 = QHBoxLayout(SelectItem)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.fr_select_item = QFrame(SelectItem)
        self.fr_select_item.setObjectName(u"fr_select_item")
        self.fr_select_item.setFrameShape(QFrame.StyledPanel)
        self.fr_select_item.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.fr_select_item)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.fr_select_item)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.txt_search = QLineEdit(self.frame)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.txt_search)

        self.cmb_st_rev = QComboBox(self.frame)
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.addItem("")
        self.cmb_st_rev.setObjectName(u"cmb_st_rev")
        self.cmb_st_rev.setMinimumSize(QSize(200, 30))

        self.horizontalLayout.addWidget(self.cmb_st_rev)

        self.btn_search = QPushButton(self.frame)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(50, 30))
        self.btn_search.setMaximumSize(QSize(50, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search.setIcon(icon)
        self.btn_search.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_search)

        self.btn_salve = QPushButton(self.frame)
        self.btn_salve.setObjectName(u"btn_salve")
        self.btn_salve.setMinimumSize(QSize(50, 30))
        self.btn_salve.setMaximumSize(QSize(50, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/salvar-e-fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salve.setIcon(icon1)
        self.btn_salve.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_salve)

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
        icon2 = QIcon()
        icon2.addFile(u":/icons/cancelar-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_close)


        self.verticalLayout.addWidget(self.frame)

        self.tb_item = QTableWidget(self.fr_select_item)
        self.tb_item.setObjectName(u"tb_item")
        self.tb_item.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tb_item.setAlternatingRowColors(True)
        self.tb_item.setColumnCount(0)

        self.verticalLayout.addWidget(self.tb_item)


        self.horizontalLayout_2.addWidget(self.fr_select_item)

        QWidget.setTabOrder(self.txt_search, self.tb_item)
        QWidget.setTabOrder(self.tb_item, self.btn_search)
        QWidget.setTabOrder(self.btn_search, self.btn_salve)
        QWidget.setTabOrder(self.btn_salve, self.btn_close)

        self.retranslateUi(SelectItem)

        QMetaObject.connectSlotsByName(SelectItem)
    # setupUi

    def retranslateUi(self, SelectItem):
        SelectItem.setWindowTitle(QCoreApplication.translate("SelectItem", u"Form", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("SelectItem", u"Digite o crit\u00e9rio de pesquisa", None))
        self.cmb_st_rev.setItemText(0, "")
        self.cmb_st_rev.setItemText(1, QCoreApplication.translate("SelectItem", u"ALT", None))
        self.cmb_st_rev.setItemText(2, QCoreApplication.translate("SelectItem", u"S/ALT", None))

#if QT_CONFIG(tooltip)
        self.btn_search.setToolTip(QCoreApplication.translate("SelectItem", u"<html><head/><body><p><span style=\" font-weight:700;\">Pesquisar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_search.setText("")
#if QT_CONFIG(tooltip)
        self.btn_salve.setToolTip(QCoreApplication.translate("SelectItem", u"<html><head/><body><p><span style=\" font-weight:700;\">Salvar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salve.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("SelectItem", u"<html><head/><body><p><span style=\" font-weight:700;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
    # retranslateUi

