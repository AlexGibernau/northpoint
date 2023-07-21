import requests
import time

def buscar_timing_anuncio(variant_url):
    try:
        response = requests.get(variant_url)
        response_text = response.text
        start_index = response_text.find("EXT-X-CUE-OUT:")
        end_index = response_text.find("EXT-X-CUE-IN", start_index)
        if start_index != -1 and end_index != -1:
            timing_anuncio = response_text[start_index + len("EXT-X-CUE-OUT:"):end_index].strip()
            return timing_anuncio
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
    return None

def buscar_variant0_m3u8(url):
    try:
        response = requests.get(url)
        if "variant0.m3u8" in response.text:
            variant_url = url[:url.rfind("/") + 1] + "variant0.m3u8"
            timing_anuncio = buscar_timing_anuncio(variant_url)
            if timing_anuncio:
                print(f"Se encontró el timing del anuncio: {timing_anuncio}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")

if __name__ == "__main__":
    link_en_vivo = "https://fast-tcseks01.thechannel.store/fast-channel-sin-filtros/fast-channel-sin-filtros.m3u8"
    
    while True:
        buscar_variant0_m3u8(link_en_vivo)
        time.sleep(60)  # Esperar 1 minuto antes de la siguiente verificación
