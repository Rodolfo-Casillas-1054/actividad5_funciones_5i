print("Manejo de funciones V1")
def hola_mundo():
  print("Hola aqui estoy")
# Llamando a la funcion 
hola_mundo()

def hola_mundo():
  print("Hola aqui estoy dentro de la funcion")

def mensa(msg):
  print (msg)
def EscribNC (Nombre,Apellido):
  print(Nombre, Apellido)
  print(f"Tu nombre es {Nombre} {Apellido}")
def suma2num(n1,n2):
  s = n1+n2
  return f"La suma de {n1} y de {n2} es: ",s
# Llamando a la funcion 
hola_mundo()
mensa ("Hola Wasap") #llama a mensa con un parametro
mensa ("El profe me sorprendió enviando mensajes") #llama a mensa con un parametro
EscribNC("Rodolfo ", "Casillas")
print("Funciones que regresan valores")
print(suma2num(7,3))
print(suma2num(15,45))