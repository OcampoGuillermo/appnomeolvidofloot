# No me olvido

Agenda de vencimientos para el día a día, en un solo archivo HTML.

## Qué es

Una app de una sola pantalla que responde a una tarea repetitiva: revisar fechas y
acordarse de trámites, pagos y entregas. Cargás un vencimiento una vez; la app calcula
cuántos días faltan, lo ordena por urgencia y, si se repite, genera la próxima fecha sola.

## Para quién

Una persona, en su celular, con dos contextos conviviendo: **casa** (luz, agua,
alquiler) e **instituto** (entregas, exámenes, planillas). Para clasificar, la app
ofrece cinco ámbitos: Casa, Instituto, Salud, Trámites y Otros. El filtro por ámbito
permite ver solo un contexto cuando hace falta.

## Qué resuelve

- No tener que recordar fechas mentalmente ni revisar una libreta.
- No volver a cargar el mismo vencimiento todos los meses.
- Ver de un vistazo qué está vencido, qué vence hoy y qué viene.

## Alcance (v1)

- Alta, edición y borrado de vencimientos: título, ámbito, fecha, repetición, aviso, notas.
- Repetición: una vez, semanal, mensual, anual. Al marcarlo listo, se crea la siguiente fecha.
- Vistas: Próximos · Todo · Resueltos. Filtro por ámbito.
- Historial de resueltos con deshacer.
- Respaldo: exportar e importar JSON. Copiar resumen para WhatsApp.
- Funciona sin internet y sin cuentas. Los datos viven en `localStorage`.

## Fuera de alcance (v1)

- Varios usuarios o datos compartidos (eso pediría Floot con base de datos).
- Avisos por mail o notificaciones push.
- Sincronización entre dispositivos.

## Restricciones técnicas

- Un solo archivo `.html`, sin dependencias externas ni fuentes remotas.
- Tiene que abrirse desde `file://` y desde un celular.
- Publicable con el Instructivo 44 (empaquetado `.json` → Floot).

## Dirección visual

**Un instrumento de precisión, no un tablero de marketing.** La pantalla se lee de
arriba abajo: fecha de hoy, el vencimiento que más urge, el resto. Sin métricas
decorativas ni tarjetas dentro de tarjetas.

- **Tipografía:** Schibsted Grotesk variable (OFL 1.1), embebida en el HTML. Numerales
  tabulares para fechas y cuentas; una sola familia para toda la interfaz.
- **Color:** monocromo cálido (papel y tinta) con una sola señal naranja reservada
  para lo vencido o urgente. El hero es la única superficie oscura en modo claro.
- **Estructura:** listas agrupadas tipo *inset* (Vencido · Hoy · Esta semana · Más
  adelante), separadores que no llegan al borde, control segmentado con indicador
  deslizante y hojas de edición con pie fijo.
- **Movimiento:** resortes cortos (hojas 420 ms, indicador 340 ms), presión a escala
  `.985`, check que se dibuja. Todo se apaga con `prefers-reduced-motion`.
- **Accesibilidad:** contraste AA verificado en claro y oscuro, foco visible, trampa
  de foco en las hojas, `Esc` y *scrim* para cerrar, filas completas como objetivo
  táctil y checks con área de 44 px.

## Principios

- Privacidad por defecto: nada sale del dispositivo.
- La urgencia se lee en un segundo, sin abrir nada.
- Hecho con IA, revisado por una persona; se declara en Ajustes.
