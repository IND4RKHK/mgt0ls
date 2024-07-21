import requests

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