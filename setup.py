import os
import time
from sys import platform

ROOT = {"root": os.getcwd(), "lang": "es"}

temp = "█"
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
            "python3",
            "apktool"

        ]

        modules = [

            "aspose-words",
            "beautifulsoup4",
            "requests",
            "pyzipper",
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
            except Exception as err:
                print(err)
                exit(0)

        print("""
╔════════════════════════════════════════════╗
║               [PASS] MGT0L$                ║
║      Se ha instalado correctamente...      ║
╚════════════════════════════════════════════╝
╔════════════════════════════════════════════╗
║                   [USOS]                   ║
╠════════════════════════════════════════════╣
║   ___         [ADVERTENCIA]                ║
║  (o,o)                                     ║
║  { " } :: Usalo bajo tu responsabilidad.   ║ 
║  -"-"-                                     ║
║ python3 fsh.py --h  =>> Uso con parámetros ║
║ python3 fsh.py lang_cfg => Change language ║
╚════════════════════════════════════════════╝
""")
except Exception as err:
    print(f"[ERROR] {err}")
