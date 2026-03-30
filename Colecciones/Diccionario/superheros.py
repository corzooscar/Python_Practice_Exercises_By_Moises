# 🦸 Ejercicio 1 — Análisis de superhéroes

# Se tiene la siguiente lista de superhéroes con diferentes características.

superheros = [
    {
        "nombre": "Spider-Man",
        "universo": "Marvel",
        "poder": "sentido arácnido",
        "fuerza": 85,
        "usa_capa": False,
        "habilidades": ["agilidad", "trepar paredes"],
        "edad": 18
    },
    {
        "nombre": "Iron Man",
        "universo": "Marvel",
        "poder": "armadura tecnológica",
        "fuerza": 90,
        "usa_capa": False,
        "habilidades": ["ingeniería", "vuelo"],
        "edad": 40
    },
    {
        "nombre": "Captain America",
        "universo": "Marvel",
        "poder": "super soldado",
        "fuerza": 88,
        "usa_capa": False,
        "habilidades": ["liderazgo", "combate"],
        "edad": 101
    },
    {
        "nombre": "Thor",
        "universo": "Marvel",
        "poder": "trueno",
        "fuerza": 100,
        "usa_capa": True,
        "habilidades": ["volar", "control del rayo"],
        "edad": 1500
    },
    {
        "nombre": "Hulk",
        "universo": "Marvel",
        "poder": "fuerza gamma",
        "fuerza": 100,
        "usa_capa": False,
        "habilidades": ["resistencia", "salto"],
        "edad": 45
    },
    {
        "nombre": "Black Widow",
        "universo": "Marvel",
        "poder": "espionaje",
        "fuerza": 65,
        "usa_capa": False,
        "habilidades": ["sigilo", "artes marciales"],
        "edad": 35
    },
    {
        "nombre": "Doctor Strange",
        "universo": "Marvel",
        "poder": "magia",
        "fuerza": 80,
        "usa_capa": True,
        "habilidades": ["hechizos", "teletransportación", "volar"],
        "edad": 42
    },
    {
        "nombre": "Scarlet Witch",
        "universo": "Marvel",
        "poder": "magia del caos",
        "fuerza": 95,
        "usa_capa": False,
        "habilidades": ["hechizos", "telequinesis", "volar"],
        "edad": 29
    },
    {
        "nombre": "Black Panther",
        "universo": "Marvel",
        "poder": "habilidades mejoradas",
        "fuerza": 85,
        "usa_capa": False,
        "habilidades": ["agilidad", "estrategia"],
        "edad": 35
    },
    {
        "nombre": "Ant-Man",
        "universo": "Marvel",
        "poder": "cambiar tamaño",
        "fuerza": 70,
        "usa_capa": False,
        "habilidades": ["tecnología", "infiltración"],
        "edad": 38
    },
    {
        "nombre": "Wolverine",
        "universo": "Marvel",
        "poder": "regeneración",
        "fuerza": 92,
        "usa_capa": False,
        "habilidades": ["garras", "resistencia"],
        "edad": 200
    },
    {
        "nombre": "Batman",
        "universo": "DC",
        "poder": "inteligencia",
        "fuerza": 70,
        "usa_capa": True,
        "habilidades": ["estrategia", "artes marciales"],
        "edad": 35
    },
    {
        "nombre": "Superman",
        "universo": "DC",
        "poder": "super fuerza",
        "fuerza": 100,
        "usa_capa": True,
        "habilidades": ["volar", "visión láser"],
        "edad": 30
    },
    {
        "nombre": "Wonder Woman",
        "universo": "DC",
        "poder": "fuerza amazona",
        "fuerza": 95,
        "usa_capa": False,
        "habilidades": ["combate", "lazo mágico", "volar"],
        "edad": 3000
    },
    {
        "nombre": "Flash",
        "universo": "DC",
        "poder": "super velocidad",
        "fuerza": 75,
        "usa_capa": False,
        "habilidades": ["velocidad", "reflejos"],
        "edad": 28
    },
    {
        "nombre": "Aquaman",
        "universo": "DC",
        "poder": "control del océano",
        "fuerza": 88,
        "usa_capa": False,
        "habilidades": ["nadar", "comunicarse con peces"],
        "edad": 32
    },
    {
        "nombre": "Green Lantern",
        "universo": "DC",
        "poder": "anillo de poder",
        "fuerza": 85,
        "usa_capa": False,
        "habilidades": ["crear energía", "volar"],
        "edad": 34
    },
    {
        "nombre": "Cyborg",
        "universo": "DC",
        "poder": "tecnología",
        "fuerza": 90,
        "usa_capa": False,
        "habilidades": ["hacking", "armas"],
        "edad": 26
    },
    {
        "nombre": "Shazam",
        "universo": "DC",
        "poder": "magia",
        "fuerza": 98,
        "usa_capa": True,
        "habilidades": ["rayos", "fuerza", "volar"],
        "edad": 15
    },
    {
        "nombre": "Nightwing",
        "universo": "DC",
        "poder": "acrobacia",
        "fuerza": 72,
        "usa_capa": False,
        "habilidades": ["acrobacia", "combate"],
        "edad": 27
    },
    {
        "nombre": "Raven",
        "universo": "DC",
        "poder": "magia oscura",
        "fuerza": 80,
        "usa_capa": True,
        "habilidades": ["telepatía", "hechizos", "volar"],
        "edad": 19
    },
    {
        "nombre": "Starfire",
        "universo": "DC",
        "poder": "energía estelar",
        "fuerza": 90,
        "usa_capa": False,
        "habilidades": ["volar", "rayos"],
        "edad": 21
    }
]

## Actividades

# Mostrar todos los superhéroes que pertenecen a Marvel.
# for superhero in superheros:
#     if superhero['universo'] == 'Marvel':
#         print(superhero['nombre'])

# Mostrar todos los superhéroes que pertenecen a DC.
# for superhero in superheros:
#     if superhero['universo'] == 'DC':
#         print(superhero['nombre'])

# Mostrar los superhéroes que usan capa.
# for superhero in superheros:
#     if superhero['usa_capa']:
#         print(superhero['nombre'])

# Mostrar los superhéroes con fuerza mayor a 90.
# for superhero in superheros:
#     if superhero['fuerza'] > 90:
#         print(superhero['nombre'])

# Mostrar los superhéroes que tienen la habilidad volar.
# for superhero in superheros: 
#     if 'volar' in superhero['habilidades'] or 'vuelo' in superhero['habilidades']:
#         print(superhero['nombre'])
        
# Encontrar el superhéroe con mayor fuerza.
# mostStrong = 0
# for superhero in superheros:
#     if superhero['fuerza'] > mostStrong:
#         name = superhero['nombre']
#         mostStrong = superhero['fuerza']

# for superhero in superheros:
#     if superhero['fuerza'] == mostStrong:
#         print(f"{superhero['nombre']} {superhero['fuerza']}")

# Mostrar los superhéroes menores de 30 años.
# for superhero in superheros:
#     if superhero['edad'] < 30:
#         print(superhero['nombre'])