import zipfile
#import zipfile36 as zipfile 

# #Descomentar en caso de ser incompatible con version python

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


         

#zipfile.extract(asca,asaf,)