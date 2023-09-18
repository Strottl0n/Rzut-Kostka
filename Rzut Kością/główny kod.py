import tkinter as tk
from random import randint
from tkinter import ttk
from PIL import Image, ImageTk
import pygame

pygame.init()
root = tk.Tk()
root.resizable(width=False, height=False)
root.iconbitmap(r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\dice.png")


sound = pygame.mixer.Sound(r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\losowanie.wav")

szerokosc_obrazu = 0
wysokosc_obrazu = 0
photo = None

root.geometry("216x245")
root.title("Rzut Kością Symulator")
title_label = ttk.Label(master=root, text='Symulator Rzutu', font=('Helvetica', 16, 'italic'))
title_label.pack()

dice_label = ttk.Label(master=root, text='Kością', font=('Helvetica', 16, 'italic'))
dice_label.pack()

title_label.config(compound='center')
title_label.pack()

result_label = ttk.Label(master=root, text='', font=('Helvetica', 14))
result_label.pack()

def losuj_kostka():
    global szerokosc_obrazu, wysokosc_obrazu, photo

    losowa_liczba = randint(1, 6)

    if losowa_liczba == 1:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\1.png"
    elif losowa_liczba == 2:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\2.png"
    elif losowa_liczba == 3:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\3.png"
    elif losowa_liczba == 4:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\4.png"
    elif losowa_liczba == 5:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\5.png"
    else:
        image_path = r"C:\Users\Miłosz\OneDrive\Pulpit\Python - Projects\Rzut Kością\strony kości\6.png"

    try:
        image = Image.open(image_path)
        image = image.resize((szerokosc_obrazu, wysokosc_obrazu), Image.NEAREST)
    except:
        # Jeśli nie udało się załadować obrazka, użyj domyślnych wartości szerokości i wysokości
        image = Image.new('RGB', (100, 100))

    new_photo = ImageTk.PhotoImage(image)

    szerokosc_obrazu = image.width
    wysokosc_obrazu = image.height

    canvas.configure(width=szerokosc_obrazu, height=wysokosc_obrazu)
    canvas.create_image(0, 0, anchor=tk.NW, image=new_photo)

    sound.play()
    result_label.config(text=f'Wynik: {losowa_liczba}')
    photo = new_photo

reset_button = ttk.Button(master=root, text='Reset', command=lambda: result_label.config(text=''))
reset_button.pack()

sab = ttk.Frame(master=root)
button = ttk.Button(master=sab, text='Rzuć Kością :)', command=losuj_kostka)
button.pack()
sab.pack()

canvas = tk.Canvas(root, width=0, height=0)
canvas.pack()

root.mainloop()
