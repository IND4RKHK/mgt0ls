import argparse
import threading
from __prog__fast__ import *
from flask import Flask, request, render_template

def gui_mg():

    execute_def = {
        "seeker": [["Nombre usuario", "username"]],
        "icmpdos": [["IP a atacar", "ip"], ["Tamaño del paquete", "size"]],
        "lopiapi": [["Número de teléfono", "number"]],
        "unzipper": [["Ruta del diccionario", "path"], ["Ruta del archivo ZIP", "zip_path"]],
        "tempmail": [["Alias a utilizar", "alias"], ["Mensaje a leer", "email_read"]],
        "urljump": [["RRSS para generar", "url_rrss"], ["Cantidad", "cant_gen"]],
        "wordinfect": [["Ruta del archivo DOCM", "docm_path"], ["Ruta de la macro", "macro_path"]],
        "macromaker": [],
        "findperson": [["Nombre de la persona", "name"], ["Código del país", "country_code"]],
        "iplocate": [["Dirección IP", "ip"]],
        "httpflood": [["URL del servidor", "url"]],
        "ftpbrute": [["Modo de ataque", "mode"], ["Servidor FTP", "ftp_server"], ["Usuario o diccionario", "user"], ["Diccionario de contraseñas", "dict_password"]],
        "webdumper": [["Modo", "mode"], ["URL base", "url"], ["Diccionario", "dict_path"]],
        "unlocker": [["Modo de cifrado", "hash_mode"], ["Diccionario de palabras", "dict_path"], ["Hash a romper", "hash"]],
        "sc4pk": [["ID de la víctima", "follow_id"], ["Scam a usar", "scam_type"]],
        "reverhttp": [["Puerto o URL", "port_or_url"]],
        "m4cware": [],
        "shorty": [["Plataforma", "platform"], ["URL a acortar", "url"], ["Alias", "alias"]],
        "webmap": [["Página web", "url"], ["Modo", "mode"]],
        "sshforce": [["IP del servidor", "ip"], ["Puerto", "port"], ["Usuario o diccionario", "user"], ["Contraseña o diccionario", "password"]],
        "eashi": [["Ruta del archivo MHTML", "mhtml_path"]],
        "fireleak": [["Ruta del archivo APK", "apk_path"]],
        "wpscrap": [["Página web", "url"], ["Modo de escaneo", "mode"], ["Check mode", "check"]]
    }

    app = Flask(__name__)

    @app.route('/', methods=['GET', 'POST'])
    def home():
        tools_list = execute_def  # Asegúrate de obtener la lista de herramientas

        if request.method != 'POST':
            return render_template("menu.html", section_ = "selection", lista_ = tools_list)
        
        if request.form["use_button"] == "use":
            # Obtenemos la herramienta seleccionada en el post
            selected_tool = request.form['tools']

            # Retornamos la seccion del codigo que activaremos y su herramienta seleccionada para ser leidos
            return render_template(
                "menu.html",
                section_ = "form_dict", # Enviamos la seccion a la cual pertenecera el formulario
                name_tool = selected_tool, # Enviamos el nombre de la herramienta seleccionada
                tool_ = tools_list[selected_tool], # Y enviamos los Place holders y Names contenidos en la lista
                descrip_tool = execute_s[selected_tool][2].replace("<", "").replace(">", "").replace("\n", "<br>") # Enviamos la descripcion y el modo de uso de la herramienta
                )

        # Si el usuario usa el boton en ataque
        if request.form["use_button"] == "attack":

            # Aqui obtenemos el nombre de la herramienta
            name_tool = request.form["name_tool"]

            params__ = []
            # Listamos los key y obtenemos el valor dentro del formulario
            for elem in tools_list[name_tool]:

                # Bucle encargado de eliminar "" para que nuestro programa lo ejecute sin problemas
                elemento = request.form[elem[1]]
                if elemento == "":
                    elemento = None

                params__.append(elemento)

            call_process = globals()[name_tool]

            # Con threading ejecutamos esto en otro proceso pasandole los parametros desempaquetados
            try:
                multi_process = threading.Thread(target=call_process(*params__), daemon=True)
                multi_process.start()
                multi_process.join()
            except KeyboardInterrupt:
                pass
            except Exception as err:
                print(err)
                pass
            
            end_message = f"La herramienta {name_tool} se ha terminado de ejecutar.<br>Porfavor verifica los resultados en tu consola :)."

            # Retornamos el nombre de la herramienta ejecutada y el mensaje de finalizado
            return render_template("menu.html", section_ = "passed", name_tool=name_tool, end_message=end_message)
    
    if __name__ == '__main__':
        app.run(debug=True, use_reloader=False)

