#leer y mostrar un archivo de texto linea a linea
#crea un archivo notas.txt con varias lineas de texto
#escribe un script que abra notas.txt en modo lectura y muestre cada linea numerada)
#si el archivo no existe, captura la excepcion FileNotFoundError

print('TITULOS EN CARTELERA\n')
try:
    with open("notas.txt", "r") as f:
        for i, linea in enumerate(f, start=1):
            print(f"{i}: {linea.strip()}")
except FileNotFoundError:
    print("Los titulos no se encuentran actualmente, por favor intente mas tarde")    



#f significa file

