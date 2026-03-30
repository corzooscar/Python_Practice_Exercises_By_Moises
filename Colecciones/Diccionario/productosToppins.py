Productos = []
Toppins = []

cantidadProductos = int(input("Cuantos productos desea ingresar: "))

for i in range(cantidadProductos):
    nombre = input("Ingrese el nombre del producto: ")

    cantidadToppins = int(input("Cuantos toppins usa el producto?: "))
    for i in range(cantidadToppins):
        Toppins.append(input("Ingrese que toppins usa el producto: "))

    Productos.append({
        "nombre": nombre,
        "toppins": Toppins
    })   
    
    


print(Productos)
