from PySide6.QtWidgets import QMessageBox, QInputDialog,  QLineEdit
from PySide6.QtCore import Qt

def MsgQuestion(msg_info, backgroundcolor="rgb(240, 240, 240)"): 
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")
    msg.setIcon(QMessageBox.Question)    
    msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
    msg.setButtonText(QMessageBox.Yes, 'Sim')
    msg.setButtonText(QMessageBox.No, 'Não')
    
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')
    
    
    msg.setMinimumSize(400, 200)
    #Comando para alinhar os botões da MSG --> QDialogButtonBox { qproperty-centerButtons: true; }
   
    resp = msg.exec() 

    return resp
    


def MsgErro(msg_info, backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")    
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Critical)
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')
    
    msg.setMinimumSize(300, 300)  # Definir tamanho mínimo
    msg.resize(300, 300)
    
    msg.exec()
    
def MsgWarning(msg_info, backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")    
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Warning)
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')
    
    msg.setMinimumSize(300, 300)  # Definir tamanho mínimo
    msg.resize(300, 300)
    
    msg.exec()

def MsgCancelado(backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText("Processo cancelado pelo usuário!")
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')
    
    msg.setIcon(QMessageBox.Warning)
    msg.exec()

def MsgFinalizado(msg_info, backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')
    
    msg.setIcon(QMessageBox.Information)
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec()

def MsgAlteracao(msg_text, msg_info, msg_icon, backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    if msg_icon == 'Information':
        msg.setIcon(QMessageBox.Information)
    else:
        msg.setIcon(QMessageBox.Critical)

    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')

    msg.StandardButton(QMessageBox.Ok)
    msg.exec()

def MsgInformation(msg_info, backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText(f"\n    {msg_info}")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Information)

    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')         
    
    msg.exec()

def MsgInfoCodAlter(backgroundcolor="rgb(240, 240, 240)"):
    msg = QMessageBox()
    msg.setWindowTitle('Revisão PDS')
    msg.setText("Informar o Código Exceção:") 
    msg.setStandardButtons(QMessageBox.Ok)
    msg.setIcon(QMessageBox.Information)
    msg.setStyleSheet('''
                      QMessageBox{min-width: 1000px; border-style: ridge; border-width: 1px; border-color: rgb(220, 220, 220); padding: 20px;} 
                      
                      QWidget{color: rgb(0, 0, 0); font: 10pt; background-color: '''+backgroundcolor+''';}
                      
                      QLabel{padding: 0px 0px 20px 0px; color: black; font: bold 10pt "Segoe UI";}
                      
                      QPushButton{background-color: rgb(240, 240, 240); border-style: solid; border-width: 1px; border-color: rgb(200, 200, 200); border-radius: 3px; color: rgb(0, 0, 0); font: 10pt "Segoe UI"; min-width: 80px;padding: 2px 0px 2px 0px; text-align: center;} 
                      
                      QPushButton:hover {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      QPushButton:focus {background-color: rgb(235, 255, 255); border-width: 2px; border-color: rgb(0, 170, 255); border-style: outset;}
                      
                      ''')  
    msg.exec()