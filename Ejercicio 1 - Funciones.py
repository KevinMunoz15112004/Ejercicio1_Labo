'''Un profesor tiene un salario inicial de $1500, y recibe un incremento
de 10 % anual durante 6 años. ¿Cuál es su salario al cabo de 6
años? ¿Qué salario ha recibido en cada uno de los 6 años? '''

from os import system

salario=float(input("Ingrese su salario: "))

#Definimos las funciones a utilizar
def salario_por_año():
    for i in range(1,7):
        salariot = salario*(1+ 0.1)**i
        print(f"El salario en el año {i} es: {salariot: .2f} dolares.")

def salarioTotal():
    salariofinal = salario*(1 + 0.1)**6
    print("--- SALARIO ANUAL ---")
    print(f"Salario después de 6 años es: {salariofinal:.2f} dolares.")
    print("---------------------")
def main():
    while True:
        print("--- SALARIOS ---")
        print("1)Calcular Salario Total \n2)Ver Salarios Por Año \n3)Salir")
        opcion = int(input("Ingrese la opción: "))
        system("cls")
        if opcion == 1:
            salarioTotal()
        elif opcion == 2:
            salario_por_año()
        elif opcion == 3:
            print("Muchas Gracias \nHa Salido Del Sistema")
            break
        else:
            print("Ingrese una opción válida")
            system("cls")
#Invocamos la funcion main
main()    

