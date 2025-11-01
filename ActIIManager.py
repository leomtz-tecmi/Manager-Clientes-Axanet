import json
import random
import datetime
import os

def crearCliente():     #Se encarga de la logica para crear el archivo de un cliente

    nombre = input("Ingrese el nombre del cliente: ")

    def generarIDCliente():     #Esta funcion anidada toma el primer caracter del string del nombre, y lo concatena con un int convertido a string generado "aleatoriamente"
        return nombre[0] + str(random.randint(1000, 9999))

    idCliente = generarIDCliente()
    telefono = int(input("Ingrese el telefono del cliente: "))
    correo = input("Ingrese el correo del cliente: ")
    fechaReg = str(datetime.datetime.now())     #Regresa la fecha y hora actual al momento del registro convertida a string
    servicio = input("Ingrese el servicio del cliente: ")

    datos = {   #Estructura del archivo en formato JSON
        "Nombre": nombre,
        "ID": idCliente,
        "Telefono": telefono,
        "Correo_Electronico": correo,
        "Fecha_Registro": fechaReg,
        "Servicios": [servicio]
    }
    nombreArchivo = f"{nombre}_Axanet"     #Es el formato del nombre del archivo, tomando el nombre del cliente y anadiendole _Axanet

    with open(nombreArchivo, "w") as json_file:
        json.dump(datos, json_file, indent=4)
    print("Se ha creado el cliente")    #Se crea el archivo del cliente como un JSON

def mostrarClientes():  #Lista el contenido del directorio donde se archivan los clientes utilizando un for loop
    contenido = os.listdir("C:\\Users\\Leonardo\\Desktop\\School\\DevOps\\axanet_clientes")
    print("Lista de Clientes Axanet:")

    for item in contenido:
        print(item)

def eliminarArchivo():  #Elimina el archivo especificado en el directorio
    archivoEliminado = input("Inserta el nombre del cliente a eliminar: ")
    os.remove(archivoEliminado)

def agregarArchivo():   #Hace un append en el diccionario ligado a la llave de Servicios en el archivo JSON y posteriormente lo guarda de nuevo con un Dump
    clienteAgregar = input("Inserta el nombre del cliente al que se le anadira un servicio: ")
    
    with open(clienteAgregar, "r") as json_file:
        datos = json.load(json_file)

    nuevoServicio = input("Ingrese el nuevo servicio: ")
    datos["Servicios"].append(nuevoServicio)

    with open(clienteAgregar, "w") as json_file:
        json.dump(datos, json_file, indent=4)
