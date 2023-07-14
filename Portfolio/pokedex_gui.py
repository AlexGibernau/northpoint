import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
from tkinter import ttk
import urllib3
from io import BytesIO


def update_progress():
    # Obtener los valores de las estadísticas del Pokémon
    hp = int(pokemon.base_stats.hp)
    attack = int(pokemon.base_stats.attack)
    defense = int(pokemon.base_stats.defense)
    sp_atk = int(pokemon.base_stats.sp_atk)
    sp_def = int(pokemon.base_stats.sp_def)
    speed = int(pokemon.base_stats.speed)

    # Actualizar el valor de cada barra de progreso
    progress_bar_hp["value"] = hp
    progress_bar_attack["value"] = attack
    progress_bar_defense["value"] = defense
    progress_bar_sp_atk["value"] = sp_atk
    progress_bar_sp_def["value"] = sp_def
    progress_bar_speed["value"] = speed

    # Cambiar el color de cada barra de progreso según el valor
    color_hp = "#%02x%02x%02x" % (255 - 2 * hp, 2 * hp, 0)
    style.configure(
        "HP.Horizontal.TProgressbar", troughcolor=color_hp, background=color_hp
    )

    color_defense = "#%02x%02x%02x" % (255 - 2 * defense, 2 * defense, 0)
    style.configure(
        "Defense.Horizontal.TProgressbar",
        troughcolor=color_defense,
        background=color_defense,
    )

    color_sp_def = "#%02x%02x%02x" % (255 - 2 * sp_def, 2 * sp_def, 0)
    style.configure(
        "SpDef.Horizontal.TProgressbar",
        troughcolor=color_sp_def,
        background=color_sp_def,
    )

    color_attack = "#%02x%02x%02x" % (255 - 2 * attack, 2 * attack, 0)
    style.configure(
        "Attack.Horizontal.TProgressbar",
        troughcolor=color_attack,
        background=color_attack,
    )

    color_sp_atk = "#%02x%02x%02x" % (255 - 2 * sp_atk, 2 * sp_atk, 0)
    style.configure(
        "SpAtk.Horizontal.TProgressbar",
        troughcolor=color_sp_atk,
        background=color_sp_atk,
    )

    color_speed = "#%02x%02x%02x" % (255 - 2 * speed, 2 * speed, 0)
    style.configure(
        "Speed.Horizontal.TProgressbar", troughcolor=color_speed, background=color_speed
    )

    # Mostrar las barras de progreso
    progress_bar_hp.grid()
    progress_bar_defense.grid()
    progress_bar_sp_def.grid()
    progress_bar_attack.grid()
    progress_bar_sp_atk.grid()
    progress_bar_speed.grid()


def load_pokemon():
    global pokemon

    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))
    http = urllib3.PoolManager()

    response_default = http.request("GET", pokemon.sprites.front.get("default"))
    image_default = PIL.Image.open(BytesIO(response_default.data)).resize((250, 250))
    img_default = PIL.ImageTk.PhotoImage(image_default)
    pokemon_image_default.config(image=img_default)
    pokemon_image_default.image = img_default

    response_shiny = http.request("GET", pokemon.sprites.front.get("shiny"))
    image_shiny = PIL.Image.open(BytesIO(response_shiny.data)).resize((250, 250))
    img_shiny = PIL.ImageTk.PhotoImage(image_shiny)
    pokemon_image_shiny.config(image=img_shiny)
    pokemon_image_shiny.image = img_shiny

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text="Es tipo: " f"{format_types()}")
    pokemon_weight.config(text="Pesa: " f"{pokemon.weight / 10}" + " kg")
    pokemon_hp.config(text="Salud: " f"{pokemon.base_stats.hp}")
    pokemon_def.config(text="Defensa: " f"{pokemon.base_stats.defense}")
    pokemon_sp_def.config(text="Defensa Especial: " f"{pokemon.base_stats.sp_def}")
    pokemon_attack.config(text="Ataque: " f"{pokemon.base_stats.attack}")
    pokemon_sp_atk.config(text="Ataque Especial: " f"{pokemon.base_stats.sp_atk}")
    pokemon_speed.config(text="Velocidad: " f"{pokemon.base_stats.speed}")

    update_progress()


def format_types():
    return ", ".join(pokemon.types)


window = tk.Tk()

style = ttk.Style()
style.theme_use("default")

style.configure("HP.Horizontal.TProgressbar", troughcolor="red", background="red")
style.configure("Attack.Horizontal.TProgressbar", troughcolor="blue", background="blue")
style.configure(
    "Defense.Horizontal.TProgressbar", troughcolor="green", background="green"
)
style.configure(
    "SpAtk.Horizontal.TProgressbar", troughcolor="purple", background="purple"
)
style.configure(
    "SpDef.Horizontal.TProgressbar", troughcolor="orange", background="orange"
)
style.configure(
    "Speed.Horizontal.TProgressbar", troughcolor="yellow", background="yellow"
)

progress_bar_hp = ttk.Progressbar(
    window,
    style="HP.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_hp.grid(row=8, column=1, pady=5)
progress_bar_hp.grid_remove()  # Ocultar la barra de progreso al inicio

progress_bar_defense = ttk.Progressbar(
    window,
    style="Defense.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_defense.grid(row=9, column=1, pady=5)
progress_bar_defense.grid_remove()  # Ocultar la barra de progreso al inicio

progress_bar_sp_def = ttk.Progressbar(
    window,
    style="SpDef.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_sp_def.grid(row=10, column=1, pady=5)
progress_bar_sp_def.grid_remove()  # Ocultar la barra de progreso al inicio

progress_bar_attack = ttk.Progressbar(
    window,
    style="Attack.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_attack.grid(row=11, column=1, pady=5)
progress_bar_attack.grid_remove()  # Ocultar la barra de progreso al inicio

progress_bar_sp_atk = ttk.Progressbar(
    window,
    style="SpAtk.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_sp_atk.grid(row=12, column=1, pady=5)
progress_bar_sp_atk.grid_remove()  # Ocultar la barra de progreso al inicio

progress_bar_speed = ttk.Progressbar(
    window,
    style="Speed.Horizontal.TProgressbar",
    orient="horizontal",
    length=200,
    mode="determinate",
)
progress_bar_speed.grid(row=13, column=1, pady=5)
progress_bar_speed.grid_remove()  # Ocultar la barra de progreso al inicio

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
