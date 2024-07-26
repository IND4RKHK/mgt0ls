import os
import platform

class color:

    OK="\033[92m"
    AL="\033[93m"
    BD="\033[91m"
    NM="\033[0m"

    MG="\033[96m"


SYS=platform.system().lower()
BASE=os.getcwd()

def ayuda():
    for word in scripts_h:

        if "]\n" in word:
            print(color.MG+f"{word}".upper()+color.OK)
        else:
            print("{}".format(word).upper())

def update():
    
    import requests
    try:
        ver_base=open("shell.py")
        ver_base_all=ver_base.read()

        ver=requests.get("https://raw.githubusercontent.com/IND4RKHK/mgt0ls/main/shell.py")

        if ver.text == ver_base_all:
            print("[UPDATED] MGT0L$ ESTA ACTUALIZADO c:")
        else:

            print("[UPDATE] MGT0L$ TIENE UNA ACTUALIZACION DISPONIBLE!!")
            """
            try:
                up_str=input("[UPDATE] ACTUALIZAR MGT0LS? [S/N]: ").lower()

                while up_str != "s" and up_str != "n":
                    up_str=input("[UPDATE] ACTUALIZAR MGT0LS? [S/N]: ").lower()
            except:
                pass
            else:
                print("[PROCESS] IN PROCESS >") # Paths And Shell Commands to delete files and download new version
            """
    except:
        pass

######################################################## update() IN PROCESS ####################################################################

#base=str(os.get_exec_path())

scripts_dir=".scripts/"

scripts_h=[

    "\n[COMANDOS]--->> mgt0L$.py <<---[VERSION-2.1]\n",
    "findtl      [palabra clave] busca herramientas por palabras clave. ",
    "help        muestra todas las interacciones disponibles en mgtols.",
    "update      verifica si hay una nueva version disponible de mgt0l$.",
    "exit        termina la sesion de mgt0l$.",
    "\n[DOXING TOOLS]\n",
    ">seeker     recopila infromacion con nombres de usuario.",
    ">findperson busca informacion de personas por sus nombres [genealog].",
    ">iplocate   geolocaliza direcciones ip detalladamente.",
    ">lopiapi    prueba con un numero de telefono [CL].",
    "\n[SCAM TOOLS]\n",
    ">sc4pk      crea un archivo apk que se usa como scam permanente.",
    "\n[MALWARE TOOLS]\n",
    ">macromaker crea una macro para word dependiendo de tu especificacion [office].",
    ">wordinfect agrega macro infectada a un documento de word [docm].",
    ">reverhttp  controla una maquina mediante http y solicitudes post [php].",
    "\n[DDOS TOOLS]\n",
    ">icmpdos    realiza ataque ddos con protocolo icmp.",
    ">httpflood  sobrecarga un servidor enviando solicitudes falsas [http-flood].",
    "\n[VECTOR TOOLS]\n",
    ">ftpbrute   realiza ataques de diccionario a servidores ftp.",
    ">unzipper   realiza ataque de diccionario a compresiones [zip].",
    ">tempmail   email temporal basado en mailnesia.\n"

]

execute_s={

    "seeker":"seeker.py",
    "icmpdos":"icmpdos.py",
    "lopiapi":"lopiapi.py",
    "unzipper":"unzipper.py",
    "tempmail":"tempmail.py",
    "wordinfect":"wordinfect.py",
    "macromaker":"macromaker.py",
    "findperson":"findperson.py",
    "reverhttp":"reverseatak.py",
    "iplocate":"iplocate.py",
    "sc4pk":"sc4pk.py",
    "httpflood":"httpflood.py",
    "ftpbrute":"ftpbrute.py"

}

ayuda()
while True:

    try:
        shell=input(color.BD+"mgt0l$->>"+color.AL).lower()

    except:
        pass

    else:

        if execute_s.get(shell) != None:

            if shell == "reverhttp":

                os.chdir(scripts_dir+"reversehttp/")
                os.system("python3 {}".format(execute_s.get(shell)))
                os.chdir(BASE)
            
            elif shell == "sc4pk":

                os.chdir(scripts_dir+"sc4pk/")
                os.system("python3 {}".format(execute_s.get(shell)))
                os.chdir(BASE)

            else:
                os.system("python3 {}{}".format(scripts_dir,execute_s.get(shell)))

            #os.system("python3 {}{}".format(scripts_dir,execute_s.get(shell)))
        
        elif "findtl" in shell:
            si=False
            busca=shell.replace("findtl ", "")

            for clave in scripts_h:
                if busca in clave:
                    si=True
                    print(clave.upper())
            
            if si != True:
                print("[FINDTL] NADA")
            

        elif shell == "exit" or shell == "quit":
            exit(0)
        
        elif shell == "update":
            update()

        else:

            if shell == "help":

                if SYS == "windows":
                    os.system(shell)
                ayuda()

            else:

                os.system(shell) # ESTE SHELL SE ENCARGA DE EJECUTAR COMANDOS SI NO SON HELP

