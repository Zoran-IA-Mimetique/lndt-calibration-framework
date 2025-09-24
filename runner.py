#!/usr/bin/env python3
import os, subprocess, sys, glob

packs = glob.glob("domains/*/*.yaml")
if not packs:
    print("[WARN] No packs found")
    sys.exit(0)

errors = 0
for p in packs:
    print(f"==> Validating {p}")
    r = subprocess.run([sys.executable, "tools/validator.py", p])
    if r.returncode != 0:
        errors += 1

if errors == 0:
    print("[OK] All packs valid.")
else:
    print(f"[ERR] {errors} invalid pack(s).")
    sys.exit(1)
