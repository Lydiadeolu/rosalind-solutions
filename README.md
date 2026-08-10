# Rosalind Bioinformatics Solutions

Welcome to my repository of solutions for Rosalind, a platform for learning bioinformatics through problem-solving. This repository serves as a structured archive of my journey in computational biology, mapping out solutions to algorithmic challenges that bridge computer science, mathematics, and genetics.

## Repository Structure

The project is organized hierarchically by Rosalind tracks, keeping each solution isolated alongside its mathematical/biological context.

```text
rosalind-solutions/
├── README.md                                             # Main index and progress tracker
├── .gitignore                                            # Prevents clutter and raw data uploads
├── requirements.txt                                      # Python dependencies (Biopython, NumPy, etc.)
└── python_village/                                       # Introduction to Python programming
    ├── README.md                                         # Track overview
    └── INI1_installing_python/                           # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── INI2_Variables_and_Some_Arithemetics/             # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── INI3_Strings_and_Lists/                           # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── INI5_Working_with_files/                          # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── INI6_Dictionaries/                                # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms

└── stronghold/                                           # Core algorithmic bioinformatics track
    ├── README.md                                         # Track overview
    └── DNA_counting_nucleotides/                         # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── RNA_Transcribing_DNA_to_RNA/                         # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── REVC_Complementaring_a_Strand_of_DNA/                         # Dedicated problem folder
        ├── solution.py
        └── README.md                                     # Problem notes and algorithms
    └── GC_Computing_GC_Content/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── HAMM_Counting_point_Mutation/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── SUBS_Finding_a_Motif_in_DNA/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── PROT_Translating_RNA_into_Protein/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
       └── prot_Biopython.py 
    └── PRTM_Calculating_Protein_Mass/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── FIB_Rabbits_and_Recurrence_Relation/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── IPRB_Mendel_First_Law/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── ORF_Opem_Reading_Frames/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── SPLC_RNA_Splicing/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── CONS_Concensus and Profile/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── GRPH_Overlap_Graphs/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── NEED_Pairwise _Global Alignment/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── FIBD_Mortal_Fibonnaci_Rabbits/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── PERM_Enumerating_Gene_Oders/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── LCSM_Finding_a_Shared_Motifs/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── LGIS_Longest_Increasing_Subsequence/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── PMCH_Perfect_Matching_and_RNA_Structure/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── LIA_Independent_Alleeles/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── PROB_Introduction_To_Random_Strings/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── MPRT_Finding_a_Protein_Motif/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └──REVP_Locating_Restriction_Sites/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── MULT_Multiple_Alignment/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── SIGN_Enumerating_Oriented_Gene_Orderings/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing
    └── IEV_Calculating_Expected_Offspring/
       ├── README.md                        # Problem breakdown, biological background, and approach
       └── solution.py                      # Clean, runnable Python script using portable path routing

└──armory/                                                #solving problems with external biological tools
    ├── README.md  
    └── INI_Introduction_to_Armory/
       └── README.md                      # <-- Problem breakdown & execution docs
    └── GBK_GenBank_Introduction/
       ├── README.md                      # <-- Exact API syntax map documentation
       └── solution.py                    # <-- Core pathlib-driven execution script
    └── FRMT_Data_Formats/
       ├── README.md                      # <-- Exact API syntax map documentation
       └── solution.py                    # <-- Core pathlib-driven execution script
    └── Dataset/                           # <-- Centralized data download directory
       ├── rosalind_gbk.txt
       └── rosalind_need.txt
       └── rosalind_frmt.txt
       
└──utils/                                                 # Modular, reuseable helper functions
   └──bioutils.py                                         # Centalized biology logic (DNA transcription, etc.)
```

## Getting Started & Installation

    To run these scripts locally, ensure you have Python 3.8+ installed on your system.

    Clone the repository:
    Run these command
       git clone https://github.com/Lydiadeolu/rosalind-solutions.git
       cd rosalind-solutions


    Set up a virtual environment (Optional but Recommended):
    Run these command
       python -m venv venv
       source venv/bin/activate  # On Windows use: venv\Scripts\activate


    Install dependencies:
    Run these command
       pip install -r requirements.txt


## The utils/ Library (DRY Principle)

Bioinformatics problems often require repetitive tasks (e.g., transcribing DNA, calculating GC-content, translating RNA to proteins). To maintain clean code and follow DRY (Don't Repeat Yourself) principles, all core helper functions are modularized inside utils/bioutils.py.

Any solution script can easily import these shared functions:

from utils.bioutils import transcribe_dna, translate_rna


## Progress Tracker

Below is an active checklist of my completed challenges. I update this whenever I push new solutions.

### Python Village (Basics of Programming)

#### [ ] INI1 - Installing Python

#### [ ] INI2 - Variables and Four Operations

#### [ ] INI3 - Strings and Lists

#### [ ] INI4 - Conditions and Loops

#### [ ] INI5 - Working with Files

#### [ ] INI6 - Dictionaries

### Bioinformatics Stronghold (Algorithmic Biology)

#### [ ] DNA - Counting DNA Nucleotides

#### [ ] RNA - Transcribing DNA into RNA

#### [ ] REVC - Complementing a Strand of DNA

#### [ ] FIB - Rabbits and Recurrence Relations

#### [ ] GC - Computing GC Content

#### [ ] HAMM - Counting Point Mutations

#### [ ] PROT - Translating RNA into Protein

#### [ ] SUBS - Finding a Motif in DNA

#### [ ] PRTM - Calculating Protein Mass

#### [ ] IPRB - Mendel's First Law

#### [ ] ORF - Open Reading Frame

#### [ ] SPLC - RNA Splicing

#### [ ] CONS - Consensus and Profile

#### [ ] GRPH - Overlaps Graph

#### [ ] LONG - Geneome Assembly

#### [ ] LCSM - Finding a Shared Motif

#### [ ] LGIS - Longest Increasing Subsequence

#### [ ] PMCH - Perfect Matchings and RNA Secondary Structure

#### [ ] LIA - Independent Alleles

#### [ ] PROB - Introduction to Random Strings

#### [ ] MPRT - Finding a Protein Motif

#### [ ] REVP - Locating Restriction Sites

#### [ ] MULT - Multiple Alignment

#### [ ] SIGN - Enumerating Oriented Gene Orderings

#### [ ] IEV - Calculating Expected Offspring


## Bioinformatics Armory (Using Industry Tools)

#### [ ] INI - Introduction to the Bioinformatics Armory

#### [ ] DBPR - Introduction to Protein Databases

#### [ ] GBK - GenBank Introduction

#### [ ] FRMT - Data Formats


## Academic Context & Goals

This project is built to demonstrate rigorous code organization and algorithmic problem-solving in preparation for advanced studies in computational genomics. By modeling biological systems programmatically, I aim to master:

    [ ] Dynamic programming (sequence alignment, gene prediction)

    [ ] Graph theory applications (genome assembly using de Bruijn graphs)

    [ ] High-throughput data analysis and sequence modeling

    [ ] Feel free to explore the folders to view my solution scripts and associated markdown notes!