import aspose.words as aw

def integracion():

    # Load Word document.
    doc = aw.Document(ruta)
    leer=open(macro)

    # Create VBA project
    project = aw.vba.VbaProject()
    project.name = "MacroProject"
    doc.vba_project = project

    # Create a new module and specify a macro source code.
    module = aw.vba.VbaModule()
    module.name = "MacroModule"
    module.type = aw.vba.VbaModuleType.PROCEDURAL_MODULE
    module.source_code = leer.read()

    # Add module to the VBA project.
    doc.vba_project.modules.add(module)

    # Save document.
    doc.save(ruta_save)


try:

    ruta=input("Ingresa la ruta de tu documento [.docm]: ")

    while len(ruta) < 0 or ".docm" not in ruta:
        ruta=input("Ingresa la ruta de tu documento [.docm]: ")

    macro=input("Introduce la ruta de tu macro: ")

    while len(macro) < 0:
        macro=input("Introduce la ruta de tu macro: ")
    
except:
    pass

else:
    try:
        ruta_save=ruta.replace(".docm","_2.docm")
        integracion()
    except:
        pass
    else:
        print("[WORD INFECTADO] ===> {}".format(ruta_save))
