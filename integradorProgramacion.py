
import time #Para hacer pausas y visualizar mejor el proceso
import random #para las listas radom
import os #para limpiar la consola en los pasos
from colorama import Fore, Back, Style #para colorear los prints

#declaracion de variables 
posicion = 0    #Variable para las posiciones de la lista, se usa como contador 

#funcion for que imprime el grafico de la lista inicial
def imprimir_lista_inicial(lista):
    print(Fore.GREEN + f"lista inicial: {lista}" + Style.RESET_ALL)     #muestra la lista incial en verde con colorama
    for numero in lista_ordenada:
        print(Fore.GREEN + f"\n\n{numero} ", end ="" + Style.RESET_ALL)     #imprime los numeros de la lista
        for numero in range(numero):
            print("▢ ", end ="")    #imprime un cuadrado al lado de cada numero de la lista

#funcion que imprime los pasos mientras ordenamos
def imprimir_lista_pasos_intermedios(lista_ordenada):
    global posicion
    for numero in lista_ordenada:
        if lista_ordenada[posicion] == numero:      #Si el numero a imprimir uno de los dos que estamos comparando, se imprime en rojo
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        elif lista_ordenada[posicion+1] == numero:      #el siguiente numero que estamos comparando es posicion+1 tambien se marca en rojo
            print("\n")
            print(Fore.RED + f"{numero} ", end ="")
        else:           #si no es uno de los dos numeros, se imprime sin estilo
            print("\n")
            print(Style.RESET_ALL + f"{numero} ", end ="")
        for numero in range(numero):
            print("▢ ", end ="")


#funcion que verifica si la lista esta ordenada
def funcion_lista_esta_ordenada(lista_ordenada):
    global posicion, tamaño_lista, lista_ordenada_chequeo
    
    if lista_ordenada == lista_ordenada_chequeo:        #se chequea que la lista este ordenada
        print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 
        print(Fore.YELLOW + "\nLISTA ORDENADA" + Style.RESET_ALL)
        print(Fore.YELLOW + f"{lista_ordenada}" + Style.RESET_ALL)

        #ciclo for que imprime el grafico de la lista ordenada al final
        for numero in lista_ordenada:
            print("\n")
            print(Fore.RED + f"{numero} "+ Style.RESET_ALL , end ="")
            for numero in range(numero):
                print(Fore.RED + "▢ " + Style.RESET_ALL, end = "")

        #mostramos la cantidad de iteraciones que llevo el programa para finalizar el ordenamiento
        print(Fore.YELLOW + f"\n\nCantidad de iteraciones realizadas: {pasos}" + Style.RESET_ALL)
        print("\nEste fue el programa sobre algoritmos de busqueda y ordenamiento de Hugo Catalan y Matias Carro, Muchas gracias!\n")
        input(Fore.YELLOW + "\n\nPresione Enter para salir del programa..." + Style.RESET_ALL)
    
    else:       #si no esta ordenada se vuelve a llamar a la funcion que ordena
        funcion_ordenamiento(lista_ordenada)

