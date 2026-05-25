import tkinter as tk
# Calculadora en Tkinter:

def sumar(num1,num2):
    resultado = num1 + num2
    return resultado

def restar(num1,num2):
    resultado = num1 - num2
    return resultado

def multiplicar(num1,num2):
    resultado = num1 * num2
    return resultado

def dividir(num1,num2):
    if num2 == 0:
        return "ERROR"
    else:
        resultado = num1 / num2
        return resultado

def hacer_botones(ventana, entrada):
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
        agregar_pantalla("ANS")
    
    def poner_c():
        entrada.delete(0, tk.END)
    
    def poner_suma():
        agregar_pantalla("+")
    
    def poner_resta():
        agregar_pantalla("-")
    
    def poner_multiplicacion():
        agregar_pantalla("*")
    
    def poner_division():
        agregar_pantalla("/")
        
    def poner_igual():
        try:
            operacion = entrada.get()
            if "+" in operacion:
                partes = operacion.split("+")
                num1 = int(partes[0])
                num2 = int(partes[1])
                resultado_final = sumar(num1, num2)
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, resultado_final)
            elif "-" in operacion:
                partes = operacion.split("-")
                num1 = int(partes[0])
                num2 = int(partes[1])
                resultado_final = restar(num1, num2)
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, resultado_final)
            elif "*" in operacion:
                partes = operacion.split("*")
                num1 = int(partes[0])
                num2 = int(partes[1])
                resultado_final = multiplicar(num1, num2)
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, resultado_final)
            elif "/" in operacion:
                partes = operacion.split("/")
                num1 = int(partes[0])
                num2 = int(partes[1])
                resultado_final = dividir(num1, num2)
                entrada.delete(0, tk.END)
                entrada.insert(tk.END, resultado_final)
        except:
            entrada.delete(0, tk.END)
            entrada.insert(tk.END, "ERROR")
    
    # Boton "7":
    boton7 = tk.Button(ventana, text="7", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_7)
    boton7.grid(row = 1, column = 0, padx = 3, pady = 3)
    # Boton "8":
    boton8 = tk.Button(ventana, text = "8",bg="#334155", fg="white", font=("Arial", 18),width = 5, height = 2, command = poner_8)
    boton8.grid(row = 1, column = 1, padx = 3, pady = 3)
    # Boton "9":
    boton9 = tk.Button(ventana, text = "9",bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_9)
    boton9.grid(row = 1, column = 2,  padx = 3, pady = 3)
    # Boton "/":
    boton_dividir = tk.Button(ventana, text = "/", bg="#0ea5e9", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_division)
    boton_dividir.grid(row = 1, column = 3, padx = 3, pady = 3)
    
    #Boton "4":
    boton4 = tk.Button(ventana, text="4", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_4)
    boton4.grid(row =2, column=0, padx = 3, pady = 3)
    #Boton "5":
    boton5 = tk.Button(ventana, text="5", bg="#334155", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_5)
    boton5.grid(row =2, column=1, padx = 3, pady = 3)
    #Boton "6":
    boton6 = tk.Button(ventana, text="6", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_6)
    boton6.grid(row =2, column=2, padx = 3, pady = 3)
    #Boton "*":
    boton_multiplicar = tk.Button(ventana, text="*", bg="#0ea5e9", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_multiplicacion)
    boton_multiplicar.grid(row =2, column=3, padx = 3, pady = 3)
    
    
    #Boton "1":
    boton1 = tk.Button(ventana, text="1", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_1)
    boton1.grid(row =3, column=0, padx = 3, pady = 3)
    #Boton "2":
    boton2 = tk.Button(ventana, text="2", bg="#334155", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_2)
    boton2.grid(row =3, column=1, padx = 3, pady = 3)
    #Boton "3":
    boton3 = tk.Button(ventana, text="3", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_3)
    boton3.grid(row =3, column=2, padx = 3, pady = 3)
    #Boton "-":
    boton_resta = tk.Button(ventana, text="-", bg="#0ea5e9", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_resta)
    boton_resta.grid(row =3, column=3, padx = 3, pady = 3)
    
    
    #Boton "0":
    boton0 = tk.Button(ventana, text="0", bg="#334155", fg="white", font=("Arial", 18), width = 5, height = 2,command = poner_0 )
    boton0.grid(row =4, column=0, padx = 3, pady = 3)
    #Boton "ANS":
    boton_ans = tk.Button(ventana, text="ANS", bg="#334155", fg="white", font=("Arial", 18),  width = 5, height = 2, command = poner_ans)
    boton_ans.grid(row =4, column=1, padx = 3, pady = 3)
    #Boton "C":
    botonC = tk.Button(ventana, text="C", bg="#ef4444", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_c)
    botonC.grid(row =4, column=2, padx = 3, pady = 3)
    #Boton "+":
    boton_sumar = tk.Button(ventana, text="+", bg="#0ea5e9", fg="white", font=("Arial", 18), width = 5, height = 2, command = poner_suma)
    boton_sumar.grid(row =4, column=3, padx = 3, pady = 3)
    
    #Boton "=":
    boton_igual = tk.Button(ventana, text="=", bg = "#0ea5e9", fg="white", font=("Arial", 18),height = 2, command = poner_igual)
    boton_igual.grid(row = 5, column = 0, columnspan = 4, padx = 3, pady=3, sticky="nsew" )

def la_interfaz(ventana):
    # PANTALLA:
    entrada = tk.Entry(ventana, font=("Arial", 24), border = 0, bg="#1e3a5f", fg="white", justify="right")
    entrada.grid(row = 0, column = 0, columnspan = 4, ipadx = 8, ipady = 20, padx = 10, pady = 10 )
    hacer_botones(ventana, entrada)

def iniciar_calculadora():
    ventana = tk.Tk()
    ventana.title("CALCULADORA")
    #ventana.geometry("400x450")
    ventana.resizable(False, False)
    ventana.config(bg="#0f172a")

    la_interfaz(ventana)
    ventana.mainloop()

iniciar_calculadora()