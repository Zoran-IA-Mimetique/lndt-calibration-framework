# LNDT v1 — Calibration & Certification Framework for Enterprise AI

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1234567.svg)](https://doi.org/10.5281/zenodo.1234567)
![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Build](https://img.shields.io/github/actions/workflow/status/Zoran-IA-Mimetique/lndt-calibration-framework/python-app.yml?branch=main)

---

## 🔎 About
**LNDT v1** (Laboratoire de Normalisation et de Diagnostic Technique) is the **first open-source modular framework** for **benchmarking, calibration, and certification** of Large Language Models (LLMs).

- **Universal Nucleus**: core ethical, regulatory, and compliance rules (RGPD, AI Act, HIPAA).
- **Domain Packs**: YAML/JSON packs for insurance, healthcare, legal, finance, education.
- **Governance & Certification**: cryptographic traceability with glyph-address and SHA-256 hashes.
- **CI/CD Ready**: run validation pipelines in <100 ms.

---

## 📂 Repository Structure
| Folder | Content |
|--------|---------|
| `core/` | nucleus.yaml, formats.md, schema.json, LICENSE |
| `domains/` | sector calibration packs (healthcare, legal, finance, insurance_btp, education) |
| `tools/` | injecteur.py, validator.py, runner.py |
| `research/` | taxonomy.md/json, roadmap.md |
| `docs/` | CONTRIBUTING.md, GOVERNANCE.md, whitepaper-v4.pdf |
| `README.md` | this file |

---

## ⚙️ Installation
```bash
git clone https://github.com/Zoran-IA-Mimetique/lndt-calibration-framework.git
cd lndt-calibration-framework
pip install pyyaml jsonschema


---

🚀 Usage Examples

Validate a pack

python tools/validator.py --pack domains/insurance_btp/pack-insurance-btp-v1.yaml

Validate all packs

python tools/runner.py

Example pack (insurance_btp)

type: pack
pack: "Insurance BTP v1.0"
domain: "insurance_btp"
extends_nucleus:
  id: lndt-nucleus-universel
  version: "1.0.0"
prompts:
- id: btp-001
  q: "Is a decennial insurance mandatory in France?"
  g: "Yes, according to French Civil Code art. 1792"
  fmt: "text_sem"
  axis: "legal"
  weight: 4


---

📜 Whitepaper

Read the full whitepaper (v4) in docs/whitepaper-v4.pdf.
Also available on Zenodo.


---

🌍 Community & Contribution

Contributions welcome via Pull Requests.

Please follow docs/CONTRIBUTING.md.

Governance model described in docs/GOVERNANCE.md.



---

📈 Roadmap

6 months: pilots in insurance & healthcare.

12 months: open-source nucleus + auto-generation of packs.

24 months: LNDT Foundation, glyph explorer, third-party certification.



---

📢 References

Institute IA

Medium Article

Zenodo Record



---

📄 License

This project is licensed under the MIT License — see the LICENSE file for details.
