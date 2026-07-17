# Genuino — 002_NODE_MODEL.md

**Versión:** 0.2
**Estado:** Draft
**Cambios v0.2:** se añade la nota terminológica ficha = nodo (decisión del fundador, 2026-07-17). El resto del contenido permanece sin cambios respecto a v0.1.

---

# Nota terminológica

En documentos y código anteriores del proyecto (incluido el patrón técnico heredado de `salvacion/`: `ficha.css`, `ficha.js`), la unidad de significado se llamó **"ficha"**.

**"Ficha" y "Nodo" son sinónimos.** El término oficial y unificado del protocolo es **Nodo**. Toda referencia a "ficha" en código o documentación previa debe entenderse como Nodo; el término legacy podrá mantenerse en nombres de archivos existentes hasta que se refactoricen, pero no debe usarse en documentación ni código nuevo.

---

# Introducción

El Nodo constituye la unidad fundamental del protocolo Genuino.

Toda la información representada dentro del ecosistema se construye mediante nodos y las relaciones existentes entre ellos.

El protocolo no presupone una estructura jerárquica.

La complejidad surge de la combinación de muchos nodos simples.

---

# ¿Qué es un Nodo?

Un Nodo es una unidad de significado.

Representa cualquier elemento que una persona considere parte de su modelo interno.

No representa únicamente conocimiento verificable.

Puede representar conceptos, experiencias, preguntas, hipótesis, intuiciones, decisiones, recuerdos, proyectos o cualquier otra construcción mental.

El protocolo no limita aquello que puede representarse mediante un Nodo.

---

# La unidad mínima de significado

Idealmente, un Nodo representa una única idea suficientemente coherente como para poder comprenderse por sí misma.

Cuando un Nodo comienza a contener múltiples ideas independientes, probablemente deba dividirse en varios nodos relacionados.

No existe una regla absoluta.

La granularidad dependerá del contexto y de la utilidad para quien construye el modelo.

---

# Todo puede ser un Nodo

Ejemplos:

* una persona;
* un concepto;
* un país;
* una organización;
* una emoción;
* una experiencia;
* una conversación;
* una pregunta;
* una respuesta;
* una teoría;
* una definición;
* una decisión;
* un proyecto;
* una tarea;
* un libro;
* un artículo;
* un vídeo;
* una fotografía;
* un principio;
* una hipótesis;
* una cita;
* un algoritmo.

La lista permanece abierta.

---

# Un Nodo evoluciona

Los Nodos no son entidades estáticas.

Pueden:

* modificarse;
* ampliarse;
* resumirse;
* dividirse;
* fusionarse;
* especializarse;
* generalizarse.

El protocolo debe facilitar esa evolución.

---

# La evolución también es información

El estado actual de un Nodo representa únicamente una parte de su historia.

La evolución del propio Nodo constituye información valiosa.

Siempre que resulte posible, las implementaciones deberían conservar la trazabilidad de cambios importantes.

Comprender cómo evolucionó una idea puede aportar tanto valor como conocer su versión más reciente.

---

# El Nodo no conoce su ubicación

Un Nodo no pertenece a una única carpeta.

No posee una ubicación fija.

Puede participar simultáneamente en múltiples estructuras.

Las carpetas, colecciones o categorías constituyen únicamente distintas formas de visualizar el mismo conjunto de nodos.

---

# Etiquetas

Las etiquetas permiten clasificar nodos desde distintas perspectivas.

Un Nodo puede poseer tantas etiquetas como resulten útiles.

Las etiquetas son flexibles.

No sustituyen las relaciones.

---

# Relaciones

Las relaciones constituyen información de primera clase dentro del protocolo.

No representan únicamente enlaces.

Representan significado.

Ejemplos:

* explica;
* requiere;
* depende de;
* desarrolla;
* resume;
* inspira;
* ejemplifica;
* contradice;
* responde;
* continúa;
* deriva de;
* complementa.

La lista permanece abierta.

Las futuras aplicaciones podrán definir nuevos tipos de relaciones sin alterar la naturaleza del protocolo.

---

# Los atributos son abiertos

El protocolo no establece una lista cerrada de atributos.

Cada Nodo puede incorporar únicamente aquellos atributos que resulten útiles.

Ejemplos:

* identificador;
* título;
* descripción;
* tipo;
* estado;
* idioma;
* autor;
* fecha de creación;
* fecha de modificación;
* nivel de confianza;
* prioridad;
* etiquetas;
* referencias;
* relaciones;
* complejidad;
* fuentes.

La lista permanecerá abierta para permitir la evolución del protocolo.

---

# El significado también evoluciona

Un Nodo no solamente puede cambiar su contenido.

También puede cambiar la comprensión que su autor tiene acerca de él.

Una misma idea puede adquirir nuevos significados conforme evoluciona el conocimiento.

Por ello, las implementaciones deberían favorecer la conservación de esa evolución conceptual cuando resulte útil.

---

# Las vistas

Un mismo conjunto de Nodos puede representarse mediante múltiples vistas.

Por ejemplo:

* árbol;
* grafo;
* mapa mental;
* cronología;
* lista;
* tablero;
* documento;
* buscador.

Las vistas pertenecen a las aplicaciones.

No al protocolo.

---

# Independencia tecnológica

La definición conceptual de un Nodo es independiente de cualquier tecnología específica.

Puede almacenarse en:

* archivos;
* bases de datos;
* sistemas distribuidos;
* redes descentralizadas;
* futuras tecnologías.

El protocolo describe el significado.

No la implementación.

---

# La IA como asistente

La Inteligencia Artificial puede colaborar en la construcción de modelos internos.

Puede:

* sugerir nuevos nodos;
* detectar duplicados;
* encontrar contradicciones;
* descubrir relaciones;
* recomendar reorganizaciones;
* ayudar a estructurar información escrita libremente.

La decisión final siempre corresponde al usuario.

---

# Principio de simplicidad

La potencia del protocolo no debe provenir de la complejidad de cada Nodo.

Debe surgir de la combinación de muchos nodos simples y de relaciones bien definidas.

Siempre que exista una alternativa más simple y suficientemente expresiva, deberá preferirse.

---

# Nodo y Protocolo

El Nodo constituye el vocabulario básico de Genuino.

Las relaciones forman su gramática.

Las aplicaciones construyen diferentes formas de leer y escribir ese lenguaje común.

Esta separación permite que el ecosistema evolucione sin depender de una única implementación.

---

# Evolución

Esta especificación constituye un punto de partida.

La comprensión de qué representa un Nodo evolucionará mediante la experiencia obtenida durante el desarrollo de Erick OS y de futuras aplicaciones.

El protocolo deberá aprender junto con quienes lo utilicen.

La evolución forma parte de su diseño.

