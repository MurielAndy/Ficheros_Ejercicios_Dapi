def cargar_pib(archivo):
    
    with open(archivo, 'r', encoding='utf-8') as archivo_pib:
        lineas = archivo_pib.readlines()

    años = lineas.pop(0).strip().split('\t')[1:]  
    pib = {linea.split(',')[1].strip(): dict(zip(años, linea.strip().split('\t')[1:])) 
           for linea in lineas if ',' in linea}

    return pib

def mostrar_pib(pib, pais):
    
    if pais in pib:
        print("\nPIB per cápita de", pais)
        for año, valor in pib[pais].items():
            print(año, ":", valor)
    else:
        print("No hay datos para", pais)


pib = cargar_pib("estat_sdg_08_10.tsv")
 
mostrar_pib(pib, input("Ingrese el código del país (ej. ES, FR, DE): ").upper())
