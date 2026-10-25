"""DiRT 2's launch test, to see whether the car's physics keep their speed at another frame rate: from the "TERMINAL
DAMAGE" (or pause) menu, the race restarted with the throttle held, the screen filmed, and a sheet made of the race
clock beside the speedometer every half second of the clock's time, to read at the same clock times at 60 and at 120.

    py -3 scripts/arrancada.py rotulo [pausa]     from the pause menu (RESTART RACE below) or the damage one (to the right);
                                                  the sheet goes to arrancada_<rotulo>.png"""
import subprocess
import sys
import time
from pathlib import Path

from PIL import Image

sys.path.insert(0, str(Path(__file__).resolve().parent))
from port import ROOT  # noqa: E402
from qte import camera  # noqa: E402
from tecla import press  # noqa: E402


def main():
    label = sys.argv[1] if len(sys.argv) > 1 else 'teste'
    press('DOWN' if 'pausa' in sys.argv[2:] else 'RIGHT', 0.15)  # RESTART RACE / RESTART
    time.sleep(0.8)
    press('A', 0.2)
    time.sleep(1.5)
    press('A', 0.2)       # RESTART RACE? RESTART
    press('RT', 16)
    cam = camera()
    frames, t0 = [], time.time()
    while time.time() - t0 < 15:
        frames.append((time.time() - t0, cam.grab().copy()))
        time.sleep(0.1)
    cam.close()
    # the clock (top left) and the speedometer (bottom right), side by side, every 5th frame (half a second)
    tiles = []
    for t, im in frames[::5]:
        w, h = im.size
        clock = im.crop((60, 85, 180, 112)).resize((240, 54))
        speed = im.crop((int(w * 0.80), int(h * 0.80), int(w * 0.95), int(h * 0.90))).resize((240, 96))
        tile = Image.new('RGB', (480, 96))
        tile.paste(clock, (0, 20))
        tile.paste(speed, (240, 0))
        tiles.append(tile)
    cols = 3
    rows = (len(tiles) + cols - 1) // cols
    sheet = Image.new('RGB', (480 * cols, 96 * rows))
    for i, tile in enumerate(tiles):
        sheet.paste(tile, (480 * (i % cols), 96 * (i // cols)))
    sheet.save(ROOT / f'arrancada_{label}.png')
    print(f'{len(frames)} quadros; folha arrancada_{label}.png')


if __name__ == '__main__':
    main()
