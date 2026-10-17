# -*- coding: utf-8 -*-
"""Renderiza un .txt de evidencia/ como PNG de terminal. No es una captura de pantalla."""
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

RAIZ = Path(__file__).resolve().parents[1]
FUENTES = [
    Path(r"C:\Windows\Fonts\consola.ttf"),
    Path(r"C:\Windows\Fonts\cour.ttf"),
    Path(r"C:\Windows\Fonts\DejaVuSansMono.ttf"),
]
COLUMNAS = 118
ALTO_LINEA = 18
MARGEN_X = 14
MARGEN_Y = 10
MAX_LINEAS = 42
FONDO = (12, 12, 12)
TEXTO = (204, 204, 204)
TITULO_FONDO = (32, 32, 32)
TITULO_TEXTO = (230, 230, 230)


def fuente(tamano):
    for ruta in FUENTES:
        if ruta.exists():
            return ImageFont.truetype(str(ruta), tamano)
    return ImageFont.load_default()


def trozos(linea, columnas):
    if linea == "":
        return [""]
    return [linea[i:i + columnas] for i in range(0, len(linea), columnas)]


def render(lineas, comando, destino):
    envueltas = []
    for linea in lineas:
        envueltas.extend(trozos(linea.rstrip("\n"), COLUMNAS))
    if not envueltas:
        envueltas = [""]
    bloques = [
        envueltas[i:i + MAX_LINEAS]
        for i in range(0, len(envueltas), MAX_LINEAS)
    ]
    letra = fuente(15)
    interfaz = fuente(13)
    ancho_char = max(letra.getlength("M"), 1)
    ancho = int(MARGEN_X * 2 + ancho_char * COLUMNAS)
    alto_titulo = 28
    rutas = []
    for indice, bloque in enumerate(bloques, start=1):
        alto = alto_titulo + MARGEN_Y * 2 + ALTO_LINEA * len(bloque)
        imagen = Image.new("RGB", (ancho, alto), FONDO)
        dibujo = ImageDraw.Draw(imagen)
        dibujo.rectangle((0, 0, ancho, alto_titulo), fill=TITULO_FONDO)
        dibujo.text((12, 6), comando, font=interfaz, fill=TITULO_TEXTO)
        y = alto_titulo + MARGEN_Y
        for linea in bloque:
            dibujo.text((MARGEN_X, y), linea, font=letra, fill=TEXTO)
            y += ALTO_LINEA
        if len(bloques) == 1:
            salida = destino
        else:
            salida = destino.with_name(f"{destino.stem}_{indice}{destino.suffix}")
        imagen.save(salida, "PNG")
        rutas.append(salida)
    return rutas


def main():
    if len(sys.argv) != 4:
        print("uso: render_terminal.py entrada.txt comando salida.png")
        return 1
    entrada = Path(sys.argv[1])
    comando = sys.argv[2]
    destino = Path(sys.argv[3])
    destino.parent.mkdir(parents=True, exist_ok=True)
    lineas = entrada.read_text(encoding="utf-8").splitlines()
    for ruta in render(lineas, comando, destino):
        print(ruta)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
