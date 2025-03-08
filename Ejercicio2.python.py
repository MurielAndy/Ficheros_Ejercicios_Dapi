n = input("Ingrese un número entre 1 y 10: ")  

nombre = "tabla-n.txt".replace("n", n)  

try:  
    
    file = open(nombre, "r")  
    print(file.read())
    file.close() 
except FileNotFoundError:  
    
    print("El archivo no existe.")