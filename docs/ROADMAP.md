# Genuino — Roadmap (documento vivo)

> La priorización global aún no está definida y no debe ser inventada por
> Claude Code. Cuando exista, debe priorizar los retos listados en
> 004_ARCHITECTURE.md y ser consistente con 003_FIRST_PRINCIPLES.md.
> Referencias actualizadas al esquema unificado de documentos (2026-07-17).

## Ya identificado como candidato a primer prototipo

- Un grafo de conceptos real (ver 003_FIRST_PRINCIPLES.md, principio 3, y
  006_KNOWLEDGE_ARCHITECTURE.md) — el proyecto propone que el conocimiento
  se represente como grafo vivo; el primer prototipo de eso debería ser el
  propio conocimiento acumulado del proyecto Genuino, no solo una idea
  teórica.

## Ideas de aplicaciones exploradas (no decisiones cerradas)

### "Concurso A4" (nombre provisional)

Una app de concurso de ideas: cada participante manda una hoja A4 con un
dibujo/mensaje/explicación de una idea. Mecánica:

1. Presentas tu hoja A4 a un concurso.
2. Te llegan dos hojas de otros participantes a tu "buzón".
3. Eliges la que más te gusta o con la que más estás de acuerdo.
4. Se va ganando en base a estas evaluaciones cruzadas.
5. Los concursos pueden ser de cualquier tamaño de grupo (5-6 personas,
   20-30, o globales).
6. Los concursos globales están asistidos por IA.
7. Se ingresa con identidad digital gestionada por el propio individuo
   (Genuino) — ninguna cuenta de plataforma tradicional.

**Rol de la IA en la evaluación (resuelto, con matiz):** preferencia por
evaluación puramente humana. Una IA simple puede intervenir donde sea
necesaria para que el proceso ocurra (ej. logística, emparejamiento) —
no como reemplazo del juicio humano, consistente con el principio "la IA
propone, el humano decide" (003_FIRST_PRINCIPLES.md, principio 4). Si en
el futuro la IA llega a evaluar contenido directamente (no solo facilitar
logística), debe cumplir el estándar de "IA garantizada"
(004_ARCHITECTURE.md).

**Tema de los concursos (resuelto):** ambos tipos existen — libres y de
tema específico.

**Mecánica de evaluación (resuelta, con nota):** eliminatoria directa
(bracket tipo torneo). El objetivo no es solo determinar un ganador — es
**extraer las mejores ideas**. Por eso la herramienta/mecanismo de
extracción debe poder evolucionar con el tiempo (no está grabado en
piedra que siempre sea bracket puro; puede mejorarse si aparece algo que
extraiga mejor las ideas valiosas).

**Selección de temas específicos (resuelta):** los temas salen de un
algoritmo que identifica temas en común entre los **árboles/grafos de
conocimiento de los participantes** (ver patrón "[Nombre] OS" en
001_ECOSYSTEM.md). De forma inicial, una IA elige los temas, priorizando
aquellos que ayuden al civismo colectivo y a armonizar la sociedad.

> **Conexión importante:** esto es la primera vez que dos piezas de
> Genuino se conectan funcionalmente, no solo filosóficamente — el
> concurso usa directamente el grafo de conocimiento personal (Erick OS /
> patrón "[Nombre] OS") como fuente de temas. Vale la pena tenerlo presente
> como ejemplo de por qué las apps no deberían diseñarse aisladas unas de
> otras.

### Economía del concurso

Participar tiene un costo, que puede ser tan bajo como satoshis. Ese costo
financia:

1. el premio para quien gana (en criptomoneda / Bitcoin);
2. los costos operativos del concurso.

Esto es la primera aplicación concreta de la capa económica descrita en
004_ARCHITECTURE.md (anclaje en blockchain / Bitcoin) — un concurso
autofinanciado, sin necesidad de un intermediario que cobre por publicidad
o venta de datos.

> **[PREGUNTA ABIERTA — mecanismo de pago]** ¿Cómo se gestiona el cobro y
> el pago del premio de forma no intermediada — vía la misma identidad
> digital de Genuino, una wallet asociada, o algo distinto?

### Genuino Social (nombre provisional)

Conocer personas comparando grafos «[Nombre] OS» (ver 001_ECOSYSTEM.md,
DECISIONS.md 2026-07-17). Es la continuación directa de la v1 original de
Genuino (perfil + preguntas + comparación lado a lado + score de
afinidad, ahora solo en el historial de git) — el mismo mecanismo, pero
aplicado a un grafo de nodos real en vez de un cuestionario fijo.

Mecánica esperada, a nivel de idea (no cerrada):

1. Dos personas exponen, cada una desde su propio nivel de soberanía,
   parte de su grafo «[Nombre] OS».
2. La app compara nodos y relaciones en común y señala diferencias — no
   solo respuestas idénticas, también conceptos relacionados o caminos
   parecidos dentro del grafo.
3. La compatibilidad de pareja es un caso particular de esta comparación
   general (aplica el mismo mecanismo a conocer amigos, colaboradores o
   comunidad) — no se diseña como una app de dating separada.

> **[PREGUNTA ABIERTA]** ¿Cuánto del grafo se expone por defecto y cuánto
> queda privado? ¿La comparación es un score numérico, una vista lado a
> lado, o ambas (como en v1)? Pendiente de definir con el fundador.

## Retos técnicos a priorizar (de 004_ARCHITECTURE.md)

Ver 004_ARCHITECTURE.md → sección "Retos identificados" para la lista
completa (nombres sin intermediarios, recuperación de llaves,
disponibilidad, costo de descentralización, spam/suplantación, migración
real).
