import tkinter as tk
from tkinter import messagebox
ans = 0 #Variable encargada de guardar los resultados de operaciones anteriores
def guardar_datos(operacion_texto):
    """Esta funcion se encarga de escribir y registrar las operaciones hechas en la calculadora
    en el archivo local
    Args:
        operacion_texto(str): La cadena con la operacion y su resultado a guardar"""
    try:
        # Abre en modo append "a" para escribir datos nuevos sin borrar otros
        with open("HISTORIAL.txt", "a") as archivo:
            archivo.write("OPERACION:\n")
            archivo.write(operacion_texto + "\n")
            archivo.write("-"*30 + "\n")
    except Exception as e:
        messagebox.showerror("Error de archivo", f"Nose pudo escribir en el historial: {e}")

def cargar_datos():
    """Esta funcion se encarga de leer el archivo local y muestra el historial en 
    un messagebox y muestra una alerta si el historial esta vacio"""
    try:
        # Abre en modo read "r" para leer el historial
        with open("HISTORIAL.txt", "r") as archivo:
            contenido = archivo.read()
        #Verificacion si el archivo existe pero no tiene nada escrito
        if contenido.strip() == "":
            messagebox.showinfo("Historial", "El historial de operaciones esta vacio")
        else:
            messagebox.showinfo("Historial de operaciones", contenido)
    except FileNotFoundError:
        # Si el archivo txt aun no ha sido creado por el programa
        messagebox.showinfo("Historial", "No hay operaciones en el historial todavia")
    except Exception as e:
        messagebox.showerror("Error de archivo", f"No se pudo leer el historial: {e}")

def sumar(num1,num2):
    """Esta funcion realiza la suma de dos numeros enteros.
    Args:
        num1(int): Primer numero a sumar
        num2(int): Segundo numero a sumar
    Returns:
        int: El resultado de la suma.
    """
    resultado = num1 + num2
    return resultado

def restar(num1,num2):
    """ Esta funcion realiza la resta de 2 numeros enteros
    Args:
        num1(int): Primer numero a restar
        num2(int): Segundo numero a restar
    Returns:
        int:El resultado de la resta
    """
    resultado = num1 - num2
    return resultado

def multiplicar(num1,num2):
    """ Esta funcion realiza la multiplicacion de 2 numeros enteros.
    Args:
        num1(int): Primer numero de la multiplicacion
        num2(int): Segundo numero de la multiplicacion
    Returns:
        int: El resultado de la multiplicacion"""
    resultado = num1 * num2
    return resultado

def dividir(num1,num2):
    """Esta funcion realiza la division de 2 numeros entreros.
    Args:
        num1(int): Dividendo (Numero a dividir)
        num2(int): Divisor (numero que divide)
    Returns:
        int o str: El resultado entero de la division o 'ERROR' si se divide entre cero
    """
    # Validacion para evitar la division entre cero
    if num2 == 0:
        return "ERROR"
    else:
        division = num1 / num2
        resultado = int(division)
        return resultado

def evaluar_expresion(expresion):
    """Esta funcion sirve para evaluar expresiones matematicas respetando la jerarquia
    de operaciones y poder realizar operaciones largas
    Args:
        expresion(str): La expresion matematica como texto
    Returns:
        int o str: El resultado entero o "ERROR" si hay division entre cero
    """
    numeros = [] #Lista para guardar los numeros de la expresion
    operadores = [] #Lista para agregar los operadores matematicos de la expresion
    numero_actual = "" #Variable para ir armando los numeros dados 
    #SEPARACION DE NUMEROS Y OPERADORES
    for i in range(len(expresion)):
        caracter = expresion[i]
        
        signo_negativo = (caracter == "-") and (i == 0 or expresion[i-1] in "+-*/")#Detecta los negativos
        
        if caracter in "+*-/" and not signo_negativo:
            if numero_actual != "":
                numeros.append(int(numero_actual))
                numero_actual = ""
            operadores.append(caracter)
        else:
            numero_actual += caracter #Si no es operador pega el numero
    
    if numero_actual != "": #Por si queda un ultimo numero en la expresion
        numeros.append(int(numero_actual))
    
    if len(numeros) == 0:
        return "ERROR"
    # RESOLUCION DE MULTIPLICACIONES O DIVISIONES SI HAY:
    i = 0 #Revision de operadores por posicion en este caso el 0
    while i < len(operadores):
        if operadores[i] == "*":
            resultado = multiplicar(numeros[i], numeros[i+1])
            numeros[i] = resultado
            numeros.pop(i+1)
            operadores.pop(i)
        elif operadores[i] == "/":
            resultado = dividir(numeros[i], numeros[i+1])
            if resultado == "ERROR":
                return "ERROR"
            numeros[i] = resultado
            numeros.pop(i+1)
            operadores.pop(i)
        else:
            i += 1
    #RESOLUCION DE SUMAS Y RESTAS SI HAY EN LA EXPRESION:
    while len(operadores) > 0:
        if operadores[0] == "+":
            resultado = sumar(numeros[0], numeros[1])
        else:
            resultado = restar(numeros[0], numeros[1])
        numeros[0] = resultado
        numeros.pop(1)
        operadores.pop(0)
        
    return numeros[0]

