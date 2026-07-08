from gfrom gestion import *
from estadisticas import *
from validaciones import *

# Diccionario que mapea las opciones numéricas con sus funciones respectivas
acciones = {
    1: ingresar_vehiculo,
    2: opcion_egresar,
    3: verificar_disp,
    4: mostrar_stats,
    5: modificar_tipo_vehiculo
}
           
opcion = None
while True:
    try:
        opcion = int(input("Menu de opciones: \n1. Ingresar vehiculo \n2. Egresar vehiculo "
                           "\n3. Verificar disponibilidad \n4. Revisar estadísticas "
                           "\n5. Modificar tipo de vehículo \n0. Cerrar el programa \nIngrese un número para avanzar: "))
        if opcion not in range(0, 6):
            raise ValueError
            
    except ValueError:
        print("Error: Debes ingresar un número del 0 al 5 para avanzar\n")
        continue  # <--- CORRECCIÓN: Reinicia el bucle immediately y evita evaluar código innecesario

    # Si la opción es válida y está en el diccionario de acciones, se ejecuta
    if opcion in acciones:
        acciones[opcion]()

    # Si la opción es 0, se vacía el estacionamiento, se guardan stats y se corta el ciclo
    elif opcion == 0:
        vaciar_estacionamiento()
        mostrar_stats()  # Guarda en el archivo lo acumulado en esta sesión
        break

    opcion = None

print("Se han guardado las estadísticas y se han quitado todos los vehiculos del estacionamiento. Gracias por usar el programa.")
