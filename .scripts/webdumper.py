import requests
from tabulate import tabulate

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
        exit(0)

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

        finder = requests.get(url_100, timeout=8)

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
