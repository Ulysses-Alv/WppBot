import tkinter as tk
import _addBirthday as add
import _deleteMessage as delete


def guardar():
    if input_nombre.get() == "":
        label_error.config(text="Ingrese un nombre válido")

    elif not input_mes.get().isdigit() or not 1 <= int(input_mes.get()) <= 12:
        label_error.config(text="Ingrese un mes válido")

    elif not input_dia.get().isdigit() or not 1 <= int(input_dia.get()) <= 31:
        label_error.config(text="Ingrese un día válido")

    elif input_texto.get() == "":
        label_error.config(text="Ingrese un texto válido")

    else:
        label_error.config(text="")
        nombre = input_nombre.get()
        mes = input_mes.get()
        dia = input_dia.get()
        texto = input_texto.get()
        fecha = "{}/{}".format(dia, mes)
        add.addMessage(nombre, fecha, texto)

        # Borra el contenido de los inputs
        input_nombre.delete(0, tk.END)
        input_mes.delete(0, tk.END)
        input_dia.delete(0, tk.END)
        input_texto.delete(0, tk.END)


def borrar():
    if not delete.deleteMessage(input_nombreToDelete.get(), "birthdays.json"):
        label_errorDel.config(
            text="Ese nombre no existe. \n Ingrese un nombre válido")
    else:
        delete.deleteMessage(input_nombreToDelete.get(), "birthdays.json")
        input_nombreToDelete.delete(0, tk.END)


root = tk.Tk()
root.geometry("450x600+0+0")
root.resizable(False, False)
root.attributes('-fullscreen', False)

label_title = tk.Label(root, text="Agregar mensaje de cumpleaños", font=("Arial", 20), anchor="n")
label_title.pack(fill="x")

label_nombre = tk.Label(root, text="Nombre")
label_nombre.pack()
input_nombre = tk.Entry(root)
input_nombre.pack()

label_mes = tk.Label(root, text="Mes (1-12, sin 0)")
label_mes.pack()
input_mes = tk.Entry(root)
input_mes.pack()

label_dia = tk.Label(root, text="Dia (1-31, sin 0)")
label_dia.pack()
input_dia = tk.Entry(root)
input_dia.pack()

label_texto = tk.Label(root, text="Texto")
label_texto.pack()
input_texto = tk.Entry(root)
input_texto.pack()

boton_guardar = tk.Button(root, text="Guardar", command=guardar)
boton_guardar.pack()

label_error = tk.Label(root, fg="red")
label_error.pack()

# FUNCION DE BORRAR

label_secondtitle = tk.Label(
    root, text="Borrar mensaje", font=("Arial", 30), anchor="n")
label_secondtitle.pack(fill="x")

label_nombreToDelete = tk.Label(root, text="Nombre")
label_nombreToDelete.pack()
input_nombreToDelete = tk.Entry(root)
input_nombreToDelete.pack()

boton_guardarDelete = tk.Button(root, text="Borrar", command=borrar)
boton_guardarDelete.pack()

label_errorDel = tk.Label(root, fg="red")
label_errorDel.pack()

root.mainloop()
