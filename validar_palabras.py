'''
Validar palabras mayusculas y minusculas 
'''
# import string para poder usar ascii_letters
import string

def validar(palabra_usuario):

    mi_lista = []
    
    for letra in palabra_usuario:

        if letra not in string.ascii_letters and letra != " ":
            mi_lista.clear() #si alguna tiene caracter diferente a letras limpia la lista
            print(f"No se aceptan caracteres especiales: {palabra_usuario}")
            return True
        
        elif letra.isupper() == True: #validamos si la letra que recorre el for es mayúscula
            mi_lista.clear() #si alguna es mayuscula limpiamos la lista
            print(f"No se aceptan mayusculas: {palabra_usuario}")
            return True
        
        elif letra.isupper() == False: #de lo contrario se valida que no se tiene alguna mayúscula
            mi_lista.append(letra) # append agrega un elemento al final de la lista
            