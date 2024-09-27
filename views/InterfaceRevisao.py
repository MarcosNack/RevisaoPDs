# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'InterfaceRevisao.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QComboBox,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPlainTextEdit,
    QProgressBar, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)
import assets.icons_rc

class Ui_MainReviewPD(object):
    def setupUi(self, MainReviewPD):
        if not MainReviewPD.objectName():
            MainReviewPD.setObjectName(u"MainReviewPD")
        MainReviewPD.resize(955, 670)
        MainReviewPD.setMinimumSize(QSize(955, 670))
        MainReviewPD.setStyleSheet(u"#centralwidget{	\n"
"	border-style: ridge;\n"
"    border-width: 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"	background-color: rgb(180, 180, 180);\n"
"}\n"
"\n"
"#centralwidget{\n"
"	background-color:rgb(225, 225, 225);\n"
"	border-style: ridge;\n"
"	border-width: 4px;\n"
"    border-radius: 0px;\n"
"    border-color: rgb(234, 234, 234);\n"
"	padding-left: 5px;\n"
"	}\n"
"\n"
"#fr_home{	\n"
"	border-style: groove;\n"
"    border-width: 3px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"#frame_8{	\n"
"	border-style: groove;\n"
"    border-width: 0px 0px 0px 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"#stackedWidget{	\n"
"	border-style: groove;\n"
"    border-width: 1px 0px 0px 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	font: 9pt \"Segoe UI\";\n"
"	}\n"
"QTableWidget QLineEdit::focus{\n"
"	background-color: rgb(170, 255, 255);\n"
"    border-style: ridge;\n"
"	border-width: 2px;\n"
"	color: rgb(0, 0, 0);\n"
""
                        "	}\n"
"QTableWidget QWidget {\n"
"	background-color: rgb(126, 126, 126);\n"
"    color: #fffff8;\n"
"	font: bold 9pt \"Segoe UI\";\n"
"	}\n"
"QTableWidget QHeaderView::section {\n"
"	background-color: rgb(126, 126, 126);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
" 	padding-left: 2px;\n"
"  }\n"
"QTableWidget QTableCornerButton::section {\n"
"  	background-color: rgb(126, 126, 126);\n"
"	border-style: ridge;\n"
"   	border-width: 2px;\n"
"    border-color: rgb(170, 170, 170);\n"
"	border-radius: 2px;\n"
"}\n"
"QLabel{	\n"
"	border-style: solid;\n"
"	border-width: 0px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QLineEdit{\n"
"	padding: 0px 0px 0px 5px;\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"	border-radius: 4px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
"QPlainTextEdit{\n"
"	background-color: rgb(230, 230, 23"
                        "0);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"	border-radius: 4px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 10px;\n"
"}\n"
"QComboBox{\n"
"	padding: 0px 5px 0px 5px;\n"
"	background-color: rgb(230, 230, 230);\n"
"	border-style: ridge;\n"
"	border-width: 3px;\n"
"	border-radius: 4px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;\n"
"}\n"
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
"#br_progress{		\n"
"	border-style: sold;\n"
"	border-width: 2px;\n"
"	border-radius: 5px;\n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 16px;\n"
"	\n"
"}")
        self.centralwidget = QWidget(MainReviewPD)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(3, 3, 3, 3)
        self.fr_home = QFrame(self.centralwidget)
        self.fr_home.setObjectName(u"fr_home")
        self.fr_home.setMinimumSize(QSize(240, 0))
        self.fr_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(227, 227, 227);\n"
