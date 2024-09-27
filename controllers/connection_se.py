import pandas as pd

import math
from time import sleep
from selenium import webdriver

import pyautogui

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from subprocess import CREATE_NO_WINDOW




# Validar se foi aberto o SoftExpert
def ValidaSiteAberto(self):
    try:
        self.browser.switch_to.window(self.window_principal)
        site = self.browser.current_url
        if "portal.berneck.com.br" in site:
            return "OK", ""
        else:
            return connection_softexpert(self)

    except:
        return connection_softexpert(self)

# Atualiza o webdriver do Chomer
def connection_softexpert(self):    
    try:
        # Conexão Edge
        # servico = webdriver.edge.service.Service(r"..\msedgedriver.exe")        
        servico = webdriver.edge.service.Service(r"msedgedriver.exe")
        
        servico.creation_flags = CREATE_NO_WINDOW            
        self.browser = webdriver.Edge(service=servico)
        self.browser.maximize_window()

        dimensao = self.browser.get_window_size()
        width = int(dimensao["width"])
        self.height = int(dimensao["height"])
        
        self.novo_width = width*50/100

        self.browser.get('https://portal.berneck.com.br/softexpert/workspace?page=execution,105,1')

        self.window_principal = self.browser.current_window_handle
        
        self.browser.set_window_size(self.novo_width+20, self.height)
        self.browser.set_window_position(self.novo_width-30,0)
        
        
        try:
            sleep(5)
            # Digite o texto no alerta
            pyautogui.write('berneck\\mhnc010337')
            # Envie a tecla Tab
            pyautogui.press('tab')
            # Adicione mais texto, se necessário
            pyautogui.write('010337*MHnc')
            pyautogui.press('Enter')
            
        except:
            pass
        
        return "OK", ""

    except:
        return "Erro", "Erro ao conectar ao SE. Verificar a versão do Driver."


