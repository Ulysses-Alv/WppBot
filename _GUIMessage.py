import tkinter as tk
import _addMessage as add
import _deleteMessage as delete
import os
import _generateLogAdded as genLog

if not os.path.exists('./database/automatizeMessage.json'):
    # Si el archivo no existe, lo creamos
    with open('./database/automatizeMessage.json', 'w') as f:
        f.write('{"Gente": []}')


def guardar():
    if input_nombre.get() == "":
        label_error.config(text="Ingrese un nombre válido")

    elif not input_hora.get().isdigit() or not 0 <= int(input_hora.get()) <= 23:
        label_error.config(text="Ingrese una hora válida (0-23)")

    elif not input_minutos.get().isdigit() or not 0 <= int(input_minutos.get()) <= 59:
        label_error.config(text="Ingrese minutos válidos (0-59)")

    elif input_texto.get() == "":
        label_error.config(text="Ingrese un texto válido")

    else:
        label_error.config(text="")

        nombre = input_nombre.get()
        hora = int(input_hora.get())
        minutos = int(input_minutos.get())
        texto = input_texto.get()
        is_one_time_var = var_one_time.get()

        add.addMessage(nombre, hora, minutos, texto, is_one_time_var)
        gen_id = add.newId
        genLog.generateLogAdd(nombre, hora, minutos, texto, is_one_time_var, gen_id)

        # Borra el contenido de los inputs

        input_nombre.delete(0, tk.END)
        input_hora.delete(0, tk.END)
        input_minutos.delete(0, tk.END)
        input_texto.delete(0, tk.END)
        var_one_time.set(False)
        checkbox_one_time.deselect()


def borrar():
    if not delete.deleteMessageByName(input_nombreToDelete.get(), "./database/automatizeMessage.json"):
        label_errorDel.config(text="Ese nombre no existe. \n Ingrese un nombre válido")
    else:
        delete.deleteMessageByName(input_nombreToDelete.get(), "./database/automatizeMessage.json")
        input_nombreToDelete.delete(0, tk.END)


root = tk.Tk()
root.geometry("450x600+0+0")
root.resizable(False, False)
root.attributes('-fullscreen', False)

label_title = tk.Label(root, text="Agregar mensaje",
                       font=("Arial", 30), anchor="n")
label_title.pack(fill="x")

label_nombre = tk.Label(root, text="Nombre")
label_nombre.pack()
input_nombre = tk.Entry(root)
input_nombre.pack()

label_hora = tk.Label(root, text="Hora (0-23)")
label_hora.pack()
input_hora = tk.Entry(root)
input_hora.pack()

label_minutos = tk.Label(root, text="Minutos (0-59)")
label_minutos.pack()
input_minutos = tk.Entry(root)
input_minutos.pack()

label_texto = tk.Label(root, text="Texto")
label_texto.pack()
input_texto = tk.Entry(root)
input_texto.pack()

label_one_time = tk.Label(root, text="¿Es un mensaje único?")
label_one_time.pack()
var_one_time = tk.BooleanVar()
checkbox_one_time = tk.Checkbutton(root, variable=var_one_time)
checkbox_one_time.pack()

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
