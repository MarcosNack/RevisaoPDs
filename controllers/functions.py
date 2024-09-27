from PySide6.QtWidgets import (QTableWidgetItem, QPushButton, QCheckBox, QLineEdit, QApplication, QFileDialog, QHeaderView)
from PySide6.QtGui import QColor, QIcon
from PySide6.QtCore import QSize, Qt

from msgbox.msgbox import *


from controllers.connection_db import db_query_database, db_updata_database, db_insert_database
from controllers.connection_se import (ValidaSiteAberto, open_pd_form, load_pd_form, update_pd_form)

from datetime import datetime



#---------- Functions Main Interface ----------#
#--> Start Interface selection item
def start_interface_selection(self, on_btn_pressed):
    from controllers.interfaces import SelectItem
    self.select_item = SelectItem(self, on_btn_pressed)
    self.select_item.show()

#--> Start Interface selection contents
def start_interface_search_content(self, object_tab, pd=None, on_btn_pressed=None):
    from controllers.interfaces import MainSearchContent
    row = object_tab.currentRow()
    caract = object_tab.item(row, 0).text()
    serch_contents = MainSearchContent(self, on_btn_pressed=on_btn_pressed, row=row, pd=pd, caract=caract, object_tab=object_tab)
    serch_contents.show()

#--> Start Interface Cadastro Contents
def start_interface_select_content(self, object_tab, on_btn_pressed=None):
    from controllers.interfaces import MainCadContents
    row = object_tab.currentRow()
    dados = {"pd_abrev": "", "pd": "", "txt_carac": "", "desc_long": "", "desc_curta": "", "sigla": ""}    
    dados["pd_abrev"] = self.txt_cod_pd.text()
    dados["pd"] = self.txt_tit_pd.text()
    dados["txt_carac"] = object_tab.item(row, 0).text()
    dados["desc_long"] = object_tab.item(row, 1).text()
    dados["desc_curta"] = object_tab.item(row, 3).text()
    dados["sigla"] = object_tab.item(row, 4).text()
    
    serch_contents = MainCadContents(self, dados=dados)
    serch_contents.show()

#--> Start Convert Unidadde Medidas
def start_interface_convert(self):
    from controllers.interfaces import MainConvert
    self.main_convert = MainConvert()
    self.main_convert.show()

#--> Atalizar os dados do PD
def update_new_pd_data(self):
    def to_uppercase(text):
        lower_to_upper = {c: c.upper() for c in "abcdefghijklmnopqrstuvwxyz"}
        return text.translate(str.maketrans(lower_to_upper))
    
    total_lines = int(self.tb_new_pd.rowCount())
    # self.status = "TOTAL"
    for i in range(total_lines):
        pd_abrev =  self.txt_cod_pd.text()
        caract = self.tb_new_pd.item(i, 0).text()
        if self.tb_new_pd.item(i, 1):
            conteudo = to_uppercase(str(self.tb_new_pd.item(i, 1).text()).replace("1PLES", "SIMPLES").replace("'", ""))
            cont_pesq = "".join(conteudo.strip().split())
            str_sql = f"SELECT DESC_LONGA, DESC_CURTA, SIGLA FROM PD_CARAC_CONT WHERE PD_ABREV == '{pd_abrev}' AND CARACTERISTICA == '{caract}' AND CHAVE_CONT = '{cont_pesq}'"
            result = db_query_database(self.str_path, str_sql)
            if result["status"] == "OK":
                if len(result["df"]) > 0:
                    self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str(result["df"].loc[0, "DESC_LONGA"]).replace("1PLES", "SIMPLES")))
                    self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str(result["df"].loc[0, "DESC_CURTA"]).replace("1PLES", "SIMPLES")))
                    self.tb_new_pd.setItem(i, 4, QTableWidgetItem(str(result["df"].loc[0, "SIGLA"])))
                else:
                    self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str(self.tb_new_pd.item(i, 1).text()).replace("1PLES", "SIMPLES")))
                    if caract in ["FABRICANTE", "FABRICANTE-REFERENCIA", "REFERENCIA", "OPCIONAIS MOTOR"]:
                        self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str("")))
                        self.tb_new_pd.setItem(i, 4, QTableWidgetItem(str("")))
                        self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str(self.tb_new_pd.item(i, 1).text())))
                    else:
                        # self.status = "PARCIAL"
                        self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str("")))
                        self.tb_new_pd.setItem(i, 4, QTableWidgetItem(str("")))
                        self.novos_cont.append([pd_abrev, caract, conteudo, "", "", cont_pesq.replace("'", "\'")])
                        
    for i in range(total_lines):
        if (self.tb_new_pd.item(i, 0).text() == "OPCIONAIS MOTOR" or self.tb_new_pd.item(i, 0).text() == "CARACTERISTICAS ADICIONAIS") and self.tb_new_pd.item(i, 1).text() == "":
            self.tb_new_pd.item(i, 1).setText("N/A")
            self.tb_new_pd.item(i, 3).setText("N/A")
        elif (self.tb_new_pd.item(i, 0).text() == "OPCIONAIS MOTOR" or self.tb_new_pd.item(i, 0).text() == "CARACTERISTICAS ADICIONAIS") and self.tb_new_pd.item(i, 1).text() != "":
            self.tb_new_pd.item(i, 3).setText(self.tb_new_pd.item(i, 1).text())
            
        if self.tb_new_pd.item(i, 3).text() == "":
            self.tb_new_pd.item(i, 0).setBackground(QColor(204, 0, 0))
        else:
            self.tb_new_pd.item(i, 0).setBackground(QColor(0, 0, 0, 0))
    
    view_new_description(self)
          
    self.pd_atuali = "OK"
    self.btn_salve.setVisible(True)
    # self.btn_cad_cont.setVisible(True)


