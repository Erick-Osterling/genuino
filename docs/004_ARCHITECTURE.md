# Genuino — 004_ARCHITECTURE.md

**Versión:** 0.2
**Estado:** Draft
**Cambios v0.2:** fusiona la arquitectura conceptual (borrador numerado) con las notas técnicas de ARCHITECTURE.md (producto central, niveles de soberanía, IA garantizada, anclaje en blockchain y retos identificados). Ninguna de las dos fuentes se contradecía; esta versión las integra.

---

# Introducción

Este documento describe la arquitectura conceptual y de producto del ecosistema Genuino.

No constituye una especificación técnica definitiva. Su objetivo es orientar las decisiones de diseño para que las distintas implementaciones evolucionen en una dirección coherente.

La arquitectura deberá poder cambiar conforme el proyecto madure, preservando siempre que sea posible la compatibilidad con los principios fundamentales (003_FIRST_PRINCIPLES.md).

---

# El producto central

Más que una aplicación, Genuino es un conjunto de **protocolos** que permiten a cualquier persona, con ayuda de IA garantizada, tener una página / identidad web no intermediada — su propio servidor sobre sí misma, en el sentido de control real sobre su presencia en internet.

---

# Capas del ecosistema

Genuino se organiza mediante capas relativamente independientes.

```text
Personas
    │
Aplicaciones
    │
Inteligencia Artificial
    │
Protocolos
    │
Identidad
    │
Infraestructura
```

Cada capa posee responsabilidades diferentes.

## Personas

Las personas constituyen el centro del ecosistema. Todo el diseño debe favorecer: comprensión, autonomía, propiedad de la información y libertad para crear nuevos modelos. Las demás capas existen para servir a las personas.

## Aplicaciones

Las aplicaciones resuelven problemas concretos. No constituyen el protocolo. Cada aplicación puede utilizar únicamente los protocolos que necesite, y diferentes aplicaciones pueden compartir exactamente los mismos protocolos.

## Inteligencia Artificial

La IA ocupa una posición intermedia. No reemplaza a las personas ni a los protocolos: facilita la interacción entre ambos. Entre sus posibles responsabilidades: estructurar información libre, sugerir relaciones, detectar inconsistencias, facilitar búsquedas, resumir modelos y generar distintas vistas.

## Protocolos

Los protocolos representan el lenguaje común del ecosistema. Definen estructuras, reglas, significado e interoperabilidad. Las aplicaciones evolucionan; los protocolos deberían cambiar con mucha menor frecuencia.

## Identidad

La identidad constituye una capa independiente. El protocolo no debería depender de un proveedor específico de identidad. Idealmente, cualquier mecanismo que permita identidad soberana podrá integrarse con el ecosistema. La identidad deberá ser portable.

## Infraestructura

La infraestructura debe permanecer desacoplada de los protocolos. Un mismo protocolo debería poder utilizarse sobre distintas tecnologías: archivos locales, Git, IPFS, Nostr, almacenamiento distribuido o futuros sistemas aún inexistentes.

---

# Niveles de soberanía (modelo híbrido)

No existe un único camino técnico. Existen niveles, y cada persona elige el suyo:

| Nivel | Descripción | Fricción | Soberanía real |
|---|---|---|---|
| Entrada | Ej. GitHub Pages u hosting convencional, pero con identidad y datos propios, portables | Baja | Parcial |
| Intermedio | Almacenamiento/cómputo descentralizado (tipo IPFS), datos en manos del individuo | Media | Alta |
| Avanzado | Infraestructura propia (nodo/servidor propio) | Alta | Máxima |

**Principio de diseño: el punto de entrada debe ser fácil. El camino hacia mayor soberanía debe estar siempre disponible, nunca cerrado** (principio 7 de 003_FIRST_PRINCIPLES.md).

La data en todos los niveles pertenece al individuo. Lo que cambia entre niveles es dónde y cómo se aloja/computa, no de quién es.

---

# IA garantizada

Cada persona elige libremente la IA con la que desea trabajar — incluida una IA local o un SLM personal. «Garantizada» no restringe esa elección; describe una propiedad deseable de cualquier IA, sin importar si es un agente externo grande o un modelo personal:

* su programación no debe ser incomprensible/opaca para un grupo confiable de la comunidad (auditable, no una caja negra imposible de revisar);
* distintas IA pueden tener programaciones muy diversas, y eso en sí mismo es un riesgo que la humanidad debe vigilar — no todo agente merece confianza por default;
* el objetivo central no es certificar contenido ni imponer un único proveedor: es **evitar la suplantación de identidad**. Un sistema sin gatekeeper central necesita que la confianza venga de la transparencia del agente, no de una autoridad que apruebe o rechace personas.

En resumen: «garantizada» ≈ auditable y transparente, aplicable por igual a un agente externo conocido o a un SLM local propio. La libertad de elección de IA es un principio no negociable; la transparencia de esa IA es la condición que la hace confiable dentro de Genuino.