#funcion que ordena la lista
def funcion_ordenamiento(lista_ordenada):
    #variable globales que maneja la funcion
    global posicion, lista_inicial, pasos

    #titulo con lista inicial
    print(Fore.GREEN + f"Lista inicial: {lista_inicial}" + Style.RESET_ALL) 
    print(Fore.YELLOW + f"\nOrdenando lista: " + Style.RESET_ALL, end = "")

    #si la posicion es igual al largo de la lista menos 1, se vuelve a 0 para reiniciar el ordenamiento
    #esto reinicia el ordenamiento para recorrer la lista nuevamente
    if posicion == len(lista_ordenada)-1:        
        posicion = 0

    #Imprime los dos numeros que se comparan al momento 
    print(f"\nNumeros comparados en esta iteracion: " + Fore.RED + f"{lista_ordenada[posicion]} y {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    #desicion que verifica si el primer numero que esta siendo comparado es mayor al segundo numero, si lo es se rotan
    
    if lista_ordenada[posicion] > lista_ordenada[posicion+1]:         #se chequea si la posicion es mayor a la posicion +1
        numero_triangulado = lista_ordenada[posicion]                 #si es asi, se intercambian los valores de lugar, se utiliza una tercer variable para triangular
        lista_ordenada[posicion] = lista_ordenada[posicion+1]
        lista_ordenada[posicion+1] = numero_triangulado
        #se muestra al usuario el paso que se realizo
        print(f"Se ordenan los numeros {lista_ordenada[posicion+1]} y {lista_ordenada[posicion]} porque " + Fore.RED + f"{lista_ordenada[posicion]} es menor a {lista_ordenada[posicion+1]}" + Style.RESET_ALL)
    else:
        print(f"Estos dos numeros se encuentran ordenados correctamente")
    
    #se imprime como la lista va siendo ordenada al momento
    print(Fore.YELLOW + f"\nLista ordenada al momento: " + Style.RESET_ALL)
    print(f"{lista_ordenada}")

    #se llama a la funcion que imprime la lista mientras la estamos ordenando
    imprimir_lista_pasos_intermedios(lista_ordenada)

    posicion += 1           #se sube la posicion en un valor 
    pasos += 1      #cantidad de pasos realizados

    #se espera que el usuario presione enter para continuar
    input(Fore.YELLOW +"\n\nPresione ENTER para continuar..." + Style.RESET_ALL)
    #limpia la pantalla para que el programa sea mas facil de entender
    os.system('cls')
    
    #se llama a la funcion lista ordenada, que verifica si se logro ordenar en este paso, si no, se vuelve a realizar el ordenamiento
    funcion_lista_esta_ordenada(lista_ordenada)

def validacion_datos(numero_ingresado): #Valida que el numero ingresado sea correcto
    while True: #Se repite el loop hasta que la funcion retorne el numero
        try: #intenta pasar el ingreso a un integer
            numero = int(numero_ingresado) #si es integer, se guarda en la variable numero
            if numero >= 3 and numero <= 10: #verifica que el entero sea positivo y menoro igual a 20 si no lo es, vuelve a pedir ingreso de datos
                return numero #si es entero, positivo, y menor a 999, devuelve el numero
            else:
                print("\nDatos ingresados incorrectos")
                numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo entre 3 y 10:\n") #volvemos a pedir ingreso
        except ValueError: #en caso de error, el ingreso no era correcto. Tenia otros caracteres o era decimal
            print("\nDatos ingresados incorrectos")
            numero_ingresado = input("Ingrese otro numero, recuerde que tiene que ser un entero positivo entre 3 y 10:\n") #volvemos a pedir ingreso


#inicio del programa titulo
print(Fore.GREEN +"Bienvenido al programa de Algoritmos de Busqueda y ordenamiento, realizado por Hugo Catalan y Matias Carro."+ Style.RESET_ALL)
print("Para el trabajo practico integrador 2 de la materia de Programacion UTN TUPaD")

#Comienza parte busqueda binaria


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

#Comienza seccion de ordenamiento

input(Fore.YELLOW + "\n\nPresione Enter para continuar con la parte de ordenamiento..." + Style.RESET_ALL)
os.system('cls')
print(Fore.GREEN + "\nPrograma que muestra como se ordena con Bubble Sorting una lista al azar, paso a paso" + Style.RESET_ALL)
print("\nPara poder demostrar el ejemplo, ingrese un numero para elegir el total de elementos de la lista aleatoria") 
print("Por favor un numero entre 3 y 10 ya que mas de 10 el programa seria demasiado largo para su demostracion practica")
#Se solicita ingreso al usuario
numero_ingresado = input("Ingrese un numero:\n")       

#verificacion de ingreso de datos
tamaño_lista = validacion_datos(numero_ingresado)

#Se crea la lista random
lista = random.sample(range(1, tamaño_lista+1), tamaño_lista)    
lista_inicial = list(lista)     #guardamos la lista inicial
lista_ordenada = list(lista)    #vamos a utilizar esta lista para ordenar
lista_ordenada_chequeo = sorted(lista)      #lista ordenada por python para chequear que hayamos ordenado correctamente
pasos = 0 #contador con los pasos que realiza bubble sort para resolver

#se llama a la funcion que imprime la lista inicial
imprimir_lista_inicial(lista)

#pausa en el programa, espera a que el usuario presione enter para continuar
input(Fore.YELLOW + "\n\nPresione Enter para comenzar a ordernar la lista..." + Style.RESET_ALL)
#limpia la pantalla para que el programa sea mas facil de entender
os.system('cls')

#inicio del ordenamiento, se llama a la funcion que verifica si la lista esta ordenada
funcion_ordenamiento(lista_ordenada)