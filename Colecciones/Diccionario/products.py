# Ejercicio — Análisis de Inventario de Productos
"""
Se tiene una lista de productos de una tienda.  
Cada producto contiene información como su nombre, precio, categoría, cantidad en inventario y si es importado o no.

A partir de esta información debes analizar los datos y responder diferentes preguntas usando programación.
"""
## Lista de productos

productos = [
{"nombre":"Laptop","precio":3500.0,"categoria":"tecnologia","stock":5,"importado":True},
{"nombre":"Mouse","precio":25.0,"categoria":"tecnologia","stock":50,"importado":True},
{"nombre":"Teclado","precio":45.0,"categoria":"tecnologia","stock":40,"importado":True},
{"nombre":"Monitor","precio":500.0,"categoria":"tecnologia","stock":10,"importado":True},
{"nombre":"Audifonos","precio":120.0,"categoria":"tecnologia","stock":15,"importado":True},
{"nombre":"Cargador","precio":30.0,"categoria":"tecnologia","stock":35,"importado":True},
{"nombre":"USB","precio":15.0,"categoria":"tecnologia","stock":60,"importado":True},

{"nombre":"Arroz","precio":3.5,"categoria":"alimentos","stock":100,"importado":False},
{"nombre":"Frijoles","precio":4.0,"categoria":"alimentos","stock":80,"importado":False},
{"nombre":"Leche","precio":2.5,"categoria":"alimentos","stock":70,"importado":False},
{"nombre":"Pan","precio":1.8,"categoria":"alimentos","stock":60,"importado":False},
{"nombre":"Huevos","precio":5.5,"categoria":"alimentos","stock":90,"importado":False},
{"nombre":"Pasta","precio":2.0,"categoria":"alimentos","stock":75,"importado":False},
{"nombre":"Cereal","precio":6.5,"categoria":"alimentos","stock":40,"importado":True},

{"nombre":"Silla","precio":80.0,"categoria":"hogar","stock":20,"importado":False},
{"nombre":"Mesa","precio":150.0,"categoria":"hogar","stock":10,"importado":False},
{"nombre":"Lampara","precio":35.0,"categoria":"hogar","stock":25,"importado":True},
{"nombre":"Sofa","precio":900.0,"categoria":"hogar","stock":5,"importado":True},
{"nombre":"Almohada","precio":20.0,"categoria":"hogar","stock":45,"importado":False},
{"nombre":"Cobija","precio":40.0,"categoria":"hogar","stock":30,"importado":False},

{"nombre":"Shampoo","precio":8.0,"categoria":"aseo","stock":50,"importado":False},
{"nombre":"Jabon","precio":2.0,"categoria":"aseo","stock":70,"importado":False},
{"nombre":"Pasta dental","precio":3.0,"categoria":"aseo","stock":60,"importado":False},
{"nombre":"Desodorante","precio":5.0,"categoria":"aseo","stock":55,"importado":True},
{"nombre":"Papel higienico","precio":6.0,"categoria":"aseo","stock":80,"importado":False}
]

# Calcular cuántos productos hay en cada categoría.
# categorias = {}

# for producto in productos:
#         if producto.get("categoria", None) in categorias:
#                 categorias[producto["categoria"]] += 1
#         else: 
#             categorias[producto["categoria"]] = 1
#             # categorias = {"tecnologia": 1}

# for key, Value in categorias.items():
#        print(key,Value)

# technologyProducts = 0
# foodProducts = 0
# homeProducts = 0
# cleaningProducts = 0

# for producto in productos:
#     for key, value in producto.items():
#         if key == 'categoria' and value == 'tecnologia':
#             technologyProducts += 1
#         elif key == 'categoria' and value == 'alimentos':
#             foodProducts += 1
#         elif key == 'categoria' and value == 'hogar':
#             homeProducts += 1
#         elif key == 'categoria' and value == 'aseo':
#             cleaningProducts += 1

# print(f"""Categories | Quantity
# tecnologia  {technologyProducts}
# alimentos  {foodProducts}
# hogar  {homeProducts}
# aseo  {cleaningProducts}""")

                
# Calcular el valor total del inventario por categoría.

# precioTotal = 0
# categorias = {}
# for producto in productos:
#     if producto.get("categoria") not in categorias:
#         categorias[producto["categoria"]] = producto["precio"]
#     else:
#         categorias[producto["categoria"]] += producto["precio"]
#     # precio += producto.get("precio")
    
# for key, value in categorias.items():
#     precioTotal += value
#     print(f"{key}: ${value}")

# print(f"el precio total es: ${precioTotal}")

# El valor de cada producto se calcula multiplicando su precio por el stock disponible.

# for producto in productos:
#     print(f"Nombre: {producto["nombre"]}, Precio: ${producto.get("precio")}, stock: {producto.get("stock")}\nTotal valor del stock: {producto.get("precio")*producto.get("stock")}\n")

# Encontrar los tres productos con mayor valor en inventario.

def myFunc(e):
    return e["precio"]
    
productos.sort(reverse=True,key=myFunc)

for i in range(3):
    print(productos[i])

# Mostrar los productos que:

# tengan stock menor a 20

# y precio mayor a 50.

# Determinar qué categoría tiene más productos registrados.

# Calcular el porcentaje de productos importados dentro del inventario.

# Encontrar el producto más caro de cada categoría.

# Crear una lista con los nombres de los productos que:

# cuesten menos de 10

# y tengan stock mayor a 50.

# Mostrar las categorías ordenadas según la cantidad de productos que tienen.

# Determinar cuál es la categoría con mayor valor total de inventario.