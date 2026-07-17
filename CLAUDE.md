# Genuino — CLAUDE.md

Punto de entrada para Claude Code. Este repositorio contiene la
documentación fundacional del proyecto Genuino, unificada y aprobada por
el fundador el 2026-07-17.

## Antes de hacer cualquier cosa

Lee `docs/005_AGENT_INSTRUCTIONS.md`. Ahí está tu rol, el orden de
lectura obligatorio y las reglas del proyecto. Resumen mínimo:

1. **Lectura obligatoria en orden:** `docs/000_VISION.md` →
   `docs/001_ECOSYSTEM.md` → `docs/002_NODE_MODEL.md` →
   `docs/003_FIRST_PRINCIPLES.md` → `docs/004_ARCHITECTURE.md` →
   `docs/005_AGENT_INSTRUCTIONS.md` → `docs/DECISIONS.md` →
   `docs/ROADMAP.md`.
2. **Según la tarea:** `docs/007_ERICK_OS.md` (si trabajas en Erick OS),
   `docs/008_PROTOCOL_EVOLUTION.md` (si propones algo al protocolo),
   `docs/006_KNOWLEDGE_ARCHITECTURE.md` y
   `docs/009_REPRESENTATION_THEORY.md` (contexto exploratorio).

## Reglas no negociables

- Ninguna decisión técnica importante puede contradecir
  `docs/003_FIRST_PRINCIPLES.md` (10 principios, vigentes). Si hay
  conflicto, señálalo; no lo resuelvas por tu cuenta.
- La documentación es la fuente de verdad, no el código.
- Tú implementas; la visión y los principios se deciden entre el fundador
  y Claude (chat). No los reinterpretes ni los completes.
- Registra (no decidas) en `docs/DECISIONS.md` cuando el fundador
  confirme una decisión durante una sesión contigo.
- Términos definidos que se usan tal cual: **Nodo** (= "ficha", término
  legacy), **Erick OS**, **IA garantizada**, **niveles de soberanía**,
  **patrón «[Nombre] OS»**.
- No completes secciones marcadas como PENDIENTE (ej. la priorización
  global de `docs/ROADMAP.md`).

## Estado actual del proyecto

- Documentación fundacional unificada (2026-07-17): `000`–`009` +
  `ROADMAP.md` + `DECISIONS.md`. Versiones y decisiones registradas en
  `docs/DECISIONS.md`.
- Candidato a primer prototipo (ver `docs/ROADMAP.md`): un grafo de
  conceptos real cuyo primer contenido sea el propio conocimiento
  acumulado del proyecto Genuino.
- Existe trabajo previo de Erick OS fuera de este árbol: carpeta
  `/erick-os` junto a `genuino/` y `salvacion/`, que reutiliza el patrón
  técnico de tarjetas de `salvacion/` (`ficha.css`, `ficha.js`) con
  acento violeta/índigo. Ver `docs/007_ERICK_OS.md` y `docs/DECISIONS.md`
  (2026-07-10).

## Cómo trabajar

Comprender antes que programar. Simplicidad antes que sofisticación.
Proponer alternativas ante la incertidumbre, con ventajas y desventajas,
y pedir decisión al fundador antes de consolidar cambios importantes.
