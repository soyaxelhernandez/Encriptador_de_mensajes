'''
Programa para desncriptar mensaje
'''

def sniffer(u, a, b): #defino una funcion con join para buscar las letras

    mi_lista = u.split(a)
    separador = b
    nueva_palabra = separador.join(mi_lista)
    return nueva_palabra


def desencriptar(palabra_usuario): #defino una funcion utilizando el sniffer para generar la palabra

    if palabra_usuario.split("ai"):
        resultado = sniffer(palabra_usuario, "ai", "a")
        
        if resultado.split("imes"):
            resultado = sniffer(resultado, "imes", "i")

            if resultado.split("enter"):
                resultado = sniffer(resultado, "enter", "e")

                if resultado.split("ober"):
                    resultado = sniffer(resultado, "ober", "o")

                if resultado.split("ufat"):
                    resultado = sniffer(resultado, "ufat", "u")
    print(f"La palabra desencriptada es: {resultado}")