#!/usr/bin/env python3
import json, yaml, sys
from jsonschema import validate

schema = json.load(open("core/schema.json"))
doc = yaml.safe_load(open(sys.argv[1]))
validate(instance=doc, schema=schema)
print("[OK] Valid pack")