"	padding: 0px 0px 0px 10px;\n"
"	border-width: 2px 0px 2px 2px;\n"
"	border-radius: 0px;\n"
"	text-align: left;	\n"
"	font: bold 9pt \"Segoe UI\";\n"
"}\n"
"QPushButton::hover {\n"
"    background-color:rgb(244, 244, 244);\n"
"    border-style: ridge;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-style: ridge;\n"
"}\n"
"\n"
"QLabel{\n"
"	font: bold 12pt \"Segoe UI\";\n"
"	border-width: 0px;	\n"
"}\n"
"#frame_8{\n"
"	border-width: 0px 0px 2px 0px;\n"
"}\n"
"")
        self.fr_home.setFrameShape(QFrame.Shape.StyledPanel)
        self.fr_home.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.fr_home)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.fr_home)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMinimumSize(QSize(0, 35))
        self.frame_8.setMaximumSize(QSize(16777215, 45))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_8)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.verticalLayout_5.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_4.addWidget(self.frame_8)

        self.frame_10 = QFrame(self.fr_home)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy)
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_10)
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(10, 10, 0, 0)
        self.btn_home_pg_alt_pad = QPushButton(self.frame_10)
        self.btn_home_pg_alt_pad.setObjectName(u"btn_home_pg_alt_pad")
        self.btn_home_pg_alt_pad.setMinimumSize(QSize(0, 30))

        self.verticalLayout_6.addWidget(self.btn_home_pg_alt_pad)

        self.btn_home_pg_alt_pd = QPushButton(self.frame_10)
        self.btn_home_pg_alt_pd.setObjectName(u"btn_home_pg_alt_pd")
        self.btn_home_pg_alt_pd.setMinimumSize(QSize(0, 30))
        self.btn_home_pg_alt_pd.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.btn_home_pg_alt_pd.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.btn_home_pg_alt_pd)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer)


        self.verticalLayout_4.addWidget(self.frame_10)


        self.gridLayout_2.addWidget(self.fr_home, 0, 0, 2, 1)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pg_updata_mat = QWidget()
        self.pg_updata_mat.setObjectName(u"pg_updata_mat")
        self.verticalLayout = QVBoxLayout(self.pg_updata_mat)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 0)
        self.frame = QFrame(self.pg_updata_mat)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 300))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(3)
        self.gridLayout.setVerticalSpacing(2)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setSpacing(4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 4, 0)
        self.txt_cod_pd = QLineEdit(self.frame_6)
        self.txt_cod_pd.setObjectName(u"txt_cod_pd")
        self.txt_cod_pd.setMinimumSize(QSize(0, 30))
        self.txt_cod_pd.setMaximumSize(QSize(100, 16777215))
        self.txt_cod_pd.setStyleSheet(u"")
        self.txt_cod_pd.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_cod_pd)

        self.txt_tit_pd = QLineEdit(self.frame_6)
        self.txt_tit_pd.setObjectName(u"txt_tit_pd")
        self.txt_tit_pd.setMinimumSize(QSize(0, 30))
        self.txt_tit_pd.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_tit_pd)

        self.txt_abrev_pd = QLineEdit(self.frame_6)
        self.txt_abrev_pd.setObjectName(u"txt_abrev_pd")
        self.txt_abrev_pd.setMinimumSize(QSize(0, 30))
        self.txt_abrev_pd.setMaximumSize(QSize(16777215, 16777215))
        self.txt_abrev_pd.setStyleSheet(u"")
        self.txt_abrev_pd.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.txt_abrev_pd)

        self.btn_search_pd = QPushButton(self.frame_6)
        self.btn_search_pd.setObjectName(u"btn_search_pd")
        self.btn_search_pd.setMinimumSize(QSize(30, 30))
        self.btn_search_pd.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u":/icons/pesquisar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_search_pd.setIcon(icon)
        self.btn_search_pd.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_search_pd)

        self.horizontalSpacer_7 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_7)

        self.btn_update = QPushButton(self.frame_6)
        self.btn_update.setObjectName(u"btn_update")
        self.btn_update.setMinimumSize(QSize(35, 30))
        self.btn_update.setMaximumSize(QSize(50, 16777215))
        self.btn_update.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons8-refresh-66.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_update)

        self.horizontalSpacer_4 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)

        self.btn_salve = QPushButton(self.frame_6)
        self.btn_salve.setObjectName(u"btn_salve")
        self.btn_salve.setMinimumSize(QSize(35, 30))
        self.btn_salve.setMaximumSize(QSize(50, 16777215))
        self.btn_salve.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/salvar.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_salve.setIcon(icon2)
        self.btn_salve.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_salve)

        self.horizontalSpacer_5 = QSpacerItem(30, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.btn_cad_cont = QPushButton(self.frame_6)
        self.btn_cad_cont.setObjectName(u"btn_cad_cont")
        self.btn_cad_cont.setMinimumSize(QSize(35, 30))
        self.btn_cad_cont.setMaximumSize(QSize(50, 16777215))
        self.btn_cad_cont.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/icons/banco-de-dados-de-pesquisa.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cad_cont.setIcon(icon3)
        self.btn_cad_cont.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.btn_cad_cont)


        self.gridLayout.addWidget(self.frame_6, 3, 0, 1, 8)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 16777215))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tb_item = QTableWidget(self.frame_5)
        self.tb_item.setObjectName(u"tb_item")
        self.tb_item.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_item.setAlternatingRowColors(True)
        self.tb_item.setSortingEnabled(False)
        self.tb_item.setRowCount(0)
        self.tb_item.setColumnCount(0)
        self.tb_item.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_item.horizontalHeader().setStretchLastSection(True)

        self.horizontalLayout_2.addWidget(self.tb_item)

        self.ptxt_txt_long = QPlainTextEdit(self.frame_5)
        self.ptxt_txt_long.setObjectName(u"ptxt_txt_long")
        self.ptxt_txt_long.setMinimumSize(QSize(300, 0))
        self.ptxt_txt_long.setMaximumSize(QSize(400, 16777215))
        self.ptxt_txt_long.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.ptxt_txt_long)


        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 8)

        self.frame_15 = QFrame(self.frame)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(0, 0))
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.txt_new_desc = QLineEdit(self.frame_15)
        self.txt_new_desc.setObjectName(u"txt_new_desc")
        self.txt_new_desc.setMinimumSize(QSize(0, 30))
        self.txt_new_desc.setMaximumSize(QSize(16777215, 16777215))
        self.txt_new_desc.setDragEnabled(False)
        self.txt_new_desc.setReadOnly(True)

        self.gridLayout_4.addWidget(self.txt_new_desc, 1, 0, 2, 3)

        self.txt_n_carac = QLineEdit(self.frame_15)
        self.txt_n_carac.setObjectName(u"txt_n_carac")
        self.txt_n_carac.setMinimumSize(QSize(50, 30))
        self.txt_n_carac.setMaximumSize(QSize(50, 30))
        self.txt_n_carac.setStyleSheet(u"font: bold 11pt \"Segoe UI\";")
        self.txt_n_carac.setReadOnly(True)

        self.gridLayout_4.addWidget(self.txt_n_carac, 1, 3, 1, 1)

        self.ptxt_new_desc = QPlainTextEdit(self.frame_15)
        self.ptxt_new_desc.setObjectName(u"ptxt_new_desc")
        self.ptxt_new_desc.setMinimumSize(QSize(0, 54))
        self.ptxt_new_desc.setMaximumSize(QSize(16777215, 150))
        self.ptxt_new_desc.setReadOnly(True)

        self.gridLayout_4.addWidget(self.ptxt_new_desc, 3, 0, 1, 4)


        self.gridLayout.addWidget(self.frame_15, 4, 0, 1, 8, Qt.AlignmentFlag.AlignTop)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(0, 47))
        self.frame_11.setStyleSheet(u"QLabel{\n"
"	padding: 0px 0px 0px 2px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_11)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.txt_tot_itens = QLineEdit(self.frame_11)
        self.txt_tot_itens.setObjectName(u"txt_tot_itens")
        self.txt_tot_itens.setMinimumSize(QSize(50, 30))
        self.txt_tot_itens.setMaximumSize(QSize(50, 16777215))
        self.txt_tot_itens.setReadOnly(True)

        self.gridLayout_6.addWidget(self.txt_tot_itens, 2, 8, 1, 1)

        self.cmb_st_pad = QComboBox(self.frame_11)
        self.cmb_st_pad.addItem("")
        self.cmb_st_pad.addItem("")
        self.cmb_st_pad.addItem("")
        self.cmb_st_pad.setObjectName(u"cmb_st_pad")
        self.cmb_st_pad.setMinimumSize(QSize(85, 30))

        self.gridLayout_6.addWidget(self.cmb_st_pad, 2, 3, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_2, 0, 10, 3, 2)

        self.cmb_st_se = QComboBox(self.frame_11)
        self.cmb_st_se.addItem("")
        self.cmb_st_se.addItem("")
        self.cmb_st_se.setObjectName(u"cmb_st_se")
        self.cmb_st_se.setMinimumSize(QSize(50, 30))

        self.gridLayout_6.addWidget(self.cmb_st_se, 2, 4, 1, 1)

        self.txt_cod_sap = QLineEdit(self.frame_11)
        self.txt_cod_sap.setObjectName(u"txt_cod_sap")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.txt_cod_sap.sizePolicy().hasHeightForWidth())
        self.txt_cod_sap.setSizePolicy(sizePolicy1)
        self.txt_cod_sap.setMinimumSize(QSize(90, 30))
        self.txt_cod_sap.setMaximumSize(QSize(130, 16777215))
        self.txt_cod_sap.setReadOnly(True)

        self.gridLayout_6.addWidget(self.txt_cod_sap, 2, 9, 1, 1)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer, 0, 6, 3, 1)

        self.txt_search_old = QLineEdit(self.frame_11)
        self.txt_search_old.setObjectName(u"txt_search_old")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.txt_search_old.sizePolicy().hasHeightForWidth())
        self.txt_search_old.setSizePolicy(sizePolicy2)
        self.txt_search_old.setMinimumSize(QSize(95, 30))
        self.txt_search_old.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_search_old.setReadOnly(False)

        self.gridLayout_6.addWidget(self.txt_search_old, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_3, 0, 12, 3, 2)

        self.txt_search = QLineEdit(self.frame_11)
        self.txt_search.setObjectName(u"txt_search")
        sizePolicy2.setHeightForWidth(self.txt_search.sizePolicy().hasHeightForWidth())
        self.txt_search.setSizePolicy(sizePolicy2)
        self.txt_search.setMinimumSize(QSize(95, 30))
        self.txt_search.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.txt_search.setReadOnly(False)

        self.gridLayout_6.addWidget(self.txt_search, 2, 0, 1, 1)

        self.btn_alt_massiva = QPushButton(self.frame_11)
        self.btn_alt_massiva.setObjectName(u"btn_alt_massiva")
        self.btn_alt_massiva.setMinimumSize(QSize(35, 30))
        self.btn_alt_massiva.setMaximumSize(QSize(50, 16777215))
        self.btn_alt_massiva.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(255, 170, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(186, 124, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(186, 124, 0);\n"
"    border-style: inset;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/editar-60.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_alt_massiva.setIcon(icon4)
        self.btn_alt_massiva.setIconSize(QSize(20, 20))

        self.gridLayout_6.addWidget(self.btn_alt_massiva, 2, 13, 1, 1)

        self.btn_carregar = QPushButton(self.frame_11)
        self.btn_carregar.setObjectName(u"btn_carregar")
        self.btn_carregar.setMinimumSize(QSize(35, 30))
        self.btn_carregar.setMaximumSize(QSize(50, 16777215))
        self.btn_carregar.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/salvar-como.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_carregar.setIcon(icon5)
        self.btn_carregar.setIconSize(QSize(20, 20))

        self.gridLayout_6.addWidget(self.btn_carregar, 2, 11, 1, 1)

        self.btn_search_item = QPushButton(self.frame_11)
        self.btn_search_item.setObjectName(u"btn_search_item")
        self.btn_search_item.setMinimumSize(QSize(35, 30))
        self.btn_search_item.setMaximumSize(QSize(50, 16777215))
        self.btn_search_item.setIcon(icon)
        self.btn_search_item.setIconSize(QSize(20, 20))

        self.gridLayout_6.addWidget(self.btn_search_item, 2, 5, 1, 1)

        self.cmb_sm = QComboBox(self.frame_11)
        self.cmb_sm.addItem("")
        self.cmb_sm.addItem("")
        self.cmb_sm.addItem("")
        self.cmb_sm.addItem("")
        self.cmb_sm.setObjectName(u"cmb_sm")
        self.cmb_sm.setMinimumSize(QSize(0, 30))

        self.gridLayout_6.addWidget(self.cmb_sm, 2, 2, 1, 1)

        self.label_11 = QLabel(self.frame_11)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_6.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_12 = QLabel(self.frame_11)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_6.addWidget(self.label_12, 1, 1, 1, 1)

        self.label_13 = QLabel(self.frame_11)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_6.addWidget(self.label_13, 1, 2, 1, 1)

        self.label_14 = QLabel(self.frame_11)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_6.addWidget(self.label_14, 1, 3, 1, 1)

        self.label_15 = QLabel(self.frame_11)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_6.addWidget(self.label_15, 1, 4, 1, 1)

        self.label_16 = QLabel(self.frame_11)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_6.addWidget(self.label_16, 1, 9, 1, 1)

        self.label = QLabel(self.frame_11)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_6.addWidget(self.label, 1, 8, 1, 1)


        self.gridLayout.addWidget(self.frame_11, 0, 0, 1, 8)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.pg_updata_mat)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(600, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.tb_pd_old = QTableWidget(self.frame_3)
        if (self.tb_pd_old.columnCount() < 2):
            self.tb_pd_old.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_pd_old.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_pd_old.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tb_pd_old.rowCount() < 1):
            self.tb_pd_old.setRowCount(1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_pd_old.setItem(0, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_pd_old.setItem(0, 1, __qtablewidgetitem3)
        self.tb_pd_old.setObjectName(u"tb_pd_old")
        self.tb_pd_old.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_pd_old.setAlternatingRowColors(True)
        self.tb_pd_old.setColumnCount(2)
        self.tb_pd_old.horizontalHeader().setCascadingSectionResizes(False)
        self.tb_pd_old.horizontalHeader().setProperty("showSortIndicator", False)
        self.tb_pd_old.horizontalHeader().setStretchLastSection(True)
        self.tb_pd_old.verticalHeader().setDefaultSectionSize(28)

        self.verticalLayout_3.addWidget(self.tb_pd_old)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tb_new_pd = QTableWidget(self.frame_4)
        if (self.tb_new_pd.columnCount() < 7):
            self.tb_new_pd.setColumnCount(7)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tb_new_pd.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        if (self.tb_new_pd.rowCount() < 6):
            self.tb_new_pd.setRowCount(6)
        self.tb_new_pd.setObjectName(u"tb_new_pd")
        self.tb_new_pd.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tb_new_pd.setAlternatingRowColors(True)
        self.tb_new_pd.setSortingEnabled(False)
        self.tb_new_pd.setRowCount(6)
        self.tb_new_pd.horizontalHeader().setMinimumSectionSize(25)
        self.tb_new_pd.horizontalHeader().setStretchLastSection(True)
        self.tb_new_pd.verticalHeader().setDefaultSectionSize(28)

        self.verticalLayout_2.addWidget(self.tb_new_pd)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        self.br_progress = QProgressBar(self.pg_updata_mat)
        self.br_progress.setObjectName(u"br_progress")
        self.br_progress.setValue(24)
        self.br_progress.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.br_progress)

        self.stackedWidget.addWidget(self.pg_updata_mat)
        self.pg_updata_pd = QWidget()
        self.pg_updata_pd.setObjectName(u"pg_updata_pd")
        self.pg_updata_pd.setStyleSheet(u"QLabel{	\n"
"	border-style: ridge;\n"
"	border-width: 3px 3px 0px 3px;\n"
"	border-radius: 0px; \n"
"    border-color: rgb(170, 170, 170);\n"
"    font: bold 12px;	\n"
"	color: rgb(0, 0, 0);\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.pg_updata_pd)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 0)
        self.frame_7 = QFrame(self.pg_updata_pd)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_7)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_7)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMinimumSize(QSize(0, 36))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.frame_12)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMaximumSize(QSize(16777215, 115))
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_9)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setHorizontalSpacing(4)
        self.gridLayout_5.setVerticalSpacing(1)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.alt_pd_chb_tt_red = QCheckBox(self.frame_9)
        self.alt_pd_chb_tt_red.setObjectName(u"alt_pd_chb_tt_red")
        self.alt_pd_chb_tt_red.setChecked(False)

        self.gridLayout_5.addWidget(self.alt_pd_chb_tt_red, 3, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.alt_pd_txt_oid = QLineEdit(self.frame_9)
        self.alt_pd_txt_oid.setObjectName(u"alt_pd_txt_oid")
        self.alt_pd_txt_oid.setMinimumSize(QSize(0, 30))
        self.alt_pd_txt_oid.setMaximumSize(QSize(16777215, 16777215))
        self.alt_pd_txt_oid.setStyleSheet(u"")
        self.alt_pd_txt_oid.setReadOnly(True)

        self.gridLayout_5.addWidget(self.alt_pd_txt_oid, 1, 0, 1, 2)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_5, 0, 0, 1, 2)

        self.label_8 = QLabel(self.frame_9)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_8, 2, 1, 1, 5)

        self.alt_pd_txt_date_rev = QLineEdit(self.frame_9)
        self.alt_pd_txt_date_rev.setObjectName(u"alt_pd_txt_date_rev")
        self.alt_pd_txt_date_rev.setMinimumSize(QSize(100, 30))
        self.alt_pd_txt_date_rev.setMaximumSize(QSize(100, 16777215))
        self.alt_pd_txt_date_rev.setStyleSheet(u"color: rgb(255, 0, 0);\n"
"font: 700 10pt \"Segoe UI\";")
        self.alt_pd_txt_date_rev.setReadOnly(True)

        self.gridLayout_5.addWidget(self.alt_pd_txt_date_rev, 3, 6, 1, 1)

        self.alt_pd_txt_tit_red = QLineEdit(self.frame_9)
        self.alt_pd_txt_tit_red.setObjectName(u"alt_pd_txt_tit_red")
        self.alt_pd_txt_tit_red.setMinimumSize(QSize(0, 30))
        self.alt_pd_txt_tit_red.setStyleSheet(u"")
        self.alt_pd_txt_tit_red.setDragEnabled(False)
        self.alt_pd_txt_tit_red.setReadOnly(True)

        self.gridLayout_5.addWidget(self.alt_pd_txt_tit_red, 3, 1, 1, 5)

        self.alt_pd_txt_cod_pd = QLineEdit(self.frame_9)
        self.alt_pd_txt_cod_pd.setObjectName(u"alt_pd_txt_cod_pd")
        self.alt_pd_txt_cod_pd.setMinimumSize(QSize(0, 30))
        self.alt_pd_txt_cod_pd.setMaximumSize(QSize(150, 16777215))
        self.alt_pd_txt_cod_pd.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.alt_pd_txt_cod_pd.setReadOnly(False)

        self.gridLayout_5.addWidget(self.alt_pd_txt_cod_pd, 1, 2, 1, 1)

        self.label_9 = QLabel(self.frame_9)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_5.addWidget(self.label_9, 2, 6, 1, 1)

        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_3, 0, 2, 1, 1)

        self.label_7 = QLabel(self.frame_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_10 = QLabel(self.frame_9)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(90, 0))
        self.label_10.setMaximumSize(QSize(90, 16777215))
        self.label_10.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.label_10.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_10, 2, 7, 1, 1)

        self.alt_pd_chb_st_rev = QCheckBox(self.frame_9)
        self.alt_pd_chb_st_rev.setObjectName(u"alt_pd_chb_st_rev")
        self.alt_pd_chb_st_rev.setChecked(False)

        self.gridLayout_5.addWidget(self.alt_pd_chb_st_rev, 3, 7, 1, 1, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.label_6 = QLabel(self.frame_9)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_5.addWidget(self.label_6, 0, 3, 1, 5)

        self.alt_pd_txt_tt_pd = QLineEdit(self.frame_9)
        self.alt_pd_txt_tt_pd.setObjectName(u"alt_pd_txt_tt_pd")
        self.alt_pd_txt_tt_pd.setMinimumSize(QSize(0, 30))
        self.alt_pd_txt_tt_pd.setMaximumSize(QSize(16777215, 16777215))
        self.alt_pd_txt_tt_pd.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.alt_pd_txt_tt_pd.setReadOnly(False)

        self.gridLayout_5.addWidget(self.alt_pd_txt_tt_pd, 1, 3, 1, 5)


        self.horizontalLayout_4.addWidget(self.frame_9)

        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setSpacing(10)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(11, 0, 4, 0)
        self.alt_pd_btn_search_item = QPushButton(self.frame_13)
        self.alt_pd_btn_search_item.setObjectName(u"alt_pd_btn_search_item")
        self.alt_pd_btn_search_item.setMinimumSize(QSize(35, 30))
        self.alt_pd_btn_search_item.setMaximumSize(QSize(50, 16777215))
        self.alt_pd_btn_search_item.setIcon(icon)
        self.alt_pd_btn_search_item.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.alt_pd_btn_search_item)

        self.alt_pd_btn_update = QPushButton(self.frame_13)
        self.alt_pd_btn_update.setObjectName(u"alt_pd_btn_update")
        self.alt_pd_btn_update.setMinimumSize(QSize(35, 30))
        self.alt_pd_btn_update.setMaximumSize(QSize(50, 16777215))
        self.alt_pd_btn_update.setStyleSheet(u"")
        icon6 = QIcon()
        icon6.addFile(u":/icons/hist\u00f3rico-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.alt_pd_btn_update.setIcon(icon6)
        self.alt_pd_btn_update.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.alt_pd_btn_update)

        self.alt_pd_btn_salve = QPushButton(self.frame_13)
        self.alt_pd_btn_salve.setObjectName(u"alt_pd_btn_salve")
        self.alt_pd_btn_salve.setMinimumSize(QSize(35, 30))
        self.alt_pd_btn_salve.setMaximumSize(QSize(50, 16777215))
        self.alt_pd_btn_salve.setStyleSheet(u"QPushButton{	\n"
"	background-color: rgb(0, 255, 0);\n"
"\n"
"}\n"
"QPushButton::hover {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(0, 150, 0);\n"
"    border-style: inset;\n"
"}")
        self.alt_pd_btn_salve.setIcon(icon2)
        self.alt_pd_btn_salve.setIconSize(QSize(20, 20))

        self.verticalLayout_7.addWidget(self.alt_pd_btn_salve)


        self.horizontalLayout_4.addWidget(self.frame_13)


        self.gridLayout_3.addWidget(self.frame_12, 1, 0, 1, 9, Qt.AlignmentFlag.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_14 = QFrame(self.pg_updata_pd)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.alt_pd_tb_ant = QTableWidget(self.frame_14)
        if (self.alt_pd_tb_ant.columnCount() < 4):
            self.alt_pd_tb_ant.setColumnCount(4)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.alt_pd_tb_ant.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.alt_pd_tb_ant.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.alt_pd_tb_ant.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.alt_pd_tb_ant.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        if (self.alt_pd_tb_ant.rowCount() < 35):
            self.alt_pd_tb_ant.setRowCount(35)
        self.alt_pd_tb_ant.setObjectName(u"alt_pd_tb_ant")
        self.alt_pd_tb_ant.setMaximumSize(QSize(700, 16777215))
        self.alt_pd_tb_ant.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.alt_pd_tb_ant.setAlternatingRowColors(True)
        self.alt_pd_tb_ant.setRowCount(35)
        self.alt_pd_tb_ant.setColumnCount(4)
        self.alt_pd_tb_ant.horizontalHeader().setCascadingSectionResizes(False)
        self.alt_pd_tb_ant.horizontalHeader().setMinimumSectionSize(15)
        self.alt_pd_tb_ant.horizontalHeader().setProperty("showSortIndicator", False)
        self.alt_pd_tb_ant.horizontalHeader().setStretchLastSection(True)
        self.alt_pd_tb_ant.verticalHeader().setDefaultSectionSize(25)

        self.horizontalLayout_8.addWidget(self.alt_pd_tb_ant)

        self.alt_pd_tb_novo = QTableWidget(self.frame_14)
        if (self.alt_pd_tb_novo.columnCount() < 8):
            self.alt_pd_tb_novo.setColumnCount(8)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(6, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.alt_pd_tb_novo.setHorizontalHeaderItem(7, __qtablewidgetitem22)
        if (self.alt_pd_tb_novo.rowCount() < 35):
            self.alt_pd_tb_novo.setRowCount(35)
        self.alt_pd_tb_novo.setObjectName(u"alt_pd_tb_novo")
        self.alt_pd_tb_novo.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.alt_pd_tb_novo.setAlternatingRowColors(True)
        self.alt_pd_tb_novo.setRowCount(35)
        self.alt_pd_tb_novo.setColumnCount(8)
        self.alt_pd_tb_novo.horizontalHeader().setCascadingSectionResizes(False)
        self.alt_pd_tb_novo.horizontalHeader().setMinimumSectionSize(15)
        self.alt_pd_tb_novo.horizontalHeader().setProperty("showSortIndicator", False)
        self.alt_pd_tb_novo.horizontalHeader().setStretchLastSection(True)
        self.alt_pd_tb_novo.verticalHeader().setDefaultSectionSize(25)

        self.horizontalLayout_8.addWidget(self.alt_pd_tb_novo)


        self.verticalLayout_9.addWidget(self.frame_14)

        self.stackedWidget.addWidget(self.pg_updata_pd)

        self.gridLayout_2.addWidget(self.stackedWidget, 1, 1, 1, 3)

        self.frame_17 = QFrame(self.centralwidget)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setStyleSheet(u"#frame_17{\n"
"	border-style: groove;\n"
"    border-width: 0px 0px 0px 2px;\n"
"    border-color: rgb(255, 255, 255);\n"
"}")
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_17)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_17)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(30, 36))
        self.btn_home.setMaximumSize(QSize(34, 45))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(227, 227, 227);\n"
