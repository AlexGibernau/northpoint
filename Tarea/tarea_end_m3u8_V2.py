import logging
import sys
import time

import m3u8

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)
master_url = sys.argv[1]
master_m3u8 = m3u8.load(master_url)
variant_selected = int(0)
if len(sys.argv) > 2:
    variant_selected = int(sys.argv[2])
logging.info("Start of cue out and cue in calculation")

variant_url = master_m3u8.playlists[variant_selected].absolute_uri

print(variant_url)


def find_cue(variant_m3u8):
    global time_cue_out, time_cue_in
    if "EXT-X-CUE-OUT:" in variant_m3u8.dumps():
        if time_cue_out is None:
            time_cue_out = time.time()
        logging.debug("EXT-X-CUE-OUT found")
    elif "EXT-X-CUE-IN" in variant_m3u8.dumps():
        if time_cue_in is None:
            time_cue_in = time.time()
        logging.debug("EXT-X-CUE-IN found")
    else:
        logging.debug("not happened")


time_cue_out = None
time_cue_in = None

while True:
    variant_m3u8 = m3u8.load(variant_url)
    find_cue(variant_m3u8)
    if time_cue_out is not None and time_cue_in is not None:
        tiempo_pasado = time_cue_in - time_cue_out
        logging.info(f"Time between CUE OUT and CUE IN: {tiempo_pasado:.2f} seconds")
        break
    time.sleep(1)
