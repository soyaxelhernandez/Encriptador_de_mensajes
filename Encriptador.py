'''
Prototipo para elegir si desencriptar o encriptar
'''
import validar_palabras
import encriptar_mensaje
import desencriptar_mensaje

eleccion = input("Introduzca 'e' para encriptar un mensaje o 'd' para desencriptarlo: ")

#Con este if iniciamos el programa para validar si se desea encriptar o desencriptar
if eleccion== "e":
    
    encriptar = input("Introduzca el mensaje a encriptar: ")
    if validar_palabras.validar(encriptar) != True:
        encriptar_mensaje.encriptar(encriptar)


elif eleccion == "d":

    mensaje_encriptado = input("Introduzca el mensaje a desencriptar: ")
    if validar_palabras.validar(mensaje_encriptado) != True:
        desencriptar_mensaje.desencriptar(mensaje_encriptado)

else:
    print("opcion no valida")
