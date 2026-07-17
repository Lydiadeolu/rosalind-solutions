# Bioinformatics Stronghold

This section contains solutions for the **Bioinformatics Stronghold** track on [Rosalind](https://rosalind.info/problems/list-view/). This track is focused on implementing real-world core biosequence algorithms, covering molecular biology patterns, structural genomics, combinatorics, and introductory mass spectrometry.

---

## Track Progress Dashboard

| Problem ID | Title | Core Focus | Status |
| :--- | :--- | :--- | :--- |
| **DNA** | [Counting DNA Nucleotides](./DNA_Counting_DNA_Nucleotides/) | String character frequency counting |  Completed |
| **RNA** | [Transcribing DNA into RNA](./RNA_Transcribing_DNA_into_RNA/) | Nucleotide substitution dynamics |  Completed |
| **REVC** | [Complementing a Strand of DNA](./REVC_Complementing_a_Strop_of_DNA/) | Reverse complement generation |  Completed |
| **GC** | [Computing GC Content](./GC_Computing_GC_Content/) | FASTA parsing & percentage ratio scanning |  Completed |
| **HAMM** | [Counting Point Mutations](./HAMM_Counting_Point_Mutations/) | Evaluating Hamming distance metrics |  Completed |
| **SUBS** | [Finding a Motif in DNA](./SUBS_Finding_a_Motif_in_DNA/) | Substring substring coordinate scanning |  Completed |
| **PROT** | [Translating RNA into Protein](./PROT_Translating_RNA_into_Protein/) | Codon array translation logic |  Completed |
| **PRTM** | [Calculating Protein Mass](./PRTM_Calculating_Protein_Mass/) | Monoisotopic mass lookup calculation |  Completed |
| **FIB** | [Rabbits and Recurrence Relations](./FIB_Rabbits_and_Recurrence_Relations/) | Dynamic programming & Fibonacci modeling |  Completed |
| **IPRB** | [Mendelian Inheritance](./IPRB_Mendelian_Inheritance/) | Analytical probability tree matrices |  Completed |
| **ORF** | [Open Reading Frames](./ORF_Open_Reading_Frames/) | Six-frame translation coordinate mapping |  Completed |
| **SPLC** | [RNA Splicing](./SPLC_RNA_Splicing/) | Intron stripping and exon translation |  Completed |
| **CONS** | [Consensus and Profile](./CONS_Consensus_and_Profile/) | Matrix profile compilation and consensus sequence extraction |  Completed |
| **GRPH** | [Overlap Graphs](./GRPH_Overlap_Graphs/) | De Bruijn directed graph construction via suffix-prefix matching |  Completed |
| **LONG** | [Genome Assembly as Shortest Superstring](./LONG_Genome_Assembly_as_Shortest_Superstring/) | Greedy shortest common superstring reconstruction from reads |  Completed |
| **NEED** | [Pairwise Global Alignment](./NEED_Pairwise_Global_Alignment/) | Needleman-Wunsch sequence distance matrix with affine gap grids |  Completed |
| **FIBD** | [Mortal Fibonacci Rabbits](./FIBD_Mortal_Fibonacci_Rabbits/) | Dynamic programming via generational shifting sliding window arrays |  Completed |
| **PERM** | [Enumerating Gene Order](./PERM_Enumerating_Gene_Order/) | Combinatorial chromosome rearrangement tracking using permutations |  Completed |
| **IEV** | [Calculating Expected Offspring](./IEV_Calculating_Expected_Offspring/) | Mendelian Probability & Expected Value |	Completed |
| **SIGN** | [Orienting Random Orderings](./SIGN_Oriented_Expected_Offspring/) | Combinatorics & Signed Permutations	| Completed |
| **MPRT** | [Finding a Protein Motif](./MPRT_Finding_a_Protein_Motif/)	| UniProt API Queries & Regex Lookaheads | Completed |
| **REVP** | [Locating Restriction Sites](./REVP_Locating_Restriction_Sites/) | DNA Reverse Palindromes & Sliding Windows |	Completed |
| **LIA** | [Independent Alleles](./LIA_Independent_Alleles/) | Multigenerational Binomial Probability |	Completed |
| **PMCH** | [Perfect Matchings and RNA Secondary Structures](./PMCH_Perfect_Matchings_and_Secondary_Structures/) |	Graph Theory & RNA Secondary Structures |	Completed |
| **PROB** |	[Introduction to Random Strings	GC-Content](./PROB_Introduction_to_Random_Strings/) | Log Likelihoods & Probabilities |	Completed |
| **MULT** | [Multiple Alignment](./MULT_Multiple_Alignment/) | Global Progressive Alignment | Completed |
| **LCSM** | [Finding a Shared Motif](./LCSM_Finding_a_Shared_Motif/) | Longest Common Substring & Binary Search | 	Completed |
| **LGIS** | [Longest Increasing Subsequence](./LGIS_Longest_Increasing_Subsequence/) | Dynamic Programming & Patience Sorting |Completed |

---

## Structural Strategy

Every problem folder inside this directory is standardized with a predictable framework to keep the repository uniform, clean, and easily reproducible:

```text
stronghold/
├── Dataset/                             # Central repository for input file records
│   ├── rosalind_dna.txt
│   ├── rosalind_orf.txt
│   └── ...
├── DNA_Counting_DNA_Nucleotides/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── RNA_Transcribing_DNA_into_RNA/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
│   └── rna_Biopython.py 
├── REVC_Complememting_a_Strand_of_DNA/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── GC_Computing_GC_Content/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── HAMM_Counting_point_Mutation/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── SUBS_Finding_a_Motif_in_DNA/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── PROT_Translating_RNA_into_Protein/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
│   └── prot_Biopython.py 
├── PRTM_Calculating_Protein_Mass/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── FIB_Rabbits_and_Recurrence_Relation/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── IPRB_Mendel_First_Law/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── ORF_Opem_Reading_Frames/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── SPLC_RNA_Splicing/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── CONS_Concensus and Profile/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── GRPH_Overlap_Graphs/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── NEED_Pairwise _Global Alignment/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── FIBD_Mortal_Fibonnaci_Rabbits/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── PERM_Enumerating_Gene_Oders/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── LCSM_Finding_a_Shared_Motifs/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── LGIS_Longest_Increasing_Subsequence/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── PMCH_Perfect_Matching_and_RNA_Structure/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── LIA_Independent_Alleeles/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── PROB_Introduction_To_Random_Strings/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── MPRT_Finding_a_Protein_Motif/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── REVP_Locating_Restriction_Sites/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── MULT_Multiple_Alignment/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── SIGN_Enumerating_Oriented_Gene_Orderings/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
├── IEV_Calculating_Expected_Offspring/
│   ├── README.md                        # Problem breakdown, biological background, and approach
│   └── solution.py                      # Clean, runnable Python script using portable path routing
└── ...
```
## Key Concepts Table

## Data Isolation
Individual downloaded dataset texts (rosalind_*.txt) are tracked inside a local, centralized Dataset/ directory. These files are explicitly ignored by the repository's rules where necessary to protect pipeline hygiene and honor Rosalind's unique per-user dataset dynamic.

## Robust File I/O
Script implementations calculate file paths dynamically using Python's os.path utility package (os.path.dirname(__file__)). This eliminates rigid hardcoded absolute paths, ensuring that solutions resolve file dependencies flawlessly across alternative user profiles and host platforms.

## Core Ecosystem Toolkit
While progressing through these exercises, the following intermediate bioinformatics paradigms are established:

-Dynamic Programming: Optimizing recurrence relations with memoization vectors to solve growth models like Fibonacci chains without hitting stack overflows.

-Biopython Sequence Engine (Bio.Seq): Utilizing factory-grade parsing classes to process reverse-complements and multi-frame translation operations safely.

-Structured String Parsing: Processing complex raw standard text files (such as multi-line FASTA records) into decoupled dictionary hash mappings for structural query downstream access.

-Float Matrix Rounding: Aligning mathematical precision formatting structures with absolute strict string constraints to guarantee successful integration with verification autograders.