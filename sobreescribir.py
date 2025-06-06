'''1. **Sobrescribir un archivo de texto y luego añadir contenido**
- Crea (o sobrescribe) el archivo `diario.txt` y escribe en la primera línea:
Fecha: 2025-06-02
- Luego, abre el mismo archivo en modo append (`'a'`) para agregar dos líneas más con tus actividades del día.
- Al final, vuelve a abrir en `'r'` y muestra todo el contenido por pantalla.

'''
import os
def limpiar_consola():
     os.system('cls' if os.name =='nt' else 'clear')
     

with open("diario.txt", mode='w') as f:      
      f.write("\nFecha: 2025-06-02")
Menu='''

█▄─▀█▀─▄█▄─▄▄─█▄─▀█▄─▄█▄─██─▄█
██─█▄█─███─▄█▀██─█▄▀─███─██─██
▀▄▄▄▀▄▄▄▀▄▄▄▄▄▀▄▄▄▀▀▄▄▀▀▄▄▄▄▀▀
Introduce la accion que desea realizar
1.Sobreescribir el diario
2.Agregar nueva informacion al diario
3.Ver la informacion del texto
4.Salir
'''
while True:
    limpiar_consola()
    print(Menu)
    opcion=int(input('INGRESE EL NUMERO DE LA OPCION QUE DESEA REALIZAR\n'))
    if opcion==1:  
        with open("diario.txt", mode='w') as f:      
            f.write(input("introduce el nuevo texto\n"))
            input('Presione ENTER para co1ntinuar')
    elif opcion==2:
           for i in range(2):
                with open("diario.txt", mode='a') as f:
                    text=input("introduce el nuevo texto\n")
                    f.write("\n" + text)
    elif opcion==3:
         with open("diario.txt", "r") as f:
            texto = f.read()
            print(texto)
            input('Presione ENTER para continuar')
    elif opcion==4:
         break
    else:
         print("Por favor introduce una opcion valida")
         input('Presione ENTER para continuar')
        
