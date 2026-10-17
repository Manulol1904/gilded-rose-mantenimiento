# -*- coding: utf-8 -*-
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gilded_rose import GildedRose, Item


def actualizar(nombre, sell_in, quality):
    item = Item(nombre, sell_in, quality)
    GildedRose([item]).update_quality()
    return item


class ReglasDeNegocio(unittest.TestCase):
    def test_item_normal_baja_calidad_en_uno(self):
        item = actualizar("+5 Dexterity Vest", 10, 20)
        self.assertEqual(item.sell_in, 9)
        self.assertEqual(item.quality, 19)

    def test_item_vencido_baja_calidad_en_dos(self):
        item = actualizar("Elixir of the Mongoose", 0, 10)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 8)

    def test_calidad_nunca_es_negativa(self):
        item = actualizar("+5 Dexterity Vest", 0, 1)
        self.assertEqual(item.quality, 0)
        agotado = actualizar("+5 Dexterity Vest", 5, 0)
        self.assertEqual(agotado.quality, 0)

    def test_aged_brie_sube_la_calidad(self):
        item = actualizar("Aged Brie", 2, 0)
        self.assertEqual(item.sell_in, 1)
        self.assertEqual(item.quality, 1)

    def test_calidad_no_supera_50(self):
        item = actualizar("Aged Brie", 5, 50)
        self.assertEqual(item.quality, 50)

    def test_sulfuras_no_cambia(self):
        item = actualizar("Sulfuras, Hand of Ragnaros", 0, 80)
        self.assertEqual(item.sell_in, 0)
        self.assertEqual(item.quality, 80)

    def test_backstage_sube_uno_si_faltan_mas_de_10_dias(self):
        item = actualizar("Backstage passes to a TAFKAL80ETC concert", 11, 20)
        self.assertEqual(item.quality, 21)

    def test_backstage_sube_dos_si_faltan_10_dias_o_menos(self):
        item = actualizar("Backstage passes to a TAFKAL80ETC concert", 10, 20)
        self.assertEqual(item.quality, 22)

    def test_backstage_sube_tres_si_faltan_5_dias_o_menos(self):
        item = actualizar("Backstage passes to a TAFKAL80ETC concert", 5, 20)
        self.assertEqual(item.quality, 23)

    def test_backstage_cae_a_cero_tras_el_concierto(self):
        item = actualizar("Backstage passes to a TAFKAL80ETC concert", 0, 20)
        self.assertEqual(item.sell_in, -1)
        self.assertEqual(item.quality, 0)

    def test_conjured_se_comporta_como_item_normal(self):
        conjured = actualizar("Conjured Mana Cake", 3, 6)
        normal = actualizar("+5 Dexterity Vest", 3, 6)
        self.assertEqual(conjured.sell_in, normal.sell_in)
        self.assertEqual(conjured.quality, normal.quality)
        self.assertEqual(conjured.quality, 5)


if __name__ == "__main__":
    unittest.main()
