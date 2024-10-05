'''
Prototipo de encriptador de palabras
'''

def encriptar(palabra_usuario):

    palabra = ""
    mi_lista = []

    for letra in palabra_usuario:#Con este For recorremos la palabra e introducimos cada letra en una lista
        mi_lista.append(letra) # append agrega un elemento al final de la lista
        
        for letras in mi_lista: #Con este For verifico en que índice esta la letra y después evaluó para reemplazar en ese elemento
            elemento = letras
            indice = mi_lista.index(elemento) #index() indica el índice de la primera aparición de un elemento
            
            if letras == "a":
                mi_lista.insert(indice, "ai")
                mi_lista.remove("a")
                
            elif letras == "e":
                mi_lista.remove("e")
                mi_lista.insert(indice, "enter")
                    
            elif letras == "i":
                mi_lista.remove("i")
                mi_lista.insert(indice, "imes")
                        
            elif letras == "o":
                mi_lista.remove("o")
                mi_lista.insert(indice, "ober")
                            
            elif letras == "u":
                mi_lista.remove("u")
                mi_lista.insert(indice, "ufat")
                                
    for palabra_secreta in mi_lista: #Con este For tomo cada palabra de la lista y la uno para hacerla una sola palabra
        palabra += palabra_secreta

    print(f"La palabra encriptada es: {palabra}")
    