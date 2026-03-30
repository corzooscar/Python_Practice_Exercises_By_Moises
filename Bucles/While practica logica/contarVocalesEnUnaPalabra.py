palabra = input('Ingrese una palabra: ')
i = 0
vocales = ['a','e','i','o','u']
cantidadVocales = 0
while i < len(palabra):
    if palabra[i].lower() in vocales:
        cantidadVocales += 1
    #Iteración
    i+=1

print(f'La palabra {palabra} contiene {cantidadVocales} vocales')