#####################################
#              Fin GUI              #
#####################################

dox_lst = []; ddos_lst = []
dic_lst = []; vec_lst = []
cmd_lst = []; mal_lst = []

execute_s = {

    "seeker": [
        seeker, 
        1, 
        "[DESCRIPCION]\nRecopila información sobre usuarios buscando en diversas fuentes web.\n\n"
        "[USO]\npython3 fsh.py seeker --a <USERNAME>\n\n"
        "[PARAMETROS]\n--a: Nombre de usuario a buscar, (obligatorio).",
        "dox"
    ],
    "icmpdos": [
        icmpdos, 
        2, 
        "[DESCRIPCION]\nRealiza un ataque DDoS utilizando paquetes ICMP.\n\n"
        "[USO]\npython3 fsh.py icmpdos --a <IP> --b <SIZE>\n\n"
        "[PARAMETROS]\n--a: Dirección IP del objetivo, (obligatorio).\n"
        "--b: Tamaño del paquete ICMP en bytes, (opcional, recomendado: 65550).",
        "ddos"
    ],
    "lopiapi": [
        lopiapi, 
        1, 
        "[DESCRIPCION]\nBusca información asociada a un número telefónico mediante APIs.\n\n"
        "[USO]\npython3 fsh.py lopiapi --a <NUMBER>\n\n"
        "[PARAMETROS]\n--a: Número telefónico, ejemplo: 983222434, (obligatorio).",
        "dox"
    ],
    "unzipper": [
        unzipper, 
        2, 
        "[DESCRIPCION]\nDescomprime archivos protegidos con contraseña mediante ataque de diccionario.\n\n"
        "[USO]\npython3 fsh.py unzipper --a <DICT_PATH> --b <PATH_ZIP>\n\n"
        "[PARAMETROS]\n--a: Ruta al diccionario de contraseñas, (obligatorio).\n"
        "--b: Ruta al archivo ZIP, (obligatorio).",
        "dic"
    ],
    "tempmail": [
        tempmail, 
        2, 
        "[DESCRIPCION]\nCrea correos temporales usando Mailnesia.\n\n"
        "[USO]\npython3 fsh.py tempmail --a <ALIAS> --b <NUMBER_MESSAGE>\n\n"
        "[PARAMETROS]\n--a: Alias del correo temporal, (obligatorio).\n"
        "--b: Número del mensaje en la bandeja, (opcional).",
        "vec"
    ],
        "urljump": [
        urljump, 
        2, 
        "[DESCRIPCION]\nGenera enlaces de invitacion aleatorios para RRSS.\n\n"
        "[USO]\npython3 fsh.py urljump --a <RRSS_TO_GEN> --b <COUNT>\n\n"
        "[PARAMETROS]\n--a: Enlace de RRSS a generar (e.g., `WA` para WhatsApp, `TG` para Telegram, `DC` para Discord, `BT` para Bit.ly, `YT` para YouTube, obligatorio).\n"
        "--b: Cantidad a generar, (obligatorio).",
        "vec"
    ],
    "wordinfect": [
        wordinfect, 
        2, 
        "[DESCRIPCION]\nInserta macros maliciosas en documentos Word habilitados para macros.\n\n"
        "[USO]\npython3 fsh.py wordinfect --a <PATH_DOCM> --b <PATH_MACRO>\n\n"
        "[PARAMETROS]\n--a: Ruta al archivo de Word, (.docm, obligatorio).\n"
        "--b: Ruta al archivo que contiene la macro, (obligatorio).",
        "mal"
    ],
    "macromaker": [
        macromaker, 
        1, 
        "[DESCRIPCION]\nCrea scripts de macros para Microsoft Word.\n\n"
        "[USO]\npython3 fsh.py macromaker\n\n"
        "[PARAMETROS]\nSin parámetros adicionales.",
        "mal"
    ],
    "findperson": [
        findperson, 
        2, 
        "[DESCRIPCION]\nObten el posible DNI de una persona.\n\n"
        "[USO]\npython3 fsh.py findperson --a <NAME> --b <A|C|C|G|M|V|ALL>\n\n"
        "[PARAMETROS]\n--a: Nombre de la persona a buscar, (obligatorio).\n"
        "--b: Código del país (e.g., `A` para Argentina, `C` para Chile, `V` para Venezuela, `C` para Colombia, `G` para Guatemala, `M` para Mexico, `B` para Bolivia, `ALL` para todos los países, obligatorio).",
        "dox"
    ],
    "iplocate": [
        iplocate, 
        1, 
        "[DESCRIPCION]\nLocaliza direcciones IP y proporciona detalles como ubicación, ISP y más.\n\n"
        "[USO]\npython3 fsh.py iplocate --a <IP>\n\n"
        "[PARAMETROS]\n--a: Dirección IP objetivo, (obligatorio).",
        "dox"
    ],
    "httpflood": [
        httpflood, 
        1, 
        "[DESCRIPCION]\nSatura un servidor web enviando múltiples solicitudes HTTP.\n\n"
        "[USO]\npython3 fsh.py httpflood --a <URL>\n\n"
        "[PARAMETROS]\n--a: URL del servidor objetivo, (obligatorio).",
        "ddos"
    ],
    "ftpbrute": [
        ftpbrute, 
        4, 
        "[DESCRIPCION]\nRealiza ataques de fuerza bruta contra servidores FTP.\n\n"
        "[USO]\npython3 fsh.py ftpbrute --a <MODE> --b <FTP_sERVER> --c <USER|DICT_USER> --d <DICT_PASSWORD>\n\n"
        "[PARAMETROS]\n--a: Modo de ataque (`mul` para múltiples usuarios, `one` para un único usuario, obligatorio).\n"
        "--b: Dirección del servidor FTP, (obligatorio).\n"
        "--c: Usuario o diccionario de usuarios, (obligatorio).\n"
        "--d: Diccionario de contraseñas, (obligatorio).",
        "dic"
    ],
    "webdumper": [
        webdumper, 
        3, 
        "[DESCRIPCION]\nExplora sitios web buscando directorios y archivos ocultos.\n\n"
        "[USO]\npython3 fsh.py webdumper --a <F|S> --b <URL> --c <PATH_DICT>\n\n"
        "[PARAMETROS]\n--a: Modo (`F` para inicial, `S` para recursivo, obligatorio).\n"
        "--b: URL base (obligatorio).\n"
        "--c: Diccionario con palabras clave, (obligatorio).",
        "dic"
    ],
    "unlocker": [
        unlocker, 
        3, 
        "[DESCRIPCION]\nRompe hashes MD5 y SHA1 con fuerza bruta.\n\n"
        "[USO]\npython3 fsh.py unlocker --a <MD5|SHA1> --b <PATH_DICT> --c <HASH>\n\n"
        "[PARAMETROS]\n--a: Modo (`MD5` para cifrado md5, `SHA1` para cifrado SHA1, obligatorio).\n"
        "--b: Diccionario de palabras, (obligatorio).\n"
        "--c: Hash a romper, (obligatorio).",
        "dic"
    ],
    "sc4pk": [
        sc4pk, 
        2, 
        "[DESCRIPCION]\nGenera APK maliciosos para propagar malware.\n\n"
        "[USO]\npython3 fsh.py sc4pk --a <FOLLOW_ID> --b <IG|FB|TW|GO> | Creacion del APK.\n"
        "python3 fsh.py sc4pk --a <FOLLOW_ID> | Busqueda de victimas.\n\n"
        "[PARAMETROS]\n--a: ID asociada a tus victimas, (obligatorio).\n"
        "--b: Scam a usar (IG para Instagram, FB para Facebook, TW para Twitter, GO para Google, opcional).",
        "mal"
    ],
    "reverhttp": [
        reverhttp, 
        1, 
        "[DESCRIPCION]\nEstablece un canal remoto usando solicitudes HTTP/POST.\n\n"
        "[USO]\npython3 fsh.py reverhttp --a <PORT|URL>\n\n"
        "[PARAMETROS]\n--a: PORT Para crear un host local y URL para host externo, (obligatorio).",
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
        1,
        "[DESCRIPCION]\nConfigura el idioma de mgt0ls.\n\n"
        "[USO]\npython3 fsh.py lang_cfg --a <EN|AR|ES|ETC>\n\n"
        "[PARAMETROS]\n--a: Idioma que se utilizara permanentemente, (obligatorio).",
        "cmd"
    ],
    "check_up": [
        update,
        "None",
        "[DESCRIPCION]\nVerifica si es que mgt0ls esta actualizado.\n\n"
        "[USO]\npython3 fsh.py update",
        "cmd"
    ],
    "gui_mg": [
        gui_mg,
        "None",
        "[DESCRIPCION]\nInterfaz de mgt0ls con GUI hecha en HTML.\n\n"
        "[USO]\npython3 fsh.py gui_mg",
        "cmd"
    ],
    "shorty": [
        shorty,
        3,
        "[DESCRIPCION]\nAcortador de enlaces maliciosos.\n\n"
        "[USO]\npython3 fsh.py shorty --a <GOO|LIN|WHA|YOU|RID|TIN> --b <URL> --c <ALIAS>\n\n"
        "[PARAMETROS]\n--a: Suplantar plataforma (GOO para Google, LIN para Linkedin, WHA para WhatsApp, YOU para YouTube, RID para Ride.ee, TIN para Tin.al, obligatorio).\n"
        "--b: URL a acortar, (obligatorio).\n"
        "--c: Alias para el enlace acortado, (opcional).",
        "vec"
    ],
    "webmap": [
        webmap,
        2,
        "[DESCRIPCION]\nMapeo y escaneo de pagina web.\n\n"
        "[USO]\npython3 fsh.py webmap --a <URL> --b <ONE>\n\n"
        "[PARAMETROS]\n--a: Pagina web a escanear ej: https://example.com/, (obligatorio).\n"
        "--b: Modo (ONE: Se usa para realizar un escaneo no recursivo, opcional).",
        "dic"
    ],
    "sshforce": [
        sshforce,
        4,
        "[DESCRIPCION]\nRealiza ataques de fuerza bruta contra servidores SSH.\n\n"
        "[USO]\npython3 fsh.py sshforce --a <IP> --b <PORT> --c <USER|DICT_USER> --d <PASSWORD|DICT_PASSWORD>\n\n"
        "[PARAMETROS]\n--a: Ip del servidor (obligatorio).\n"
        "--b: Puerto del servidor (obligatorio).\n"
        "--c: Usuario o diccionario de usuarios (obligatorio).\n"
        "--d: Contraseña o diccionario de contraseñas (obligatorio).",
        "dic"
    ],
    "eashi": [
        eashi,
        1,
        "[DESCRIPCION]\nClona paginas web mediante archivos MHTML.\n\n"
        "[USO]\npython3 fsh.py eashi --a <PATH_MHTML>\n\n"
        "[PARAMETROS]\n--a: Ruta del archivo .mhtml descargado (obligatorio).",
        "vec"
    ],
    "fireleak": [
        fireleak,
        1,
        "[DESCRIPCION]\nAuditor de aplicaciones con claves de Firebase hardcodeadas.\n\n"
        "[USO]\npython3 fsh.py fireleak --a <PATH_APK>\n\n"
        "[PARAMETROS]\n--a: Ruta del archivo .apk a escanear (obligatorio).",
        "vec"
    ],
    "wpscrap": [
        wpscrap,
        3,
        "[DESCRIPCION]\nHerramienta para enumerar endpoints y realizar fuerza bruta en plugins de WordPress.\n\n"
        "[USO]\npython3 fsh.py wpscrap --a <URL> --b <SET|DIC> --c <CHECK>\n\n"
        "[PARAMETROS]\n--a: URL a escanear (obligatorio).\n"
        "--b: Modo de uso (SET para escaneo normal, DIC para escaneo por diccionario, obligatorio).\n"
        "--c: CHECK para un escaneo profundo (opcional).",
        "vec"
    ]

}

