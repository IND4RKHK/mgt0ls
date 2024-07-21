import requests

def legible(json):
    
    
    if "," in json or "}" in json:
        
        
        json=json.replace("{","")
        json=json.replace("}","")
        json=json.replace(",","\n\n")
        json=json.replace('"','')
        json=json.replace("[", "")
        json=json.replace("]", "")
        json=json.upper()
        
        return json
        
    else:
        return "\n[ERROR] NO JSON\n"
        


    
try:
    
    numero=input("Ingresa el numero de telefono: ")
    
    while len(numero) < 9 or len(numero) > 9:
        
        numero=input("Ingresa el numero de telefono: ")
        
except:
    pass
            
else:
    
    try:
        consulta=requests.get("https://api-lipiapp.lipigas.cl/wapi/no_auth/usuarios/terminos/{}".format(numero))
        
        consulta_n=requests.get("https://api-lipiapp.lipigas.cl/wapi/clientes?telefono={}&pais=cl&segmento=1".format(numero))
                            
        print("\n"+legible(consulta.text)+"\n"+legible(consulta_n.text)+"\n")
    
    except:
        print("\n[ERROR] NO CONECTION 404\n")
        
    input("Presiona enter para continuar...")