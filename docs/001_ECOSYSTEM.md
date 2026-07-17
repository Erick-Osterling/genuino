# Genuino — 001_ECOSYSTEM.md

**Versión:** 0.3
**Estado:** Draft
**Cambios v0.2:** adopta la jerarquía Core / Extension para las familias de protocolos (decisión del fundador, 2026-07-17); incorpora el patrón «[Nombre] OS», la decisión «protocolo base + apps» (DECISIONS.md, 2026-07-15) y el flujo de trabajo del proyecto, provenientes de PROJECT.md.
**Cambios v0.3:** agrega descripción de Genuino Social — comparación de grafos «[Nombre] OS» para conocer personas, incluida compatibilidad de pareja como caso particular (decisión del fundador, 2026-07-17).

---

# Introducción

Genuino es un ecosistema abierto para el desarrollo de protocolos, aplicaciones y herramientas orientadas a representar, organizar y hacer evolucionar modelos internos de comprensión humana.

No es una única aplicación.

No es una única tecnología.

No depende de una empresa ni de una implementación específica.

El ecosistema está diseñado para evolucionar mediante protocolos abiertos que permitan la interoperabilidad entre distintas aplicaciones desarrolladas por diferentes personas o comunidades.

---

# Estructura general

El ecosistema Genuino se organiza en cuatro niveles principales.

```
Comunidad

↓

Protocolos

↓

Aplicaciones

↓

Usuarios
```

Cada nivel cumple una función distinta y puede evolucionar de forma relativamente independiente.

---

# La comunidad

La comunidad constituye el elemento que mantiene vivo el proyecto.

Su función es:

* proponer mejoras;
* discutir principios;
* mantener especificaciones;
* desarrollar implementaciones;
* revisar protocolos;
* compartir conocimiento.

Idealmente, la evolución del ecosistema debe distribuirse entre múltiples colaboradores y no depender de una única persona.

---

# Los protocolos

Los protocolos constituyen el núcleo de Genuino.

Definen cómo representar la información para que distintas aplicaciones puedan comprenderla e intercambiarla.

Los protocolos describen estructuras, formatos y reglas, pero no imponen una interfaz determinada.

Su objetivo es permitir la interoperabilidad.

Un protocolo bien diseñado puede sobrevivir durante décadas aunque las aplicaciones cambien completamente.

---

# Familias de protocolos: Core y Extension

Genuino no pretende resolver todos los problemas mediante un único protocolo. El ecosistema favorece múltiples protocolos pequeños, simples y bien definidos que puedan combinarse entre sí.

Los protocolos se organizan en dos niveles:

**Core Protocols** — los que toda implementación necesita para ser compatible con Genuino. Constituyen el vocabulario mínimo común del ecosistema:

* **Identidad** — quién es cada participante; identidad soberana y portable.
* **Nodos** (Knowledge Graph) — la unidad de significado (ver 002_NODE_MODEL.md).
* **Relaciones** — el significado entre nodos, información de primera clase.

**Extension Protocols** — opcionales, orientados a dominios o aplicaciones concretas. Una implementación puede adoptar solo los que necesite:

* Modelos internos.
* Reputación.
* Aprendizaje.
* Concursos (ej. Concurso A4).
* Coordinación (incluye mecanismos de votación).
* Conversaciones.

Ambas listas permanecen abiertas. La asignación inicial de cada familia a Core o Extension es una propuesta de partida: podrá ajustarse mediante el proceso de 008_PROTOCOL_EVOLUTION.md, y deberá registrarse en DECISIONS.md cuando cambie.

---

# La capa base y las aplicaciones

**Identidad y protocolos son capas de infraestructura, no aplicaciones** (ver DECISIONS.md, 2026-07-15). La arquitectura del ecosistema es protocolo base + apps encima: un protocolo compartido para poseer y representar tu información, sobre el cual corren aplicaciones — preferiblemente de código abierto — que la aprovechan.

Las aplicaciones utilizan uno o varios protocolos para resolver problemas concretos.

No representan el protocolo.

Lo implementan.

Pueden existir múltiples aplicaciones diferentes utilizando exactamente el mismo protocolo. Esto permite innovación sin fragmentar la información.

Componentes identificados hasta ahora:

* **Identidad / Protocolos** — capa base: dueño de tu información.
* **Erick OS** — app sobre la capa base (grafo de conocimiento personal).
* **Genuino Social** — app sobre la capa base: conocer personas comparando sus grafos «[Nombre] OS». Dos personas exponen (parcial o totalmente) su esquema de pensamiento y la app muestra puntos en común y diferencias — la evolución del mecanismo de la v1 original de Genuino (perfil + preguntas + comparación lado a lado + score de afinidad). La compatibilidad de pareja es un caso particular de esa comparación general de grafos, no una app aparte (ver ROADMAP.md).
* **Concurso A4** — app sobre la capa base (ver ROADMAP.md).
* **IA** — herramienta transversal, no autora.