def hacer_botones(ventana, entrada):
    """Esta funcion lo que hace es crear y posicionar los botones numericos y de memoria
    en la interfaz.
    Args:
        ventana (tk.Tk): La ventana principal de la aplicacion de la calculadora
        entrada (tk.Entry): La pantalla donde se muestran los numeros
    """
    def agregar_pantalla(valor):
        entrada.insert(tk.END, valor)
        
    def poner_7():
        agregar_pantalla("7")
    def poner_8():
        agregar_pantalla("8")
    def poner_9():
        agregar_pantalla("9")
    def poner_4():
        agregar_pantalla("4")
    def poner_5():
        agregar_pantalla("5")
    def poner_6():
        agregar_pantalla("6")
    def poner_1():
        agregar_pantalla("1")
    def poner_2():
        agregar_pantalla("2")
    def poner_3():
        agregar_pantalla("3")
    def poner_0():
        agregar_pantalla("0")
    def poner_ans():
        global ans
        agregar_pantalla(str(ans))
    #Configuracion visual y posicionamiento en cuadricula (grid) de los botones numericos
    # Boton "7":
    boton7 = tk.Button(ventana, text="7", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_7)
    boton7.grid(row = 1, column = 0, padx = 3, pady = 3)
    # Boton "8":
    boton8 = tk.Button(ventana, text = "8",bg="#798186", fg="white", font=("Arial", 18),width = 5, height = 2, command = poner_8)
    boton8.grid(row = 1, column = 1, padx = 3, pady = 3)
    # Boton "9":
    boton9 = tk.Button(ventana, text = "9",bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_9)
    boton9.grid(row = 1, column = 2,  padx = 3, pady = 3)
    #Boton "4":
    boton4 = tk.Button(ventana, text="4", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_4)
    boton4.grid(row =2, column=0, padx = 3, pady = 3)
    #Boton "5":
    boton5 = tk.Button(ventana, text="5", bg="#798186", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_5)
    boton5.grid(row =2, column=1, padx = 3, pady = 3)
    #Boton "6":
    boton6 = tk.Button(ventana, text="6", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_6)
    boton6.grid(row =2, column=2, padx = 3, pady = 3)
    #Boton "1":
    boton1 = tk.Button(ventana, text="1", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_1)
    boton1.grid(row =3, column=0, padx = 3, pady = 3)
    #Boton "2":
    boton2 = tk.Button(ventana, text="2", bg="#798186", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_2)
    boton2.grid(row =3, column=1, padx = 3, pady = 3)
    #Boton "3":
    boton3 = tk.Button(ventana, text="3", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_3)
    boton3.grid(row =3, column=2, padx = 3, pady = 3)
    #Boton "0":
    boton0 = tk.Button(ventana, text="0", bg="#798186", fg="white", font=("Arial", 18), width = 5, height = 2,command = poner_0 )
    boton0.grid(row =4, column=0, padx = 3, pady = 3)
    #Boton "ANS":
    boton_ans = tk.Button(ventana, text="ANS", bg="#798186", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_ans)
    boton_ans.grid(row =4, column=1, padx = 3, pady = 3)

