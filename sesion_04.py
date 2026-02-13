# Loops

mi_lista = [1,2,3,4,5]

for i in mi_lista:
    print("El numero es:" , i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"El resultado de la suma de mi lista es: {resultado}")

for i in range(2, 8):
    print(i)

mi_lista2 = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes",}

for i in mi_lista2:
    if i !="Lunes":
        print("Feliz {i}!")

# while loop
i = 0

while i < 5:
    i += 1
    if i ==3:
        continue
    print(i)
    if i ==4:
        break

else:
    print("i es ahora mayor o igual a 5")

#Practica 2
# dada la lista mi lista_2 = ["lunes","nartes","miercoles","jueves","viernes"]
# imprimir cada elemento de la lista 3 veces y cuando sea lunes no lo incluyas
# pista: usa los dos tipos de loops while y for en el mismo programa para lograrlo
# resultado:
# martes
# miercoles
# jueves
# viernes
# martes 
# miercoles
# jueves
# viernes

