# -*- coding: utf-8 -*-
"""Genera tests/golden_master.json con el comportamiento original. Se ejecuta una sola vez."""
import json
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ))

from gilded_rose import GildedRose, Item

NOMBRES = [
    "+5 Dexterity Vest",
    "Aged Brie",
    "Elixir of the Mongoose",
    "Sulfuras, Hand of Ragnaros",
    "Backstage passes to a TAFKAL80ETC concert",
    "Conjured Mana Cake",
]
SULFURAS = "Sulfuras, Hand of Ragnaros"
SALIDA = Path(__file__).resolve().parent / "golden_master.json"

ITEMS_FIXTURE = [
    Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
    Item(name="Aged Brie", sell_in=2, quality=0),
    Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
    Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
    Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
    Item(name="Conjured Mana Cake", sell_in=3, quality=6),
]


def estado(item):
    return {"nombre": item.name, "sell_in": item.sell_in, "quality": item.quality}


def un_dia(nombre, sell_in, quality):
    item = Item(nombre, sell_in, quality)
    GildedRose([item]).update_quality()
    return {
        "nombre": nombre,
        "sell_in": sell_in,
        "quality": quality,
        "sell_in_despues": item.sell_in,
        "quality_despues": item.quality,
    }


def main():
    combinaciones = []
    for nombre in NOMBRES:
        calidades = list(range(0, 51))
        if nombre == SULFURAS:
            calidades.append(80)
        for sell_in in range(-3, 16):
            for quality in calidades:
                combinaciones.append(un_dia(nombre, sell_in, quality))

    items = list(ITEMS_FIXTURE)
    iniciales = [estado(item) for item in items]
    dias = []
    for dia in range(1, 41):
        GildedRose(items).update_quality()
        dias.append({"dia": dia, "items": [estado(item) for item in items]})

    SALIDA.write_text(
        json.dumps(
            {
                "items_iniciales": iniciales,
                "combinaciones": combinaciones,
                "simulacion_40_dias": dias,
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"combinaciones={len(combinaciones)}")
    print(f"dias={len(dias)}")
    print(f"archivo={SALIDA}")


if __name__ == "__main__":
    main()
