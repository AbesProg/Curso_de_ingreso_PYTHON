import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Sebastián   
apellido: Campos
---
TP: ES_Facturaciones
---
Enunciado:
Para el departamento de facturación:
    A.	Ingresar tres precios de productos y mostrar la suma de los mismos.
    B.	Ingresar tres precios de productos y mostrar el promedio de los mismos.
	C.	ingresar tres precios de productos sumarlos y mostrar el precio final (más IVA 21%).
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label_1 = customtkinter.CTkLabel(master=self, text="Producto 1")
        self.label_1.grid(row=0, column=0, padx=20, pady=10)
        
        self.txt_importe_1 = customtkinter.CTkEntry(master=self)
        self.txt_importe_1.grid(row=0, column=1)

        self.label_2 = customtkinter.CTkLabel(master=self, text="Producto 2")
        self.label_2.grid(row=1, column=0, padx=20, pady=10)
        
        self.txt_importe_2 = customtkinter.CTkEntry(master=self)
        self.txt_importe_2.grid(row=1, column=1)

        self.label_3 = customtkinter.CTkLabel(master=self, text="Producto 3")
        self.label_3.grid(row=2, column=0, padx=20, pady=10)
        
        self.txt_importe_3 = customtkinter.CTkEntry(master=self)
        self.txt_importe_3.grid(row=2, column=1)
        
        self.btn_total = customtkinter.CTkButton(master=self, text="TOTAL", command=self.btn_total_on_click)
        self.btn_total.grid(row=3, pady=10, columnspan=2, sticky="nsew")
        
        self.btn_promedio = customtkinter.CTkButton(master=self, text="PROMEDIO", command=self.btn_promedio_on_click)
        self.btn_promedio.grid(row=4, pady=10, columnspan=2, sticky="nsew")

        self.btn_total_iva = customtkinter.CTkButton(master=self, text="TOTAL c/IVA", command=self.btn_total_iva_on_click)
        self.btn_total_iva.grid(row=5, pady=10, columnspan=2, sticky="nsew")

    def btn_total_on_click(self):
        producto_txt1 = self.txt_importe_1.get()
        producto_txt2 = self.txt_importe_2.get()
        producto_txt3 = self.txt_importe_3.get()

        producto1 = int(producto_txt1)
        producto2 = int(producto_txt2)
        producto3 = int(producto_txt3)

        resultado_final = producto1 + producto2 + producto3
        mensaje_final = "La suma entre {0} + {1} + {2} \nDa el valor de: ".format(producto1, producto2, producto3) + str(resultado_final)

        alert("Suma total" , mensaje_final)

    def btn_promedio_on_click(self):
        producto_txt1 = self.txt_importe_1.get()
        producto_txt2 = self.txt_importe_2.get()
        producto_txt3 = self.txt_importe_3.get()

        producto1 = int(producto_txt1)
        producto2 = int(producto_txt2)
        producto3 = int(producto_txt3)

        productos_general = [producto1, producto2, producto3]
        resultado_suma = sum(productos_general)
        resultado_cantidad = len(productos_general)
        resultado_final = resultado_suma / resultado_cantidad
        mensaje = "el promedio final entre los valores ingresados \nes de: " + str(resultado_final)

        alert("Promedio final" , mensaje)

    def btn_total_iva_on_click(self):
        producto_txt1 = self.txt_importe_1.get()
        producto_txt2 = self.txt_importe_2.get()
        producto_txt3 = self.txt_importe_3.get()

        producto1 = float(producto_txt1)
        producto2 = float(producto_txt2)
        producto3 = float(producto_txt3)

        suma = producto1 + producto2 + producto3
        iva = suma * 0.21
        final = suma  + iva

        mensaje = "El resultado de los productos es de: " + str(suma) 
        mensaje_2 = "\nEl precio sumado al iva 21% es de: " + str(final)
        
        alert("precio final" , mensaje + mensaje_2)



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()