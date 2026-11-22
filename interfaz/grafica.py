import tkinter as tk
from tkinter import ttk
from fisica import refelxion as rf

"""
Esta función inicializa la ventana donde pintamos la grafica
"""
 
def iniciar_ventana():
    ventana = tk.Tk()

    ventana.title("Simulador de la ley de Snell")
    ventana.geometry("800x600")

    grafica = tk.Canvas(ventana, width=800, height=600, bg="white")
    grafica.pack()

    grafica.create_rectangle(0,0,800,300,fill="white",outline="")#AIRE
    medio_inferior = grafica.create_rectangle(0,300,800,600,fill="lightblue",outline="")#Medio inferior

    boton = tk.Button(ventana,text="Calcular")
    grafica.create_line(400,0,400,600,fill="black",width=2,dash=(5,5))

    def actualizar_rayo(valor):
        grados = float(valor)
        x1,y1 = rf.calcularPuntos(400,300,grados,300)
        grafica.coords(rayo,x1,y1,400,300)
   

    angulo = tk.Scale(ventana,from_=0,to=90,orient="horizontal",label="Angulo de incidencia",resolution=1,command=actualizar_rayo)
    angulo.pack()

    x1,y1 = rf.calcularPuntos(400,300,angulo.get(),300)
    rayo = grafica.create_line(x1,y1,400,300,fill="purple",width=2)

    materiales = {
        "Agua":{"color":"lightblue","n":1.33},
        "Aceite":{"color":"orange","n":1.47}
    }
    menu_material = ttk.Combobox(ventana,values=list(materiales.keys()),state="readonly")
    menu_material.pack()

    

    def cambiar_material(event=None):
        elegido = menu_material.get()
        color = materiales[elegido]["color"]
        grafica.itemconfig(medio_inferior, fill=color)

    menu_material.bind("<<ComboboxSelected>>", cambiar_material)    

    boton.pack()

    ventana.mainloop()