def view_new_description(self):
    self.txt_new_desc.setText("")
    self.ptxt_new_desc.setPlainText("")
    total_lines = int(self.tb_new_pd.rowCount())
    short_text = ""
    long_text = f"{self.txt_tit_pd.text()};"
    for i in range(total_lines):
        if self.tb_new_pd.item(i, 1).text() != "N/A":
            if self.tb_new_pd.item(i, 5).text() == "1":
                if self.tb_new_pd.item(i, 3).text() != "":
                    if self.tb_new_pd.item(i, 6).text() != "":
                        short_text = f"{short_text}{self.tb_new_pd.item(i, 3).text()}{self.tb_new_pd.item(i, 6).text()}"
                    else:
                        short_text = f"{short_text}{self.tb_new_pd.item(i, 3).text()}{self.tb_new_pd.item(i, 4).text()} "
            
            if self.tb_new_pd.item(i, 1).text() != "":
                long_text = f"{long_text} {self.tb_new_pd.item(i, 0).text()}: {self.tb_new_pd.item(i, 1).text()}"
                if self.tb_new_pd.item(i, 4).text() != "":
                    long_text = f"{long_text} {self.tb_new_pd.item(i, 4).text()};"
                else:
                    long_text = f"{long_text};"                       
            else:
                long_text = f"{long_text} {self.tb_new_pd.item(i, 0).text()}: Verificar Conteúdo;"
            
    if self.txt_abrev_pd.text() != "":
        short_text = f"{self.txt_abrev_pd.text()} {short_text}"
        
    self.txt_new_desc.setText(str(short_text).strip())
    self.txt_n_carac.setText(str(len(short_text.strip())))
    if len(short_text.strip()) > 40:
        self.txt_n_carac.setStyleSheet("""background-color: rgb(255, 0, 0);""")
    else:
        self.txt_n_carac.setStyleSheet("""background-color: rgb(230, 230, 230);""")
    
    self.ptxt_new_desc.setPlainText(long_text.strip())
        
#--> Gerar nova descrição curta
def new_short_text(self):
    total_lines = int(self.tb_new_pd.rowCount())
    if self.pd_atuali != "":
        short_text = ""
        long_text = f"{self.txt_tit_pd.text()};"
        check_caract = []
        dict_pd = {}
        for i in range(total_lines):
            dict_pd[self.tb_new_pd.item(i, 0).text()] = [self.tb_new_pd.item(i, 1).text(), self.tb_new_pd.item(i, 3).text(), self.tb_new_pd.item(i, 4).text()]
            if self.tb_new_pd.item(i, 1).text() != "N/A":                
                if self.tb_new_pd.item(i, 5).text() == "1":
                    if self.tb_new_pd.item(i, 3).text() != "":
                        if self.tb_new_pd.item(i, 6).text() != "":
                            short_text = f"{short_text}{self.tb_new_pd.item(i, 3).text()}{self.tb_new_pd.item(i, 6).text()}"
                        else:
                            short_text = f"{short_text}{self.tb_new_pd.item(i, 3).text()}{self.tb_new_pd.item(i, 4).text()} "
                
                if self.tb_new_pd.item(i, 1).text() != "":
                    long_text = f"{long_text} {self.tb_new_pd.item(i, 0).text()}: {self.tb_new_pd.item(i, 1).text()}"
                    if self.tb_new_pd.item(i, 4).text() != "":
                        long_text = f"{long_text} {self.tb_new_pd.item(i, 4).text()};"
                    else:
                        long_text = f"{long_text};"                       
                else:
                    long_text = f"{long_text} {self.tb_new_pd.item(i, 0).text()}: Verificar Conteúdo;"
                    check_caract.append(self.tb_new_pd.item(i, 0).text())
                
        if self.txt_abrev_pd.text() != "":
            short_text = f"{self.txt_abrev_pd.text()} {short_text}"
            
        if len(check_caract)>0:
            status = "PARCIAL"
        else:
            status = "TOTAL"
            
        check_caract = ", ".join(check_caract)
        data_atual = datetime.now()
        dt_rev = datetime.strftime(data_atual, "%Y.%m.%d")
        
        dados = [short_text.strip(), long_text.strip(), long_text.strip(), str(dict_pd), check_caract, status, dt_rev, self.ptxt_txt_long.toPlainText(), self.txt_tit_pd.text()]        
        str_sql = f"UPDATE ITENS SET NEW_SHORT_TEXT = ?, LONG_TEXT = ?, NEW_LONG_TEXT = ?, DICT_NEW_LONG_TEXT = ?, OBSERV = ?, STATUS = ?, DT = ?, OLD_TEXT = ?, PD = ? WHERE COD_ITEM = '{self.txt_cod_sap.text()}'"
        
        dados = [short_text.strip(), long_text.strip(), long_text.strip(), str(dict_pd), check_caract, status, self.ptxt_txt_long.toPlainText(), self.txt_tit_pd.text()]        
        str_sql = f"UPDATE ITENS SET NEW_SHORT_TEXT = ?, LONG_TEXT = ?, NEW_LONG_TEXT = ?, DICT_NEW_LONG_TEXT = ?, OBSERV = ?, STATUS = ?, OLD_TEXT = ?, PD = ? WHERE COD_ITEM = '{self.txt_cod_sap.text()}'"
        
        self.txt_n_carac.setText("")
        self.txt_n_carac.setStyleSheet("""background-color: rgb(230, 230, 230);""")
        
        self.txt_new_desc.setText("")
        self.ptxt_new_desc.setPlainText("")
        
        db_updata_database(self.str_path, str_sql, dados)
       
        self.pd_atuali = ""
        for i in range(total_lines):
            self.tb_new_pd.item(i, 0).setBackground(QColor(0, 0, 0, 0))
            self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str("").upper()))                    
            self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str("").upper()))
            self.tb_new_pd.setItem(i, 4, QTableWidgetItem(str("").upper()))
            self.ptxt_txt_long.setPlainText("")
            
        self.btn_update.setVisible(False)
        self.btn_salve.setVisible(False)
        # self.btn_cad_cont.setVisible(False)
    else:
        MsgErro(f"Por gentileza atualizar a padronização")
        
