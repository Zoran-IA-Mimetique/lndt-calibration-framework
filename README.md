# LNDT v1 — Framework open-source de calibration & certification pour LLM

**Objet.** Ce dépôt fournit le noyau universel LNDT (éthique, RGPD/AI Act, formats),
des packs métiers d'étalonnage (domains/), les outils (tools/) et la recherche (research/).

## Arborescence
- `core/` : nucleus universel + formats + schema + licence
- `domains/` : packs sectoriels (ex : healthcare, legal, finance, insurance_btp, education)
- `tools/` : injecteur/validator/runner + exemples
- `research/` : taxonomie & roadmap
- `docs/` : whitepaper & gouvernance

## Usage rapide
1. Installez Python 3.10+. Recommandé : `pip install pyyaml jsonschema`
2. Validez un pack : `python tools/validator.py --pack domains/insurance_btp/pack-insurance-btp-v1.yaml`
3. Lancer un run demo : voir `tools/examples/demo_run.md`

## Licence
Apache-2.0 (voir `core/LICENSE`).
