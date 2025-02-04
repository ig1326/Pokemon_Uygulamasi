import requests
import tkinter as tk
from tkinter import Label, Entry, Button
from PIL import Image, ImageTk
from io import BytesIO


def get_pokemon_data():
    pokemon_name = entry.get().lower()
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        image_url = data["sprites"]["front_default"]
        image_response = requests.get(image_url)
        image_data = Image.open(BytesIO(image_response.content))
        image_data = image_data.resize((150, 150))
        img = ImageTk.PhotoImage(image_data)

        label_image.config(image=img)
        label_image.image = img

        types = ", ".join([t["type"]["name"].capitalize() for t in data["types"]])

        stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}

        info_text = f"""
        Adı: {data['name'].capitalize()}
        Tür: {types}
        Saldırı: {stats['attack']}
        Savunma: {stats['defense']}
        Hız: {stats['speed']}
        """
        label_info.config(text=info_text)
    else:
        label_info.config(text="Pokemon bulunamadı!")

pokemon_window = tk.Tk()
pokemon_window.title("Pokemon Bilgi Ekranı")
pokemon_window.geometry("300x400")

entry = Entry(pokemon_window, font=("Arial", 14))
entry.pack(pady=10)

btn = Button(pokemon_window, text="Pokemon Bilgilerini Getir", command=get_pokemon_data)
btn.pack()

label_image = Label(pokemon_window)
label_image.pack()

label_info = Label(pokemon_window, text="", font=("Arial", 12), justify="left")
label_info.pack(pady=10)

pokemon_window.mainloop()
