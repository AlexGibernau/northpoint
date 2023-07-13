import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))

    image = PIL.Image.open(BytesIO(response.data)).resize((500, 500))
    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text="Es tipo: " f"{pokemon.types}")
    pokemon_weight.config(text="Pesa: " f"{pokemon.weight / 10}" + " kg")
    pokemon_hp.config(text="Salud: " f"{pokemon.base_stats.hp}")
    pokemon_def.config(text="Defensa: " f"{pokemon.base_stats.defense}")
    pokemon_sp_def.config(text="Defensa Especial: " f"{pokemon.base_stats.sp_def}")
    pokemon_attack.config(text="Ataque: " f"{pokemon.base_stats.attack}")
    pokemon_sp_atk.config(text="Ataque Especial: " f"{pokemon.base_stats.sp_atk}")
    pokemon_speed.config(text="5")


window = tk.Tk()
for r in range(0, 15):
    for c in range(0, 5):
        cell = tk.Entry(window, width=10)
        cell.grid(padx=5, pady=5, row=r, column=c)
        #cell.insert(0, "({},{})".format(r, c))


title_label = tk.Label(window, text="My pokedex", font=("Arial",32)).grid(pady=5,row=0,column=2)


label_id_name = tk.Label(window, text="Pon el id o el nombre",font=("Arial",20)).grid(pady=5,row=1,column=2)


text_id_name = tk.Text(window, height=1, width=20,font=("Arial",20)).grid(pady=5,row=2,column=2)


btn_load = tk.Button(window, text="Buscar", command=load_pokemon,font=("Arial",20)).grid(pady=5,row=3,column=2)


pokemon_information = tk.Label(window,font=("Arial",12)).grid(pady=5,row=5,column=0)

pokemon_image = tk.Label(window).grid(pady=5,row=6,column=0)

pokemon_types = tk.Label(window,font=("Arial",12)).grid(pady=5,row=7,column=0)

pokemon_weight = tk.Label(window)

pokemon_hp = tk.Label(window)

pokemon_def = tk.Label(window)

pokemon_sp_def = tk.Label(window)

pokemon_attack = tk.Label(window)

pokemon_sp_atk = tk.Label(window)

pokemon_speed = tk.Label(window)


window.mainloop()
