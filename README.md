# genuino

**Algoritmo descentralizado de organización colectiva.**

Una infraestructura abierta para la conexión humana sin intermediarios. Sin algoritmos que optimicen para el conflicto. Sin empresas que moneticen la atención. Sin dueño.

---

## La idea

Las plataformas de dating y redes sociales no optimizan para que las personas se encuentren — optimizan para que sigan usando la plataforma. El conflicto entre géneros genera más tiempo en pantalla que la armonía. Es su modelo de negocio.

**genuino** propone lo opuesto: dos personas responden las mismas preguntas, comparan sus respuestas, y deciden si quieren contactarse. Sin swipes, sin likes, sin feed. El perfil del creador está firmado criptográficamente — las respuestas estaban ahí antes de que vos llegaras, y podés verificarlo.

El principio es simple: **sacar al intermediario**. El mismo principio de Bitcoin aplicado a las relaciones humanas.

---

## Cómo funciona (v1)

1. **Manifiesto** — contexto sobre por qué esto existe
2. **Perfil** — respuestas del creador, hasheadas con SHA-256, verificables
3. **Preguntas** — 4 niveles, de lo cotidiano a lo esencial
4. **Reveal** — comparación lado a lado + score de afinidad
5. **Bitcoin** — por qué el dinero descentralizado importa, y cómo empezar

Todo corre en el browser. Sin backend. Sin base de datos. Sin cookies.

---

## Estructura del proyecto

```
genuino/
├── index.html          # Manifiesto y entrada
├── profile.html        # Perfil del creador — respuestas verificables
├── questions.html      # Flujo de 4 niveles de preguntas
├── reveal.html         # Comparación de respuestas + score
├── learn.html          # Introducción a Bitcoin
├── assets/
│   ├── style.css       # Tokens de diseño compartidos
│   ├── questions.json  # Banco de preguntas — editable por la comunidad
│   └── profile.json    # Respuestas del perfil — hasheables
├── crypto/             # v2 — firma y verificación criptográfica
│   ├── sign.js
│   └── verify.js
└── nostr/              # v3 — identidad descentralizada
    ├── publish.js
    └── identity.js
```

---

## Hoja de ruta

### v1 — Cascarón estático ✅
- HTML + CSS + JSON. Cero backend.
- Deployable en IPFS o GitHub Pages.
- Preguntas en `questions.json` — cualquiera puede proponer cambios via PR.
- Hash SHA-256 de respuestas calculado en el browser (Web Crypto API).

### v2 — Firma criptográfica
- Anclar el hash de las respuestas en Bitcoin via [OpenTimestamps](https://opentimestamps.org) — sin transacción costosa, sin sobrecargar la red.
- Flujo de onboarding para wallets Bitcoin open source (Phoenix, Muun, Sparrow).
- Cualquiera puede crear su propio perfil copiando el formato de `profile.json`.

### v3 — Identidad descentralizada
- Integración con [Nostr](https://nostr.com): las respuestas se publican como eventos firmados con clave privada.
- [DID](https://www.w3.org/TR/did-core/) opcional: un humano verificado, una identidad, sin revelar datos personales.
- Micropagos Lightning para participar — costo mínimo (satoshis), compartido entre todos los participantes.

### v4 — Protocolo abierto
- El formato de perfil y preguntas se convierte en estándar abierto documentado.
- Cualquier desarrollador puede construir su propia interfaz sobre el mismo protocolo.
- Sin dueño. Las ideas son de todos.

---

## Stack técnico

| Capa | Tecnología | Por qué |
|------|-----------|---------|
| Frontend | HTML + CSS + JS vanilla | Sin dependencias, deployable en cualquier lado |
| Datos | JSON estático | Editable por la comunidad via pull request |
| Tiempo | Bitcoin + OpenTimestamps | Ancla incorruptible sin costo |
| Identidad | Nostr / DID | Un humano, una clave, sin servidor central |
| Pagos | Lightning Network | Micropagos sin banco en el medio |
| Hosting | IPFS / GitHub Pages | Sin servidor, sin punto único de falla |

---

## Cómo contribuir

Este proyecto no tiene empresa ni inversores. Crece si la comunidad lo hace crecer.

**Podés contribuir con:**

- **Preguntas** — abrí un issue con una pregunta nueva y por qué la considerás reveladora. Las preguntas viven en `assets/questions.json`.
- **Traducciones** — el proyecto debería existir en todos los idiomas. Cada idioma es un archivo JSON separado.
- **Integraciones** — si sabés de Nostr, Lightning o DID y querés implementar la v2/v3, abrí un issue.
- **Tu propio perfil** — forkear el repo y publicar tu propio perfil es la forma más directa de participar. El formato está en `assets/profile.json`.
- **Diseño** — mejorar la experiencia visual sin agregar dependencias.
- **Documentación** — explicar conceptos técnicos de forma accesible.

**Principios para contribuir:**
- Sin dependencias externas innecesarias
- Sin tracking, sin analytics, sin cookies
- El código debe ser legible por alguien que está aprendiendo
- Los cambios a `questions.json` se discuten antes de mergear

---

## Deployar tu propia instancia

### GitHub Pages (más simple)
```bash
git clone https://github.com/TU_USUARIO/genuino.git
cd genuino
# editá assets/profile.json con tus respuestas
# editá profile.html con tu nombre
git add . && git commit -m "mi perfil" && git push
# activá GitHub Pages en Settings → Pages
```

### IPFS (más descentralizado)
```bash
# con ipfs instalado
ipfs add -r genuino/
# o via Fleek: fleek.co — deploy automático desde GitHub
```

---

## Filosofía

Bitcoin demostró que es posible tener un sistema de valor sin que nadie lo controle. El mismo principio aplica a la identidad, a las relaciones, y eventualmente a cualquier forma de coordinación colectiva.

La tecnología descentralizada no es un fin — es una herramienta para que el colectivo gobierne sus propios algoritmos. Para que la "mente colectiva" pueda operar de manera colectiva, sin que nadie intermedie ni capture ese valor.

Las ideas son de todos. El código es de todos. El protocolo no tiene dueño.

---

## Licencia

[MIT](LICENSE) — libre para usar, modificar y distribuir.

---

*genuino — construido en Linux, deployable en cualquier lado, sin dueño.*
