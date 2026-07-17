# Genuino — 003_FIRST_PRINCIPLES.md

**Versión:** 1.0
**Estado:** Vigente (destilado y aprobado por el fundador, 2026-07-17)
**Origen:** fusión de los 6 principios candidatos del FIRST_PRINCIPLES.md original y los 15 principios del borrador numerado. La destilación se realizó en sesión con el fundador; el criterio de inclusión fue que cada principio pueda vetar una decisión técnica.

---

# Introducción

Este documento reúne los principios fundamentales del proyecto Genuino.

No describe implementaciones concretas. No define tecnologías específicas. Sirve como guía para todas las decisiones futuras.

**Regla del proyecto (definitiva):** ninguna decisión técnica importante puede tomarse si contradice los principios escritos aquí. Si una tarea parece entrar en conflicto con ellos, debe señalarse explícitamente antes de continuar.

Los principios podrán evolucionar, pero solo de forma explícita, documentada y aprobada por el fundador — con mucha menor frecuencia que cualquier implementación.

---

# Los principios

## 1. El protocolo es más importante que cualquier aplicación, y ninguna implementación lo representa

Las aplicaciones pueden aparecer, evolucionar o desaparecer. El protocolo debe aspirar a permanecer. Las aplicaciones implementan el protocolo; no lo definen. Erick OS es la primera implementación de referencia, pero otras implementaciones podrán tomar decisiones diferentes.

## 2. La identidad y la información pertenecen al individuo, nunca a una plataforma

Cada persona conserva el control sobre su identidad digital y sobre la información que decide compartir. La información nunca debe quedar innecesariamente cautiva dentro de una implementación específica. La identidad debe ser portable.

## 3. El conocimiento se representa como un grafo vivo de nodos y relaciones, no solo como documentos

Los documentos son una vista posible sobre el conocimiento, no su estructura fundamental. Este principio se aplica primero al propio proceso de trabajo del proyecto.

## 4. La IA asiste: propone, no decide

La IA no es autora, no decide y no es propietaria del pensamiento humano. Puede organizar, sugerir, comparar y descubrir relaciones. Las decisiones finales pertenecen siempre a las personas, y la IA no debe modificar el contenido del usuario sin su consentimiento.

## 5. La libertad de elegir IA es no negociable; la transparencia de esa IA es la condición que la hace confiable

Cualquier persona puede usar un agente externo o un modelo propio (incluido un SLM personal). Ninguna opción es obligatoria. La condición de confianza es el estándar de «IA garantizada»: programación auditable y transparente, orientada a evitar la suplantación de identidad (ver 004_ARCHITECTURE.md).

## 6. Agnosticismo tecnológico: de IA, de infraestructura y de blockchain

Genuino no depende de un proveedor de IA, de un tipo de hosting ni de una blockchain específica. Mientras más abierto, open source y transparente, mejor. Las decisiones tecnológicas no deben confundirse con los principios del protocolo.

## 7. El punto de entrada a la soberanía debe ser fácil; el camino hacia mayor soberanía debe estar siempre disponible, nunca cerrado

Existen niveles de soberanía y cada persona elige el suyo. Lo que cambia entre niveles es dónde y cómo se aloja la información, no de quién es (ver 004_ARCHITECTURE.md).

## 8. El protocolo no impone una visión del mundo

No determina qué ideas son correctas. No establece una filosofía oficial. No promueve una ideología. Cada persona conserva la libertad de construir su propia representación.

## 9. Simplicidad e interoperabilidad antes que complejidad y formatos nuevos

Un protocolo pequeño y bien comprendido vale más que uno completo pero difícil de implementar. La complejidad debe surgir por composición. La reutilización de estándares se prefiere frente a la creación innecesaria de nuevos formatos.

## 10. La evolución forma parte del diseño y se documenta

Ningún protocolo nace definitivo. Toda evolución importante debe documentarse para preservar la comprensión histórica del ecosistema. Durante las primeras etapas se prioriza comprender el problema antes que optimizar: aprender antes que optimizar.

---

# Principios absorbidos

Los siguientes conceptos del borrador de 15 principios no desaparecen: se degradaron de principio autónomo a texto de apoyo, y viven desarrollados en otros documentos:

* **Comprensibilidad de la representación** → absorbido por el principio 9; desarrollado en 002_NODE_MODEL.md.
* **El significado es más importante que el formato** → absorbido por los principios 3 y 9.
* **La información puede expresarse libremente (IA como traductor)** → absorbido por el principio 4; desarrollado en 001_ECOSYSTEM.md.
* **La comunidad es parte del diseño** → absorbido por el principio 6 (apertura); desarrollado en 001_ECOSYSTEM.md.

---

# Estado del documento

Este documento sustituye tanto al FIRST_PRINCIPLES.md marcado como PENDIENTE (6 candidatos) como al borrador de 15 principios. Ambos quedan superados por esta versión.

Nuevos principios podrán incorporarse cuando representen decisiones suficientemente estables, y su incorporación deberá registrarse en DECISIONS.md.
