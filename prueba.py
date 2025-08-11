from tkinter import *

class Calculadora:
    def __init__(self, root):
        self.root = root
        self.root.title("calculadora sencilla")
        self.root.configure(bg="gray")

        self.pantalla = Entry(self.root, width=20, bg="white", borderwidth=5, fg="black")
        self.pantalla.grid(row=0, column=0, padx=5, pady=10, columnspan=4)

        self.crear_botones()

    def crear_botones(self):
        botones = [
            ('1', 1, 0), ('2', 1, 1), ('3', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('7', 3, 0), ('8', 3, 1), ('9', 3, 2),
            ('0', 4, 0), ('+', 1, 3), ('-', 2, 3),
            ('*', 3, 3), ('/', 4, 3), ('=', 4, 1),
            ('C', 4, 2),
        ]
        for (texto, fila, columna) in botones:
            boton = Button(self.root, text=texto, padx=20, pady=20, bg="black", fg="white",
                           command=lambda t=texto: self.boton_click(t))
            boton.grid(row=fila, column=columna)

    def boton_click(self, valor):
        if valor == "=":
            try:
                result = str(eval(self.pantalla.get()))
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, result)
            except:
                self.pantalla.delete(0, END)
                self.pantalla.insert(0, "error")
        elif valor == "C":
            self.pantalla.delete(0, END)
        else:
            current = self.pantalla.get()
            self.pantalla.delete(0, END)
            self.pantalla.insert(0, current + valor)

root = Tk()
calculadora = Calculadora(root)
root.mainloop()
