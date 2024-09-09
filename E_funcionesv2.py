print("Funciones creadas por el usuario")
# Las funciones
def mi_lista():
    amigos = ["Homero", "Paty", "Lety"]
    for casillas in amigos:
        print(casillas)

def mi_tupla():
    consolas = ("Play", "Switch", "Xbox")
    for casita in consolas:
        print(casita)

def mi_set():
    colores = {"Rojo", "Verde", "Azul"}
    for escuela in colores:
        print(escuela)

def mi_diccionario():
    datos= {
        "Color": "Azul",
        "Sabor": "Chocolate",
        "Personas": 23
    }   
    for pastel in datos:
      print(pastel)

print("Mis amigos")
mi_lista()
print("Consolas")
mi_tupla()
print("Colores")
mi_set()
print("Pastel")
mi_diccionario()