El mecanismo concreto de «auditoría por grupo confiable» es una pregunta abierta de ingeniería/gobernanza (ver DECISIONS.md, pendientes).

---

# Independencia entre capas

Siempre que resulte posible:

* una aplicación puede cambiar sin modificar el protocolo;
* un protocolo puede evolucionar sin cambiar la infraestructura;
* una infraestructura puede reemplazarse sin alterar el significado de la información.

Reducir el acoplamiento constituye un objetivo permanente.

---

# Arquitectura Local First

Siempre que sea razonable, las implementaciones deberían considerar una filosofía *Local First*. La información pertenece al usuario. La sincronización constituye una capacidad adicional, no una condición necesaria para utilizar el sistema.

---

# Arquitectura modular

Cada componente debería tener una responsabilidad claramente definida. Las implementaciones deberán favorecer módulos pequeños, reutilizables y fácilmente reemplazables. La composición debe preferirse frente a grandes componentes monolíticos.

---

# Protocolos antes que APIs

Cuando una funcionalidad pueda expresarse mediante un protocolo abierto, debería preferirse frente a una API propietaria. Los protocolos sobreviven mejor que las implementaciones particulares.

---

# Versionado

Todos los protocolos deberán versionarse explícitamente. Las aplicaciones deberán declarar qué versiones soportan. Siempre que sea posible, deberá mantenerse compatibilidad hacia atrás.

---

# Evolución experimental

Las nuevas ideas deberían explorarse primero mediante implementaciones experimentales. Solo cuando una idea demuestre utilidad práctica debería proponerse su incorporación al protocolo (ver 008_PROTOCOL_EVOLUTION.md).

Erick OS constituye el principal laboratorio para realizar estos experimentos.

---

# Escalabilidad conceptual

La arquitectura debe permitir crecer sin aumentar innecesariamente la complejidad. Agregar nuevas aplicaciones no debería requerir modificar el núcleo del ecosistema. Agregar nuevos protocolos no debería romper los existentes.

---

# Seguridad

La seguridad deberá abordarse desde múltiples dimensiones: identidad, integridad, autenticidad, privacidad y verificabilidad. Las decisiones concretas dependerán de cada implementación.

---

# Descentralización

La descentralización constituye una herramienta, no un objetivo absoluto. Se utilizará cuando aporte beneficios reales al ecosistema. Las decisiones deberán justificarse por sus propiedades técnicas y sociales.

---

# Blockchain y anclaje de identidad

Las tecnologías blockchain pueden aportar: identidad, registro temporal, pagos, resistencia a la censura y verificación. No todas las aplicaciones necesitarán blockchain. Cuando se utilice, deberá hacerse por una necesidad concreta y no por preferencia tecnológica.

El uso previsto principal es el **anclaje**: un resumen eficiente y codificado de la identidad/grafo de pensamiento de cada persona se ancla en una blockchain para interoperabilidad y legitimación — no como almacenamiento completo (sería costoso e ineficiente), sino como prueba/referencia.

## Bitcoin

Bitcoin representa actualmente una de las tecnologías más relevantes para proporcionar: dinero soberano, verificabilidad temporal, resistencia a la censura y coordinación económica abierta. El anclaje descrito arriba podría realizarse posiblemente sobre Bitcoin, y el ecosistema podrá integrarse con Bitcoin cuando ello fortalezca los principios del proyecto.

No obstante, Genuino permanece conceptualmente independiente de cualquier blockchain específica y no construye su propia moneda.

---

# Retos identificados (para resolver o mitigar en ROADMAP.md)

1. **Nombres sin intermediarios** — cómo se encuentra a alguien sin DNS tradicional (ENS, Handshake, u opción propia).
2. **Recuperación de llaves** — pérdida de clave criptográfica = pérdida de identidad. Mayor punto de fricción de todo sistema soberano.
3. **Disponibilidad sin intermediario permanente** — qué garantiza que el contenido siga accesible sin una empresa de hosting cuidándolo.
4. **Costo de la descentralización** — la infraestructura verdaderamente descentralizada suele costar más / ser más lenta. Quién paga y cómo.
5. **Spam y abuso sin gatekeeper** — qué evita la suplantación de identidad en un sistema sin moderador central (irónico si ocurre, dado el nombre «Genuino»).
6. **Migración real** — la identidad debe poder moverse de un proveedor de infraestructura a otro sin pérdida, desde el diseño inicial.

---

# Estado de la arquitectura

Esta arquitectura constituye un mapa inicial. No pretende anticipar todas las decisiones futuras. Su propósito consiste en proporcionar una dirección suficientemente clara para que múltiples desarrolladores puedan colaborar sin perder coherencia.

Cada resolución de un reto o pregunta abierta debe registrarse también en DECISIONS.md.
