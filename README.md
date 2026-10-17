# Mantenimiento de Gilded Rose

Inventario de la tienda Gilded Rose, usado como componente análogo al sistema de ConstruYA: una regla de negocio nueva es una solicitud de cambio. El código parte del kata de Emily Bache, versión Python:

https://github.com/emilybache/GildedRose-Refactoring-Kata

La licencia original está en `LICENSE`. La clase `Item` y la propiedad `items` no se modifican. Un ítem cuyo nombre empieza por "Conjured" sigue comportándose como uno normal; esa regla no se implementó.

El código de producción que no es prueba suma 80 líneas (`gilded_rose.py` 46 y `texttest_fixture.py` 34). El detalle está en `evidencia/conteo_lineas.txt`.

## Estructura

- `gilded_rose.py`: clases `GildedRose` e `Item`.
- `actualizadores.py`: estrategias por tipo de producto.
- `texttest_fixture.py`: simulación de varios días, tomada del kata.
- `tests/`: golden master y pruebas de cada regla.
- `evidencia/`: salidas de pylint, lizard, coverage y unittest.
- `informe/`: informe técnico en LaTeX.

## Pruebas

```
python -m unittest discover -s tests -v
```

El golden master se generó una vez con `python tests/generar_golden_master.py` y no se vuelve a generar.

## Cobertura

```
python -m coverage run --branch --source=gilded_rose,actualizadores -m unittest discover -s tests
python -m coverage report -m
```

## Herramientas

| Uso | Herramienta |
| --- | --- |
| Estática | pylint 4.1.3 y lizard 1.24.1 (`lizard -C 10 -L 50`) |
| Dinámica | coverage.py 7.16.2 con ramas |
| Pruebas | unittest |

El informe está en `informe/main.pdf` (7 páginas).

## Repositorio

https://github.com/Manulol1904/gilded-rose-mantenimiento

La refactorización está en la rama `refactor/gilded-rose`. El merge a `main` es el tag `v1.0-refactor`.
