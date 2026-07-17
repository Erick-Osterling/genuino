# Genuino — 007_ERICK_OS.md

**Versión:** 0.2
**Estado:** Draft
**Cambios v0.2:** incorpora la presentación de nodos (idea fundacional de las fichas, hoy nodos) y la herencia técnica del patrón de `salvacion/`, provenientes de DECISIONS.md y de sesiones previas con el fundador. Terminología unificada: ficha = nodo (ver 002_NODE_MODEL.md).

---

# Introducción

Erick OS es la primera implementación de referencia del ecosistema Genuino.

No representa el protocolo.

No constituye un estándar.

Su propósito consiste en explorar, experimentar y descubrir nuevas formas de representar modelos internos utilizando los principios definidos por Genuino.

Todo aquello que demuestre resultar útil podrá, eventualmente, incorporarse al protocolo mediante un proceso explícito de documentación y consenso.

---

# Propósito

Erick OS pretende responder una pregunta:

> ¿Cómo podría una persona construir una representación digital útil de su propio modelo interno?

No intenta responder esa pregunta desde la teoría.

Pretende responderla mediante experimentación continua.

---

# Un laboratorio

Erick OS constituye un laboratorio permanente.

Aquí pueden explorarse ideas que todavía no forman parte del protocolo.

Por ejemplo:

* nuevas formas de organizar nodos;
* nuevas relaciones;
* nuevas vistas;
* nuevos atributos;
* nuevas formas de navegación;
* nuevas herramientas asistidas por IA.

No todas las ideas sobrevivirán.

Ese es precisamente el propósito del laboratorio.

---

# El usuario primero

Erick OS está diseñado inicialmente para una única persona.

Su objetivo consiste en comprender profundamente cómo una persona organiza su pensamiento antes de intentar generalizar esa experiencia.

La primera implementación no busca resolver el problema de millones de usuarios.

Busca comprender correctamente el problema.

---

# El modelo interno

Cada usuario posee un modelo interno distinto.

Erick OS permite construir una representación digital de ese modelo utilizando nodos, relaciones y vistas.

No intenta decirle al usuario cómo debe pensar.

Intenta ofrecer herramientas para organizar aquello que ya piensa.

---

# Los nodos evolucionan

Los nodos creados dentro de Erick OS no se consideran definitivos.

Pueden:

* dividirse;
* fusionarse;
* reorganizarse;
* cambiar de significado;
* adquirir nuevos atributos.

La evolución constituye una característica esperada del sistema.

---

# Las carpetas son una vista

En las primeras etapas podrán utilizarse carpetas por simplicidad.

Sin embargo, las carpetas no constituyen la organización fundamental.

Con el tiempo, los nodos podrán organizarse mediante:

* etiquetas;
* relaciones;
* colecciones;
* grafos;
* consultas;
* plantillas.

Las carpetas representan únicamente una vista más.

---

# La presentación de nodos en Erick OS

La primera interfaz de Erick OS presenta los nodos como tarjetas (históricamente llamadas "fichas") organizadas en un mapa/grafo navegable. Características definidas por el fundador:

* cada nodo puede declarar **prerrequisitos** (nodos que conviene comprender antes);
* cada nodo ofrece **niveles de profundidad** (Nivel 1 a 5: desde un resumen de dos minutos hasta la bibliografía completa);
* estados visuales de **bloqueado/desbloqueado** según los prerrequisitos recorridos;
* **caminos de navegación libres**: el lector elige su propia ruta por el grafo;
* **tono conversacional**, no académico ni de libro de texto.

Estas características son experimentos de Erick OS, no partes del protocolo. Si demuestran utilidad, podrán proponerse siguiendo el ciclo de 008_PROTOCOL_EVOLUTION.md.

---

# Herencia técnica

Erick OS reutiliza el patrón técnico de tarjetas del proyecto hermano `salvacion/` (`ficha.css` + `ficha.js` + mapa de tarjetas + tarjeta individual con diagrama/explicación/tags/caminos), con identidad visual propia (acento violeta/índigo en vez del verde de `salvacion/`) — mismo esqueleto, contenido y diseño distintos por instancia del patrón (ver DECISIONS.md, 2026-07-10).

El término "ficha" en esos archivos es legacy: conceptualmente son nodos (ver 002_NODE_MODEL.md, nota terminológica).

La estructura y el diseño se construyeron primero, con nodos de ejemplo; el contenido real de los nodos de Erick OS lo escribe el fundador.

---

# La IA como copiloto

La IA constituye un colaborador permanente.

Puede ayudar a:

* estructurar ideas;
* descubrir relaciones;
* detectar redundancias;
* proponer reorganizaciones;
* resumir información;
* sugerir nuevas conexiones.

No reemplaza al usuario.

Trabaja junto a él.

---

# La documentación es parte del desarrollo

Toda decisión importante descubierta durante la construcción de Erick OS deberá documentarse.

El conocimiento generado resulta tan valioso como el código.

La documentación forma parte del producto.

---

# Del experimento al protocolo

Cuando una característica demuestre utilidad de forma consistente, podrá seguir el siguiente camino:

Experimento → Validación → Documentación → Propuesta → Protocolo

No todo experimento debe convertirse en estándar.

---

# Compatibilidad

Siempre que resulte posible, Erick OS intentará mantenerse compatible con los protocolos definidos por Genuino.

Cuando necesite apartarse de ellos para experimentar, esa diferencia deberá quedar claramente documentada.

---

# Criterios de éxito

Erick OS no se evaluará por la cantidad de funcionalidades implementadas.

Se evaluará por su capacidad para responder preguntas como:

* ¿Representa mejor el pensamiento?
* ¿Facilita la comprensión?
* ¿Ayuda a organizar conocimiento?
* ¿Produce descubrimientos útiles para el protocolo?
* ¿Permite aprender cómo las personas organizan sus ideas?

---

# Investigación continua

Cada nueva funcionalidad constituye también una oportunidad para aprender.

El objetivo no consiste únicamente en desarrollar software.

Consiste en investigar nuevas formas de representación del conocimiento.

---

# Horizonte

Es probable que Erick OS evolucione durante muchos años.

Muchas de sus ideas desaparecerán.

Otras se convertirán en protocolos.

Y algunas darán origen a aplicaciones completamente nuevas que hoy todavía no podemos imaginar.

Ese proceso constituye una parte esencial del proyecto.
