n = input("Ingrese un número entre 1 y 10: ")  
m = int(input("Ingrese la línea que quiere ver (0 a 10): "))  

nombre = "tabla-n.txt".replace("n", n)  

try:  
    
    file = open(nombre, "r")  
    lineas = file.readlines() 
    file.close() 

    
    if 0 <= m < len(lineas):  
        print(lineas[m].strip()) 
    else:  
        print("Número de línea fuera de rango.")  
except FileNotFoundError:  
    print("El archivo no existe.")