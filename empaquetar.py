"""Empaqueta index.html como .json con base64.

El Instructivo 44 no permite subir .html a Storage › Static, así que el archivo
viaja adentro de un .json y la página de descarga lo reconstruye en el celular.

Uso:  python empaquetar.py
"""

import base64
import datetime
import hashlib
import json
import pathlib

BASE = pathlib.Path(__file__).parent
HTML = BASE / "index.html"
SALIDA = BASE / "no-me-olvido.json"

html = HTML.read_bytes()

payload = {
    "app": "No me olvido",
    "archivo": "no-me-olvido.html",
    "tipo": "text/html",
    "version": 1,
    "generado": datetime.datetime.now().astimezone().isoformat(timespec="seconds"),
    "bytes": len(html),
    "sha256": hashlib.sha256(html).hexdigest(),
    "contenido_base64": base64.b64encode(html).decode("ascii"),
}

SALIDA.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"{SALIDA.name}: {SALIDA.stat().st_size / 1024:.0f} KB (html: {len(html) / 1024:.0f} KB)")
