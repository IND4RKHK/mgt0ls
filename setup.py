import os
import time
from subprocess import getoutput
from sys import platform

ROOT = {"root": os.getcwd(), "lang": "es"}

temp = "█"
apt_err = []
mod_comm = []

try:
    for i in range(50):

        if "win" in platform:
            os.system("cls")
        else:
            os.system("clear")

        print("""
[AVISO LEGAL Y DESCARGO DE RESPONSABILIDAD]

Este software ha sido desarrollado exclusivamente con fines educativos, de
investigación y pruebas autorizadas de penetración en entornos controlados. No
se promueve ni respalda su uso indebido o ilegal.

El usuario es el único responsable de su uso, que debe cumplir con las leyes
aplicables y realizarse únicamente en entornos donde tenga autorización expresa.
Los desarrolladores no se hacen responsables de daños directos o indirectos
derivados del uso indebido del software.

Se proporciona "tal cual", sin garantías de ningún tipo.
Si no está de acuerdo con estos términos, absténgase de utilizarlo.

""")
        
        print("[LOADING]", f"{temp}> 100%" if i == 50 else f"{temp}> {(i+1)*2}%")
        temp = temp + "█"
        time.sleep(0.2)

    select = input("\n[USAGE] ¿Acepto usar el software de acorde al texto anterior? [Y/n]: ")

    if select.lower() == "y":

        print("\n[INSTALLING] Instalando modulos necesarios...")

        with open(".root", "w", encoding="utf-8") as cook_k:
            cook_k.write(str(ROOT).replace("'", '"'))

        kl_l = [

            "php",
            "pip",
            "zip",
            "apktool"

        ]

        modules = [

            "aspose-words",
            "beautifulsoup4",
            "Flask",
            "requests",
            "pyzipper",
            "paramiko",
            "tabulate",
            "StringGenerator",
            "googletrans",
            "colorama"
            
        ]

        if "win" in platform:
            try:
                for one in modules:
                    os.system(f"pip install {one}")

            except Exception as err:
                print(err)
                exit(0)
        else:
            try:
                for inst in kl_l:
                    os.system(f"apt-get install {inst} -y")
                for one in modules:
                    os.system(f"pip install {one} --break-system-packages")
                
                # Lista de paquetes instalados
                apt_pack = getoutput("apt list")

                for package_ in kl_l:
                    
                    # Si el package no esta instalado
                    if package_ not in apt_pack:
                        apt_err.append(package_)

            except Exception as err:
                print(err)
                exit(0)

        list_ = getoutput("pip list")

        # Se listan los modulos y se guaran los que no estan instalados
        for mod_ in modules:
            if mod_ not in list_:
                mod_comm.append(mod_)

        print("""
   ...    *    .   _  .
*  .  *     .   * (_)   *
  .      |*  ..   *   ..     :: DEV BY =>> [ HKNX ] ↓
   .  * \|  *  ___  . . *
*   \/   |/ \/{o,o}     .    [ https://ytub.ee/IND4RKHK ]
  _\_\   |  / /)  )* _/_ *
      \ \| /,--"-"---  ..
_-----`  |(,__,__/__/_ .      
       \ ||      ..
        ||| .            *    
        |||
        |||         $hell-root >> python3 fsh.py --help
  , -=-~' .-^- _
           `
[PASS] MGT0LS Se ha instalado correctamente   =>>  [OK]
-------------------------------------------------------
:: Script desarrollado como historial de aprendizaje ::
""")


        if apt_err != [] or mod_comm != []:

            print(" __________________________ \n[INFORME DE INSTALACION </>]\n ────────────────────────── \n")

            if "win" not in platform and apt_err != []:

                for package_ in apt_err:
                    print(f"[ERROR] El paquete {package_} no se logro instalar correctamente [apt-get install {package_}]")
                        
            # Verificando instalacion de modulos python correcta
            if mod_comm != []:

                with open("__prog__fast__.py", "r", encoding="utf-8") as moded_mg:
                    file_read = moded_mg.read()

                    for element in mod_comm:
                        moded_mg.seek(0)
                        print(f"[ERROR] El modulo {element} no se logro instalar correctamente [pip install {element} --break-system-packages]")
                        
                        for line in moded_mg:

                            # Una vez se
                            if "import" in line and element in line:
                                file_read = file_read.replace(line, "# "+line)
                                continue

                    with open("__prog__fast__.py", "w", encoding="utf-8") as save_mg:
                        save_mg.write(file_read)

            print("[INFO] Verifica la estabilidad del los paquetes para tu entorno ↓\n[SOLVED] Se han comentado las librerias confilctivas ...")

except Exception as err:
    print(f"[ERROR] {err}")