def open_pd_form(self, oid_pd):
    self.win_cad_pd = ""
    try:
        link_pd = f"https://portal.berneck.com.br/se/form/efms_exec_html/efms_exec_frame.php?fgapplication=seform&fgpreview=2&oidrevisionform=8ae445747a67a2a7017a8782f30f19e1&oidentityreg={oid_pd}&action=2&&"
        self.browser.switch_to.window(self.window_principal) 
        
        windows = self.browser.window_handles
        for window in windows:
            self.browser.switch_to.window(window)
            if self.browser.current_url == link_pd:
                self.win_cad_pd = window
                break
                
        if self.win_cad_pd == "":
            self.browser.execute_script(f"window.open('{link_pd}', '_blank')")        
            windows = self.browser.window_handles
            self.browser.switch_to.window(windows[-1])
            #Aguardar carregar a pagina
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "headerTitle"))
            )
            txt_pd = self.browser.find_element(By.ID, "headerTitle")
            if "dpdcaract" in txt_pd.text:
                self.win_cad_pd = windows[-1]            
            
        if self.win_cad_pd != "":
            self.browser.switch_to.window(self.win_cad_pd)
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "efmsExec"))
            )    
            self.browser.switch_to.frame("efmsExec")
            WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.ID, "field_8ae445747a67a2a7017a8781c3531794"))
            )
               
            check_title_red = self.browser.find_element(By.ID, 'field_8ae445747a67a2a7017a8781e2c71807').is_selected() #chb_titulo_red
            title_pd_red = self.browser.find_element(By.ID, 'field_8ae445747a67a2a7017a8781e1f41802').get_attribute("value") #titulo_pd_red
            self.id_campo_form = {
                'caract_1':['field_8ae445747a67a2a7017a8781c623179a', 'field_8ae445747a67a2a7017a8781d09917b8', 'field_8ae445747a67a2a7017a8781d98017cc', 'field_8ae445747a67a2a7017a8781e5071809', 'field_8ae445747a67a2a7017a8782971b192d', 'field_8ae445748375da270183f19435f300d6', 'field_8ae445748375da270183f19fdd70029e'],
                'caract_2':['field_8ae445747a67a2a7017a8781c696179d', 'field_8ae445747a67a2a7017a8781d1eb17ba', 'field_8ae445747a67a2a7017a8781da0517cf', 'field_8ae445747a67a2a7017a8781e5f5180b', 'field_8ae445747a67a2a7017a878298bb192f', 'field_8ae445748375da270183f19464d000df', 'field_8ae445748375da270183f1a00cb602a2'],
                'caract_3':['field_8ae445747a67a2a7017a8781c6fd17a0', 'field_8ae445747a67a2a7017a8781d27917bc', 'field_8ae445747a67a2a7017a8781daa417d2', 'field_8ae445747a67a2a7017a8781e6c7180d', 'field_8ae445747a67a2a7017a878299e41931', 'field_8ae445748375da270183f1949bc600ee', 'field_8ae445748375da270183f1a03c2e02b0'],
                'caract_4':['field_8ae445747a67a2a7017a8781c7d717a3', 'field_8ae445747a67a2a7017a8781d3ce17be', 'field_8ae445747a67a2a7017a8781dbbb17d5', 'field_8ae445747a67a2a7017a8781e8a9180f', 'field_8ae445747a67a2a7017a87829c3d1933', 'field_8ae445748375da270183f194c84500f6', 'field_8ae445748375da270183f1a067e002b8'],
                'caract_5':['field_8ae445747a67a2a7017a8781c8ed17a6', 'field_8ae445747a67a2a7017a8781d51117c0', 'field_8ae445747a67a2a7017a8781dd4e17d8', 'field_8ae445747a67a2a7017a8781e9431811', 'field_8ae445747a67a2a7017a87829dd41935', 'field_8ae445748375da270183f1950adf0107', 'field_8ae445748375da270183f1a0b20702df'],
                'caract_6':['field_8ae445747a67a2a7017a8781c94d17a9', 'field_8ae445747a67a2a7017a8781d58617c2', 'field_8ae445747a67a2a7017a8781ddd617db', 'field_8ae445747a67a2a7017a8781e9e21816', 'field_8ae445747a67a2a7017a87829f061937', 'field_8ae445748375da270183f1954fd20129', 'field_8ae445748375da270183f1a0f39602e5'],
                'caract_7':['field_8ae445747a67a2a7017a8781c9af17ac', 'field_8ae445747a67a2a7017a8781d6ba17c4', 'field_8ae445747a67a2a7017a8781de5717de', 'field_8ae445747a67a2a7017a8781eb1d1818', 'field_8ae445747a67a2a7017a8782a174193b', 'field_8ae445748375da270183f1958338012d', 'field_8ae445748375da270183f1a153380316'],
                'caract_8':['field_8ae445747a67a2a7017a8781cb7717af', 'field_8ae445747a67a2a7017a8781d7ce17c6', 'field_8ae445747a67a2a7017a8781defa17e1', 'field_8ae445747a67a2a7017a8781ec27181a', 'field_8ae445747a67a2a7017a8782a30f193d', 'field_8ae445748375da270183f195bd060131', 'field_8ae445748375da270183f1a19ffd0319'],
                'caract_9':['field_8ae445747a67a2a7017a8781cd7c17b2', 'field_8ae445747a67a2a7017a8781d83f17c8', 'field_8ae445747a67a2a7017a8781df7f17e4', 'field_8ae445747a67a2a7017a8781ee68181d', 'field_8ae445747a67a2a7017a8782a444193f', 'field_8ae445748375da270183f196124c0133', 'field_8ae445748375da270183f1a208f1031e'],
                'caract_10':['field_8ae445747a67a2a7017a8781cf1617b5', 'field_8ae445747a67a2a7017a8781d8dc17ca', 'field_8ae445747a67a2a7017a8781e04e17f0', 'field_8ae445747a67a2a7017a8781f09d181f', 'field_8ae445747a67a2a7017a8782a6cc1941', 'field_8ae445748375da270183f1964a0e0135', 'field_8ae445748375da270183f1a24ea40326'],
                'caract_11':['field_8ae445747a67a2a7017a8781f1f61821', 'field_8ae445747a67a2a7017a878217db186c', 'field_8ae445747a67a2a7017a878263a918e0', 'field_8ae445747a67a2a7017a87823b3018a0', 'field_8ae445747a67a2a7017a8782a6cc1941', 'field_8ae445748375da270183f1967eea0137', 'field_8ae445748375da270183f1a2a9bc033b'],
                'caract_12':['field_8ae445747a67a2a7017a8781f4411824', 'field_8ae445747a67a2a7017a878218b5186e', 'field_8ae445747a67a2a7017a878265ec18e3', 'field_8ae445747a67a2a7017a87823e0918a2', 'field_8ae445747a67a2a7017a8782ade71945', 'field_8ae445748375da270183f196c3bc013b', 'field_8ae445748375da270183f1a679bd03e2'],
                'caract_13':['field_8ae445747a67a2a7017a8781f5651827', 'field_8ae445747a67a2a7017a87821a871870', 'field_8ae445747a67a2a7017a878267d418e6', 'field_8ae445747a67a2a7017a87823f4918a4', 'field_8ae445747a67a2a7017a8782b0271947', 'field_8ae445748375da270183f1970307013d', 'field_8ae445748375da270183f1a6bf5b03e7'],
                'caract_14':['field_8ae445747a67a2a7017a8781f6ef182a', 'field_8ae445747a67a2a7017a87821b491872', 'field_8ae445747a67a2a7017a878269e318e9', 'field_8ae445747a67a2a7017a8782405318aa', 'field_8ae445747a67a2a7017a8782b3441949', 'field_8ae445748375da270183f197432a014c', 'field_8ae445748375da270183f1a70ae603eb'],
                'caract_15':['field_8ae445747a67a2a7017a8781f950182d', 'field_8ae445747a67a2a7017a87821c261874', 'field_8ae445747a67a2a7017a87826b4118ec', 'field_8ae445747a67a2a7017a878242d518ac', 'field_8ae445747a67a2a7017a8782b4db194b', 'field_8ae445748375da270183f1978510015f', 'field_8ae445748375da270183f1a7475b0404'],
                'caract_16':['field_8ae445747a67a2a7017a8781f9f11830', 'field_8ae445747a67a2a7017a87821cee1876', 'field_8ae445747a67a2a7017a87826cf018ef', 'field_8ae445747a67a2a7017a8782444118b0', 'field_8ae445747a67a2a7017a8782b613194d', 'field_8ae445748375da270183f197f2c6016a', 'field_8ae445748375da270183f1a785e6040a'],
                'caract_17':['field_8ae445747a67a2a7017a8781faaf1833', 'field_8ae445747a67a2a7017a87821db41878', 'field_8ae445747a67a2a7017a8782705718f2', 'field_8ae445747a67a2a7017a878245bf18b2', 'field_8ae445747a67a2a7017a8782b89f194f', 'field_8ae445748375da270183f198236f016d', 'field_8ae445748375da270183f1a7c30d0415'],
                'caract_18':['field_8ae445747a67a2a7017a8781fd4d1836', 'field_8ae445747a67a2a7017a87821fa0187a', 'field_8ae445747a67a2a7017a878271e818f5', 'field_8ae445747a67a2a7017a878248ae18b4', 'field_8ae445747a67a2a7017a8782ba171951', 'field_8ae445748375da270183f198a0b00172', 'field_8ae445748375da270183f1a7fc7c0428'],
                'caract_19':['field_8ae445747a67a2a7017a8781ff5b1839', 'field_8ae445747a67a2a7017a8782207d187c', 'field_8ae445747a67a2a7017a878273b918f8', 'field_8ae445747a67a2a7017a878249be18b8', 'field_8ae445747a67a2a7017a8782bb5f1953', 'field_8ae445748375da270183f1992d7c01a4', 'field_8ae445748375da270183f1a8b8f30432'],
                'caract_20':['field_8ae445747a67a2a7017a878201e9183c', 'field_8ae445747a67a2a7017a8782215d187e', 'field_8ae445747a67a2a7017a8782761818fb', 'field_8ae445747a67a2a7017a87824b8118ba', 'field_8ae445747a67a2a7017a8782bdf91955', 'field_8ae445748375da270183f19a100801b7', 'field_8ae445748375da270183f1a8fdd70438'],
                'caract_21':['field_8ae445747a67a2a7017a878202f1183f', 'field_8ae445747a67a2a7017a878222511880', 'field_8ae445747a67a2a7017a8782775118fe', 'field_8ae445747a67a2a7017a87824e1818bc', 'field_8ae445747a67a2a7017a8782bf591957', 'field_8ae445748375da270183f19a442e01bb', 'field_8ae445748375da270183f1a9f4860447'],
                'caract_22':['field_8ae445747a67a2a7017a878205501842', 'field_8ae445747a67a2a7017a8782231b1882', 'field_8ae445747a67a2a7017a8782791d1901', 'field_8ae445747a67a2a7017a87824f1d18c2', 'field_8ae445747a67a2a7017a8782c09c1959', 'field_8ae445748375da270183f19a8d5601be', 'field_8ae445748375da270183f1a9612b0444'],
                'caract_23':['field_8ae445747a67a2a7017a8782066c1845', 'field_8ae445747a67a2a7017a878224f91884', 'field_8ae445747a67a2a7017a87827b3b1904', 'field_8ae445747a67a2a7017a8782502f18c4', 'field_8ae445747a67a2a7017a8782c2fa195b', 'field_8ae445748375da270183f19acaf501d2', 'field_8ae445748375da270183f1aa7d4d044b'],
                'caract_24':['field_8ae445747a67a2a7017a8782080b1848', 'field_8ae445747a67a2a7017a878225c31886', 'field_8ae445747a67a2a7017a87827c491907', 'field_8ae445747a67a2a7017a8782519618c8', 'field_8ae445747a67a2a7017a8782c475195f', 'field_8ae445748375da270183f19b15b601e0', 'field_8ae445748375da270183f1b00edc0517'],
                'caract_25':['field_8ae445747a67a2a7017a878208de184b', 'field_8ae445747a67a2a7017a878226921888', 'field_8ae445747a67a2a7017a87827d80190a', 'field_8ae445747a67a2a7017a8782534018ca', 'field_8ae445747a67a2a7017a8782c78a1961', 'field_8ae445748375da270183f19b5e6d01e3', 'field_8ae445748375da270183f1b05a240525'],
                'caract_26':['field_8ae445747a67a2a7017a87820bf4184e', 'field_8ae445747a67a2a7017a8782276b188a', 'field_8ae445747a67a2a7017a87827f84190d', 'field_8ae445747a67a2a7017a878254fe18cc', 'field_8ae445747a67a2a7017a8782cadb1963', 'field_8ae445748375da270183f19ba6de020e', 'field_8ae445748375da270183f1b05a240525'],
                'caract_27':['field_8ae445747a67a2a7017a87820cf71851', 'field_8ae445747a67a2a7017a87822c16188c', 'field_8ae445747a67a2a7017a878281bc1910', 'field_8ae445747a67a2a7017a8782567e18ce', 'field_8ae445747a67a2a7017a8782ccc31965', 'field_8ae445748375da270183f19bd8ad0210', 'field_8ae445748375da270183f1b0eb2b053f'],
                'caract_28':['field_8ae445747a67a2a7017a87820e151854', 'field_8ae445747a67a2a7017a87822cfe188e', 'field_8ae445747a67a2a7017a878283511913', 'field_8ae445747a67a2a7017a8782578a18d0', 'field_8ae445747a67a2a7017a8782d0601967', 'field_8ae445748375da270183f19c2afe0220', 'field_8ae445748375da270183f1b140e50560'],
                'caract_29':['field_8ae445747a67a2a7017a87820fff1857', 'field_8ae445747a67a2a7017a87822dd91890', 'field_8ae445747a67a2a7017a878285bd1916', 'field_8ae445747a67a2a7017a87825ac518d2', 'field_8ae445747a67a2a7017a8782d2461969', 'field_8ae445748375da270183f19c5b4d0224', 'field_8ae445748375da270183f1b1a1290568'],
                'caract_30':['field_8ae445747a67a2a7017a878210ca185a', 'field_8ae445747a67a2a7017a87822ead1892', 'field_8ae445747a67a2a7017a878287ef1919', 'field_8ae445747a67a2a7017a87825bdb18d4', 'field_8ae445747a67a2a7017a8782d52b196b', 'field_8ae445748375da270183f19d4a9f022d', 'field_8ae445748375da270183f1b1e0da0577'],
                'caract_31':['field_8ae445747a67a2a7017a878215721866', 'field_8ae445747a67a2a7017a87822f841894', 'field_8ae445747a67a2a7017a87828a33191c', 'field_8ae445747a67a2a7017a87825cfc18d6', 'field_8ae445747a67a2a7017a8782d67d196d', 'field_8ae445748375da270183f19d8378023c', 'field_8ae445748375da270183f1b22b69057c'],
                'caract_32':['field_8ae445747a67a2a7017a8782129d1860', 'field_8ae445747a67a2a7017a878232421896', 'field_8ae445747a67a2a7017a87828d4f191f', 'field_8ae445747a67a2a7017a87825dfa18d8', 'field_8ae445747a67a2a7017a8782d7dd196f', 'field_8ae445748375da270183f19e714f027e', 'field_8ae445748375da270183f1b2639c057f'],
                'caract_33':['field_8ae445747a67a2a7017a878213601863', 'field_8ae445747a67a2a7017a878233271898', 'field_8ae445747a67a2a7017a87828f6c1922', 'field_8ae445747a67a2a7017a8782604c18da', 'field_8ae445747a67a2a7017a8782dafe1971', 'field_8ae445748375da270183f19de1420256', 'field_8ae445748375da270183f1b2e26905a0'],
                'caract_34':['field_8ae445747a67a2a7017a878216bc1869', 'field_8ae445747a67a2a7017a87823853189a', 'field_8ae445747a67a2a7017a8782917d1925', 'field_8ae445747a67a2a7017a8782618218dc', 'field_8ae445747a67a2a7017a8782dc571973', 'field_8ae445748375da270183f19f351e0297', 'field_8ae445748375da270183f1b370a605a8'],
                'caract_35':['field_8ae445747a67a2a7017a878211b1185d', 'field_8ae445747a67a2a7017a878239f8189c', 'field_8ae445747a67a2a7017a878293171928', 'field_8ae445747a67a2a7017a8782628018de', 'field_8ae445747a67a2a7017a8782df651975', 'field_8ae445748375da270183f19f6f580299', 'field_8ae445748375da270183f1b3aacd05d4'],
                }

            return {'status': 'OK', 'check_title_red': check_title_red, 'title_pd_red': title_pd_red}            
        else:
            return {'status': 'ERROR', 'error': 'Erro ao carregar a estrutura do PD!'}            
    except:
        return {'status': 'ERROR', 'error':'Erro ao carregar a estrutura do PD!"'}


