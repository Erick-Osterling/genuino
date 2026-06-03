#!/usr/bin/env python3
"""
Computa SHA-256 de cada respuesta en profile.json y del archivo completo.
Correr después de editar el perfil, antes de publicar.

Uso:
    python3 crypto/hash_profile.py
"""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROFILE = ROOT / "assets" / "profile.json"


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main():
    data = json.loads(PROFILE.read_text(encoding="utf-8"))

    count = 0
    for s in data["sets"]:
        for q in s["questions"]:
            answer = q.get("answer", "")
            if answer:
                q["hash"] = sha256(answer)
                count += 1

    canonical = json.dumps(data, ensure_ascii=False, indent=2) + "\n"
    PROFILE.write_text(canonical, encoding="utf-8")

    file_hash = sha256(canonical)

    print(f"✓ {count} respuestas hasheadas")
    print(f"  Hash del perfil: {file_hash}")
    print()
    print("Siguiente paso — anclar en Bitcoin:")
    print("  python3 crypto/submit_ots.py")


if __name__ == "__main__":
    main()
