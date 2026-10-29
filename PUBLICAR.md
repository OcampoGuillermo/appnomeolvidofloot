# Publicar en Floot (Instructivo 44)

## Paquete listo

| Dato | Valor |
| --- | --- |
| Archivo para subir | `no-me-olvido.json` (165 KB) |
| HTML que reconstruye | `no-me-olvido.html` |
| Tamaño del HTML | 126.817 bytes |
| SHA-256 | `e61754fedf49d59c3cc6532d9d7c9704fb8fe4a82500eecd678926317231e711` |
| Generado | 2026-10-28 22:14 (UTC-3) |

El `.json` incluye `bytes`, `sha256`, `generado` y `contenido_base64`.
La página de descarga tiene que comparar el hash del HTML decodificado con
`payload.sha256` antes de entregarlo.

> Si volvés a tocar `index.html`, corré `python empaquetar.py`. Cambian el hash
> y el tamaño: actualizá la página de descarga antes de publicar.

## Prompt para pegar en Claude (con el conector de Floot)

Adjuntá `no-me-olvido.json` y pegá esto:

```text
Tengo un programa en un solo archivo HTML, "No me olvido" (agenda de
vencimientos), ya empaquetado para Floot en `no-me-olvido.json` (base64,
165 KB). Quiero publicarlo con una página de descarga, como el Instructivo 44.

Datos del paquete:
- HTML: no-me-olvido.html
- bytes: 126817
- SHA-256: e61754fedf49d59c3cc6532d9d7c9704fb8fe4a82500eecd678926317231e711
- generado: 2026-10-28T22:14:02-03:00

Hacé esto:

1. Creá un proyecto en Floot llamado "No me olvido" y una página de descarga
   con esta identidad: papel cálido #f4f3ef, tinta #17160f, una sola señal
   naranja #b93a0e, tipografía grotesca (Schibsted Grotesk o la más parecida
   disponible), mucho aire, sin gradientes ni tarjetas dentro de tarjetas.
   Que se vea como una herramienta de precisión, no como una landing.

2. La página tiene tres partes:
   - **Descargar al celular**: baja `no-me-olvido.json` de Storage › Static,
     decodifica `contenido_base64`, verifica que el SHA-256 del HTML coincida
     con `payload.sha256` y descarga `no-me-olvido.html` como `text/html`.
     Si la huella no coincide, no descarga y muestra un error claro.
   - **Abrir acá, sin descargar**: abre el HTML decodificado en una pestaña
     nueva con una blob URL. Aclaración visible: para que los datos se guarden,
     conviene descargar el archivo y abrirlo desde el celular.
   - **Cómo usarlo**: tres pasos: descargar, abrir el archivo, "Agregar a
     pantalla de inicio".
   - Pie: "Hecha con IA, revisada por una persona. Los datos quedan en tu
     dispositivo."

3. Abrí una tarjeta de subida para que yo suba `no-me-olvido.json` a
   Storage › Static.

4. Cuando lo suba, conectá el archivo, verificá que la descarga y la huella
   funcionen, y publicá en `no-me-olvido.floot.app` (o el subdominio corto
   que esté libre).

5. Pasame el link publicado y probalo como si fueras un celular.

No cambies el HTML: la app ya está probada y el hash tiene que dar exacto.
```

## Si lo hacés a mano

1. Entrá a [floot.com](https://floot.com) → **Log in** con la misma cuenta del
   conector.
2. Abrí el proyecto → **Storage › Static** → **Upload** → `no-me-olvido.json`.
3. En la página de descarga, la lógica mínima es:

   ```js
   const payload = await (await fetch(URL_DEL_JSON)).json();
   const bytes = Uint8Array.from(atob(payload.contenido_base64), c => c.charCodeAt(0));

   const hash = [...new Uint8Array(await crypto.subtle.digest('SHA-256', bytes))]
     .map(b => b.toString(16).padStart(2, '0')).join('');
   if (hash !== payload.sha256) throw new Error('El archivo no coincide');

   const url = URL.createObjectURL(new Blob([bytes], { type: payload.tipo }));
   const a = document.createElement('a');
   a.href = url;
   a.download = payload.archivo;   // no-me-olvido.html
   a.click();
   ```

4. Publicá y probá en un celular real antes de compartir.

## Prueba en el celular

- [ ] “Descargar” baja `no-me-olvido.html` (124 KB).
- [ ] Al abrirlo se ve la app, con la fecha de hoy.
- [ ] “Nuevo vencimiento” guarda; al cerrar y volver a abrir, sigue ahí.
- [ ] “Ajustes → Descargar respaldo” baja un `.json`.
- [ ] “Abrir acá” abre la app, pero para guardar datos usá el archivo descargado.

## Límites que conviene decir

- Los datos viven en el `localStorage` del navegador de ese celular. No hay
  cuentas, servidor ni sincronización.
- No manda mails ni notificaciones: los avisos se ven al abrir la app.
- Es una versión de un solo dispositivo. La versión con base de datos de Floot
  es otro entregable (usuarios, datos compartidos y mail automático).