#--> Consultar lista de itens banco de dados
def query_database_item(self):
    str_sql = "SELECT COD_ITEM, LONG_TEXT FROM ITENS WHERE STATUS == '' ORDER BY COD_ITEM ASC"
    result = db_query_database(self.str_path, str_sql)
    if result["status"] == "OK":
        self.tb_item.setColumnCount(len(result["df"].columns))
        self.tb_item.setHorizontalHeaderLabels(result["df"].columns)  
        
        self.tb_item.clearContents()
        self.tb_item.setRowCount(0)
        for i in result["df"].index:
            last_line = int(self.tb_item.rowCount())
            self.tb_item.insertRow(last_line)
            self.tb_item.setItem(last_line, 0, QTableWidgetItem(str(result["df"].loc[i, "COD_ITEM"])))
            self.tb_item.setItem(last_line, 1, QTableWidgetItem(str(result["df"].loc[i, "LONG_TEXT"])))
            self.tb_item.setItem(last_line, 1, QTableWidgetItem(str(result["df"].loc[i, "OLD_TEXT"])))
            
        self.txt_tot_itens.setText(str(len(result["df"])))
    else:
        MsgErro(str(result["msg"])) 

#--> Alteração massiva dos PDs
def massive_change(self):
    import os
    import pandas as pd
    msg_info = f"Deseja realmente alterar a padronização de forma massiva?"
    resp = MsgQuestion(msg_info)
    if resp == 16384:
        self.novos_cont = []
        self.br_progress.setVisible(True)
        self.br_progress.setRange(0, 100)
        
        total_lines = int(self.tb_item.rowCount())
        for i in range(total_lines):
            percent_complete = int((i + 1) / total_lines * 100)
            self.br_progress.setValue(percent_complete)
            
            transfer_data(self, row_selected=i, on_btn_pressed='item')
            update_new_pd_data(self)
            new_short_text(self)
        
        def gerar_nome_arquivo(base_name, extension=".xlsx"):
            i = 1
            new_name = base_name + extension
            while os.path.exists(new_name):
                new_name = f"{base_name}{i}{extension}"
                i += 1
            return new_name 
        
        
        df = pd.DataFrame(self.novos_cont, columns=["PD_ABREV", "CARACTERISTICA", "DESC_LONGA", "DESC_CURTA", "SIGLA", "CHAVE_CONT"])
        
        if len(df) > 0:
            nome_arquivo = "NovosConteudos"
            arquivo_completo = gerar_nome_arquivo(nome_arquivo)
            df.to_excel(arquivo_completo, sheet_name="PLAN", index=False)
                    
        MsgFinalizado("Dados atualizados com sucesso!")
        self.br_progress.setVisible(False)
        
    else:
        MsgInformation("Processo cancelado!")

#--> Editar linha tabela
def edit_triggers_table(object_tab, row, col):
    item = None
    if object_tab.objectName() == "tb_new_pd":
        if col in [1, 3, 4]:
            item = object_tab.item(row, col)
            
    elif object_tab.objectName() == "alt_pd_tb_ant":
        if col in [0, 1, 3]:
            item = object_tab.item(row, col)
            
    elif object_tab.objectName() == "alt_pd_tb_novo":
        if col == 0:
            item = object_tab.item(row, col)
                  
    if item:
        item.setFlags(item.flags() | Qt.ItemIsEditable)
        object_tab.editItem(item)



#---------- Functions Interface Item Selecion ----------#
#--> Consultar lista de itens banco de dados
def query_database_pd(self, on_btn_pressed):
    if on_btn_pressed == "pd":
        str_sql = f"SELECT ABREVPD, PD, DT_REV, ST_REV FROM PD_CARACT WHERE ST_REV = '{self.cmb_st_rev.currentText()}' ORDER BY PD ASC"
    elif on_btn_pressed == "alt_pd":
        st_rev = " "
        if self.cmb_st_rev.currentText() != "":
            st_rev = f" WHERE ST_REV == '{self.cmb_st_rev.currentText()}' "
        str_sql = f"SELECT ABREVPD, PD, DT_REV, ST_REV FROM PD_CARACT{st_rev}ORDER BY PD ASC"
    
    result = db_query_database(self.str_path, str_sql)
    if result["status"] == "OK":
        self.tb_item.setColumnCount(len(result["df"].columns))
        self.tb_item.setHorizontalHeaderLabels(result["df"].columns)         
        self.tb_item.clearContents()
        self.tb_item.setRowCount(0)
        columns = result["df"].columns
        for i in result["df"].index:            
            last_line = int(self.tb_item.rowCount())
            self.tb_item.insertRow(last_line)
            for col in range(len(columns)): 
                self.tb_item.setItem(last_line, col, QTableWidgetItem(str(result["df"].loc[i, columns[col]])))
        
    else:
        MsgErro(str(result["msg"]))

