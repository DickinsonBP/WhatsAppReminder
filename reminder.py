import os
import webbrowser
import pyautogui
import time
import pywhatkit as pwk
try:
  numbers = {'+number1':'name1',
            '+number2':'name2',
            '+number3':'name3',
            '+number4':'name4',
            '+number5':'name5',}
  #hour,min = time.strftime('%H:%M', time.localtime()).split(':')#return a string
  min=30
  for number,name in numbers.items():
    print("sending message to: "+name)
    # Sending a WhatsApp message to the number XXXXXX with the message "Mensaje De Prueba" at 14:30.
    pwk.sendwhatmsg(number,"Hola "+name+"! Mañana me cobran Spotify lol acuerdate de pagarme 2.5 ty :P",14,min)
    print("The message has been sent")
    min+=1
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
  
  # Killing the chrome process.
  print("Mensajes Enviado") 

except Exception as e: 

  print("Ha ocurrido un error --> "+str(e))