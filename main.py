from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from app import Ui_MainWindow

import sys
import random

import time
class MainApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
       
        

        self.reset()
        
            
        self.actionClose.triggered.connect(self.close)
        self.actionReset.triggered.connect(self.reset)
            
        
    def reset(self):
    # Reiniciar contador de parejas
        self.parelles = 0

        # Reiniciar tiempo
        self.start = time.time()
        self.timeResultat.setText("")

        # Limpiar el diccionario de cartas actuales
        self.listaDeCartasActuales = {}

        # Generar una nueva lista de IDs para las cartas y barajar
        lineaID = "1,2,3,4,5,6,1,2,3,4,5,6"
        llistaID = lineaID.split(",")
        random.shuffle(llistaID)

        # Asignar IDs a los botones y restaurar su estado
        listaBotones = [
            (self.card_1, llistaID[0]), (self.card_2, llistaID[1]),
            (self.card_3, llistaID[2]), (self.card_4, llistaID[3]),
            (self.card_5, llistaID[4]), (self.card_6, llistaID[5]),
            (self.card_7, llistaID[6]), (self.card_8, llistaID[7]),
            (self.card_9, llistaID[8]), (self.card_10, llistaID[9]),
            (self.card_11, llistaID[10]), (self.card_12, llistaID[11])
        ]

        # Configurar cada botón
        for boton, id in listaBotones:
            # Restaurar botón activo
            boton.setEnabled(True)

            # Establecer ícono predeterminado
            iconoQuestions = QIcon()
            iconoQuestions.addFile(":/img/questions.jpg")
            boton.setIcon(iconoQuestions)
            boton.setIconSize(boton.size())

            # Desconectar señales antiguas para evitar múltiples conexiones
            try:
                boton.clicked.disconnect()
            except TypeError:
                pass  # Si no hay conexiones previas, no pasa nada

            # Conectar nuevamente la señal del botón
            boton.clicked.connect(lambda _, b=boton, id=id: self.accionAlButton(b, id))

            
        
    def accionAlButton(self, button,id):
        
        
        if len(self.listaDeCartasActuales) == 2:
            return
        
        icono = QIcon()
        icono.addFile(f":/img/{id}.jpg")
        
        iconoQuestions = QIcon()
        iconoQuestions.addFile(f":/img/questions.jpg")
        button.setIcon(icono)
        button.setIconSize(button.size())
        
        button.setEnabled(False)
        
      
        
        self.listaDeCartasActuales.update({button: id})        
        if len(self.listaDeCartasActuales) == 2:
            id1 = list(self.listaDeCartasActuales.values())[0]
            id2 = list(self.listaDeCartasActuales.values())[1]
            
            if id1 == id2:
                self.listaDeCartasActuales.clear()
                self.parelles += 1
                time.sleep(0.002)
                
                if self.parelles == 6:
                    end = time.time()

                    transcurrido = end - self.start
                    hours, remainder = divmod(transcurrido, 3600)
                    minutes, seconds = divmod(remainder, 60)
                    self.timeResultat.setText(f"Temps total {int(hours):02}:{int(minutes):02}:{int(seconds):02}")                    
                    return
            else:
                QTimer.singleShot(1000, self.resetIncorrectas)
                


    def resetIncorrectas(self):
        iconoQuestions = QIcon()
        iconoQuestions.addFile(f":/img/questions.jpg")
        for b in self.listaDeCartasActuales.keys():
            b.setIcon(iconoQuestions)
            b.setIconSize(b.size())
            b.setEnabled(True)
        self.listaDeCartasActuales.clear()
        
        
        
        
        
app =  QApplication([])
window = MainApp()
window.show()


app.exec_()