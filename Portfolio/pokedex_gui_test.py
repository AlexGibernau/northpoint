import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO


def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))


    
    image = PIL.Image.open(BytesIO(response.data)).resize((500,500))
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
    pokemon_speed.config(text= "5")


window = tk.Tk()
window.geometry("920x800")
window.title("My Pokedex")
window.config(padx=10, pady=10)



title_label = tk.Label(window, text="My pokedex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

label_id_name = tk.Label(window, text="Pon el id o el nombre")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1, width=20)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=5, pady=5)

btn_load = tk.Button(window, text="Buscar", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 12))
pokemon_information.pack(padx=5, pady=5)

pokemon_image = tk.Label(window)
pokemon_image.pack(side="left")

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 12))
pokemon_types.pack()

pokemon_weight = tk.Label(window)
pokemon_weight.config(font=("Arial", 12))
pokemon_weight.pack(side="right")

pokemon_hp = tk.Label(window)
pokemon_hp.config(font=("Arial", 12))
pokemon_hp.pack(side="right")

pokemon_def = tk.Label(window)
pokemon_def.config(font=("Arial", 12))
pokemon_def.pack(side="right")

pokemon_sp_def = tk.Label(window)
pokemon_sp_def.config(font=("Arial", 12))
pokemon_sp_def.pack(side="right")

pokemon_attack = tk.Label(window)
pokemon_attack.config(font=("Arial", 12))
pokemon_attack.pack(side="right")

pokemon_sp_atk = tk.Label(window)
pokemon_sp_atk.config(font=("Arial", 12))
pokemon_sp_atk.pack(side="right")

pokemon_speed = tk.Label(window)
pokemon_speed.config(font=("Arial", 12))
pokemon_speed.pack(side="right")







window.mainloop()
