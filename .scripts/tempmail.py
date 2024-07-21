import requests
from bs4 import BeautifulSoup

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

                        
############################################## VER COMO HACER PARA QUE QUEDE LEGIBLE