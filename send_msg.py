# Autor: Fidencio José Perez Alcanteres de la Guardia

import pyautogui as pg, webbrowser as web, time as tm
from random import randint
import keyboard

# Nota imporatnte: debe estar abierto tu ws en el navegador predeterminado

#-----------------------------------
# Variables

tiempo_de_espera_para_que_cargue_la_pagina = 5 # El tiempo depende de tu internet
numero_de_telefono = "+51941014571" #<- spameen ese numero
numero_de_mensajes = 100 # No exageres, porque no tiene boton de pausa

mensaje_a_mandar = ["a"] # Es un arreglo de mensajes, del cual se envian mensajes aleatoriamente
#-----------------------------------

web.open(f"https://web.whatsapp.com/send?phone={numero_de_telefono}")

tm.sleep(tiempo_de_espera_para_que_cargue_la_pagina)

for i in range(1,numero_de_mensajes):

    numero_random = randint(0,len(mensaje_a_mandar)-1)
    pg.write(mensaje_a_mandar[numero_random])
    pg.press("enter")
    # Esto aun no tiene un boton de pausa, pero pronto lo tendra ;3... espero