#--> Consultar lista de itens banco de dados
def query_database_filter(self, on_btn_pressed):
    if on_btn_pressed == "item":
        str_old = ""
        str_sm = ""
        str_se = ""
        if self.txt_search_old.text() != "":
            str_old = f" AND OLD_TEXT LIKE '{self.txt_search_old.text()}' "
            
        if self.cmb_sm.currentText() != "":
            str_sm = f" AND SM == '{self.cmb_sm.currentText()}' "
            
                
        str_sql = f"""SELECT COD_ITEM, SM, STATUS, DT, STATUS_SE, STATUS_SAP, LONG_TEXT, OLD_TEXT FROM ITENS 
                    WHERE (COD_ITEM == '{str(self.txt_search.text()).strip()}' OR LONG_TEXT LIKE '{str(self.txt_search.text()).strip()}%'){str_sm}
                    AND STATUS == '{self.cmb_st_pad.currentText()}'{str_old} AND STATUS_SE == '{self.cmb_st_se.currentText()}'
                    ORDER BY LONG_TEXT ASC"""
        
    elif on_btn_pressed == "pd":
        str_sql = f"SELECT ABREVPD, PD, DT_REV, ST_REV FROM PD_CARACT WHERE PD LIKE '%{str(self.txt_search.text()).replace(" ", "%").strip()}%' AND ST_REV = '{self.cmb_st_rev.currentText()}'  ORDER BY PD ASC"    
    
    elif on_btn_pressed == "alt_pd":
        st_rev = " "
        if self.cmb_st_rev.currentText() != "":
            st_rev = f" AND ST_REV == '{self.cmb_st_rev.currentText()}' "
        str_sql = f"SELECT ABREVPD, PD, DT_REV, ST_REV FROM PD_CARACT WHERE (PD LIKE '%{str(self.txt_search.text()).replace(" ", "%").strip()}%' OR ABREVPD LIKE '%{str(self.txt_search.text()).replace(" ", "%").strip()}%'){st_rev}ORDER BY PD ASC"
        
    result = db_query_database(self.str_path, str_sql)
    if result["status"] == "OK":
        if len(result["df"]) > 0:
            columns = result["df"].columns
            self.tb_item.setColumnCount(len(columns))
            self.tb_item.setHorizontalHeaderLabels(columns)
            self.tb_item.clearContents()
            self.tb_item.setRowCount(0)
            for i in result["df"].index:
                last_line = int(self.tb_item.rowCount())
                self.tb_item.insertRow(last_line)
                for col in range(len(result["df"].columns)):                    
                    self.tb_item.setItem(last_line, col, QTableWidgetItem(str(result["df"].loc[i, columns[col]])))
                
            if on_btn_pressed == "item":    
                self.txt_tot_itens.setText(str(len(result["df"])))
                
            self.tb_item.setColumnHidden(7, True)
            # Dimensionar tabela
            tb_item = self.tb_item.horizontalHeader()
            tb_item.setSectionResizeMode(QHeaderView.ResizeToContents)
            
        else:
            self.tb_item.clearContents()
            self.tb_item.setRowCount(0)
            MsgWarning("Não foi encontrado nenhum Material pendente de revisado!")
    else:
        MsgErro(str(result["msg"]))        
     
#--> Carregar dados pd antigo tabela tb_pd_old interface principal
def transfer_data(self, row_selected="", on_btn_pressed=None):
    if row_selected == "":
        row_selected = self.tb_item.selectedIndexes()[0].row()        
    if row_selected != "":
        if on_btn_pressed == "item":
            str_long_text = self.tb_item.item(row_selected, 6).text()
            str_old_text = self.tb_item.item(row_selected, 7).text()            
            self.txt_cod_sap.setText(self.tb_item.item(row_selected, 0).text())
            
            self.ptxt_new_desc.setPlainText(str(str_long_text))
            if str_old_text != "":  
                self.ptxt_txt_long.setPlainText(str(str_old_text))
            else:
                self.ptxt_txt_long.setPlainText(str(str_long_text))
                   
            load_old_pd_data(self, str_long_text)
            self.btn_update.setVisible(True)
        elif on_btn_pressed == "pd":
            str_id = self.tb_item.item(row_selected, 0).text()
            self.parent.txt_cod_pd.setText(self.tb_item.item(row_selected, 0).text())
            self.parent.txt_tit_pd.setText(self.tb_item.item(row_selected, 1).text())
            laod_new_pd_data(self, str_id)
            self.parent.txt_search.setText(self.tb_item.item(row_selected, 1).text())
            query_database_filter(self.parent, "item")            
            self.parent.btn_alt_massiva.setVisible(True)
            self.parent.btn_carregar.setVisible(True)
            self.parent.btn_search_item.setVisible(True)
            self.parent.btn_cad_cont.setVisible(True)
            self.parent.frame_11.setVisible(True)
            self.parent.frame_5.setVisible(True)
            MsgInformation("PD atualizado")
            self.close()
        
        elif on_btn_pressed == "alt_pd":
            str_id = self.tb_item.item(row_selected, 0).text()
            laod_new_pd(self, str_id)
            MsgInformation("PD atualizado")
            self.close()
    else:
        MsgErro("Por gentileza selecionar pelo menos uma linha.")

#--> Criar dicionario
def create_dict(str_long_text):
    dict_data = {}
    valores = str_long_text.split(";")[1:]
    for valor in valores:
        if ":" in valor:
            lt = valor.split(":")
            dict_data[lt[0].strip()] = lt[1].strip()            
    return dict_data

