#!/usr/bin/env python3
"""Rzut ukryty MG (Z172, `03-mg-zasady-prowadzenia.md` §2a).

Użycie:
  python -X utf8 rzut_mg.py "etykieta" P [--czas "pn 21 I 20:23"] [--nota "skutek"] [--log]

P to prawdopodobieństwo w procentach (1-99). Wynik: d100 <= P oznacza TAK.
Losowanie systemowe (SystemRandom). Z --log wiersz trafia do `mg-rzuty-ukryte.md`
(UTF-8, końce linii LF). Wyniku nie wolno zmieniać po fakcie.
"""
import argparse
import io
import os
import random

LOG = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "mg-rzuty-ukryte.md")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("etykieta")
    ap.add_argument("p", type=int)
    ap.add_argument("--czas", default="?")
    ap.add_argument("--nota", default="")
    ap.add_argument("--log", action="store_true")
    ap.add_argument("--plik", default=LOG)
    a = ap.parse_args()
    if not 1 <= a.p <= 99:
        ap.error("P musi być w zakresie 1-99")
    d = random.SystemRandom().randint(1, 100)
    wynik = "TAK" if d <= a.p else "NIE"
    print(f"{a.etykieta}: d100={d}, p={a.p}% -> {wynik}")
    if a.log:
        cell = lambda t: t.replace("|", "/").replace("\n", " ")
        row = f"| {cell(a.czas)} | {cell(a.etykieta)} | {a.p}% | {d} | {wynik} | {cell(a.nota)} |\n"
        path = os.path.normpath(a.plik)
        with io.open(path, "a", encoding="utf-8", newline="") as f:
            f.write(row)
        print("zapisano:", path)


if __name__ == "__main__":
    main()
