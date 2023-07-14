import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import ttk
import urllib3
from io import BytesIO


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response_default = http.request("GET", pokemon.sprites.front.get("default"))

    image = PIL.Image.open(BytesIO(response_default.data)).resize((250,250))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image_default.config(image=img)
    pokemon_image_default.image = img
    
    response_shiny = http.request("GET", pokemon.sprites.front.get("shiny"))

    image = PIL.Image.open(BytesIO(response_shiny.data)).resize((250,250))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image_shiny.config(image=img)
    pokemon_image_shiny.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text="Es tipo: " f"{pokemon.types}")
    pokemon_weight.config(text="Pesa: " f"{pokemon.weight / 10}" + " kg")
    pokemon_hp.config(text="Salud: " f"{pokemon.base_stats.hp}")
    pokemon_def.config(text="Defensa: " f"{pokemon.base_stats.defense}")
    pokemon_sp_def.config(text="Defensa Especial: " f"{pokemon.base_stats.sp_def}")
    pokemon_attack.config(text="Ataque: " f"{pokemon.base_stats.attack}")
    pokemon_sp_atk.config(text="Ataque Especial: " f"{pokemon.base_stats.sp_atk}")
    pokemon_speed.config(text="Velocidad: " f"{pokemon.base_stats.speed}")


window = tk.Tk()
for r in range(0, 15):
    for c in range(0, 5):
        cell = tk.Entry(window, width=10)
        #cell.grid(padx=5, pady=5, row=r, column=c)
        # cell.insert(0, "({},{})".format(r, c))


title_label = tk.Label(window, text="My pokedex", font=("Arial", 32))
title_label.grid(pady=5, row=0, column=0)


label_id_name = tk.Label(window, text="Pon el id o el nombre", font=("Arial", 20))
label_id_name.grid(pady=5, row=1, column=0)


text_id_name = tk.Text(window, height=1, width=20, font=("Arial", 20))
text_id_name.grid(pady=5, padx=5, row=2, column=0)


btn_load = tk.Button(window, text="Buscar", command=load_pokemon, font=("Arial", 20))
btn_load.grid(pady=5, row=3, column=0)


pokemon_information = tk.Label(window, font=("Arial", 12))
pokemon_information.grid(pady=5, row=4, column=0)

pokemon_image_default = tk.Label(window)
pokemon_image_default.grid(pady=5, row=5, column=0)

pokemon_image_shiny = tk.Label(window)
pokemon_image_shiny.grid(pady=5, row=5, column=1)


pokemon_types = tk.Label(window, font=("Arial", 12))
pokemon_types.grid(pady=5, row=6, column=0)

pokemon_weight = tk.Label(window, font=("Arial", 12))
pokemon_weight.grid(pady=5, row=7, column=0)

pokemon_hp = tk.Label(window, font=("Arial", 12))
pokemon_hp.grid(pady=5, row=8, column=0)

pokemon_def = tk.Label(window, font=("Arial", 12))
pokemon_def.grid(pady=5, row=9, column=0)

pokemon_sp_def = tk.Label(window, font=("Arial", 12))
pokemon_sp_def.grid(pady=5, row=10, column=0)

pokemon_attack = tk.Label(window, font=("Arial", 12))
pokemon_attack.grid(pady=5, row=11, column=0)

pokemon_sp_atk = tk.Label(window, font=("Arial", 12))
pokemon_sp_atk.grid(pady=5, row=12, column=0)

pokemon_speed = tk.Label(window, font=("Arial", 12))
pokemon_speed.grid(pady=5, row=13, column=0)


window.mainloop()