GUI_scripts = ["m4cware", "macromaker"]
MG_commands = ["update", "gui_mg"]

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


mgtols = Fore.LIGHTBLACK_EX + R"""
  __________
 / ___  ___ \     
/ / {}.{} \/ {}.{} \ \   
\ \___/\___/ /\  
 \____\/____/||  {}[ YouTube DEV ]{} ￦ {}[ mgt0l$ V2.19.2 ]{}
 /     /\\\\\//  
|     |\\\\\\    {}>{} {}https://ytub.ee/IND4RKHK{}
 \      \\\\\
   \______/\\\\  {}:: I See You ::{}
    _||_||_""".format(
        # Ojos
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,
        
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX,

        # Pre URL
        Fore.LIGHTRED_EX,
        Fore.LIGHTBLACK_EX,

        # URL
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX, 
        
        # 
        Fore.LIGHTWHITE_EX,
        Fore.LIGHTBLACK_EX) + Fore.WHITE

usage_mg_bn = """
> python3 fsh.py <nombre_de_herramienta> :: Obten ayuda respecto a tu herramienta.
> python3 fsh.py gui_mg                  :: GUI de mgt0ls en tu navegador.
> python3 fsh.py lang_cfg --a en         :: Configura el idioma a Ingles.
> python3 fsh.py update                  :: Comprueba actualizaciones de mgt0l$.

[ Estas usando mgt0l$ bajo TU RESPONSABILIDAD ] </> [ by HKNX ]

"""

