# CONDICIONALES

# condicionales simple

# if condicion_expresion_a_evaluar :
#   linea 1
#   linea 2
#   linea 3

# linea que no pertenece a la estructura

edad = 14
if edad > 18 :
    print ("sos mayor de edad(condicional 1)")
    
print ("sos menor de edad(condicional 1)")

# condicional doble
# if condicion_expresion_a_evaluar :
#   linea 1
#   linea 2
#   linea 3
#   
#   else:
#  
#   linea 1
#   linea 2
#   linea 3
    
edad = 13

if edad >= 18 :
    print ("sos mayor de edad(condicional 2)")
else:
    print ("sos menor de edad(condicional 2)")
    print ("hola(condicional 2)")

print("chau chau")

# anidamiento de condicionales

edad = 15

if edad >= 18 :
    print ("sos mayor de edad(condicional 3)")
else:
    print ("sos menor de edad(condicional 3)")
    if edad >=13:
        print("sos un adolescente(condional 3)")
    else:
        print("sos un niño(condiocinal 3)")

print("chau chau")

#condicional multiple
edad = int (input("ingresa su edad: "))

if (edad >=18) and (edad <= 100):
    print("sos mayor de edad(condicional 4)")
elif (edad >=13) and (edad <=17): #simpre hay condicion a comparar
    print("sos menor de edad(condioconal 4)")
    print("sos un adolescente(condicional 4)")
elif edad >= 1: #resolucion de la condicionales anterior que no eran True
    print("sos menor de edad(condioconal 4)")
    print("sos un niño(condicional 4)")
else:
    print("ingrese una edad valida")

# MATCH

tiempo = input("ingresa como esta el dia : ")

match tiempo :
    case "soleado":
        print("el dia esta soleado")
    case "lluvioso":
        print("esta lloviendo!!!")
    case "nublado":
        print("esta nublado!!!")
    case _:
        print("estado de tiempo invalido")
        



