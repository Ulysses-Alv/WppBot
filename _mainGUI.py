import tkinter as tk
import _addMessage as add
import _deleteMessage as delete
import os
import _generateLogAdded as genLog
from tkinter import filedialog
from PIL import Image, ImageTk

if not os.path.exists('./database/automatizeMessage.json'):
    # Si el archivo no existe, lo creamos
    with open('./database/automatizeMessage.json', 'w') as f:
        f.write('{"Gente": []}')


class App(tk.Tk):
    file_path = ""
    image_label = ""
    boton_guardarDelete = ""

    def __init__(self):
        super().__init__()

        def saveMessage():
            if input_nombre.get() == "":
                label_error.config(text="Ingrese un nombre válido")

            elif not input_hora.get().isdigit() or not 0 <= int(input_hora.get()) <= 23:
                label_error.config(text="Ingrese una hora válida (0-23)")

            elif not input_minutos.get().isdigit() or not 0 <= int(input_minutos.get()) <= 59:
                label_error.config(text="Ingrese minutos válidos (0-59)")

            elif input_texto.get() == "" and file_path == "":
                label_error.config(text="Ingrese un texto válido")
                print(file_path)
            else:
                label_error.config(text="")

                nombre = input_nombre.get()
                hora = int(input_hora.get())
                minutos = int(input_minutos.get())
                if input_texto.get() == "":
                    texto = file_path
                else:
                    texto = input_texto.get()
                is_one_time_var = var_one_time.get()

                add.addMessage(nombre, hora, minutos, texto, is_one_time_var)
                gen_id = add.newId
                genLog.generateLogAdd(
                    nombre, hora, minutos, texto, is_one_time_var, gen_id)

                # Borra el contenido de los inputs

                input_nombre.delete(0, tk.END)
                input_hora.delete(0, tk.END)
                input_minutos.delete(0, tk.END)
                input_texto.delete(0, tk.END)
                var_one_time.set(False)
                checkbox_one_time.deselect()

        def deleteMessage():
            if not delete.deleteMessageByName(input_nombreToDelete.get(), "./database/automatizeMessage.json"):
                label_errorDel.config(
                    text="Ese nombre no existe. \n Ingrese un nombre válido")
            else:
                delete.deleteMessageByName(
                    input_nombreToDelete.get(), "./database/automatizeMessage.json")
                input_nombreToDelete.delete(0, tk.END)

        def eraseImage():
            global file_path
            global image_label
            global boton_guardarDelete
            image_label.destroy()
            open_button.pack(after=input_minutos)
            label_texto.pack(after=open_button)
            input_texto.pack(after=label_texto)
            boton_guardarDelete.pack_forget()
            file_path = ""

        def open_file_dialog():
            global file_path
            global image_label
            global boton_guardarDelete

            file_path = filedialog.askopenfilename(title="Seleccionar archivo", filetypes=[
                                                   ("Archivos de imagen", "*.png;*.jpg;*.jpeg; *.jfif")])
            if not file_path == "":
                image = Image.open(file_path)
                image.thumbnail((300, 300))
                tk_image = ImageTk.PhotoImage(image)
                image_label = tk.Label(bottom_frame)
                # asigna la imagen a un atributo de la etiqueta de imagen
                image_label.image = tk_image
                image_label.configure(image=tk_image)
                image_label.pack()

                label_texto.pack_forget()
                input_texto.pack_forget()
                open_button.pack_forget()

                boton_guardarDelete = tk.Button(
                    bottom_frame, text="X", command=eraseImage)
                boton_guardarDelete.pack()

        def anotherMessage():
            if input_nombre.get() == "":
                label_error.config(text="Ingrese un nombre válido")

            elif not input_hora.get().isdigit() or not 0 <= int(input_hora.get()) <= 23:
                label_error.config(text="Ingrese una hora válida (0-23)")

            elif not input_minutos.get().isdigit() or not 0 <= int(input_minutos.get()) <= 59:
                label_error.config(text="Ingrese minutos válidos (0-59)")

            elif input_texto.get() == "" and file_path == "":
                label_error.config(text="Ingrese un texto válido")
                print(file_path)
            else:
                label_error.config(text="")

                nombre = input_nombre.get()
                hora = int(input_hora.get())
                minutos = int(input_minutos.get())
                if input_texto.get() == "":
                    texto = file_path
                else:
                    texto = input_texto.get()
                is_one_time_var = var_one_time.get()

                add.addMessage(nombre, hora, minutos, texto, is_one_time_var)
                gen_id = add.newId
                genLog.generateLogAdd(
                    nombre, hora, minutos, texto, is_one_time_var, gen_id)

                # Borra el contenido de los inputs
                eraseImage()
                input_texto.delete(0, tk.END)

        self.option_add('*font', 'Helvetica 12')
        self.config(background="lightgreen")
        self.config(highlightbackground="lightblue")

        self.title("Whatsapp Bot GUI")
        self.iconbitmap('./icon/whatsapp.ico')
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x = (screen_width // 2) - (600 // 2)
        y = (screen_height // 2) - (1050 // 2)  # 600 es el alto de la ventana
        self.resizable(True, True)
        self.geometry(f"+{x}+{y}")
        self.attributes('-fullscreen', False)

        frame_left = tk.Frame(self, width=300, height=600,
                              borderwidth=2, relief="groove", highlightthickness=1)
        frame_right = tk.Frame(self, width=300, height=600,
                               borderwidth=2, relief="groove", highlightthickness=1)
        bottom_frame = tk.Frame(self, width=300, height=300,
                                borderwidth=2, relief="groove", highlightthickness=1)

        frame_left.grid(row=0, column=0, padx=10, pady=10)
        frame_right.grid(row=0, column=1, padx=10, pady=10)
        bottom_frame.grid(row=1, column=0, columnspan=1, padx=10, pady=10)

        frame_left.pack_propagate(0)
        frame_right.pack_propagate(0)
        bottom_frame.pack_propagate(0)

        self.columnconfigure(0, minsize=300)
        self.columnconfigure(1, minsize=300)
        label_title = tk.Label(
            frame_left, text="Add \n auto-message", font=("Helvetica", 30), anchor="n")
        label_title.pack(fill="x")

        # ------------------FRAME LEFT------------------
        label_nombre = tk.Label(frame_left, text="Name")
        label_nombre.pack()
        input_nombre = tk.Entry(frame_left)
        input_nombre.pack()

        label_hora = tk.Label(frame_left, text="Hour: (0-23)")
        label_hora.pack()
        input_hora = tk.Entry(frame_left)
        input_hora.pack()

        label_minutos = tk.Label(frame_left, text="Minutes: (0-59)")
        label_minutos.pack()
        input_minutos = tk.Entry(frame_left)
        input_minutos.pack()

        open_button = tk.Button(
            frame_left, text="Seleccionar archivo", command=open_file_dialog)
        open_button.pack()

        label_texto = tk.Label(frame_left, text="Text")
        label_texto.pack()
        input_texto = tk.Entry(frame_left)
        input_texto.pack()

        label_one_time = tk.Label(frame_left, text="Is a One Time Message?")
        label_one_time.pack()
        var_one_time = tk.BooleanVar()
        checkbox_one_time = tk.Checkbutton(frame_left, variable=var_one_time)
        checkbox_one_time.pack()

        boton_guardar = tk.Button(frame_left, text="Save", command=saveMessage)
        boton_guardar.pack()

        boton_another = tk.Button(
            frame_left, text="Save and Send another", command=anotherMessage)
        boton_another.pack()

        label_error = tk.Label(frame_left, fg="red")
        label_error.pack()

        # FUNCION DE BORRAR

        label_secondtitle = tk.Label(
            frame_left, text="Delete", font=("Helvetica", 30), anchor="n")
        label_secondtitle.pack(fill="x")

        label_nombreToDelete = tk.Label(frame_left, text="Name")
        label_nombreToDelete.pack()
        input_nombreToDelete = tk.Entry(frame_left)
        input_nombreToDelete.pack()

        boton_guardarDelete = tk.Button(
            frame_left, text="Delete", command=deleteMessage)
        boton_guardarDelete.pack()

        label_errorDel = tk.Label(frame_left, fg="red")
        label_errorDel.pack()

        def guardar():
            if input_nombre.get() == "":
                label_error.config(text="Ingrese un nombre válido")

            elif not input_mes.get().isdigit() or not 1 <= int(input_mes.get()) <= 12:
                label_error.config(text="Ingrese un mes válido")

            elif not input_dia.get().isdigit() or not 1 <= int(input_dia.get()) <= 31:
                label_error.config(text="Ingrese un día válido")

            elif input_texto_right.get() == "":
                label_error.config(text="Ingrese un texto válido")

            else:
                label_error.config(text="")
                nombre = input_nombre.get()
                mes = input_mes.get()
                dia = input_dia.get()
                texto = input_texto_right.get()
                fecha = "{}/{}".format(dia, mes)
                add.addMessage(nombre, fecha, texto)

                # Borra el contenido de los inputs
                input_nombre.delete(0, tk.END)
                input_mes.delete(0, tk.END)
                input_dia.delete(0, tk.END)
                input_texto_right.delete(0, tk.END)

        def borrar():
            if not delete.deleteMessageByName(input_nombreToDelete.get(), "./database/birthdays.json"):
                label_errorDel.config(
                    text="Ese nombre no existe. \n Ingrese un nombre válido.")
            else:
                delete.deleteMessageByName(
                    input_nombreToDelete.get(), "./database/birthdays.json")
                input_nombreToDelete.delete(0, tk.END)

        # END FRAME LEFT

        # FRAME RIGHT

        label_title_right = tk.Label(
            frame_right, text="Add Birthday Message", font=("Helvetica", 20), anchor="n")
        label_title_right.pack(fill="x")

        label_nombre_right = tk.Label(frame_right, text="Nombre")
        label_nombre_right.pack()
        input_nombre_right = tk.Entry(frame_right)
        input_nombre_right.pack()

        label_mes_right = tk.Label(frame_right, text="Mes (1-12, sin 0)")
        label_mes_right.pack()
        input_mes_right = tk.Entry(frame_right)
        input_mes_right.pack()

        label_dia_right = tk.Label(frame_right, text="Dia (1-31, sin 0)")
        label_dia_right.pack()
        input_dia_right = tk.Entry(frame_right)
        input_dia_right.pack()

        label_texto_right = tk.Label(frame_right, text="Texto")
        label_texto_right.pack()
        input_texto_right = tk.Entry(frame_right)
        input_texto_right.pack()

        boton_guardar_right = tk.Button(
            frame_right, text="Guardar", command=guardar)
        boton_guardar.pack()

        label_error_right = tk.Label(frame_right, fg="red")
        label_error_right.pack()

        label_secondtitle_right = tk.Label(
            frame_right, text="Borrar mensaje", font=("Helvetica", 30), anchor="n")
        label_secondtitle_right.pack(fill="x")

        label_nombreToDelete_right = tk.Label(frame_right, text="Nombre")
        label_nombreToDelete_right.pack()
        input_nombreToDelete_right = tk.Entry(frame_right)
        input_nombreToDelete_right.pack()

        boton_guardarDelete_right = tk.Button(
            frame_right, text="Borrar", command=borrar)
        boton_guardarDelete_right.pack()

        label_errorDel_right = tk.Label(frame_right, fg="red")
        label_errorDel_right.pack()

        # END FRAME RIGHT

        # FRAME BOTTOM

        # END FRAME BOTTOM


if __name__ == "__main__":
    app = App()
    app.mainloop()