scripts_h = "\n[ DOXING TOOLS ]\n" + tb_dox + "\n[ DDoS TOOLS ]\n" + tb_ddos + "\n[ BRUTE FORCE TOOLS ]\n" + tb_dic + "\n[ MALWARE TOOLS ]\n" + tb_mal + "\n[ VECTOR TOOLS ]\n" + tb_vec + "\n[ SETTINGS ]\n" + tb_cmd + "\n[ USAGE MGT0L$ ]\n" + usage_mg_bn

parse = argparse.ArgumentParser(usage=mgtols+translate(scripts_h))

parse.add_argument("tool", type=str, help="<tool_to_execute_usage>")
parse.add_argument("--a", type=str, help="<optional>")
parse.add_argument("--b", type=str, help="<optional>")
parse.add_argument("--c", type=str, help="<optional>")
parse.add_argument("--d", type=str, help="<optional>")

arguments = parse.parse_args()

try:

    # Si la funcion no se encuentra
    if arguments.tool not in globals():
        print(translate("[ERROR] Funcion no encontrada ..."))
        exit(0)
        
    # Si llaman a una herramienta que esta en GUI
    if arguments.tool in GUI_scripts:
        globals().get(arguments.tool)()

    # Si llaman a un comando de configuracion
    elif arguments.tool in MG_commands:
        print(translate(globals().get(arguments.tool)()))

    # Si la llaman a la herramienta solo para ayuda
    elif arguments.tool in execute_s and arguments.a == None:
        print(translate(execute_s[arguments.tool][2]))
    
    # Si la herramienta tiene parametros y se usa desde consola
    elif arguments.tool not in GUI_scripts and arguments.tool not in MG_commands:

        # Ejecucion de scripts #
        buffer_args = []
        for elem_x in arguments._get_kwargs():
            buffer_args.append(elem_x[1])

        # Eliminamos el primer parametro ingresado 
        buffer_args.pop(0)

        # Obtenemos la cantidad de argumentos que usa la herramienta desde la variable execute_s
        num_ = execute_s.get(arguments.tool)[1]

        # Cortamos el diccionario en el numero del argumento que se usa en la tool
        buffer_args = buffer_args[:num_] 

        # Ejecutamos desde las funciones globales los argumentos necesarios
        globals().get(arguments.tool)(*buffer_args)
    
    # Termino del programa una vez terminado los condicionales
    exit(0)

except TypeError:
    if arguments.tool != "gui_mg":
        print(translate(f"[ERROR] No colocaste todos los parametros en {arguments.tool} ..."))

except Exception as err:
    print(translate(f"[ERROR] {err}"))