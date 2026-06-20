# Python Village

This section contains solutions for the **Python Village** introductory track on [Rosalind](https://rosalind.info/problems/list-view/?v=pv). This track is designed to establish a basic working foundation in Python mechanics, file handling, and programming logic before diving into complex biosequence algorithms.

---

## Track Progress Dashboard

| Problem ID | Title | Core Focus | Status |
| :--- | :--- | :--- | :--- |
| **INI1** | [Introduction to the Python Environment](./INI1_introduction_to_the_python_environment/) | Setting up Python & Packages |  Completed |
| **INI2** | [Variables and Some Arithmetic](./INI2_variables_and_some_arithmetic/) | Variable assignment & math bounds |  Completed |
| **INI3** | [Strings and Lists](./INI3_strings_and_lists/) | Inclusive coordinate string slicing |  Completed |
| **INI4** | [Conditions and Loops](./INI4_conditions_and_loops/) | Control flow & numerical filtering |  Completed |
| **INI5** | [Working with Files](./INI5_working_with_files/) | File I/O & even-numbered line parsing | ⏳ In Progress |
| **INI6** | [Dictionaries](./INI6_dictionaries/) | Key-value frequency mapping | ⏳ In Progress |

---

## Structural Strategy

Every problem folder inside this directory is standardized with a predictable framework to keep the repository uniform, clean, and easily reproducible:

```text
python_village/
├── INI1_introduction_to_the_python_environment/
│   ├── README.md      # Problem breakdown, concepts, and biology tie-in
│   └── solution.py    # Clean, runnable Python script matching Rosalind constraints
├── INI2_variables_and_some_arithmetic/
│   ├── README.md
│   └── solution.py
├── INI3_Strings_and_Lists/
│   ├── README.md
│   └── solution.py
├── INI4_Conditions_and_Loops/
│   ├── README.md
│   └── solution.py
├── INI3_Strings_and_Lists/
│   ├── README.md
│   └── solution.py
├── INI4_Conditions_and_Loops/
│   ├── README.md
    └── solution.py

```
## Data Isolation

Individual downloaded dataset texts (rosalind_ini*.txt) are explicitly ignored by .gitignore to protect pipeline hygiene and honor Rosalind's unique per-user dataset dynamic.

## Robust File I/O

Script implementations wrap file handling inside context managers (with open()) paired with structural fallbacks to execute flawlessly in both production pipelines or standalone text executions

## Core Ecosystem Toolkit

While progressing through these exercises, the following fundamental properties of Python are established:
1. Dynamic Typing: On-the-fly variable assignment without explicit type declarations.
2. Zero-Indexing & Exclusive Upper Bounds: Navigating ranges and structural slices where the upper bound boundary is consistently non-inclusive ([start:stop]).
3. Immutability Rules: Manipulating strings securely while understanding they cannot be modified in-place.
4. Dictionary Lookups: Leveraging Hash maps for O(1) efficiency when computing large counts or data frequencies.

# Next Track: Bioinformatics Stronghold ➔