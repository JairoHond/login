import tkinter as tk
from tkinter import messagebox
import mysql.connector
import subprocess  # Importar el módulo subprocess

def verificar_credenciales(usuario, contraseña):
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="sa1bd"
        )

        cursor = conexion.cursor()
        consulta = "SELECT * FROM usuairo WHERE codUsuario = %s AND clave = %s"
        cursor.execute(consulta, (usuario, contraseña))
        resultado = cursor.fetchone()
        conexion.close()

        if resultado:
            messagebox.showinfo("Inicio de sesión exitoso", "¡Bienvenido!")
            root.destroy()  # Cerrar la ventana actual de inicio de sesión
            subprocess.run(["python", "menu.py"])  # Abrir la página de menú
        else:
            messagebox.showerror("Error de inicio de sesión", "Credenciales incorrectas")
    except mysql.connector.Error as error:
        messagebox.showerror("Error de conexión", f"No se pudo conectar a la base de datos: {error}")

def iniciar_sesion():
    usuario = entry_usuario.get()
    contraseña = entry_contraseña.get()
    verificar_credenciales(usuario, contraseña)

root = tk.Tk()
root.title("Inicio de sesión")

# Cambiar el fondo de la aplicación
root.configure(bg="#66E7E5")

# Dimensionar la ventana a la mitad de la pantalla
ancho_ventana = root.winfo_screenwidth() // 2
alto_ventana = root.winfo_screenheight() // 2
posicion_x = (root.winfo_screenwidth() - ancho_ventana) // 2
posicion_y = (root.winfo_screenheight() - alto_ventana) // 2
root.geometry(f"{ancho_ventana}x{alto_ventana}+{posicion_x}+{posicion_y}")

# Agregar un logo arriba
try:
    imagen_logo = tk.PhotoImage(file="logo.png")
    label_logo = tk.Label(root, image=imagen_logo, bg="#66E7E5")
    label_logo.pack(pady=20)  # Padding en la parte superior
except tk.TclError:
    print("No se pudo cargar el logo.")

# Cambiar la fuente del texto
fuente = ("Arial Black", 12)

label_usuario = tk.Label(root, text="Usuario:", font=fuente, bg='#66E7E5')
label_usuario.pack()
entry_usuario = tk.Entry(root, font=fuente)
entry_usuario.pack()

label_contraseña = tk.Label(root, text="Contraseña:", font=fuente , bg='#66E7E5')
label_contraseña.pack()
entry_contraseña = tk.Entry(root, show="*", font=fuente)
entry_contraseña.pack()

# Diseño exclusivo para el botón "Ingresar"
boton_ingresar = tk.Button(root, text="Ingresar", command=iniciar_sesion, font=fuente, bg='#007bff', fg='white', bd=0)
boton_ingresar.pack(pady=10)  # Padding entre el botón y los campos de entrada

root.mainloop()