"	border-width: 0px;\n"
"	border-radius: 0px;\n"
"}\n"
"QPushButton::hover {\n"
"    background-color:rgb(244, 244, 244);\n"
"    border-style: ridge;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: rgb(244, 244, 244);\n"
"    border-style: ridge;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/menu-arredondado.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icons/duplo-para-a-esquerda.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.btn_home.setIcon(icon7)
        self.btn_home.setIconSize(QSize(25, 25))
        self.btn_home.setCheckable(True)

        self.horizontalLayout_9.addWidget(self.btn_home)

        self.horizontalSpacer_14 = QSpacerItem(10, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_14)

        self.label_4 = QLabel(self.frame_17)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(217, 30))
        self.label_4.setMaximumSize(QSize(217, 30))
        self.label_4.setTextFormat(Qt.TextFormat.PlainText)
        self.label_4.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.label_4)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_13)

        self.btn_convert = QPushButton(self.frame_17)
        self.btn_convert.setObjectName(u"btn_convert")
        self.btn_convert.setMinimumSize(QSize(35, 30))
        self.btn_convert.setMaximumSize(QSize(50, 16777215))
        self.btn_convert.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons8-transferir-50.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_convert.setIcon(icon8)
        self.btn_convert.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.btn_convert)


        self.gridLayout_2.addWidget(self.frame_17, 0, 1, 1, 3)

        MainReviewPD.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainReviewPD)
        self.btn_home.toggled.connect(self.fr_home.setVisible)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainReviewPD)
    # setupUi

    def retranslateUi(self, MainReviewPD):
        MainReviewPD.setWindowTitle(QCoreApplication.translate("MainReviewPD", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainReviewPD", u"HOME", None))
        self.btn_home_pg_alt_pad.setText(QCoreApplication.translate("MainReviewPD", u"ALTERAR PADRONIZA\u00c7\u00c3O", None))
        self.btn_home_pg_alt_pd.setText(QCoreApplication.translate("MainReviewPD", u"ALTERAR PD", None))
        self.txt_cod_pd.setText("")
#if QT_CONFIG(tooltip)
        self.btn_search_pd.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Pesquisar PD</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_search_pd.setText("")
#if QT_CONFIG(tooltip)
        self.btn_update.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Atualizar PD</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_update.setText("")
#if QT_CONFIG(tooltip)
        self.btn_salve.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Salvar PD</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_salve.setText("")
#if QT_CONFIG(tooltip)
        self.btn_cad_cont.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Cadastrar Conte\u00fado</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_cad_cont.setText("")
        self.txt_new_desc.setText("")
        self.txt_n_carac.setText("")
        self.txt_tot_itens.setText("")
        self.cmb_st_pad.setItemText(0, "")
        self.cmb_st_pad.setItemText(1, QCoreApplication.translate("MainReviewPD", u"PARCIAL", None))
        self.cmb_st_pad.setItemText(2, QCoreApplication.translate("MainReviewPD", u"TOTAL", None))

#if QT_CONFIG(tooltip)
        self.cmb_st_pad.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p>Status Padroniza\u00e7\u00e3o</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.cmb_st_se.setItemText(0, "")
        self.cmb_st_se.setItemText(1, QCoreApplication.translate("MainReviewPD", u"OK", None))

#if QT_CONFIG(tooltip)
        self.cmb_st_se.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p>Status Padroniza\u00e7\u00e3o</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.txt_cod_sap.setText(QCoreApplication.translate("MainReviewPD", u"80000000", None))
        self.txt_search_old.setPlaceholderText(QCoreApplication.translate("MainReviewPD", u"Digite o crit\u00e9rio de pesquisa", None))
        self.txt_search.setPlaceholderText(QCoreApplication.translate("MainReviewPD", u"Digite o crit\u00e9rio de pesquisa", None))
#if QT_CONFIG(tooltip)
        self.btn_alt_massiva.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Altera\u00e7\u00e3o Massiva</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_alt_massiva.setText("")
#if QT_CONFIG(tooltip)
        self.btn_carregar.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Transferir Dados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_carregar.setText("")
#if QT_CONFIG(tooltip)
        self.btn_search_item.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Pesquisar material</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_search_item.setText("")
        self.cmb_sm.setItemText(0, "")
        self.cmb_sm.setItemText(1, QCoreApplication.translate("MainReviewPD", u"Z2", None))
        self.cmb_sm.setItemText(2, QCoreApplication.translate("MainReviewPD", u"Z3", None))
        self.cmb_sm.setItemText(3, QCoreApplication.translate("MainReviewPD", u"Z4", None))

#if QT_CONFIG(tooltip)
        self.cmb_sm.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p>Status Padroniza\u00e7\u00e3o</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.label_11.setText(QCoreApplication.translate("MainReviewPD", u"Pesq.Texto Atual", None))
        self.label_12.setText(QCoreApplication.translate("MainReviewPD", u"Pesq.Texto Antigo", None))
        self.label_13.setText(QCoreApplication.translate("MainReviewPD", u"SM", None))
        self.label_14.setText(QCoreApplication.translate("MainReviewPD", u"St.Pad.", None))
        self.label_15.setText(QCoreApplication.translate("MainReviewPD", u"St.SE", None))
        self.label_16.setText(QCoreApplication.translate("MainReviewPD", u"C\u00f3d. Item", None))
        self.label.setText(QCoreApplication.translate("MainReviewPD", u"Tatal", None))
        ___qtablewidgetitem = self.tb_pd_old.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainReviewPD", u"Caracteristica", None));
        ___qtablewidgetitem1 = self.tb_pd_old.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainReviewPD", u"Conte\u00fado", None));

        __sortingEnabled = self.tb_pd_old.isSortingEnabled()
        self.tb_pd_old.setSortingEnabled(False)
        ___qtablewidgetitem2 = self.tb_pd_old.item(0, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainReviewPD", u"MODELO CARCACA REDUTOR", None));
        ___qtablewidgetitem3 = self.tb_pd_old.item(0, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainReviewPD", u"EIXO MACICO 1PLES C/CHAVETA", None));
        self.tb_pd_old.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem4 = self.tb_new_pd.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainReviewPD", u"Caracteristica", None));
        ___qtablewidgetitem5 = self.tb_new_pd.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainReviewPD", u"Conte\u00fado Longo", None));
        ___qtablewidgetitem6 = self.tb_new_pd.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainReviewPD", u"40 Caract.", None));
        ___qtablewidgetitem7 = self.tb_new_pd.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainReviewPD", u"Unid.Med.", None));
        ___qtablewidgetitem8 = self.tb_new_pd.horizontalHeaderItem(5)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainReviewPD", u"DescCurt", None));
        ___qtablewidgetitem9 = self.tb_new_pd.horizontalHeaderItem(6)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainReviewPD", u"Sep", None));
        self.alt_pd_chb_tt_red.setText("")
        self.label_5.setText(QCoreApplication.translate("MainReviewPD", u"OID", None))
        self.label_8.setText(QCoreApplication.translate("MainReviewPD", u"Texto T\u00edtulo Reduzido", None))
        self.alt_pd_txt_date_rev.setText("")
        self.alt_pd_txt_cod_pd.setText("")
        self.label_9.setText(QCoreApplication.translate("MainReviewPD", u"Data Ult. Rev.", None))
        self.label_3.setText(QCoreApplication.translate("MainReviewPD", u"C\u00f3d. PD", None))
        self.label_7.setText(QCoreApplication.translate("MainReviewPD", u"T\u00edtulo Reduzido", None))
        self.label_10.setText(QCoreApplication.translate("MainReviewPD", u"PD Revisado?", None))
        self.alt_pd_chb_st_rev.setText("")
        self.label_6.setText(QCoreApplication.translate("MainReviewPD", u"T\u00edtulo PD", None))
        self.alt_pd_txt_tt_pd.setText("")
#if QT_CONFIG(tooltip)
        self.alt_pd_btn_search_item.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Pesquisar material</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_pd_btn_search_item.setText("")
#if QT_CONFIG(tooltip)
        self.alt_pd_btn_update.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p>Visualizar PD Antigo</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_pd_btn_update.setText("")
#if QT_CONFIG(tooltip)
        self.alt_pd_btn_salve.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Salvar PD</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.alt_pd_btn_salve.setText("")
        ___qtablewidgetitem10 = self.alt_pd_tb_ant.horizontalHeaderItem(0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainReviewPD", u"Caracteristicas Atuais", None));
        ___qtablewidgetitem11 = self.alt_pd_tb_ant.horizontalHeaderItem(1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainReviewPD", u"Ref.Cat", None));
        ___qtablewidgetitem12 = self.alt_pd_tb_ant.horizontalHeaderItem(2)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainReviewPD", u"40 Carac.", None));
        ___qtablewidgetitem13 = self.alt_pd_tb_ant.horizontalHeaderItem(3)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainReviewPD", u"Agr.Class.", None));
        ___qtablewidgetitem14 = self.alt_pd_tb_novo.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainReviewPD", u"Caracteristicas Novas", None));
        ___qtablewidgetitem15 = self.alt_pd_tb_novo.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainReviewPD", u"Comp\u00f5e 40 Caract.", None));
        ___qtablewidgetitem16 = self.alt_pd_tb_novo.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainReviewPD", u"Sim/N\u00e3o", None));
        ___qtablewidgetitem17 = self.alt_pd_tb_novo.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainReviewPD", u"Desc. Manual", None));
        ___qtablewidgetitem18 = self.alt_pd_tb_novo.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainReviewPD", u"Mais Conte\u00fado?", None));
        ___qtablewidgetitem19 = self.alt_pd_tb_novo.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainReviewPD", u"Possui Separador?", None));
        ___qtablewidgetitem20 = self.alt_pd_tb_novo.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainReviewPD", u"Separador", None));
        self.btn_home.setText("")
        self.label_4.setText("")
#if QT_CONFIG(tooltip)
        self.btn_convert.setToolTip(QCoreApplication.translate("MainReviewPD", u"<html><head/><body><p><span style=\" font-weight:700;\">Transferir Dados</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_convert.setText("")
    # retranslateUi

