# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
MIN_QUALITY = 0
MAX_QUALITY = 50
UMBRAL_BACKSTAGE_DOBLE = 11
UMBRAL_BACKSTAGE_TRIPLE = 6


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def _bajar_calidad(self, item):
        if item.quality > MIN_QUALITY:
            item.quality = item.quality - 1

    def _subir_calidad(self, item):
        if item.quality < MAX_QUALITY:
            item.quality = item.quality + 1

    def update_quality(self):
        for item in self.items:
            if item.name != AGED_BRIE and item.name != BACKSTAGE_PASSES:
                if item.name != SULFURAS:
                    self._bajar_calidad(item)
            else:
                self._subir_calidad(item)
                if item.name == BACKSTAGE_PASSES:
                    if item.sell_in < UMBRAL_BACKSTAGE_DOBLE:
                        self._subir_calidad(item)
                    if item.sell_in < UMBRAL_BACKSTAGE_TRIPLE:
                        self._subir_calidad(item)
            if item.name != SULFURAS:
                item.sell_in = item.sell_in - 1
            if item.sell_in < MIN_QUALITY:
                if item.name != AGED_BRIE:
                    if item.name != BACKSTAGE_PASSES:
                        if item.name != SULFURAS:
                            self._bajar_calidad(item)
                    else:
                        item.quality = item.quality - item.quality
                else:
                    self._subir_calidad(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
