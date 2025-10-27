from ActIIManager import *
import sys

def menu():
    while True:
        print("\n===== Menú Principal Axanet =====")
        print("1. Crear cliente")
        print("2. Mostrar clientes")
        print("3. Eliminar cliente")
        print("4. Agregar servicio a cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crearCliente()
        elif opcion == "2":
            mostrarClientes()
        elif opcion == "3":
            eliminarArchivo()
        elif opcion == "4":
            agregarArchivo()
        elif opcion == "5":
            print("Saliendo del programa...")
            sys.exit(0)
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    menu()