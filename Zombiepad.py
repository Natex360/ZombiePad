#!/usr/bin/python
import customtkinter as ctk
from customtkinter import END, LEFT, TOP
from tkinter import messagebox, filedialog

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

mainWindow = ctk.CTk()
mainWindow.minsize(1280, 1000)
mainWindow.title("Zombie Editor")
mainWindow.geometry("1280x1000")
filename = ""
tmp = open("PREF")
preffered_dir = tmp.readline()
del tmp

font_size = 14


def change_pref_dir():
    set_pref_dir = filedialog.askdirectory(initialdir=preffered_dir,
                                           title="change preffered directory",)
    f = open("PREF", "w")
    f.write(set_pref_dir)


def save_as_func():
    global preffered_dir
    global filename
    filename = filedialog.asksaveasfilename(initialdir=preffered_dir,
                                            title="save as",
                                            filetypes=(("all files", "*"),
                                                       ("txt files", "*.txt")))
    if messagebox.askyesno("Are you sure", "do you want to proceed"):
        try:
            f = open(filename, "w")
            f.write(text_box.get("1.0", END))
        except FileNotFoundError:
            messagebox.showerror("ERROR", "file not found")
        except PermissionError:
            messagebox.showerror("ERROR", "permission denied")


def save_func():
    if filename != "":
        try:
            f = open(filename, "w")
            f.write(text_box.get("1.0", END))
        except FileNotFoundError:
            messagebox.showerror("ERROR", "file not found")
        except PermissionError:
            messagebox.showerror("ERROR", "premission denied")
    else:
        save_as_func()


def open_func():
    global filename
    global preffered_dir
    filename = filedialog.askopenfilename(initialdir=preffered_dir,
                                          title="open",
                                          filetypes=(("all files", "*"),
                                                     ("txt files", "*.txt"),
                                                     ))
    if messagebox.askyesno("Are you sure", "do you want to proceed"):
        try:
            f = open(filename)
            text_box.delete("1.0", END)
            text_box.insert("1.0", f.read())
        except FileNotFoundError:
            messagebox.showerror("ERROR", "file not found")
        except PermissionError:
            messagebox.showerror("ERROR", "permission denied")
        except TypeError:
            pass


def font_size_up():
    global font_size
    font_size = font_size + 1
    text_box.configure(font=("TkDefaultFont", font_size))


def font_size_down():
    global font_size
    if font_size > 0:
        font_size = font_size - 1
        text_box.configure(font=("TkDefaultFont", font_size))


def exit_app():
    exit()


def clear():
    text_box.delete("1.0", END)


text_box = ctk.CTkTextbox(master=mainWindow, width=1200, height=900, font=("TkDefaultFont", font_size))
text_box.pack(side=TOP, expand=True)

exit_button = ctk.CTkButton(master=mainWindow, text="Wyjdź", command=exit_app)
exit_button.pack(side=LEFT)

save_as_button = ctk.CTkButton(master=mainWindow, text="Zapisz W Katalogu", command=save_as_func)
save_as_button.pack(side=LEFT)

save_button = ctk.CTkButton(master=mainWindow, text="Zapisz", command=save_func)
save_button.pack(side=LEFT)

open_button = ctk.CTkButton(master=mainWindow, text="Otwórz", command=open_func)
open_button.pack(side=LEFT)

clear_button = ctk.CTkButton(master=mainWindow, text="Wyczyść Tekst", command=clear)
clear_button.pack(side=LEFT)

font_size_up_button = ctk.CTkButton(master=mainWindow, text="Powiększ Tekst", command=font_size_up)
font_size_up_button.pack(side=LEFT)

font_size_down_button = ctk.CTkButton(master=mainWindow, text="Pomniejsz Tekst", command=font_size_down)
font_size_down_button.pack(side=LEFT)

add_pref_dir_button = ctk.CTkButton(master=mainWindow, text="Ustaw Preferowany Katalog", command=change_pref_dir)
add_pref_dir_button.pack(side=LEFT)


add_pref_dir_button = ctk.CTkButton(master=mainWindow, text="Otwórz Szablony", command=open_func)
add_pref_dir_button.pack(side=LEFT)


mainWindow.mainloop()
