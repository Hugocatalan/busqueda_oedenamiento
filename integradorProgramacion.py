

import time #Para hacer pausas y visualizar mejor el proceso

def busquedaBinaria(lista, objetivo): # Defino la función de búsqueda binaria
    inicio = 0 #Defino el inicio de la lista
    fin = len(lista) - 1 #Defino el fin de la lista

    while inicio <= fin:# Mientras el inicio sea menor o igual al fin
        medio = (inicio + fin) // 2# Calculo el punto medio de la lista
        print(f"📍 Verificando índice {medio} (valor: {lista[medio]})") # Mostramos la posicion y el valor que estamos analizando 
        time.sleep(1)  # Espera 1 segundo para visualizar

        if lista[medio] == objetivo: # comparo el valor del medio con el objetivo
            print(f"✅ El número: {objetivo} se encuentra en la posición {medio}")
            print(f" Felicitaciones, has encontrado el número {objetivo} en la lista.")
            return medio
        elif lista[medio] < objetivo:# Si el valor del medio es menor que el objetivo a la derecha
            print(f"🔽 Buscando el {objetivo}  en la mitad derecha...\n")
            inicio = medio + 1 # actualizo el inicio a la mitad derecha
        else:#si el valor del medio es mayor que el objetivo busco a la izquierda
            print(f"🔼 Buscando el {objetivo} en la mitad izquierda...\n")
            fin = medio - 1 # actualizo el fin a la mitad izquierda
        time.sleep(1)

    print(f"❌ El numero:{objetivo} que esta buscado no fue encontrado")
    return -1

# Prueba
lista = range(0,100,2) # Defino una lista de números del 0 al 100, de 2 en 2
objetivo = int(input("Ingrese un número a buscar en la lista: "))
busquedaBinaria(lista, objetivo)
