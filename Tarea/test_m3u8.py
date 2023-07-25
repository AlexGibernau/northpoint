import m3u8
import time

master_url = "https://fast-tcseks01.thechannel.store/fast-channel-sin-filtros/fast-channel-sin-filtros.m3u8"

master_m3u8 = m3u8.load(master_url)

variant0_url = master_m3u8.playlists[0].absolute_uri

def busca_cue(variant_m3u8):
    global time_cue_out, time_cue_in
    if "EXT-X-CUE-OUT:" in variant_m3u8.dumps():
        if time_cue_out is None:  
            time_cue_out = time.time()
        print("ENCONTRADO EL CUE OUT")
    elif "EXT-X-CUE-IN" in variant_m3u8.dumps():
        if time_cue_in is None: 
            time_cue_in = time.time()
        print("Encontrado el CUE IN")
    else:
        print("de momento nada")

time_cue_out = None
time_cue_in = None

while True:
    variant_m3u8 = m3u8.load(variant0_url)
    busca_cue(variant_m3u8)
    if time_cue_out is not None and time_cue_in is not None:
        tiempo_pasado = time_cue_in - time_cue_out
        print(f"Tiempo entre CUE OUT y CUE IN: {tiempo_pasado:.2f} segundos")
        break
    time.sleep(8)
