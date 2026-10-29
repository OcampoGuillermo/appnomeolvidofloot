r"""Reemplaza la fuente embebida en index.html por un woff2 local.

Uso:
  python incrustar-fuente.py ruta\SchibstedGrotesk-Variable.woff2 "Schibsted Grotesk"

Busca el @font-face embebido (src:url("data:font/woff2;base64,...")) y cambia
el binario. Si se pasa el nombre de familia, actualiza también el @font-face y
el token --ui para que no queden desincronizados.
"""
import base64
import pathlib
import re
import sys

raiz = pathlib.Path(__file__).resolve().parent
html = raiz / "index.html"
if len(sys.argv) < 2:
    print(__doc__)
    raise SystemExit(1)

fuente = pathlib.Path(sys.argv[1])
familia = sys.argv[2] if len(sys.argv) > 2 else None
texto = html.read_text(encoding="utf-8")
b64 = base64.b64encode(fuente.read_bytes()).decode("ascii")

patron = r'src:url\("data:font/woff2;base64,[^"]+"\) format\("woff2"\);'
nuevo, n = re.subn(
    patron,
    'src:url("data:font/woff2;base64,' + b64 + '") format("woff2");',
    texto,
    count=1,
)
if n != 1:
    print("No se encontró el @font-face embebido en index.html.")
    raise SystemExit(1)

if familia:
    nuevo, n1 = re.subn(
        r'(@font-face\{[^}]*?font-family:")[^"]+(")',
        lambda m: m.group(1) + familia + m.group(2),
        nuevo,
        count=1,
    )
    nuevo, n2 = re.subn(r'(--ui:")[^"]+(",)', lambda m: m.group(1) + familia + m.group(2), nuevo, count=1)
    if not (n1 and n2):
        print("Aviso: no se pudo actualizar el nombre de familia; revisalo a mano.")
    else:
        print(f"Familia actualizada: {familia}")

html.write_text(nuevo, encoding="utf-8")
print(f"Incrustada: {fuente.name} ({len(b64)} caracteres base64)")
print(f"index.html: {html.stat().st_size} bytes")
