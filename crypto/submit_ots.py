#!/usr/bin/env python3
"""
Manda el hash de profile.json a OpenTimestamps y guarda el proof en crypto/timestamps.ots

Uso:
    python3 crypto/submit_ots.py

Para verificar después (requiere opentimestamps-client):
    pip install opentimestamps-client
    ots verify crypto/timestamps.ots -f assets/profile.json
"""

import hashlib
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).parent.parent
PROFILE = ROOT / "assets" / "profile.json"
OTS_FILE = Path(__file__).parent / "timestamps.ots"

# OTS binary file format: magic + version byte + ops tree from calendar
OTS_MAGIC = b"\x00OpenTimestamps\x00\x00Proof\x00\xbf\x89\xe2\xe8\x84\xe8\x92\x94"
OTS_VERSION = b"\x01"

CALENDARS = [
    "https://a.pool.opentimestamps.org/digest",
    "https://b.pool.opentimestamps.org/digest",
    "https://c.pool.opentimestamps.org/digest",
    "https://d.pool.opentimestamps.org/digest",
]


def sha256_bytes(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()


def submit(url: str, digest: bytes) -> bytes | None:
    req = urllib.request.Request(
        url,
        data=digest,
        headers={"Content-Type": "application/octet-stream"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return resp.read()
    except urllib.error.URLError as e:
        print(f"  ✗ {url.split('/')[2]}: {e.reason}")
        return None
    except Exception as e:
        print(f"  ✗ {url.split('/')[2]}: {e}")
        return None


def main():
    if not PROFILE.exists():
        print(f"Error: no se encuentra {PROFILE}")
        print("Corré primero: python3 crypto/hash_profile.py")
        sys.exit(1)

    content = PROFILE.read_bytes()
    digest = sha256_bytes(content)
    hex_hash = digest.hex()

    print(f"Hash del perfil: {hex_hash}")
    print()
    print("Conectando a calendarios OpenTimestamps...")

    ops = None
    used_calendar = None
    for url in CALENDARS:
        result = submit(url, digest)
        if result:
            ops = result
            used_calendar = url.split("/")[2]
            print(f"  ✓ {used_calendar}")
            break

    if not ops:
        print()
        print("Error: no se pudo conectar a ningún calendario.")
        print("Verificá tu conexión a internet e intentá de nuevo.")
        sys.exit(1)

    ots_data = OTS_MAGIC + OTS_VERSION + ops
    OTS_FILE.write_bytes(ots_data)

    print()
    print(f"✓ Proof guardado en crypto/timestamps.ots ({len(ots_data)} bytes)")
    print()
    print("Estado: PENDIENTE — se confirma en el próximo bloque de Bitcoin (~10 min).")
    print()
    print("Agregá estos archivos al commit:")
    print("  git add assets/profile.json crypto/timestamps.ots")
    print()
    print("Para verificar una vez confirmado:")
    print("  pip install opentimestamps-client")
    print("  ots upgrade crypto/timestamps.ots")
    print("  ots verify  crypto/timestamps.ots -f assets/profile.json")


if __name__ == "__main__":
    main()
