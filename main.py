from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from app import Ui_MainWindow

import sys
import random

class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.listaDeCartasActuales = []
        lineaID = "1,2,3,4,5,6,1,2,3,4,5,6"
        llistaID = lineaID.split(",")
        
        random.shuffle(llistaID)
        print(llistaID)
        
        listaBotones = {}
        

        #Agg los botones a la lista
        
        
        listaBotones = [(self.card_1, llistaID[0]),(self.card_2, llistaID[1]),(self.card_3, llistaID[2]),(self.card_4, llistaID[3]),(self.card_5, llistaID[4]),(self.card_6, llistaID[5]),(self.card_7, llistaID[6]),(self.card_8, llistaID[7]),(self.card_9, llistaID[8]),(self.card_10, llistaID[9]),(self.card_11, llistaID[10]),(self.card_12, llistaID[11])]
        
        for boton,id in listaBotones:
            boton.clicked.connect(lambda _, b=boton, id=id: self.accionAlButton(b,id))
            #Agregar un icono a los botones
            
        
    def accionAlButton(self, button,id):
        
        icono = QIcon()
        icono.addFile(f":/img/{id}.jpg")
        
        iconoQuestions = QIcon()
        iconoQuestions.addFile(f":/img/questions.jpg")
        button.setIcon(icono)
        button.setIconSize(button.size())
        
        
        self.listaDeCartasActuales.append(id)
        
        if len(self.listaDeCartasActuales) == 2:
            
            if self.listaDeCartasActuales[0] == self.listaDeCartasActuales[1]:
                print("Correcto")
            else:
                print("Incorrecto")
                button.setIcon(iconoQuestions)
                
            self.listaDeCartasActuales.clear()
        
        button.setEnabled(False)
        
        
        
        
app =  QApplication([])
window = MainApp()
window.show()
app.exec_()