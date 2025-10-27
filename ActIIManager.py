import json
import random
import datetime
import os

def crearCliente():

    nombre = input("Ingrese el nombre del cliente: ")

    def generarIDCliente():
        return nombre[0] + str(random.randint(1000, 9999))

    idCliente = generarIDCliente()
    telefono = int(input("Ingrese el telefono del cliente: "))
    correo = input("Ingrese el correo del cliente: ")
    fechaReg = str(datetime.datetime.now())
    servicio = input("Ingrese el servicio del cliente: ")

    datos = {
        "Nombre": nombre,
        "ID": idCliente,
        "Telefono": telefono,
        "Correo_Electronico": correo,
        "Fecha_Registro": fechaReg,
        "Servicios": [servicio]
    }
    nombreArchivo = f"{nombre}_Axanet"

    with open(nombreArchivo, "w") as json_file:
        json.dump(datos, json_file, indent=4)
    print("Se ha creado el cliente")

def mostrarClientes():
    contenido = os.listdir("C:\\Users\\Leonardo\\Desktop\\School\\DevOps\\axanet_clientes")
    print("Lista de Clientes Axanet:")

    for item in contenido:
        print(item)

def eliminarArchivo():
    archivoEliminado = input("Inserta el nombre del cliente a eliminar: ")
    os.remove(archivoEliminado)

def agregarArchivo():
    clienteAgregar = input("Inserta el nombre del cliente al que se le anadira un servicio: ")
    
    with open(clienteAgregar, "r") as json_file:
        datos = json.load(json_file)

    nuevoServicio = input("Ingrese el nuevo servicio: ")
    datos["Servicios"].append(nuevoServicio)

    with open(clienteAgregar, "w") as json_file:
        json.dump(datos, json_file, indent=4)