#--> Carregar os dados dos materiais antigos
def load_old_pd_data(self, str_long_text):
    def to_uppercase(text):
        lower_to_upper = {c: c.upper() for c in "abcdefghijklmnopqrstuvwxyz"}
        return text.translate(str.maketrans(lower_to_upper))
    dict_data = create_dict(str_long_text.replace("Ê", "E").replace("FABRICANTE- REFERENCIA", "FABRICANTE-REFERENCIA").replace("FABRI CANTE-REFERENCIA", "FABRICANTE-REFERENCIA").replace("FABRICA NTE-REFERENCIA", "FABRICANTE-REFERENCIA"))
    fab_ref = ""
    self.tb_pd_old.clearContents()
    self.tb_pd_old.setRowCount(0)
    
    fab_ref = {"fab": "", "ref": ""}
    if "FABRICANTE-REFERENCIA" in dict_data.keys():
        if len(to_uppercase(str(dict_data["FABRICANTE-REFERENCIA"])).split("-")) > 1:
            fab_ref["fab"] = to_uppercase(str(dict_data["FABRICANTE-REFERENCIA"])).split("-")[0].strip()
            fab_ref["ref"] = to_uppercase(str(dict_data["FABRICANTE-REFERENCIA"])).split("-")[1].strip()
    
    fab_ref_un = []
    if "FABRICANTE" in dict_data.keys():
        if len(to_uppercase(str(dict_data["FABRICANTE"]))) > 1:
            fab_ref_un.append(to_uppercase(str(dict_data["FABRICANTE"])).strip())
    if "REFERENCIA" in dict_data.keys():
        if len(to_uppercase(str(dict_data["REFERENCIA"]))) > 1:
            fab_ref_un.append(to_uppercase(str(dict_data["REFERENCIA"])).strip())
            
    fab_ref_un = "-".join(fab_ref_un)
                        
    total_lines = int(self.tb_new_pd.rowCount())
    for i in range(total_lines):
        self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str("")))
        self.tb_new_pd.setItem(i, 3, QTableWidgetItem(str("")))
        self.tb_new_pd.setItem(i, 4, QTableWidgetItem(str("")))
        
    for row in dict_data.keys():
        last_line = int(self.tb_pd_old.rowCount())
        self.tb_pd_old.insertRow(last_line)
        self.tb_pd_old.setItem(last_line, 0, QTableWidgetItem(str(row)))
        self.tb_pd_old.setItem(last_line, 1, QTableWidgetItem(str(dict_data[row])))
        
        if row in self.keys_upload.keys():
            for i in range(total_lines):
                caract = self.tb_new_pd.item(i, 0).text()
                if self.keys_upload[row][0] == caract:
                    if self.tb_new_pd.item(i, 1).text() == "":
                        self.tb_new_pd.setItem(i, 1, QTableWidgetItem(to_uppercase(str(dict_data[row]))))
                    else:
                        cont = f"{self.tb_new_pd.item(i, 1).text()}{self.keys_upload[row][1]}{dict_data[row]}"
                        self.tb_new_pd.setItem(i, 1, QTableWidgetItem(to_uppercase(str(cont))))                        
                    break
                
    for i in range(total_lines):
        caract = self.tb_new_pd.item(i, 0).text()                
        if self.tb_new_pd.item(i, 0).text() == "REFERENCIA" and self.tb_new_pd.item(i, 1).text() == "":
            self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str(fab_ref["ref"])))
            
        elif self.tb_new_pd.item(i, 0).text() == "FABRICANTE" and self.tb_new_pd.item(i, 1).text() == "":
            self.tb_new_pd.setItem(i, 1, QTableWidgetItem(str(fab_ref["fab"])))
        
        elif self.tb_new_pd.item(i, 0).text() == "FABRICANTE-REFERENCIA" and self.tb_new_pd.item(i, 1).text() == "":
            self.tb_new_pd.setItem(i, 1, QTableWidgetItem(fab_ref_un))

#--> Carregar os dados do novo PD
def laod_new_pd_data(self, str_id):
    str_sql = f"SELECT * FROM PD_CARACT WHERE ABREVPD == '{str_id}'"    
    result = db_query_database(self.str_path, str_sql)
    if result["status"] == "OK":
        self.parent.tb_new_pd.clearContents()
        self.parent.tb_new_pd.setRowCount(0)
        self.parent.txt_abrev_pd.setText(result["df"].loc[0, result["df"].columns[3]])
        df_dict = eval(result["df"].loc[0, "EST_PD"])        
        self.parent.keys_upload = eval(result["df"].loc[0, "DE_PARA"])
        for i in range(35):
            caract = df_dict["caract"][i]
            if caract != "N/A":
                curta = df_dict["desc_curt"][i]
                sep = df_dict["sep"][i]
                last_line = int(self.parent.tb_new_pd.rowCount())
                self.parent.tb_new_pd.insertRow(last_line)
                self.parent.tb_new_pd.setItem(last_line, 0, QTableWidgetItem(str(caract)))
                self.parent.tb_new_pd.setItem(last_line, 1, QTableWidgetItem(str("")))
                
                btn_search_content = new_btn_search_content(self.parent)                
                btn_search_content.clicked.connect(lambda: start_interface_search_content(self.parent, object_tab=self.parent.tb_new_pd, pd=self.parent.txt_tit_pd.text(), on_btn_pressed="cont"))
                
                self.parent.tb_new_pd.setCellWidget(last_line, 2, btn_search_content)
                
                self.parent.tb_new_pd.setItem(last_line, 3, QTableWidgetItem(str("")))
                self.parent.tb_new_pd.setItem(last_line, 4, QTableWidgetItem(str("")))
                self.parent.tb_new_pd.setItem(last_line, 5, QTableWidgetItem(str(curta)))
                self.parent.tb_new_pd.setItem(last_line, 6, QTableWidgetItem(str(sep)))
                
                i += 1
            else:
                break
        
    else:
        MsgErro(str(result["msg"]))

