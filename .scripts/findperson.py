import requests
import os

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

