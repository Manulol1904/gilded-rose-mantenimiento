# -*- coding: utf-8 -*-
import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gilded_rose import GildedRose, Item

DATOS = Path(__file__).resolve().parent / "golden_master.json"


class GoldenMaster(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.datos = json.loads(DATOS.read_text(encoding="utf-8"))

    def test_todas_las_combinaciones_coinciden(self):
        for caso in self.datos["combinaciones"]:
            item = Item(caso["nombre"], caso["sell_in"], caso["quality"])
            GildedRose([item]).update_quality()
            self.assertEqual(item.sell_in, caso["sell_in_despues"], caso)
            self.assertEqual(item.quality, caso["quality_despues"], caso)

    def test_simulacion_de_40_dias_coincide(self):
        items = [
            Item(item["nombre"], item["sell_in"], item["quality"])
            for item in self.datos["items_iniciales"]
        ]
        for dia in self.datos["simulacion_40_dias"]:
            GildedRose(items).update_quality()
            obtenido = [
                {"nombre": item.name, "sell_in": item.sell_in, "quality": item.quality}
                for item in items
            ]
            self.assertEqual(obtenido, dia["items"], dia["dia"])
        self.assertEqual(len(self.datos["simulacion_40_dias"]), 40)


if __name__ == "__main__":
    unittest.main()