#--> Carregar os dados do novo PD
def laod_new_pd(self, str_id):
    str_sql = f"SELECT * FROM PD_CARACT WHERE ABREVPD == '{str_id}'"
    result = db_query_database(self.str_path, str_sql)
    if result["status"] == "OK":
        ValidaSiteAberto(self.parent)
        self.parent.alt_pd_txt_oid.setText(result["df"].loc[0, "OID"])
        self.parent.alt_pd_txt_cod_pd.setText(result["df"].loc[0, "ABREVPD"])
        self.parent.alt_pd_txt_tt_pd.setText(result["df"].loc[0, "PD"])
        self.parent.alt_pd_txt_date_rev.setText(result["df"].loc[0, "DT_REV"])

        self.parent.alt_pd_tb_ant.clearContents()
        self.parent.alt_pd_tb_ant.setRowCount(0)
        
        self.parent.alt_pd_tb_novo.clearContents()
        self.parent.alt_pd_tb_novo.setRowCount(0)
        if self.parent.win_cad_pd != "":
            self.parent.browser.switch_to.window(self.parent.win_cad_pd)
            self.parent.browser.close()
            self.parent.win_cad_pd = ""
            
        result_se = open_pd_form(self.parent, result["df"].loc[0, "OID"])
        if result_se['status'] == "OK":
            if result_se['title_pd_red'] != "":
                self.parent.alt_pd_chb_tt_red.setChecked(True)
                self.parent.alt_pd_txt_tit_red.setText(result_se['title_pd_red'])
            else:
                self.parent.alt_pd_chb_tt_red.setChecked(False)
                self.parent.alt_pd_txt_tit_red.setText("")
                
            # df_dict = eval(result["df"].loc[0, "EST_PD"])
            for i in range(35):                
                caract, desc_curt, desc_man, adic, sep = load_pd_form(self.parent, i)
                # caract = df_dict["caract"][i]
                # desc_curt = df_dict["desc_curt"][i]
                # desc_man = df_dict["desc_man"][i]
                # adic = df_dict["adic"][i]
                # sep = df_dict["sep"][i]
                
                last_line = int(self.parent.alt_pd_tb_ant.rowCount())
                self.parent.alt_pd_tb_ant.insertRow(last_line)
                self.parent.alt_pd_tb_ant.setItem(last_line, 0, QTableWidgetItem(str(caract)))
                if caract != "N/A":
                    self.parent.alt_pd_tb_ant.setItem(last_line, 1, QTableWidgetItem(str(i+1)))
                else:
                    self.parent.alt_pd_tb_ant.setItem(last_line, 1, QTableWidgetItem(str("")))
                
                self.parent.alt_pd_tb_novo.insertRow(last_line)
                self.parent.alt_pd_tb_novo.setItem(last_line, 0, QTableWidgetItem(str(caract)))
                    
                #Configuração botão pesquisa Nova Caracteristica  
                btn_search_content = new_btn_search_content(self.parent)                
                btn_search_content.clicked.connect(lambda: start_interface_search_content(self.parent, object_tab=self.parent.alt_pd_tb_novo, on_btn_pressed="car"))               
                self.parent.alt_pd_tb_novo.setCellWidget(last_line, 1, btn_search_content)
                
                chb = new_chb(self.parent)
                self.parent.alt_pd_tb_novo.setCellWidget(last_line, 2, chb)
                if desc_curt == 1:
                    chb.setChecked(True)
                    self.parent.alt_pd_tb_novo.setItem(last_line, 3, QTableWidgetItem(str("Sim")))
                    self.parent.alt_pd_tb_ant.setItem(last_line, 2, QTableWidgetItem(str("Sim")))
                else:
                    chb.setChecked(False)
                    self.parent.alt_pd_tb_novo.setItem(last_line, 3, QTableWidgetItem(str("Não")))
                    self.parent.alt_pd_tb_ant.setItem(last_line, 2, QTableWidgetItem(str("Não")))
                self.parent.alt_pd_tb_ant.setItem(last_line, 3, QTableWidgetItem(str("")))                
                chb.stateChanged.connect(lambda: change_chb_curto(self.parent.alt_pd_tb_novo, 3))
                chb = new_chb(self.parent)
                if desc_man == 1:
                    chb.setChecked(True)
                else:
                    chb.setChecked(False)
                self.parent.alt_pd_tb_novo.setCellWidget(last_line, 4, chb)
                chb = new_chb(self.parent)
                if adic == 1:
                    chb.setChecked(True)
                else:
                    chb.setChecked(False)
                self.parent.alt_pd_tb_novo.setCellWidget(last_line, 5, chb)            
                chb = new_chb(self.parent)
                txt = new_txt(self.parent)            
                if sep != "":
                    chb.setChecked(True)
                    self.parent.alt_pd_tb_novo.setCellWidget(last_line, 6, chb)
                    txt.setText(sep)
                    txt.setReadOnly(False)
                    self.parent.alt_pd_tb_novo.setCellWidget(last_line, 7, txt)
                else:
                    chb.setChecked(False)
                    self.parent.alt_pd_tb_novo.setCellWidget(last_line, 6, chb)
                    txt.setText(sep)
                    txt.setReadOnly(True)                
                    self.parent.alt_pd_tb_novo.setCellWidget(last_line, 7, txt)                
                chb.stateChanged.connect(lambda: change_chb_sep(self.parent.alt_pd_tb_novo, 7))
                i += 1
    else:
        MsgErro(str(result["msg"]))

#--> Criar botão pesquisa tabelas
def new_btn_search_content(self):
    self.btn_search_content = QPushButton(self.frame)
    self.btn_search_content.setMaximumSize(QSize(30, 25))
    icon = QIcon()
    icon.addFile(u":/icons/pesquisar.png", QSize(), QIcon.Normal, QIcon.Off)
    self.btn_search_content.setIcon(icon)
    self.btn_search_content.setIconSize(QSize(15, 15))
    self.btn_search_content.setToolTip("Visualizar Conteúdo")
    self.btn_search_content.setStyleSheet("""QPushButton{background-color:rgb(220, 220, 220); border-style: outset; border-width: 2px; border-radius: 0px; border-color: rgb(181, 181, 181); text-align: center; color: rgb(255, 255, 255);} QPushButton::hover {background-color: rgb(141, 211, 211); border-style: inset; } QPushButton::pressed {background-color: rgb(141, 211, 211); border-style: inset;}""")       
    return self.btn_search_content

#--> Configuração QCheckBox Adicional Mais de um conteúdo
def new_chb(self):    
    self.chb = QCheckBox()
    self.chb.setStyleSheet("background-color: rgba(0, 0, 0, 0); padding-Left: 50px;")
    return self.chb

