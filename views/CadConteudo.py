# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CadConteudo.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)
import assets.icons_rc

class Ui_MainCadContents(object):
    def setupUi(self, MainCadContents):
        if not MainCadContents.objectName():
            MainCadContents.setObjectName(u"MainCadContents")
        MainCadContents.resize(830, 195)
        MainCadContents.setMinimumSize(QSize(830, 195))
        MainCadContents.setMaximumSize(QSize(830, 195))
        MainCadContents.setStyleSheet(u"#centralwidget{\n"
"	background-color:rgb(225, 225, 225);\n"
"	border-style: ridge;\n"
"	border-width: 4px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	padding-left: 5px;\n"
"	}\n"
"\n"
"QLineEdit{\n"
"	padding: 0px 0px 0px 5px;\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"	border-radius: 4px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"\n"
"QPushButton{	\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-radius: 3px; \n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 181, 181);\n"
"    border-style: ridge;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 181, 181);\n"
"    border-style: ridge;\n"
"}\n"
"\n"
"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 3px 3px 0px 3px;\n"
"	border-radius: 0px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bo"
                        "ld 12px;	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.centralwidget = QWidget(MainCadContents)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(2, 3, 2, 2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(4, 4, 4, 4)
        self.txt_chave_cont = QLineEdit(self.frame_2)
        self.txt_chave_cont.setObjectName(u"txt_chave_cont")
        self.txt_chave_cont.setMinimumSize(QSize(0, 30))
        self.txt_chave_cont.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txt_chave_cont, 7, 1, 1, 2)

        self.txt_pd = QLineEdit(self.frame_2)
        self.txt_pd.setObjectName(u"txt_pd")
        self.txt_pd.setMinimumSize(QSize(0, 30))
        self.txt_pd.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_pd, 2, 1, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 25))
        self.label_2.setMaximumSize(QSize(16777215, 25))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.txt_pd_abrev = QLineEdit(self.frame_2)
        self.txt_pd_abrev.setObjectName(u"txt_pd_abrev")
        self.txt_pd_abrev.setMinimumSize(QSize(0, 30))
        self.txt_pd_abrev.setMaximumSize(QSize(100, 16777215))
        self.txt_pd_abrev.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_pd_abrev, 2, 0, 1, 1)

        self.txt_desc_curta = QLineEdit(self.frame_2)
        self.txt_desc_curta.setObjectName(u"txt_desc_curta")
        self.txt_desc_curta.setMinimumSize(QSize(0, 30))
        self.txt_desc_curta.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txt_desc_curta, 4, 2, 1, 1)

        self.txt_desc_long = QLineEdit(self.frame_2)
        self.txt_desc_long.setObjectName(u"txt_desc_long")
        self.txt_desc_long.setMinimumSize(QSize(0, 30))
        self.txt_desc_long.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txt_desc_long, 4, 0, 1, 2)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 25))
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 25))
        self.label.setMaximumSize(QSize(16777215, 25))
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(0, 25))
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)

        self.txt_carac = QLineEdit(self.frame_2)
        self.txt_carac.setObjectName(u"txt_carac")
        self.txt_carac.setMinimumSize(QSize(0, 30))
        self.txt_carac.setReadOnly(True)

        self.gridLayout.addWidget(self.txt_carac, 2, 2, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 25))
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_8, 6, 1, 1, 2)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(0, 25))
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_5, 3, 2, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(0, 25))
        self.label_4.setMaximumSize(QSize(16777215, 25))
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 2)

        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 0, 0, 0)
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
        icon = QIcon()
        icon.addFile(u":/icons/cancelar-50.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_close.setIcon(icon)
        self.btn_close.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_close)

        self.btn_salve = QPushButton(self.frame)
        self.btn_salve.setObjectName(u"btn_salve")
        self.btn_salve.setMinimumSize(QSize(50, 30))
        self.btn_salve.setMaximumSize(QSize(50, 16777215))
        icon1 = QIcon()
        icon1.addFile(u":/icons/salvar-e-fechar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_salve.setIcon(icon1)
        self.btn_salve.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.btn_salve)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addWidget(self.frame, 1, 3, 4, 2)

        self.txt_sigla = QLineEdit(self.frame_2)
        self.txt_sigla.setObjectName(u"txt_sigla")
        self.txt_sigla.setMinimumSize(QSize(0, 30))
        self.txt_sigla.setMaximumSize(QSize(100, 16777215))
        self.txt_sigla.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.txt_sigla, 7, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        MainCadContents.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.txt_desc_long, self.txt_desc_curta)
        QWidget.setTabOrder(self.txt_desc_curta, self.txt_sigla)
        QWidget.setTabOrder(self.txt_sigla, self.txt_chave_cont)
        QWidget.setTabOrder(self.txt_chave_cont, self.btn_salve)
        QWidget.setTabOrder(self.btn_salve, self.btn_close)
        QWidget.setTabOrder(self.btn_close, self.txt_carac)
        QWidget.setTabOrder(self.txt_carac, self.txt_pd)
        QWidget.setTabOrder(self.txt_pd, self.txt_pd_abrev)

        self.retranslateUi(MainCadContents)

        QMetaObject.connectSlotsByName(MainCadContents)
    # setupUi

    def retranslateUi(self, MainCadContents):
        MainCadContents.setWindowTitle(QCoreApplication.translate("MainCadContents", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainCadContents", u"PD_ABREV", None))
        self.txt_desc_long.setText("")
        self.label_3.setText(QCoreApplication.translate("MainCadContents", u"CARACTERISTICA", None))
        self.label.setText(QCoreApplication.translate("MainCadContents", u"PD", None))
        self.label_6.setText(QCoreApplication.translate("MainCadContents", u"SIGLA", None))
        self.label_8.setText(QCoreApplication.translate("MainCadContents", u"CHAVE_CONT", None))
        self.label_5.setText(QCoreApplication.translate("MainCadContents", u"DESC_CURTA", None))
        self.label_4.setText(QCoreApplication.translate("MainCadContents", u"DESC_LONGA", None))
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainCadContents", u"<html><head/><body><p><span style=\" font-weight:700;\">Fechar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
#if QT_CONFIG(tooltip)
        self.btn_salve.setToolTip(QCoreApplication.translate("MainCadContents", u"<html><head/><body><p><span style=\" font-weight:700;\">Salvar</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salve.setText("")
    # retranslateUi

