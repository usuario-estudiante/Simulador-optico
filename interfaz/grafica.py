import tkinter as tk
from tkinter import ttk
import math
from fisica import refraccion as rf
from fisica import refelxion as rl


def iniciar_ventana():
    ventana = tk.Tk()

    ventana.title("Simulador de la ley de Snell")
    ventana.geometry("1250x700")

    panel_derecho = tk.Frame(ventana, width=800, height=600)
    panel_derecho.pack(side="right", fill="both", expand="true")

    grafica = tk.Canvas(panel_derecho, width=800, height=600, bg="white")
    grafica.pack(expand="true")

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
        "Diamante": {"color": "cyan", "n": 2.417},
    }

    # Ventana de el lado izquierdo
    panel_izquierdo = tk.Frame(ventana, width=200, height=600, padx=12, pady=12)
    panel_izquierdo.pack(side="left", fill="both", expand="true")

    tk.Label(panel_izquierdo, text="Controles", font=("Arial", 13, "bold")).pack(
        anchor="w", padx=10, pady=(4, 10)
    )

    # El menu para seleccionar el medio superior
    tk.Label(panel_izquierdo, text="Medio superior:").pack(anchor="w", padx=10, pady=(4, 0))
    menu_material_superior = ttk.Combobox(
        panel_izquierdo, values=list(materiales.keys()), state="readonly"
    )
    menu_material_superior.set("Aire")
    menu_material_superior.pack(fill="x", padx=10, pady=(2, 10))

    # La barrita para seleccionar el medio inferior
    tk.Label(panel_izquierdo, text="Medio inferior:").pack(anchor="w", padx=10, pady=(4, 0))
    menu_material_inferior = ttk.Combobox(
        panel_izquierdo, values=list(materiales.keys()), state="readonly"
    )
    menu_material_inferior.set("Agua")
    menu_material_inferior.pack(fill="x", padx=10, pady=(2, 12))

    medio_superior = grafica.create_rectangle(0, 0, 800, 300, fill="white", outline="")  # AIRE
    medio_inferior = grafica.create_rectangle(0, 300, 800, 600, fill="lightblue", outline="")  # Medio inferior
    linea_normal = grafica.create_line(400, 0, 400, 600, fill="black", width=2, dash=(4, 4))

    # Etiquetas de ángulos en la gráfica
    txt_graf_incidente = grafica.create_text(
        345, 220, text="θ₁ = 0.0°", fill="black", font=("Arial", 10, "bold")
    )
    txt_graf_reflexion = grafica.create_text(
        455, 220, text="θr = 0.0°", fill="black", font=("Arial", 10, "bold")
    )
    txt_graf_refraccion = grafica.create_text(
        455, 380, text="θ₂ = 0.0°", fill="black", font=("Arial", 10, "bold")
    )

    def cambiar_material_inferior(event=None):
        elegido = menu_material_inferior.get()
        color = materiales[elegido]["color"]
        grafica.itemconfig(medio_inferior, fill=color)
        actualizar_rayo(angulo.get())

    def cambiar_material_superior(event=None):
        elegido = menu_material_superior.get()
        color = materiales[elegido]["color"]
        grafica.itemconfig(medio_superior, fill=color)
        actualizar_rayo(angulo.get())

    menu_material_superior.bind("<<ComboboxSelected>>", cambiar_material_superior)
    menu_material_inferior.bind("<<ComboboxSelected>>", cambiar_material_inferior)

    def actualizar_rayo(valor):
        grados = float(valor)
        elegido_inferior = menu_material_inferior.get()
        indice_inferior = materiales[elegido_inferior]["n"]
        elegido_superior = menu_material_superior.get()
        indice_superior = materiales[elegido_superior]["n"]
        x1, y1 = rf.calcularPuntos(400, 300, grados, 300)
        grafica.coords(rayo, x1, y1, 400, 300)
        x3, y3 = rf.calcularRayoRefractado(grados, indice_superior, indice_inferior)
        grafica.coords(rayo_refractado, 400, 300, x3, y3)
        x4, y4 = rl.calcularReflexion(400, 300, grados, 300)
        grafica.coords(rayo_reflectado, 400, 300, x4, y4)

        seno_t2 = (indice_superior / indice_inferior) * math.sin(math.radians(grados))
        etiqueta_t1.config(text=f"Incidencia: {grados:.1f}°")
        etiqueta_tr.config(text=f"Reflexión: {grados:.1f}°")
        grafica.itemconfig(txt_graf_incidente, text=f"θ₁ = {grados:.1f}°")
        grafica.itemconfig(txt_graf_reflexion, text=f"θr = {grados:.1f}°")

        if seno_t2 > 1.0:
            etiqueta_t2.config(text="Refracción: Reflexión total")
            grafica.itemconfig(txt_graf_refraccion, text="Ref. total")
        else:
            ang_t2 = round(math.degrees(math.asin(seno_t2)), 1)
            etiqueta_t2.config(text=f"Refracción: {ang_t2:.1f}°")
            grafica.itemconfig(txt_graf_refraccion, text=f"θ₂ = {ang_t2:.1f}°")

    angulo = tk.Scale(
        panel_izquierdo,
        from_=0,
        to=90,
        orient="horizontal",
        label="Angulo de incidencia",
        resolution=1,
        length=190,
        command=actualizar_rayo,
    )
    angulo.pack(fill="x", padx=10, pady=(4, 6))

    frame_btns = tk.Frame(panel_izquierdo)
    frame_btns.pack(fill="x", padx=10, pady=(0, 10))
    for g in [0, 30, 45, 60]:
        tk.Button(
            frame_btns,
            text=f"{g}°",
            command=lambda val=g: (angulo.set(val), actualizar_rayo(val)),
        ).pack(side="left", padx=2, expand=True, fill="x")

    mostrar_normal = tk.BooleanVar(value=True)
    tk.Checkbutton(
        panel_izquierdo,
        text="Línea normal",
        variable=mostrar_normal,
        command=lambda: grafica.itemconfig(
            linea_normal, state="normal" if mostrar_normal.get() else "hidden"
        ),
    ).pack(anchor="w", padx=10, pady=(2, 10))

    # Siguientes elementos
    tk.Label(panel_izquierdo, text="Longitud de onda:").pack(anchor="w", padx=10, pady=(2, 6))

    cajita_angulos = tk.LabelFrame(panel_izquierdo, text="Ángulos", padx=12, pady=10)
    cajita_angulos.pack(fill="x", padx=10, pady=(6, 10))
    etiqueta_t1 = tk.Label(cajita_angulos, text="Incidencia: 0.0°", pady=2)
    etiqueta_t1.pack(anchor="w")
    etiqueta_tr = tk.Label(cajita_angulos, text="Reflexión: 0.0°", pady=2)
    etiqueta_tr.pack(anchor="w")
    etiqueta_t2 = tk.Label(cajita_angulos, text="Refracción: 0.0°", pady=2)
    etiqueta_t2.pack(anchor="w")

    x1, y1 = rf.calcularPuntos(400, 300, angulo.get(), 300)
    x3, y3 = rf.calcularRayoRefractado(angulo.get(), 1.0003, 1.333)
    x4, y4 = rl.calcularReflexion(400, 300, angulo.get(), 300)

    rayo = grafica.create_line(x1, y1, 400, 300, fill="purple", width=2)
    rayo_refractado = grafica.create_line(400, 300, x3, y3, fill="purple", width=2)
    rayo_reflectado = grafica.create_line(400, 300, x4, y4, fill="purple", width=2)

    ventana.mainloop()