#--> Configuração QLineEdit Nova Caracteristica
def new_txt(self):
    self.txt = QLineEdit(self.frame)
    self.txt.setMaximumSize(60, 25)
    self.txt.setReadOnly(True)
    self.txt.setStyleSheet("background-color: rgb(197, 197, 197); color: rgb(0, 0, 0); border-width: 2px; border-radius: 0px;")
    return self.txt
  
#--> Alterar as opção Sim/Não
def change_chb_curto(object_tab, col):
    row = object_tab.currentRow()
    if object_tab.cellWidget(row,2).isChecked():
        object_tab.setItem(row, col, QTableWidgetItem(str("Sim")))
    else:
        object_tab.setItem(row, col, QTableWidgetItem(str("Não")))
 
#--> Alterar o campo do separador
def change_chb_sep(object_tab, col):
    row = object_tab.currentRow()
    if object_tab.cellWidget(row,6).isChecked():
        object_tab.cellWidget(row,7).setReadOnly(False)
        object_tab.cellWidget(row,7).setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0); border-width: 2px; border-radius: 0px;")
    else:
        object_tab.cellWidget(row,7).setText("")
        object_tab.cellWidget(row,7).setStyleSheet("background-color: rgb(197, 197, 197); color: rgb(0, 0, 0); border-width: 2px; border-radius: 0px;")
        object_tab.cellWidget(row,7).setReadOnly(True)



#---------- Functions Interface Search Contents ----------#
#--> Lista Conteúdos PD
def query_database_contents(self, pd, caract, filter=""):
    if filter != "":
        cont_search = f" AND DESC_LONGA LIKE '%{filter}%'"
    else:
        cont_search = ""        
    str_sql = f"SELECT DISTINCT PD_ABREV, PD, CARACTERISTICA, DESC_LONGA, DESC_CURTA, SIGLA FROM PD_CARAC_CONT WHERE PD = '{pd}' AND CARACTERISTICA = '{caract}'{cont_search} ORDER BY DESC_LONGA ASC"
    
    result = db_query_database(self.parent.str_path, str_sql)    
    if result["status"] == "OK":
        columns_result = result["df"].columns
        self.tb_contents.setColumnCount(len(columns_result))
        self.tb_contents.setHorizontalHeaderLabels(columns_result)        
        self.tb_contents.clearContents()
        self.tb_contents.setRowCount(0)
        for i in result["df"].index:
            last_line = int(self.tb_contents.rowCount())
            self.tb_contents.insertRow(last_line)
            self.tb_contents.setItem(last_line, 0, QTableWidgetItem(str(result["df"].loc[i, columns_result[0]])))
            self.tb_contents.setItem(last_line, 1, QTableWidgetItem(str(result["df"].loc[i, columns_result[1]])))
            self.tb_contents.setItem(last_line, 2, QTableWidgetItem(str(result["df"].loc[i, columns_result[2]])))
            self.tb_contents.setItem(last_line, 3, QTableWidgetItem(str(result["df"].loc[i, columns_result[3]])))
            self.tb_contents.setItem(last_line, 4, QTableWidgetItem(str(result["df"].loc[i, columns_result[4]])))
            self.tb_contents.setItem(last_line, 5, QTableWidgetItem(str(result["df"].loc[i, columns_result[5]])))
    else:
        MsgErro(str(result["msg"]))

#--> Lista Caracteristicas
def query_database_caract(self, filter=""):
    if filter != "":
        cont_search = f"WHERE CARACT LIKE '%{filter}%' "
    else:
        cont_search = ""
    str_sql = f"SELECT CARACT FROM CARACT {cont_search}ORDER BY CARACT ASC"
    result = db_query_database(self.parent.str_path, str_sql)    
    if result["status"] == "OK":
        columns_result = result["df"].columns
        self.tb_contents.setColumnCount(len(columns_result))
        self.tb_contents.setHorizontalHeaderLabels(columns_result)        
        self.tb_contents.clearContents()
        self.tb_contents.setRowCount(0)
        for i in result["df"].index:
            last_line = int(self.tb_contents.rowCount())
            self.tb_contents.insertRow(last_line)
            self.tb_contents.setItem(last_line, 0, QTableWidgetItem(str(result["df"].loc[i, columns_result[0]])))

    else:
        MsgErro(str(result["msg"]))

#--> Selecionar os conteúdos
def select_content(self, on_btn_pressed, object_tab):
    row_selected = self.tb_contents.selectedIndexes()
    if row_selected:
        if on_btn_pressed == "car":
            str_id = self.tb_contents.item(row_selected[0].row(), 0).text()
            object_tab.setItem(self.row, 0, QTableWidgetItem(str(str_id)))
        elif on_btn_pressed == "cont":
            if self.tb_contents.item(row_selected[0].row(), 5).text() != "":
                str_id = f"{self.tb_contents.item(row_selected[0].row(), 3).text()} {self.tb_contents.item(row_selected[0].row(), 5).text()}"
            else:
                str_id = f"{self.tb_contents.item(row_selected[0].row(), 3).text()}"                
            object_tab.setItem(self.row, 1, QTableWidgetItem(str(str_id)))
        else:
            MsgErro("Erro")
        self.close()
    else:
        MsgErro("Por gentileza selecionar pelo menos uma linha.")
        


#---------- INTERFACE FUNCTIONS PD'S REVIEW ----------#
#--> Habilitar Campo Titulo Reduzido
def change_shortened_title(self):
    if  self.alt_pd_chb_tt_red.isChecked():
        self.alt_pd_txt_tit_red.setReadOnly(False)
        self.alt_pd_txt_tit_red.setText("")
        self.alt_pd_txt_tit_red.setStyleSheet("background-color: rgb(255, 255, 255); color: rgb(0, 0, 0);")
    else:
        self.alt_pd_txt_tit_red.setReadOnly(True)
        self.alt_pd_txt_tit_red.setText("")
        self.alt_pd_txt_tit_red.setStyleSheet("background-color: rgb(197, 197, 197); color: rgb(0, 0, 0);")
        