def load_pd_form(self, row):
    carac = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][0]).get_attribute("value") #carac_1
    comp_desc_curta = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][1]).is_selected() #comp_desc_curta_1
    # sim_nao = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][4]).get_attribute("value") #sim_nao_1
    desc_manual = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][3]).is_selected() #desc_manual_1
    mais_conteudo = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][4]).is_selected() #mais_conteudo_1
    # possui_separador = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][5]).is_selected() #possui_separador_1
    separador = self.browser.find_element(By.ID, self.id_campo_form[f'caract_{row+1}'][6]).get_attribute("value") #separador_1

    return carac, comp_desc_curta, desc_manual, mais_conteudo, separador


def update_pd_form(self, chb_title_red, title_red, carac, comp_desc_curta, desc_manual, mais_conteudo, sim_nao, possui_separador, separador, row):
    try:        
        self.browser.execute_script(f"document.getElementById('field_8ae445747a67a2a7017a8781e2c71807').checked = '{str(chb_title_red).replace('True', 'yes').replace('False', '')}'") #chb_titulo_red
        self.browser.execute_script(f"document.getElementById('field_8ae445747a67a2a7017a8781e1f41802').value = '{title_red}'") #titulo_pd_red
                
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][0]}').value = '{carac}'") #carac_1
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][1]}').checked = '{comp_desc_curta}'") #comp_desc_curta_1
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][2]}').value = '{sim_nao}'") #sim_nao_1        
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][3]}').checked = '{desc_manual}'") #desc_manual_1
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][4]}').checked = '{mais_conteudo}'") #mais_conteudo_1
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][5]}').checked = '{possui_separador}'") #possui_separador_1
        self.browser.execute_script(f"document.getElementById('{self.id_campo_form[f'caract_{row+1}'][6]}').value = '{separador}'") #separador_1
        
    except:
        self.st_rev_pd = "ERRO"
        

def close_softexpert(self):
    try:
        self.browser.switch_to.window(self.window_principal)
        windows = self.browser.window_handles
        for window in windows:
            self.browser.switch_to.window(window)
            self.browser.close()
    except:
        pass

    