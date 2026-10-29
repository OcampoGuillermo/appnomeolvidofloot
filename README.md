# No me olvido

Agenda de vencimientos en un solo archivo. Funciona sin internet, sin cuentas y sin servidor.

**Abrir:** doble clic en `index.html`.

---

## Qué hace

- Cargás un vencimiento una vez: título, ámbito (Casa / Instituto / Salud / Trámites / Otros), fecha, repetición y aviso.
- La app calcula cuántos días faltan y ordena todo por urgencia: **Vencido · Hoy · Esta semana · Más adelante**.
- Al marcarlo listo, si se repite, genera sola la próxima fecha (semanal, mensual o anual).
- Historial de resueltos con deshacer.
- Filtro por ámbito y tres vistas: **Próximos**, **Todo**, **Resueltos**.
- Respaldo completo en `.json` y resumen para copiar a WhatsApp.

## Dónde quedan los datos

En el `localStorage` del navegador, bajo la clave `no-me-olvido:v1`.
**Nada sale del dispositivo**: no hay servidor, no hay cuentas, no hay analítica.

Si se borran los datos del navegador, se pierde todo. Por eso conviene
**Ajustes → Descargar respaldo** de vez en cuando.

## Publicar en Floot (Instructivo 44)

1. Generar el paquete:

   ```powershell
   python empaquetar.py
   ```

   Eso crea `no-me-olvido.json` con el HTML adentro, en base64, más `bytes` y
   `sha256` para verificar que la descarga llegue intacta.

2. Subir `no-me-olvido.json` a **Storage › Static**.

3. La página de descarga de la app toma ese `.json` y reconstruye el archivo:

   ```js
   const bin = atob(payload.contenido_base64);
   const bytes = Uint8Array.from(bin, (c) => c.charCodeAt(0));
   const url = URL.createObjectURL(new Blob([bytes], { type: payload.tipo }));
   // descargar como payload.archivo
   ```

4. En el celular: abrir el `.html` descargado y usar **Agregar a pantalla de inicio**.

> Si cambiás `index.html`, volvé a correr `empaquetar.py`. El `.json` no se actualiza solo.

El prompt exacto para pegar en Claude/Floot, la lógica de verificación y la
prueba en celular están en **`PUBLICAR.md`**.

## Estructura de un vencimiento

```js
{
  id: "abc123",
  titulo: "Pagar la luz",
  ambito: "casa",              // casa | instituto | salud | tramites | otros
  fecha: "2026-11-03",         // ISO, fecha local
  repeticion: "mensual",       // unica | semanal | mensual | anual
  aviso: 3,                    // 0 | 1 | 3 | 7 | 15 días antes
  notas: "",
  creado: 1761686400000,
  resueltoEl: null,            // "2026-10-28" cuando se marca listo
  siguienteId: null            // id del siguiente vencimiento, si se repite
}
```

## Límites conocidos

- **No manda notificaciones push ni mails.** El aviso se ve al abrir la app
  (la pestaña *Próximos* filtra por la ventana de aviso de cada vencimiento).
- Es de un solo dispositivo: no sincroniza entre celular y computadora.
  Para eso haría falta la versión con base de datos en Floot.
- Hecha con IA y revisada por una persona: para fechas críticas, verificá
  siempre contra el papel o el sitio oficial.

## Archivos

| Archivo | Qué es |
| --- | --- |
| `index.html` | La app completa (HTML + CSS + JS, sin dependencias externas). |
| `empaquetar.py` | Genera el `.json` con base64, `bytes` y `sha256` para publicar en Floot. |
| `PUBLICAR.md` | Prompt para Floot, verificación del hash y prueba en celular. |
| `checkpack.py` | Verifica que el `.json` reconstruya el HTML byte a byte. |
| `incrustar-fuente.py` | Reemplaza la tipografía embebida por otro `.woff2` local. |
| `PRODUCT.md` | Decisión de producto: alcance, principios y límites. |

## Créditos

- Tipografía: **Schibsted Grotesk** (Copyright 2023 The Schibsted-Grotesk
  Project Authors), SIL Open Font License 1.1, embebida en el HTML como
  `woff2` + base64. No se descarga desde ningún servidor.
