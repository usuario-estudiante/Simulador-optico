import tkinter as tk
from tkinter import ttk
from fisica import refraccion as rf
 
def iniciar_ventana():
    ventana = tk.Tk()

    ventana.title("Simulador de la ley de Snell")
    ventana.geometry("800x600")                                                                                                                        

    grafica = tk.Canvas(ventana, width=800, height=600, bg="white")
    grafica.pack()

    materiales = {
        "Vacio": {"color": "white", "n": 1.0},
        "Aire": {"color": "aliceblue", "n": 1.0003},
        "Agua": {"color": "lightblue", "n": 1.333},
        "Hielo": {"color": "azure", "n": 1.31},
        "Alcohol etilico": {"color": "lightyellow", "n": 1.361},
        "Aceite": {"color": "orange", "n": 1.47},
        "Glicerina": {"color": "plum", "n": 1.473},
        "Cuarzo": {"color": "lightgray", "n": 1.544},
        "Vidrio": {"color": "silver", "n": 1.52},
        "Zafiro": {"color": "royalblue", "n": 1.77},
        "Diamante": {"color": "cyan", "n": 2.417}
        }
    
    menu_material_superior = ttk.Combobox(ventana,values=list(materiales.keys()),state="readonly")
    menu_material_superior.pack()
    
    menu_material_inferior = ttk.Combobox(ventana,values=list(materiales.keys()),state="readonly")
    menu_material_inferior.pack()

    medio_superior = grafica.create_rectangle(0,0,800,300,fill="white",outline="")#AIRE
    medio_inferior = grafica.create_rectangle(0,300,800,600,fill="lightblue",outline="")#Medio inferior


    def cambiar_material_inferior(event=None):
        elegido = menu_material_inferior.get()
        color = materiales[elegido]["color"]
        grafica.itemconfig(medio_inferior, fill=color)

    def cambiar_material_superior(event=None):
        elegido = menu_material_superior.get()
        color = materiales[elegido]["color"]
        grafica.itemconfig(medio_superior, fill=color)

    boton = tk.Button(ventana,text="Calcular")
    grafica.create_line(400,0,400,600,fill="black",width=2,dash=(5,5))
    menu_material_inferior.bind("<<ComboboxSelected>>", cambiar_material_inferior)
    menu_material_superior.bind("<<ComboboxSelected>>", cambiar_material_superior)
    menu_material_inferior.current(1)  
    menu_material_superior.current(2)  
    boton.pack()
    

   

    

    

    def actualizar_rayo(valor):
        grados = float(valor)
        elegido_inferior = menu_material_inferior.get()
        indice_inferior = materiales[elegido_inferior]["n"]
        elegido_superior = menu_material_superior.get()
        indice_superior =materiales[elegido_superior]["n"]
        x1,y1 = rf.calcularPuntos(400,300,grados,300)
        grafica.coords(rayo,x1,y1,400,300)
        x3,y3 = rf.calcularRayoRefractado(grados,indice_superior,indice_inferior)
        grafica.coords(rayo_refractado,400,300,x3,y3)

    angulo = tk.Scale(ventana,from_=0,to=90,orient="horizontal",label="Angulo de incidencia",resolution=1,command=actualizar_rayo)
    angulo.pack()
    
      

    x1,y1 = rf.calcularPuntos(400,300,angulo.get(),300)
    rayo = grafica.create_line(x1,y1,400,300,fill="purple",width=2)
    x3,y3 = rf.calcularRayoRefractado(angulo.get(),1.0003,1.333)

   


   

    
    rayo_refractado = grafica.create_line(400,300,x3,y3,fill="purple",width=2)

  

 
    


   
    ventana.mainloop()