---

# El patrón «[Nombre] OS»

Un «[Nombre] OS» es un esquema de pensamiento individual, representado como un grafo de **nodos** (conceptos) con atributos y relaciones entre ellos. Cada persona puede tener el suyo, si lo desea. El patrón es replicable: no existe «un» sistema operativo de pensamiento, existen tantos como personas lo adopten.

**Lo colectivo no está en ninguna instancia individual — está en el patrón.** Cuando muchas personas tienen su propio «[Nombre] OS» interoperando sobre el mismo protocolo, el proyecto se vuelve colectivo, sin que ningún esquema individual deje de pertenecerle a su dueño.

---

# Erick OS

Erick OS constituye la primera implementación de referencia del ecosistema: el esquema de pensamiento de una sola persona, no una combinación de varias (ver 007_ERICK_OS.md).

Su objetivo no consiste únicamente en resolver necesidades personales.

También funciona como laboratorio para descubrir cómo deben evolucionar los protocolos de Genuino.

Muchas decisiones experimentales podrán realizarse primero en Erick OS antes de incorporarse, si corresponde, a los protocolos generales.

---

# Otras aplicaciones

El ecosistema está diseñado para permitir la aparición de múltiples aplicaciones.

Entre las primeras ideas exploradas se encuentran:

* herramientas para representar modelos internos;
* aplicaciones para comparación de modelos;
* mecanismos de aprendizaje colectivo;
* concursos de ideas (como A4);
* sistemas de coordinación comunitaria;
* herramientas de investigación.

No existe un número limitado de aplicaciones posibles.

El protocolo debe permitir que aparezcan nuevas aplicaciones que hoy todavía no imaginamos.

---

# El papel de la Inteligencia Artificial

La Inteligencia Artificial forma parte del ecosistema como herramienta de asistencia.

Una de sus funciones más importantes consiste en actuar como traductor entre la expresión humana y los protocolos de Genuino.

Las personas deberían poder expresarse libremente.

Posteriormente, una IA puede ayudar a estructurar esa información utilizando los protocolos correspondientes.

La decisión final sobre la representación siempre pertenece al usuario.

---

# Niveles de estructuración

El ecosistema debe permitir distintos niveles de formalización.

Por ejemplo:

1. Expresión libre.
2. Interpretación asistida por IA.
3. Representación mediante protocolos básicos.
4. Representación mediante protocolos especializados.
5. Uso por aplicaciones.

De este modo, una persona no necesita conocer los detalles técnicos del protocolo para participar.

---

# Interoperabilidad

Toda aplicación desarrollada dentro del ecosistema debería intentar reutilizar protocolos existentes antes de crear nuevos.

La interoperabilidad constituye uno de los objetivos centrales de Genuino.

Siempre que dos aplicaciones utilicen el mismo protocolo, deberán poder intercambiar información sin pérdida significativa.

---

# Flujo de trabajo del proyecto

```
Fundador (decide)
      ↓
Claude (pensamiento, arquitectura conceptual, coautoría de documentos)
      ↓
Claude Code (implementación, ingeniería)
      ↓
Git
```

ChatGPT actúa como cuarto rol: arquitectura conceptual, crítica, coherencia filosófica y planificación — en paralelo, no en la cadena de implementación.

Los documentos fundacionales se actualizan por consenso entre fundador y Claude antes de propagarse a Claude Code (ver 005_AGENT_INSTRUCTIONS.md).

---

# Evolución

Los protocolos evolucionarán.

Las aplicaciones evolucionarán.

La comunidad evolucionará.

El ecosistema está diseñado para permitir esa evolución sin romper innecesariamente la compatibilidad con versiones anteriores.

---

# Lo que Genuino no es

Genuino no es:

* una red social;
* un gestor de notas;
* una blockchain;
* una inteligencia artificial;
* una única aplicación;
* una empresa;
* una ideología;
* una religión.

Puede utilizar tecnologías relacionadas con algunos de estos conceptos.

Puede inspirar aplicaciones similares.

Pero su propósito consiste en proporcionar una infraestructura abierta sobre la que puedan construirse muchas soluciones diferentes.

---

# Principio de apertura

El éxito del ecosistema no dependerá de que exista una aplicación dominante.

Dependerá de que cualquier persona pueda comprender los protocolos, implementarlos, extenderlos y construir nuevas herramientas compatibles.

La apertura constituye uno de los principios fundamentales de Genuino.