#--> Atualizar a estrutura do PD
def update_pd_structure(self, oid):
    # Exibir a caixa de mensagem
    msg_info = f"Deseja realmente alterar a estrutura do PD {self.alt_pd_txt_tt_pd.text()}?"
    resp = MsgQuestion(msg_info)
    if resp == 16384:
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.wait import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        rows = self.alt_pd_tb_novo.rowCount()
        str_sql = f"SELECT EST_PD FROM PD_CARACT WHERE OID == '{oid}'"
        result = db_query_database(self.str_path, str_sql)
        if result["status"] == "OK":
            est_pd_ant = result["df"].loc[0, "EST_PD"]
        cod_pd = str(self.alt_pd_txt_tt_pd.text()).strip()
        titulored = str(self.alt_pd_txt_tit_red.text()).strip()
        dict_pd = {"caract": [], "desc_curt": [], "desc_man":[], "adic": [], "sep": []}
        de_para = {}
        self.st_rev_pd = ""
        
        try:
            self.browser.switch_to.window(self.win_cad_pd)
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "efmsExec"))
            )    
            self.browser.switch_to.frame("efmsExec")
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "field_8ae445747a67a2a7017a8781c3531794"))
            )
        except:
            open_pd_form(self, oid)
        
        for row in range(rows):
            carac = str(self.alt_pd_tb_novo.item(row, 0).text()).strip()
            dict_pd["caract"].append(carac)   

            if self.alt_pd_tb_novo.cellWidget(row, 2).isChecked():
                dict_pd["desc_curt"].append(1)
                comp_desc_curta = "yes"
                sim_nao = "Sim"
            else:
                dict_pd["desc_curt"].append(0)
                comp_desc_curta = ""
                sim_nao = "Não"
                
            if self.alt_pd_tb_novo.cellWidget(row, 4).isChecked():
                dict_pd["desc_man"].append(1)
                desc_manual = 'yes'
            else:
                dict_pd["desc_man"].append(0)
                desc_manual = ''   
                            
            if self.alt_pd_tb_novo.cellWidget(row, 5).isChecked():
                dict_pd["adic"].append(1)
                mais_conteudo = "yes"
            else:
                dict_pd["adic"].append(0) 
                mais_conteudo = ""  
                             
            if self.alt_pd_tb_novo.cellWidget(row, 6).isChecked():
                separador = self.alt_pd_tb_novo.cellWidget(row, 7).text()
                dict_pd["sep"].append(separador)
                possui_separador = "yes"                
            else:
                separador = self.alt_pd_tb_novo.cellWidget(row, 7).text()
                dict_pd["sep"].append(separador)
                possui_separador = ""
                                
            ref_ant = self.alt_pd_tb_ant.item(row, 1).text()
            if ref_ant != "":
                de_para[self.alt_pd_tb_ant.item(row, 0).text()] = [str(self.alt_pd_tb_novo.item(int(ref_ant)-1, 0).text()).strip(), self.alt_pd_tb_ant.item(row, 3).text()]
            
            if titulored != "":
                chb_title_red = "yes"
            else:
                chb_title_red = ""
                
            update_pd_form(self, chb_title_red, titulored, carac, comp_desc_curta, desc_manual, mais_conteudo, sim_nao, possui_separador, separador, row)
            
        self.browser.switch_to.window(self.win_cad_pd)        
        self.browser.find_element(By.ID, "btnSaveExit-btnWrap").click()
        self.win_cad_pd = ""
              
        if self.alt_pd_chb_st_rev.isChecked():
            st_rev = "ALT"
        else:
            st_rev = "S/ALT"
            
        if self.st_rev_pd == "":
            data_atual = datetime.now()
            dt_rev = datetime.strftime(data_atual, "%Y.%m.%d")
            str_sql = f"UPDATE PD_CARACT SET PD = ?, TITULORED = ?, EST_PD = ?, EST_PD_ANT = ?, DE_PARA = ?, DT_REV = ?, ST_REV = ? WHERE OID == '{oid}'"
            dados = [cod_pd, titulored, str(dict_pd), est_pd_ant, str(de_para), dt_rev, st_rev]        
            result = db_updata_database(self.str_path, str_sql, dados)        
            if result["status"] == "OK":
                self.alt_pd_tb_ant.clearContents()
                self.alt_pd_tb_ant.setRowCount(0)
                self.alt_pd_tb_novo.clearContents()
                self.alt_pd_tb_novo.setRowCount(0)
                MsgInformation(f"Estrutura do PD {self.alt_pd_txt_tt_pd.text()} atualizada com sucesso!")
            else:
                MsgErro(str(result["msg"]))
        else:
            MsgErro("Erro para alterar o PD")
    else:
        MsgInformation("Processo cancelado!")



#---------- INTERFACE FUNCTIONS CADASTRO CONTENTS ----------#        
#--> Cadastrar novo conteúdo
def cad_contents(self):
    columns = ['PD_ABREV', 'PD', 'CARACTERISTICA', 'DESC_LONGA', 'DESC_CURTA', 'SIGLA', 'CHAVE_CONT']
    dados = [[self.txt_pd_abrev.text(), self.txt_pd.text(), self.txt_carac.text(), self.txt_desc_long.text(), self.txt_desc_curta.text(), self.txt_sigla.text(), self.txt_chave_cont.text()]]
    result = db_insert_database(str_path=self.str_path, tab="PD_CARAC_CONT", dados=dados, columns=columns)    
    if result["status"] == "OK":
        self.close()
    else:
        MsgErro(str(result["msg"])) 


