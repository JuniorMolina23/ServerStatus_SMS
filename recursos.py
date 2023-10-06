#!/usr/bin/python

import psutil
from whatapi import send_sms, validator

def check_resources():
    mensaje_enviado = False
    try:
        with open("status_message.txt", "r") as archivo_estado:
            mensaje_enviado = archivo_estado.read() == "True"
    except FileNotFoundError:
        pass
    
    cpu = psutil.cpu_percent(interval=0.5)
    memory = psutil.virtual_memory().percent

    umbral = 90
    
    if cpu > umbral or memory > umbral:
        if not mensaje_enviado:
            mensaje = f"Los recursos del servidor superaron el {umbral}%:\n CPU al {cpu}%\n Memoria al {memory}%"
            send_sms(mensaje)
            validator("True")
    else:
        validator("False")
    

if __name__ == "__main__":
    check_resources()