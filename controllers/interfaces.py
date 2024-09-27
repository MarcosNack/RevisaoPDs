import os
import json

from PySide6.QtWidgets import QMainWindow, QHeaderView, QWidget
from PySide6.QtCore import QThread, Signal, Qt
from PySide6.QtGui import QPixmap, QIcon



from views.InterfaceRevisao import Ui_MainReviewPD
from views.SelectItem import Ui_SelectItem
from views.SearchContent import Ui_SearchContent
from views.CadConteudo import Ui_MainCadContents
from views.Convert import Ui_MainConvert


from controllers.functions import (start_interface_selection, query_database_item, query_database_pd, query_database_filter, 
                                   transfer_data, update_new_pd_data, new_short_text, massive_change, query_database_contents,
                                   select_content, change_shortened_title, query_database_caract, edit_triggers_table,
                                   update_pd_structure, start_interface_select_content, cad_contents, load_old_pd_data, start_interface_convert)

from controllers.connection_se import (connection_softexpert, close_softexpert)




# Class control main interface PD review
class MainReviewPD(QMainWindow, Ui_MainReviewPD):
    def __init__(self):
        super(MainReviewPD, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Revisão PD")
        
        #Select the Company Logo and app Icon 
        current_path = os.getcwd()
                
        ico_path = os.path.join(current_path, "icone.ico")
        image_path = os.path.join(current_path, "logo.png")

        self.setWindowIcon(QIcon(ico_path))        
        self.label_4.setPixmap(QPixmap(image_path))

        
        # Load the json file with the database data
        with open('config.json', 'r') as f:
            config = json.load(f)

        db_path = config['database']['db_path']            
        self.str_path = os.path.join(current_path, db_path)

        
        self.win_cad_pd = ""        

        
        #---------- CONFIGURE THE HOME ----------#
        self.fr_home.setVisible(False)
                
        self.btn_home_pg_alt_pd.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_updata_pd))
        self.btn_home_pg_alt_pd.clicked.connect(lambda: self.btn_home.setChecked(False))
        
        self.btn_home_pg_alt_pad.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_updata_mat))
        self.btn_home_pg_alt_pad.clicked.connect(lambda: self.btn_home.setChecked(False))  
        
        
        #---------- CONFIGURE THE MATERIAL UPADATE PAGE ----------#
        #--> CONFIGURE THE TABLE PD OLD
        self.tb_pd_old.clearContents()
        self.tb_pd_old.setRowCount(0)
        tb_pd_old = self.tb_pd_old.horizontalHeader()
        tb_pd_old.setSectionResizeMode(QHeaderView.ResizeToContents)
        
        #--> CONFIGURE THE TABLE NEW PD
        self.tb_new_pd.clearContents()
        self.tb_new_pd.setRowCount(0)
        tb_new_pd = self.tb_new_pd.horizontalHeader()
        tb_new_pd.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.tb_new_pd.clicked.connect(lambda: edit_triggers_table(object_tab=self.tb_new_pd, row=self.tb_new_pd.currentRow(), col=self.tb_new_pd.currentColumn()))
        # self.tb_new_pd.cellActivated.connect(lambda: edit_triggers_table(object_tab=self.tb_new_pd, row=self.tb_new_pd.currentRow(), col=self.tb_new_pd.currentColumn()))
        self.tb_new_pd.currentCellChanged.connect(lambda: edit_triggers_table(object_tab=self.tb_new_pd, row=self.tb_new_pd.currentRow(), col=self.tb_new_pd.currentColumn()))
        
        #--> HIDE PROGRESS BAR
        self.br_progress.setVisible(False)
        
        #--> BUTTON CONFIGURATION
        self.btn_search_item.clicked.connect(lambda: query_database_filter(self, 'item'))
        self.txt_search.editingFinished.connect(lambda: query_database_filter(self, 'item'))
        self.cmb_sm.currentTextChanged.connect(lambda: query_database_filter(self, 'item'))
        self.cmb_st_pad.currentTextChanged.connect(lambda: query_database_filter(self, 'item'))
        self.btn_search_item.setVisible(False)
        
        self.btn_search_pd.clicked.connect(lambda: start_interface_selection(self, 'pd'))
        
        self.btn_carregar.clicked.connect(lambda: transfer_data(self, on_btn_pressed='item'))
        self.btn_carregar.setVisible(False)
        self.tb_item.doubleClicked.connect(lambda: transfer_data(self, on_btn_pressed='item'))
        
        self.btn_alt_massiva.clicked.connect(lambda: massive_change(self))
        self.btn_alt_massiva.setVisible(False)

        
        self.btn_update.clicked.connect(lambda: update_new_pd_data(self))
        self.btn_update.setVisible(False)
        
        self.btn_salve.clicked.connect(lambda: new_short_text(self))
        self.btn_salve.clicked.connect(lambda: query_database_filter(self, 'item'))
        self.btn_salve.setVisible(False)        
        
        self.btn_cad_cont.clicked.connect(lambda: start_interface_select_content(self, self.tb_new_pd))
        self.btn_cad_cont.setVisible(False)
        
        self.btn_convert.clicked.connect(lambda: start_interface_convert(self))
        
        self.pd_atuali = ""
        self.novos_cont = []

        self.frame_11.setVisible(False)
        self.frame_5.setVisible(False)
        
        #---------- CONFIGURE THE PD UPDATA PAGE ----------#
        #--> CONFIGURE THE TABLE PD
        self.alt_pd_tb_ant.clearContents()
        self.alt_pd_tb_ant.setRowCount(0)
        alt_pd_tb_ant = self.alt_pd_tb_ant.horizontalHeader()
        alt_pd_tb_ant.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.alt_pd_tb_ant.clicked.connect(lambda: edit_triggers_table(object_tab=self.alt_pd_tb_ant, row=self.alt_pd_tb_ant.currentRow(), col=self.alt_pd_tb_ant.currentColumn()))

        self.alt_pd_tb_novo.clearContents()
        self.alt_pd_tb_novo.setRowCount(0)
        alt_pd_tb_novo = self.alt_pd_tb_novo.horizontalHeader()
        alt_pd_tb_novo.setSectionResizeMode(QHeaderView.ResizeToContents)        
        self.alt_pd_tb_novo.clicked.connect(lambda: edit_triggers_table(object_tab=self.alt_pd_tb_novo, row=self.alt_pd_tb_novo.currentRow(), col=self.alt_pd_tb_novo.currentColumn()))

        
        #--> BUTTON CONFIGURATION
        self.alt_pd_chb_tt_red.stateChanged.connect(lambda: change_shortened_title(self))
        self.alt_pd_btn_search_item.clicked.connect(lambda: start_interface_selection(self, 'alt_pd'))
        
        self.alt_pd_btn_salve.clicked.connect(lambda: update_pd_structure(self, self.alt_pd_txt_oid.text()))

   

    # Função Envento para Fechar a Conexão
    def closeEvent(self, event):
        import ctypes
        from msgbox.msgbox import MsgQuestion
        # ctypes.windll.user32.MessageBoxW(0, "Não foi encontrado nenhum Material pendente de revisado!", "Error", 0x00000010)
        msg_info = f"Deseja realmente fechar o App?"
        resp = MsgQuestion(msg_info)
        if resp == 16384:
            try:
                self.LimparBaseCadastro() 
                if self.valid_open_site == "OK":
                    close_softexpert(self)        
            except:
                pass
            
            event.accept()
        else:
            event.ignore()


