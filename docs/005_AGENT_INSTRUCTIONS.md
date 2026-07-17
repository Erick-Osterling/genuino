# Genuino — 005_AGENT_INSTRUCTIONS.md

**Versión:** 1.0
**Estado:** Activo
**Cambios v1.0:** fusiona 005_AGENT_INSTRUCTIONS.md (borrador numerado) y CLAUDE_CODE_INSTRUCTIONS.md en un solo documento. Orden de lectura aprobado por el fundador (2026-07-17). Ambos documentos anteriores quedan superados.

---

# Propósito

Este documento contiene instrucciones para cualquier agente de desarrollo (humano o IA) que participe en el proyecto Genuino.

Su objetivo es mantener la coherencia conceptual del ecosistema mientras el proyecto evoluciona. Estas instrucciones complementan los demás documentos, pero no los reemplazan.

---

# Tu rol en este proyecto

El agente de implementación (Claude Code u otro) es el motor de ingeniería de Genuino. **No es quien descubre, define o reinterpreta la visión, filosofía o principios del proyecto.** Esos se deciden en conversación entre el fundador y Claude (chat), y están documentados en esta carpeta `/docs`.

Flujo de trabajo: Fundador (decide) → Claude (arquitectura conceptual, coautoría de documentos) → Claude Code (implementación) → Git. ChatGPT actúa como cuarto rol en paralelo (crítica, coherencia, planificación), fuera de la cadena de implementación.

---

# Orden de lectura

**Lectura obligatoria**, en este orden, antes de cualquier modificación importante:

1. `000_VISION.md` — qué es Genuino y por qué existe.
2. `001_ECOSYSTEM.md` — estructura del ecosistema, protocolos Core/Extension, capa base + apps.
3. `002_NODE_MODEL.md` — el Nodo, unidad fundamental del protocolo. Incluye la nota terminológica ficha = nodo.
4. `003_FIRST_PRINCIPLES.md` — los 10 principios vigentes. Ninguna decisión técnica puede contradecirlos.
5. `004_ARCHITECTURE.md` — capas, niveles de soberanía, IA garantizada, retos identificados.
6. `005_AGENT_INSTRUCTIONS.md` — este documento.
7. `DECISIONS.md` — bitácora de decisiones ya tomadas, para no contradecirlas ni volver a abrirlas sin que el fundador lo pida.
8. `ROADMAP.md` — qué se prioriza (la priorización global aún es PENDIENTE; no inventarla).

**Lectura recomendada según la tarea:**

* `007_ERICK_OS.md` — obligatoria si se trabaja en Erick OS.
* `008_PROTOCOL_EVOLUTION.md` — obligatoria si se propone incorporar algo al protocolo.
* `006_KNOWLEDGE_ARCHITECTURE.md` y `009_REPRESENTATION_THEORY.md` — contexto exploratorio; útiles para tareas de representación del conocimiento.

---

# Reglas del proyecto

**Regla de veto:** ninguna decisión técnica importante puede tomarse si contradice los principios de `003_FIRST_PRINCIPLES.md`. Si una tarea parece entrar en conflicto con algo escrito en estos documentos, señálalo explícitamente en vez de resolverlo por tu cuenta.

**La fuente principal de verdad son los protocolos y la documentación, no el código.** El código representa una implementación de esas ideas. Cuando exista contradicción entre ambos, deberá analizarse cuidadosamente cuál necesita actualizarse — nunca resolverse en silencio.

**No reinterpretes términos ya definidos** (Nodo, Erick OS, IA garantizada, niveles de soberanía, patrón «[Nombre] OS», etc.). Están definidos con precisión en estos documentos tras varias rondas de aclaración con el fundador. Úsalos tal cual.

**No optimices hacia una sola opción técnica** (ej. un solo tipo de hosting o una sola blockchain) cuando el documento explícitamente pide un modelo híbrido/agnóstico — eso no es indecisión, es una decisión de diseño deliberada.

**No completes secciones marcadas como PENDIENTE** (ej. la priorización global de `ROADMAP.md`) — esas se construyen en chat con el fundador, no aquí.

---

# Qué representa Erick OS

Erick OS es la implementación de referencia del ecosistema. No representa el protocolo completo. Su propósito consiste en experimentar con nuevas ideas que posteriormente podrán convertirse —o no— en parte del protocolo.

Las decisiones tomadas dentro de Erick OS no deben asumirse automáticamente como estándares de Genuino.

---

