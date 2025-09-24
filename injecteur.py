#!/usr/bin/env python3
import yaml, json, sys

def load_pack(path):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

if __name__ == "__main__":
    if len(sys.argv)<2:
        print("Usage: injecteur.py <pack.yaml>")
        sys.exit(1)
    print(json.dumps(load_pack(sys.argv[1]), indent=2, ensure_ascii=False))