# Class control interface item selection
class SelectItem(QWidget, Ui_SelectItem):
    def __init__(self, parent=None, on_btn_pressed=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.str_path = self.parent.str_path
        self.resize(self.parent.size())
        
        self.btn_close.clicked.connect(lambda: self.close())
        
        self.btn_search.clicked.connect(lambda: query_database_filter(self, on_btn_pressed))        
        self.txt_search.editingFinished.connect(lambda: query_database_filter(self, on_btn_pressed))
        
        self.cmb_st_rev.currentIndexChanged.connect(lambda: query_database_filter(self, on_btn_pressed))
        
        self.btn_salve.clicked.connect(lambda: transfer_data(self, on_btn_pressed=on_btn_pressed))
        self.tb_item.doubleClicked.connect(lambda: transfer_data(self, on_btn_pressed=on_btn_pressed))
        
        # Dimensionar tabela
        tb_item = self.tb_item.horizontalHeader()
        tb_item.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.cmb_st_rev.clear()
        self.cmb_st_rev.setVisible(False)
        if on_btn_pressed == "item":
            query_database_item(self)
        elif on_btn_pressed == "pd":
            self.cmb_st_rev.setVisible(True)
            self.cmb_st_rev.addItems(["ALT", "S/ALT"])
            query_database_pd(self, on_btn_pressed)
        elif on_btn_pressed == "alt_pd":
            self.cmb_st_rev.setVisible(True)
            self.cmb_st_rev.addItems(["", "ALT", "S/ALT"])            
            query_database_pd(self, on_btn_pressed)
        elif on_btn_pressed == "car":
            query_database_pd(self, on_btn_pressed)    
        else:
            print("Erro")
    
        self.parent.resizeEvent = self.auto_resized
        
    def auto_resized(self, event):
        self.resize(self.parent.size())


# Class control interface item selection
class MainSearchContent(QMainWindow, Ui_SearchContent):
    def __init__(self, parent=None, on_btn_pressed=None, row=int, pd=None|str, caract=None|str, object_tab=None):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent
        self.row = row
        self.pd = pd
        self.caract = caract
    
        if on_btn_pressed == "car":
            query_database_caract(self)
        elif on_btn_pressed == "cont":        
            query_database_contents(self, self.pd, self.caract)
        else:
            print("Erro")
        
        # Dimensionar tabela
        tb_contents = self.tb_contents.horizontalHeader()
        tb_contents.setSectionResizeMode(QHeaderView.ResizeToContents)

        self.btn_close.clicked.connect(lambda: self.close())
        
        self.btn_search.clicked.connect(lambda: self.query(on_btn_pressed))
        self.txt_search.editingFinished.connect(lambda: self.query(on_btn_pressed))
        
        self.tb_contents.doubleClicked.connect(lambda: select_content(self,on_btn_pressed=on_btn_pressed, object_tab=object_tab))
        
        self.btn_salve.clicked.connect(lambda: select_content(self,on_btn_pressed=on_btn_pressed, object_tab=object_tab))

    def query(self, on_btn_pressed):
        if on_btn_pressed == "car":
            query_database_caract(self, str(self.txt_search.text()).strip())
        elif on_btn_pressed == "cont":        
            query_database_contents(self, self.pd, self.caract, str(self.txt_search.text()).strip())
        else:
            print("Erro")


# Class control interface item selection
class MainCadContents(QMainWindow, Ui_MainCadContents):
    def __init__(self, parent=None, dados=None|dict):
        super().__init__(parent)
        self.setupUi(self)
        self.parent = parent

        self.btn_close.clicked.connect(lambda: self.close())
        self.btn_salve.clicked.connect(lambda: cad_contents(self))
        
        self.txt_desc_long.editingFinished.connect(self.upadate_chave_cont)
        self.txt_sigla.editingFinished.connect(self.upadate_chave_cont)
        
        self.str_path = self.parent.str_path
        
        self.txt_pd_abrev.setText(str(dados["pd_abrev"]))
        self.txt_pd.setText(str(dados["pd"]))
        self.txt_carac.setText(str(dados["txt_carac"]))
        self.txt_desc_long.setText(str(dados["desc_long"]))
        self.txt_desc_curta.setText(str(dados["desc_curta"]))
        self.txt_sigla.setText(str(dados["sigla"]))
        
        
        
    def upadate_chave_cont(self):
        cont = "".join(self.txt_desc_long.text().split())
        self.txt_chave_cont.setText(f"{cont}{self.txt_sigla.text()}")


from PySide6.QtGui import QIntValidator, QDoubleValidator
from fractions import Fraction
class MainConvert(QMainWindow, Ui_MainConvert):    
    def __init__(self):
        super(MainConvert, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Pesquisa Material')       
    
        self.fr_in.setVisible(False)
        self.fr_mm.setVisible(False)
        self.fr_plg.setVisible(False)

        self.txt_result_in.setVisible(False)
        self.txt_result_in_un.setVisible(False)
        self.txt_result_mm.setVisible(False)
        self.txt_result_mm_un.setVisible(False)
        self.txt_result_plg.setVisible(False)
        self.txt_result_plg_un.setVisible(False)
        
        self.btn_close.clicked.connect(lambda: self.close())
        
        self.cmb_st_rev.currentIndexChanged.connect(self.exibir_fr)
        
        self.btn_search.clicked.connect(self.convert_valor)

    def exibir_fr(self):
        if self.cmb_st_rev.currentText() == "Polegada Imperial":
            self.fr_in.setVisible(True)
            self.fr_mm.setVisible(False)
            self.fr_plg.setVisible(False)
            self.txt_result_in.setVisible(False)
            self.txt_result_in_un.setVisible(False)
            self.txt_result_mm.setVisible(True)
            self.txt_result_mm_un.setVisible(True)
            self.txt_result_plg.setVisible(True)
            self.txt_result_plg_un.setVisible(True)
            
            self.txt_result_mm.setText("")
            self.txt_result_in.setText("")
            self.txt_result_plg.setText("")
            
            
        elif self.cmb_st_rev.currentText() == "Milimetro":
            self.fr_mm.setVisible(True)
            self.fr_in.setVisible(False)
            self.fr_plg.setVisible(False)
            self.txt_result_mm.setVisible(False)
            self.txt_result_mm_un.setVisible(False)
            self.txt_result_in.setVisible(True)
            self.txt_result_in_un.setVisible(True)
            self.txt_result_plg.setVisible(True)
            self.txt_result_plg_un.setVisible(True)
            
            self.txt_result_mm.setText("")
            self.txt_result_in.setText("")
            self.txt_result_plg.setText("")
            
        elif self.cmb_st_rev.currentText() == "Polegada":
            self.fr_plg.setVisible(True)
            self.fr_in.setVisible(False)
            self.fr_mm.setVisible(False)
            self.txt_result_plg.setVisible(False)
            self.txt_result_plg_un.setVisible(False)
            self.txt_result_mm.setVisible(True)
            self.txt_result_mm_un.setVisible(True)
            self.txt_result_in.setVisible(True)
            self.txt_result_in_un.setVisible(True)            
            
            self.txt_result_mm.setText("")
            self.txt_result_in.setText("")
            self.txt_result_plg.setText("")
            
            
    def convert_valor(self):
        if self.cmb_st_rev.currentText() == "Polegada Imperial":
            mm = self.in_to_mm(self.txt_dig_in.text())
            self.txt_result_mm.setText(mm)
            self.txt_result_plg.setText(self.mm_to_inches_fraction(mm))


        elif self.cmb_st_rev.currentText() == "Milimetro":
            self.txt_result_in.setText(self.mm_to_in(self.txt_dig_mm.text()))
            self.txt_result_plg.setText(self.mm_to_inches_fraction(self.txt_dig_mm.text()))
            

        elif self.cmb_st_rev.currentText() == "Polegada":
            mm = self.inches_fraction_to_mm(self.txt_dig_plg1.text(), self.txt_dig_plg2.text(), self.txt_dig_plg3.text())
            self.txt_result_mm.setText(mm)
            self.txt_result_in.setText(self.mm_to_in(mm))
            
            

    def mm_to_inches_fraction(self, value):
        try:
            valor = float(value)
        except:
            if "." in value:
                valor = float(value.replace(".", "").replace(",", "."))
            else:
                valor = float(value.replace(",", "."))
        
        inches = valor * 0.0393701  # Converte mm para polegadas
        whole_part = int(inches)  # Parte inteira das polegadas
        decimal_part = inches - whole_part  # Parte decimal das polegadas        
        # Converte a parte decimal para a fração mais próxima com denominador 16
        fraction = Fraction(decimal_part).limit_denominator(16)        
        # Formata o resultado
        if fraction.numerator == 0:  # Caso a parte fracionada seja zero
            return f'{whole_part}'
        elif whole_part != 0 and fraction.numerator != 0:
            return f'{whole_part}.{fraction.numerator}/{fraction.denominator}'
        else:    
            return f'{fraction.numerator}/{fraction.denominator}'



    def mm_to_in(self, value):
        try:
            valor = float(value)
        except:
            if "." in value:
                valor = float(value.replace(".", "").replace(",", "."))
            else:
                valor = float(value.replace(",", "."))
                
        return str(round(valor / 25.4, 4)).replace(".", ",")


    def in_to_mm(self, value):
        try:
            valor = float(value)
        except:
            if "." in value:
                valor = float(value.replace(".", "").replace(",", "."))
            else:
                valor = float(value.replace(",", "."))
                  
        return str(round(valor * 25.4, 2)).replace(".", ",")
    
    
    def inches_fraction_to_mm(self, whole_part, numerator, denominator):
        # Converte a fração para decimal e soma com a parte inteira
        if whole_part != "" and  numerator != "" and denominator != "":
            inches = int(whole_part) + (int(numerator) / int(denominator))
            
        elif numerator != "" and denominator != "":
            inches = (int(numerator) / int(denominator))
            
        else:
            inches = int(whole_part)
        # Converte polegadas para milímetrosN
        mm = inches / 0.0393701
        
        return str(round(mm, 2)).replace(".", ",")
    
    
    
    
    
    
    
    
    