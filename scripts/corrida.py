"""DiRT 2 from a fresh start to the first career race's start line (Battersea, rallycross), for tests in a race: the
same steps that were found by hand, with a print at each stop in corrida/ to check where it went. The game asks for
the driver's details on every start (the profile is not kept between runs).

    py -3 scripts/corrida.py [--var REX_FPS=120 ...]      leaves the game running at the start line"""
import argparse
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from port import EXE, ROOT  # noqa: E402
from tecla import press  # noqa: E402

STEPS = [
    # (button, hold, wait after, print name)
    ('DOWN', 0.15, 0.7, None), ('DOWN', 0.15, 0.7, None), ('DOWN', 0.15, 0.7, None), ('DOWN', 0.15, 0.7, None),
    ('A', 0.2, 3, 'nome'),            # driver details: DONE
    ('A', 0.2, 3, None), ('A', 0.2, 4, None), ('A', 0.2, 4, 'mesa'),  # the spoken name, then the trailer's table
    ('DOWN', 0.15, 0.8, None), ('DOWN', 0.15, 0.8, None), ('DOWN', 0.15, 0.8, None),
    ('A', 0.2, 6, None), ('A', 0.2, 4, None), ('A', 0.2, 6, 'cartao'),  # the map and the event's card
    ('UP', 0.15, 0.8, None), ('UP', 0.15, 0.8, None), ('A', 0.2, 12, 'preparacao'),
    ('DOWN', 0.15, 0.8, None), ('DOWN', 0.15, 0.8, None), ('DOWN', 0.15, 0.8, None),
    ('A', 0.2, 8, 'carros'), ('A', 0.2, 3, None), ('A', 0.2, 3, None), ('A', 0.2, 8, 'submenu'),
    ('A', 0.2, 8, 'garagem'),       # SELECT FOR RACE
    ('A', 0.2, 25, 'largada'),      # RACE!
]


def shot(name):
    out = ROOT / 'corrida'
    out.mkdir(exist_ok=True)
    subprocess.run([sys.executable, '-I', str(ROOT / 'scripts' / 'ver.py')], capture_output=True)
    (out / f'{name}.png').write_bytes((ROOT / 'tela_agora.png').read_bytes())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--var', action='append', default=[])
    ap.add_argument('--segundos', type=int, default=3600)
    a = ap.parse_args()
    subprocess.run(['taskkill', '/F', '/IM', EXE.name], capture_output=True)
    time.sleep(3)  # the last run's process gone first
    args = [sys.executable, '-I', str(ROOT / 'scripts' / 'rodar.py'), '--y', '1000', '--segundos', str(a.segundos),
            '--prints', str(a.segundos - 1), '--pad', '12:START,20:START,25-60@3:A', '--var', 'REX_MOSTRAR_FPS=true']
    for v in a.var:
        args += ['--var', v]
    subprocess.Popen(args, cwd=ROOT, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    time.sleep(170)  # the opening video, the X Games intro and the trailer, to the driver's details
    shot('ficha')
    for button, hold, after, name in STEPS:
        press(button, hold)
        time.sleep(after)
        if name:
            shot(name)
    print('na largada (ver corrida/largada.png)')


if __name__ == '__main__':
    main()
