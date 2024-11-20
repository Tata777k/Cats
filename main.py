from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        img.thumbnail((600, 500), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибкаЖ {e}")
        return None


def open_new_window():
    tag = tag_entry.get()
    url_tag = f"https://cataas.com/cat/{tag}" if tag else "https://cataas.com/cat"
    img = load_image(url_tag)

    if img:
        new_window = Toplevel()
        new_window.title("Котё")
        new_window.geometry("600x500")
        label = Label(new_window, image=img)
        label.pack()
        label.image = img

def exit():
    window.destroy()

window = Tk()
window.title("Cats.")
window.geometry("600x550")

tag_entry = Entry()
tag_entry.pack()


load_button = Button(text="Загрузить по тегу", command=open_new_window)
load_button.pack()

menu_b = Menu(window)
window.config(menu=menu_b)

file_menu = Menu(menu_b, tearoff=0)
menu_b.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)

url = "https://cataas.com/cat"


window.mainloop()