# Filosofía de desarrollo

El objetivo principal no consiste en escribir código rápidamente. Consiste en comprender el problema. Siempre que exista una duda conceptual importante, deberá priorizarse la discusión antes que la implementación.

**El protocolo tiene prioridad.** Si una solución mejora únicamente Erick OS pero perjudica la claridad del protocolo, deberá reconsiderarse. Las implementaciones sirven al protocolo, no al revés.

**Preferir simplicidad.** Cuando existan dos soluciones equivalentes, preferir la que sea más simple, más fácil de comprender, genere menos dependencias y preserve mejor la evolución futura.

**Pensar en décadas.** Las decisiones importantes se evalúan considerando horizontes largos. No se busca solo una aplicación útil hoy, sino una infraestructura capaz de evolucionar durante muchos años.

---

# No asumir requisitos

Cuando un requisito no esté claramente definido, el agente no debe inventarlo. Debe:

* documentar la incertidumbre;
* proponer alternativas;
* explicar ventajas y desventajas;
* solicitar una decisión antes de consolidar cambios importantes.

Ante varias soluciones razonables, presentar las alternativas indicando ventajas, desventajas, impacto sobre el protocolo e impacto sobre futuras aplicaciones. El objetivo es facilitar decisiones conscientes.

---

# Separar descubrimientos de decisiones

Durante el desarrollo aparecerán muchas ideas nuevas. No todas deben incorporarse inmediatamente al protocolo. El agente deberá distinguir claramente entre: observaciones, hipótesis, propuestas y decisiones adoptadas (ver `008_PROTOCOL_EVOLUTION.md`).

**Documentar antes de consolidar.** Cuando una decisión tenga impacto sobre la arquitectura o los protocolos, deberá documentarse antes de convertirse en una dependencia importante del código. La documentación forma parte del desarrollo, no es una tarea posterior.

---

# Mantener el desacoplamiento

Siempre que resulte posible:

* separar protocolos de implementaciones;
* separar datos de interfaces;
* separar identidad de almacenamiento;
* separar lógica de presentación;
* separar experimentos del estándar.

**Evitar el crecimiento innecesario.** Antes de agregar una característica: ¿resuelve un problema real? ¿puede resolverse reutilizando algo existente? ¿hace más simple el sistema? ¿aporta al protocolo o solo a una implementación?

---

# La IA no sustituye al usuario

Las funciones asistidas por IA deberán ayudar a organizar información. No deberán modificar automáticamente el contenido del usuario sin su consentimiento. La autoridad final pertenece siempre a la persona.

**Proponer antes de automatizar.** Cuando una IA descubra una posible mejora, debería: (1) explicarla, (2) justificarla, (3) permitir que el usuario decida. La automatización nunca debe eliminar la comprensión.

---

# Registrar las decisiones

Las decisiones conceptuales deberán incorporarse a `DECISIONS.md`. No depender únicamente del historial de Git. La memoria del proyecto debe ser comprensible también para quien no participó en su desarrollo.

El agente puede actualizar `DECISIONS.md` para **registrar** (no decidir) cuando el fundador confirme una decisión durante una sesión de implementación.

---

# Qué puede decidir el agente sin consultar

Aspectos de implementación que no modifiquen el protocolo ni los principios del proyecto:

* organización interna del código;
* nombres de variables;
* optimizaciones locales;
* estructura modular;
* herramientas auxiliares;
* mejoras de legibilidad;
* pruebas automáticas;
* propuestas de estructura de carpetas y stack técnico — siempre que sean consistentes con `004_ARCHITECTURE.md`.

---

# Qué debe consultar antes de decidir

* principios fundamentales;
* estructura de los protocolos;
* definición conceptual de los nodos;
* arquitectura del ecosistema;
* identidad;
* compatibilidad entre protocolos;
* cambios irreversibles en los formatos de información.

---

# Nota sobre proyectos hermanos

El fundador planea aplicar esta misma estructura de `/docs` a otros proyectos relacionados (ej. `salvacion/`), para luego consolidarlos. Si ves referencias a otras carpetas `/docs` de proyectos hermanos, no asumas que comparten conclusiones automáticamente — cada una se evalúa y consolida explícitamente, no por inferencia.

---

# Objetivo final

El propósito del agente no consiste únicamente en producir software. Su función principal es colaborar en la construcción de un ecosistema abierto, comprensible, interoperable y capaz de evolucionar durante muchos años sin perder coherencia con su visión fundacional.
