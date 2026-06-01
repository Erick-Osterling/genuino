# genuino — contexto para Claude

## Qué es este proyecto

App estática (HTML + CSS + JS vanilla) para conocer personas sin intermediarios. Sin backend, sin base de datos, sin cookies. Deployable en GitHub Pages o IPFS.

El perfil del dueño tiene respuestas a preguntas organizadas en sets. El visitante responde las mismas preguntas antes de poder ver las respuestas del dueño. Al final se comparan lado a lado con un score de cosas en común.

## Cómo correrlo localmente

```bash
python3 -m http.server 8765 --directory /home/erick/repos/genuino
# Abre en Brave: http://localhost:8765
```

Para testing automatizado (Selenium + geckodriver):
```bash
cd /tmp && npm install selenium-webdriver
# geckodriver disponible en /snap/firefox/current/usr/lib/firefox/geckodriver
# firefox binary en /snap/firefox/current/usr/lib/firefox/firefox
```

## Estructura de archivos

```
genuino/
├── index.html           # Manifiesto / entrada
├── profile.html         # Perfil del dueño — bloqueado hasta que el visitante conteste
├── questions.html       # Flujo de preguntas (lee de assets/profile.json)
├── reveal.html          # Comparación de respuestas + score
├── learn.html           # Introducción a Bitcoin
├── assets/
│   ├── style.css        # Tokens de diseño compartidos
│   ├── profile.json     # Perfil público — preguntas + respuestas del dueño
│   └── questions.json   # Banco de preguntas por tema (referencia, no se usa en el flujo principal)
└── .gitignore           # Excluye perfiles privados (tyler.html, etc.)
```

## Estructura de datos (v2.0.0)

### assets/profile.json

```json
{
  "version": "2.0.0",
  "name": "Pedro",
  "sets": [
    {
      "id": "lo-basico",
      "title": "Lo básico",
      "desc": "el día a día",
      "requires": [],
      "questions": [
        {
          "id": "p1_1",
          "text": "¿Qué hacés lo primero cuando llegás a tu casa?",
          "type": "open",
          "answer": "...",
          "hash": ""
        }
      ]
    },
    {
      "id": "gustos",
      "title": "Gustos",
      "requires": ["lo-basico"],
      "questions": [...]
    }
  ]
}
```

El campo `requires` es la clave de la arquitectura: un set solo es accesible después de completar los sets que lista. Si está vacío, el set está disponible desde el inicio. Soporta tanto progresión lineal como estructuras ramificadas.

### assets/questions.json

Banco público de preguntas organizado por tópicos (`topics[]`). No se usa en el flujo principal — sirve como referencia para que otros creen sus propios perfiles.

## Flujo de usuario

1. Visitante entra a `profile.html` → ve perfil bloqueado con mensaje "respondé primero"
2. Va a `questions.html` → responde los sets en orden (respeta `requires`)
3. Al terminar, las respuestas se guardan en `sessionStorage` con clave `genuino_answers`
4. Redirige a `reveal.html` → comparación lado a lado + score de cosas en común
5. Vuelve a `profile.html` → ahora ve las respuestas del dueño

## Decisiones de diseño tomadas

- **Las respuestas del dueño se ocultan** hasta que el visitante conteste — nadie ve lo del otro antes de comprometerse a responder.
- **questions.html lee directamente de profile.json** (no del banco questions.json). El perfil es la fuente de verdad de qué preguntas se hacen.
- **El perfil público es Pedro** (16 años, preguntas livianas). El perfil de Tyler es privado y está en .gitignore.
- **Sin framing romántico** — el lenguaje es neutro, orientado a conocer personas en general (no dating).
- **Sin jerga técnica** en los textos visibles — nada de "firmado criptográficamente", "forkear", "JSON", etc.

## Perfil actual (Pedro)

- 3 sets: "Lo básico" → "Gustos" → "Amigos y planes"
- Preguntas livianas y concretas, no filosóficas
- Email de contacto: pedro@proton.me

## Roadmap

- **v1** — cascarón estático ✅
- **v2** — firma criptográfica via OpenTimestamps (hash SHA-256 ya preparado en profile.json)
- **v3** — identidad descentralizada via Nostr + Lightning micropayments
- **v4** — protocolo abierto, cualquiera construye sobre el mismo formato

## GitHub

- Repo: `git@github.com:Erick-Osterling/genuino.git`
- Branch principal: `main`
- GitHub Pages: `https://erick-osterling.github.io/genuino/`
