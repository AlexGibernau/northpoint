import m3u8
import time

master_url = "https://fast-tcseks01.thechannel.store/fast-channel-sin-filtros/fast-channel-sin-filtros.m3u8"

master_m3u8 = m3u8.load(master_url)

variant0_url = master_m3u8.playlists[0].absolute_uri
while True:
    variant_m3u8 = m3u8.load(variant0_url)
    print(variant_m3u8.segments[0].absolute_uri)
    time.sleep(6)