import os
import pywhatkit as pwk
try: 
  
  # Sending a WhatsApp message to the number XXXXXX with the message "Mensaje De Prueba" at 14:30.
  pwk.sendwhatmsg("XXXXXX","Mensaje de prueba",14,30)
  
  # Killing the chrome process.
  os.system("taskkill /im chrome.exe /f")
  print("Mensaje Enviado") 

except Exception as e: 

  print("Ha ocurrido un error --> "+str(e))