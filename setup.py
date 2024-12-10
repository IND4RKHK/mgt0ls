import os
from sys import platform

ROOT = os.getcwd()

with open(".root", "w", encoding="utf-8") as cook_k:
    cook_k.write(ROOT)

print("[INSTALLING] Instalando modulos necesarios...")

kl_l = [

    "php",
    "pip",
    "zip",
    "python3"

]

modules = [

    "aspose-words",
    "beautifulsoup4",
    "requests",
    "pyzipper",
    "tabulate"
    
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
[PASS] MGT0L$ Se ha instalado correctamente...
----------------------------------------------
[USOS]

python3 shell.py   =>> Menu de herramientas

python3 fsh.py --h =>> Uso mediante parametros

----------------------------------------------
""")
