# Genuino

**Un protocolo abierto para representar, organizar y hacer evolucionar modelos internos de comprensión humana.**

Sin intermediarios. Sin plataforma dueña de tu información. Sin un único "feed" optimizado para retenerte.

---

## Qué es esto

Genuino parte de una idea simple: cada persona construye, a lo largo de su vida, un modelo interno con el que interpreta el mundo — conceptos, preguntas, experiencias, intuiciones, relaciones. Gran parte de ese modelo nunca llega a organizarse de una forma que se pueda compartir, revisar o hacer evolucionar.

Genuino no es una app. Es un protocolo (y un conjunto de aplicaciones de referencia que lo implementan) para representar esos modelos internos como un grafo de **nodos** y **relaciones**, de forma soberana e interoperable — cualquiera puede leerlo, implementarlo o construir algo nuevo encima.

La documentación completa de la visión, los principios y la arquitectura está en [`docs/`](docs/) — empezá por [`docs/000_VISION.md`](docs/000_VISION.md).

## Origen

La primera versión de este repositorio (mayo–julio 2026) era una app concreta: dos personas respondían las mismas preguntas y comparaban sus respuestas lado a lado, sin swipes ni feed. Esa mecánica de comparación no desapareció — se generalizó. Sigue viva como la idea de **Genuino Social**: comparar grafos completos en vez de un cuestionario fijo (ver [`docs/ROADMAP.md`](docs/ROADMAP.md)). La v1 original queda disponible en el historial de git.

## Estructura del repositorio

```
genuino/
├── docs/          # Documentación fundacional: visión, principios, arquitectura, decisiones, roadmap
├── erick-os/      # Primera implementación de referencia — grafo de conocimiento de una persona (en construcción)
├── salvacion/     # Prototipo previo (fichas sobre dinero/Bitcoin/descentralización) — donante del patrón visual/técnico de tarjetas
└── CLAUDE.md      # Instrucciones para agentes IA que trabajen en este repo
```

## Estado actual

Etapa de documentación y prototipo temprano. `erick-os/` y `salvacion/` tienen la estructura de navegación (mapa + tarjetas) armada, pero todavía sin contenido real — el primer paso pendiente es escribir nodos reales, no seguir expandiendo plantillas. Ver [`docs/ROADMAP.md`](docs/ROADMAP.md) y [`docs/DECISIONS.md`](docs/DECISIONS.md) para el estado detallado y las decisiones tomadas hasta ahora.

## Cómo correr los prototipos localmente

```bash
python3 -m http.server 8765 --directory /home/erick/repos/genuino
# erick-os:   http://localhost:8765/erick-os/
# salvacion:  http://localhost:8765/salvacion/
```

## GitHub

- Repo: `git@github.com:Erick-Osterling/genuino.git`
- Branch principal: `main`
