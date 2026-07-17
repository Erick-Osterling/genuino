# Genuino — Decisions Log

> Bitácora cronológica. Cada decisión conceptual importante se registra
> aquí, corto, tipo bitácora. Este archivo SÍ puede y debe ser actualizado
> por cualquier agente (Claude, Claude Code) cuando se tome una decisión
> nueva — pero solo para registrar, nunca para decidir por su cuenta.

## 2026-07-09

- **Erick OS es individual**, no colectivo. Es la primera instancia del
  patrón general "[Nombre] OS": un esquema de pensamiento personal,
  representado como grafo de nodos (conceptos) con atributos. Lo
  colectivo está en el patrón (muchas personas con su propio OS
  interoperando), no en cada instancia individual.
- **Genuino es agnóstico de IA.** Cualquier persona puede usar un agente
  externo (Claude, ChatGPT, etc.) o un modelo propio (SLM personal). Ambos
  caminos son válidos, ninguno obligatorio.
- **Genuino es agnóstico de infraestructura de hosting.** Modelo híbrido de
  niveles de soberanía (entrada fácil tipo GitHub → almacenamiento
  descentralizado → nodo propio). La persona elige su nivel; los datos
  siempre son suyos, sin importar el nivel elegido.
- **Genuino es agnóstico de blockchain.** No construye su propia moneda.
  Es compatible con anclar identidad/grafo de pensamiento en una
  blockchain (posiblemente Bitcoin) como forma de legitimación —
  anclaje eficiente/codificado, no almacenamiento completo.
- **"IA garantizada" definida:** no restringe la libertad de elegir IA
  (incluida una IA local/SLM personal). Significa que la programación de
  la IA es transparente/auditable por un grupo confiable de la comunidad,
  no una caja negra. El objetivo central de este estándar es evitar la
  suplantación de identidad, no certificar contenido ni imponer un
  proveedor único.

## 2026-07-10

- **Erick OS arranca como carpeta nueva** (`/erick-os`) al mismo nivel que
  `genuino/` y `salvacion/` en este repo — no se resuelve todavía la
  pregunta abierta sobre monorepo "protocolos de libertad" vs. capas/apps
  independientes. Queda pendiente para sesión con el fundador.
  *(Resuelta el 2026-07-15, ver más abajo.)*
- **Erick OS reutiliza el patrón técnico de tarjetas de `salvacion/`**
  (`ficha.css` + `ficha.js` + mapa de tarjetas + tarjeta individual con
  diagrama/explicación/tags/caminos), pero con identidad visual propia
  (acento violeta/índigo en vez del verde de `salvacion/`) — mismo
  esqueleto, contenido y diseño distintos por instancia del patrón.
- **Se construyó estructura y diseño primero, contenido después**: dos
  nodos de ejemplo (`00-ejemplo.html`, `01-ejemplo.html`) que demuestran
  la anatomía de un nodo y cómo se conectan vía "caminos", sin inventar
  los nodos reales de Erick — esos los escribe el fundador.

## 2026-07-15

- **Arquitectura del proyecto: protocolo base + apps encima.** "Identidad"
  y "Protocolos" son capas de infraestructura, no aplicaciones al mismo
  nivel que Erick OS o Genuino Social. Un protocolo compartido para poseer
  y representar tu información, sobre el cual corren aplicaciones —
  preferiblemente de código abierto — que la aprovechan (Erick OS,
  Genuino Social, Concurso A4). No es un monorepo de apps independientes.
  Esto resuelve la pregunta abierta del 2026-07-10.
  *(Entrada registrada retroactivamente el 2026-07-17: la decisión se tomó
  el 15 pero no se había asentado en esta bitácora; confirmada por el
  fundador.)*

## 2026-07-17 — Sesión de conjugación documental

- **Listado único de documentos.** Los dos conjuntos de documentación
  (PROJECT/ARCHITECTURE/FIRST_PRINCIPLES/ROADMAP/DECISIONS/
  CLAUDE_CODE_INSTRUCTIONS y el conjunto numerado 000–009) se fusionan en
  una sola estructura numerada: `000`–`009` fundacionales + `ROADMAP.md` y
  `DECISIONS.md` como documentos vivos sin numerar. La información aditiva
  se sumó; las contradicciones se resolvieron una por una con el fundador.
- **FIRST_PRINCIPLES destilado y vigente (v1.0).** Los 6 candidatos
  originales y el borrador de 15 principios se fusionaron en 10 principios
  definitivos, aprobados por el fundador. Cuatro principios del borrador se
  degradaron a texto de apoyo. Ver 003_FIRST_PRINCIPLES.md.
- **Terminología unificada: ficha = nodo.** Son sinónimos; el término
  oficial del protocolo es **Nodo**. "Ficha" queda como nombre legacy en
  archivos existentes de `salvacion/` hasta que se refactoricen; no se usa
  en documentación ni código nuevo. Ver 002_NODE_MODEL.md.
- **Genuino Social conecta con el proyecto original.** Comparar dos grafos
  «[Nombre] OS» para conocer personas (amistad, comunidad, pareja) es la
  evolución natural del mecanismo de la v1 de Genuino (perfil + preguntas
  + reveal + score de afinidad, ver historial de git previo a esta
  reestructuración). La compatibilidad de pareja es un caso particular de
  la comparación general de grafos, no una aplicación aparte. Confirmado
  por el fundador. Ver 001_ECOSYSTEM.md y ROADMAP.md.
- **Se reestructura el repositorio `genuino`.** Deja de contener la app
  v1 (perfil/preguntas/reveal) como código activo — queda solo en el
  historial de git — y pasa a alojar la documentación fundacional del
  ecosistema (`docs/`) junto a los prototipos `erick-os/` y `salvacion/`.
  Confirmado por el fundador.

## Pendiente para próximas sesiones

- Definir mecanismo concreto de "auditoría por grupo confiable" para IA
  garantizada (pregunta de ingeniería/gobernanza, no filosófica).
- ROADMAP.md: priorizar retos técnicos de 004_ARCHITECTURE.md.
- Mecanismo de pago no intermediado del Concurso A4 (ver ROADMAP.md).
- Documento de gobernanza del proyecto (repos, contribuciones, flujo de
  trabajo) — planeado, aún sin posición en el listado.
