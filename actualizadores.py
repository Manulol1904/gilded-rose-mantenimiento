# -*- coding: utf-8 -*-

AGED_BRIE = "Aged Brie"
SULFURAS = "Sulfuras, Hand of Ragnaros"
BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
MIN_QUALITY = 0
MAX_QUALITY = 50
UMBRAL_BACKSTAGE_DOBLE = 11
UMBRAL_BACKSTAGE_TRIPLE = 6


def bajar_calidad(item):
    if item.quality > MIN_QUALITY:
        item.quality = item.quality - 1


def subir_calidad(item):
    if item.quality < MAX_QUALITY:
        item.quality = item.quality + 1


def actualizar_normal(item):
    bajar_calidad(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in >= MIN_QUALITY:
        return
    bajar_calidad(item)


def actualizar_brie(item):
    subir_calidad(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in >= MIN_QUALITY:
        return
    subir_calidad(item)


def actualizar_backstage(item):
    subir_calidad(item)
    if item.sell_in < UMBRAL_BACKSTAGE_DOBLE:
        subir_calidad(item)
    if item.sell_in < UMBRAL_BACKSTAGE_TRIPLE:
        subir_calidad(item)
    item.sell_in = item.sell_in - 1
    if item.sell_in >= MIN_QUALITY:
        return
    item.quality = item.quality - item.quality


def actualizar_sulfuras(_item):
    return


DESPACHO = {
    AGED_BRIE: actualizar_brie,
    BACKSTAGE_PASSES: actualizar_backstage,
    SULFURAS: actualizar_sulfuras,
}


def actualizar_item(item):
    DESPACHO.get(item.name, actualizar_normal)(item)