def operaciones(ventana, entrada):
    """Esta funcion crea los botones de operaciones matematicas, borrado y maneja la logica
    de resolucion e historial.
    Args:
        ventana (tk.Tk): La ventana principal de la aplicacion de la calculadora
        entrada (tk.Entry): La panatalla donde se muestran los resultados"""
    def agregar_pantalla(valor):
        entrada.insert(tk.END, valor)
    
    def poner_c():
        entrada.delete(0, tk.END) #Limpia la pantalla desde el inicio(0) hasta el final
    
    def borrar():
        texto_actual = entrada.get()
        #Verifica que haya texto en la pantalla para borrar el ultimo caracter
        if len(texto_actual) > 0:
            entrada.delete(len(texto_actual) - 1, tk.END)
    
    def poner_suma():
        agregar_pantalla("+")
    
    def poner_resta():
        agregar_pantalla("-")
    
    def poner_multiplicacion():
        agregar_pantalla("*")
    
    def poner_division():
        agregar_pantalla("/")
        
    def poner_igual():
        global ans
        try: # Usamos try_except para capturar los errores de valores ingresados erroneos  
            operacion = entrada.get()
            # MANDAMOS LA EXPRESION A LA FUNCION DE EVALUACION:
            resultado_final = evaluar_expresion(operacion)
            
            if resultado_final == "ERROR":
                messagebox.showwarning("Division invalida", "No se puede dividir entre cero :(")
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, "ERROR")
            else:
                ans = resultado_final
                guardar_datos(f"{operacion} = {resultado_final}")
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, resultado_final)
        except Exception:
            # Si el codigo falla por datos erroneos, varios simbolos, etc, muestra un erro
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "ERROR")
            messagebox.showerror("Error de entrada", "Operacion no valida revisa los valores ingresados porfa :(")
    

    # Boton "/":
    boton_dividir = tk.Button(ventana, text = "/", bg="#4B5156", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_division)
    boton_dividir.grid(row = 1, column = 3, padx = 3, pady = 3)
    #Boton "*":
    boton_multiplicar = tk.Button(ventana, text="*", bg="#4B5156", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_multiplicacion)
    boton_multiplicar.grid(row =2, column=3, padx = 3, pady = 3)
    #Boton "-":
    boton_resta = tk.Button(ventana, text="-", bg="#4B5156", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_resta)
    boton_resta.grid(row =3, column=3, padx = 3, pady = 3)
    #Boton "C":
    botonC = tk.Button(ventana, text="C", bg="#E01E15", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_c)
    botonC.grid(row =4, column=2, padx = 3, pady = 3)
    #Boton "+":
    boton_sumar = tk.Button(ventana, text="+", bg="#4B5156", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_suma)
    boton_sumar.grid(row =4, column=3, padx = 3, pady = 3)
    #Boton "=":
    boton_igual = tk.Button(ventana, text="=", bg = "#F36211", fg="white", font=("Arial", 18),height = 2, command = poner_igual)
    boton_igual.grid(row = 5, column = 0, columnspan = 3, padx = 3, pady=3, sticky="nsew" )
    #Boton de borrar:
    boton_borrar = tk.Button(ventana, text="Borrar", bg="#E01E15", fg="white", font=("Arial", 17, "bold"), width =5, height=2, command=borrar)
    boton_borrar.grid(row=5, column=3, padx=3, pady=3)
    # Boton historial:
    boton_historial = tk.Button(ventana, text="Ver historial", bg="#4B5156", fg="white", font=("Arial", 12, "bold"), height=2, command=cargar_datos)
    boton_historial.grid(row=6, column = 0, columnspan=4, padx=3, pady=3, sticky="nsew")

def la_interfaz(ventana):
    """Esta funcion configura la pantalla de la calculadora y manda llamar a los bloques
    constructores de los botones.
    Args:
        ventana(tk.Tk): La ventana principal de la aplicacion de la calculadora
    """
    entrada = tk.Entry(ventana, font=("Arial", 24), border = 0, bg="#C1D0A3", fg="black", justify="right")
    entrada.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 20, padx = 10, pady = 10 )
    hacer_botones(ventana, entrada)
    operaciones(ventana, entrada)

def iniciar_calculadora():
    """Esta funcion inicializa la raiz de Tkinter, define propiedades
    de la ventana y arranca el ciclo principal."""
    ventana = tk.Tk()
    ventana.title("CALCULADORA")
    ventana.resizable(False, False)
    ventana.config(bg="#0A1C20")
    
    la_interfaz(ventana)
    ventana.mainloop() #Arranca el loop infinito para que la ventana se mantenga abierta 

iniciar_calculadora()