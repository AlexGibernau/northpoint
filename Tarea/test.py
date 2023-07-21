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

def busca_cue():
    if "EXT-X-CUE-OUT:" in response.text:
        print("ENCONTRADO EL CUE OUT")
    elif "EXT-X-CUE-IN" in response.text:
        print("Encontrado el CUE IN")
    else:
        print("de momento nada")

if __name__ == "__main__":
    while True:
        response = requests.get(url_nueva)
        print(response.text)
        busca_cue()
        time.sleep(8)
