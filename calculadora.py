import tkinter
from tkinter import messagebox


ventana = tkinter.Tk()
ventana.title("calculadora")
ventana.geometry("+480+180")
ventana.iconbitmap(r"C:\Users\Admin\Desktop\proyectos-course\calculadora\Calculator.ico")

def sumar():
    
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row=9, column=2,columnspan=2 )

        if valor1 == "" or valor2 == "":
           label_resultado["text"] = "¡ Faltan valores para sumar !"
           messagebox.showwarning("Error","Faltan valores para sumar")
        else:
           resultado = int (valor1) + int (valor2)
           label_resultado["text"] =resultado
    except:
        messagebox.showerror("Error nivel 2", "Error, valores no validos")

       
       
       
def Restar():
    
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row=9, column=2,columnspan=2 )

        if valor1 == "" or valor2 == "":
           label_resultado["text"] = "¡ Faltan valores para restar !"
           messagebox.showwarning("Error","Faltan valores para restar")
        else:
           resultado = int (valor1) - int (valor2)
           label_resultado["text"] =resultado
    except:
        messagebox.showerror("Error nivel 2", "Error, valores no validos")

      
      
      
       
def Multiplicar():
    
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row=9, column=2,columnspan=2 )

        if valor1 == "" or valor2 == "":
           label_resultado["text"] = "¡ Faltan valores para multiplicar !"
           messagebox.showwarning("Error","Faltan valores para multiplicar")
        else:
           resultado = int (valor1) * int (valor2)
           label_resultado["text"] =resultado
    except:
        messagebox.showerror("Error nivel 2", "Error, valores no validos")

       
       
       
def Dividir():

    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row=9, column=2,columnspan=2 )

        if valor1 == "" or valor2 == "":
           label_resultado["text"] = "¡ Faltan valores para Dividir !"
           messagebox.showwarning("Error","Faltan valores para Dividir")
        else:
           resultado = int (valor1) / int (valor2)
           label_resultado["text"] =resultado
    except:
        messagebox.showerror("Error nivel 2", "Error, valores no validos")


         
         
def potencia():
    
    try:
        valor1 = e_valor1.get()
        valor2 = e_valor2.get()
        label_resultado.grid(row=9, column=2,columnspan=2 )

        if valor1 == "" or valor2 == "":
           label_resultado["text"] = "¡ Faltan valores para potenciar !"
           messagebox.showwarning("Error","Faltan valores para potenciar")
        else:
           resultado = int (valor1) ** int (valor2)
           label_resultado["text"] =resultado
    except:
        messagebox.showerror("Error nivel 2", "Error, valores no validos")

ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=1)

ventana.rowconfigure(0,weight=1)
ventana.rowconfigure(1,weight=1)
ventana.rowconfigure(2,weight=1)
ventana.rowconfigure(3,weight=1)
ventana.rowconfigure(4,weight=1)
ventana.rowconfigure(5,weight=1)
ventana.rowconfigure(6,weight=1)
ventana.rowconfigure(7,weight=1)

label_titulo = tkinter.Label(ventana,text="calculadora",font=" arial 25")

label_valor1=tkinter.Label(ventana,text="valor 1",font="arial 12")
label_valor2=tkinter.Label(ventana,text="valor 2",font="arial 12")

e_valor1= tkinter.Entry(ventana,font="arial 15")
e_valor2= tkinter.Entry(ventana,font="arial 15")

button_suma = tkinter.Button(ventana,text="suma",bg="black", fg="white", font="arial 12", width=25, command= lambda: sumar ())
button_resta = tkinter.Button(ventana,text="resta",bg="black", fg="white", font="arial 12", width=25, command=  Restar )
button_mul = tkinter.Button(ventana,text="multiplica",bg="black", fg="white", font="arial 12", width=25, command=  Multiplicar)
button_div = tkinter.Button(ventana,text="divide",bg="black", fg="white", font="arial 12", width=25, command=  Dividir )
button_pot = tkinter.Button(ventana,text="potencia",bg="black", fg="white", font="arial 12", width=25, command= potencia)

label_titulo.grid(row=0, column=0, columnspan=2, pady=8)

label_valor1.grid(row=1,column=0,pady=5)
label_valor2.grid(row=2,column=0,)

e_valor1.grid(row=1,column=1,padx=8)
e_valor2.grid(row=2,column=1)

button_suma.grid(row=3,column=0,pady=5,columnspan=2)
button_resta.grid(row=4,column=0,pady=5,columnspan=2)
button_mul.grid(row=5,column=0,pady=5,columnspan=2)
button_div.grid(row=6,column=0,pady=5,columnspan=2)
button_pot.grid(row=7,column=0,pady=5,columnspan=2)

label_resultado = tkinter.Label(ventana, font="arial 60")




ventana.mainloop()