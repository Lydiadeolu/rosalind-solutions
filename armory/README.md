# Rosalind: Bioinformatics Armory Tracker

This section serves as a centralized archive for production-grade solutions targeting the **Bioinformatics Armory** track on Rosalind. Unlike the algorithmic challenges in the Stronghold track—which require building logic blocks from scratch—the Armory focus shifts toward mastering **industry-standard software suites, databases, and mature biological frameworks** (such as Biopython, NCBI Entrez, and alignment tools).

---

##  Core Learning Objectives

* **API Automation:** Communicating with public federal repositories (NCBI GenBank, UniProt) via direct E-Utilities scripting without browser interface dependency.
* **Production Library Competency:** Mastering advanced, highly optimized C-backed tools within `Bio.Seq`, `Bio.Align`, and `Bio.motifs`.
* **Modern Workspace Pipeline:** Restructuring file workflows away from standard legacy string systems into cross-platform, deterministic `pathlib.Path` objects.

---

## Track Progress & Inventory Mapping

Below is the directory map tracking implemented solutions, algorithms used, and database links.

| Problem Code | Challenge Name | Primary Tools/Modules | Key Methodology | Status |
| :--- | :--- | :--- | :--- | :--- |
| **INI** | Introduction to the Armory | `Bio.Seq.Seq` | Optimized nucleotide extraction & processing |  Completed |
| **GBK** | GenBank Introduction | `Bio.Entrez.esearch` | Parameterized historical date-bound API queries |  Completed |
| **FRMT** | Data Formats | `Bio.Entrez.esearch` | Parameterized historical date-bound API queries |  Completed |

---

## Repository Architectural Design

Every problem folder contains a standardized layout to ensure portability and clarity:

```text
armory/
├── README.md                          # <-- This global track dashboard
├── INI_Introduction_to_Armory/
│   └── README.md                      # <-- Problem breakdown & execution docs
├── GBK_GenBank_Introduction/
│   ├── README.md                      # <-- Exact API syntax map documentation
│   └── solution.py                    # <-- Core pathlib-driven execution script
├── FRMT_Data_Formats/
│   ├── README.md                      # <-- Exact API syntax map documentation
│   └── solution.py                    # <-- Core pathlib-driven execution script
└── Dataset/                           # <-- Centralized data download directory
    ├── rosalind_gbk.txt
    └── rosalind_need.txt
    └── rosalind_frmt.txt
```
---

## Path-Safe Philosophy
All scripts avoid hardcoded file locations or native terminal slashes (\ vs /). Inputs are evaluated relative to the active file's birthplace using explicit object hooks:

```Python
from pathlib import Path
current_dir = Path(__file__).resolve().parent
dataset_path = current_dir / ".." / "Dataset" / "target_file.txt"
```

---

## Setup & Dependency Matrix
To execute these solutions locally, initialize an isolated virtual environment (.venv) and install the verified biological dependencies:

Bash
# 1. Activate your virtual workspace environment
source .venv/Scripts/activate  # On Windows Git Bash

# 2. Install required bioinformatics dependencies
pip install biopython

# 3. Verify local library installation success
python -c "import Bio; print(f'Biopython version configured: {Bio.__version__}')"

---

## NCBI Server Requirement Notice: 

For all problems executing remote server queries (like GBK or NEED), ensure you configure a real email address payload (Entrez.email = "name@domain.com"). This identifies your programmatic connection stream, preventing permanent IP blocks or request throttling from federal server firewalls.