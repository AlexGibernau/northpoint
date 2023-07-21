import requests
import time

url = "https://fast-tcseks01.thechannel.store/fast-channel-sin-filtros/fast-channel-sin-filtros.m3u8"
url_requests = requests.get(url)

url_nueva = ""

def buscador():
    global url_nueva
    if "variant_0.m3u8" in url_requests.text:
        url_nueva = url.replace("fast-channel-sin-filtros.m3u8", "variant_0.m3u8")
    else:
        print("no se ha encontrado ninguna variante")

buscador()

response = requests.get(url_nueva)

time_cue_out = None
time_cue_in = None

def busca_cue():
    global time_cue_out, time_cue_in
    if "EXT-X-CUE-OUT:" in response.text:
        if time_cue_out is None:  
            time_cue_out = time.time()
        print("ENCONTRADO EL CUE OUT")
    elif "EXT-X-CUE-IN" in response.text:
        if time_cue_in is None: 
            time_cue_in = time.time()
        print("Encontrado el CUE IN")
    else:
        print("de momento nada")


if __name__ == "__main__":
    while True:
        response = requests.get(url_nueva)
        busca_cue()
        if time_cue_out is not None and time_cue_in is not None:
            tiempo_pasado = time_cue_in - time_cue_out
            print(f"Tiempo entre CUE OUT y CUE IN: {tiempo_pasado:.2f} segundos")
            break
        time.sleep(8)
