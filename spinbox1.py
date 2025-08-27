#spinbox de numeros del 1 al 10 para edad 
import tkinter as tk 
from tkinter import messagebox, tkk

vetnanaPrincipal=tk.Tk

labelEdad=tk.Label(vetnanaPrincipal,text="Eddad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")
spin=tk.Spinbox(vetnanaPrincipal,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)
boton=tk.Button(vetnanaPrincipal,text="Obtener valor",command=mostrarEdad)
boton.grid(row=1,column=0,padx=10,pady=10)
def mostrarEdad():
    tk.messagebox.showinfo("Edad",f"La edad seleccionada es :{spin.get()}")
    
vetnanaPrincipal.mainloop()