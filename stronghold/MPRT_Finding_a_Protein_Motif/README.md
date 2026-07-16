# MPRT -- Finding a Protein Motif

**Section:** Bioinformatics Stronghold
**Difficulty:** Medium
**Topics:** `string-algorithms` `regular-expressions` `network-apis` `uniprot`
**Rosalind Link:** https://rosalind.info/problems/mprt/
**Date Solved:** 2026-07-11

---

## Biological & Mathematical Background

### Protein Motifs and N-glycosylation
A protein motif is a structural or sequence-level pattern of amino acids shared across different proteins that typically dictates a specific biological function. One structurally vital motif is the **N-glycosylation motif**, which indicates where a carbohydrate chain can attach to a nitrogen atom on an Asparagine (N) residue. 

The motif is standardly written as:

N\ [^P]\ [ST]\ [^P]

This notation translates to:
1. An **Asparagine** (N) base.
2. Followed by **any amino acid except Proline** ([^P]).
3. Followed by either a **Serine** (S) or **Threonine** (T).
4. Followed by **any amino acid except Proline** ([^P]).

### Programmatic Sequence Extraction via UniProt API
Instead of manually copying genomic data, we programmatically pull official amino acid configurations from the **UniProt Knowledgebase (UniProtKB)**. Given a simple UniProt Accession ID, our engine requests the raw, unformatted FASTA text block directly from UniProt's endpoints over standard HTTP protocols.

<Image src="image_agent_tag_2781573052254647065" alt="Diagram showing alignment of protein signatures to construct a regular expression motif like [AC]-x-V-x(4)-{ED}" caption="Translating Protein Motifs to Regular Expressions" />

### Overcoming Regex Overlap Limitations
Standard regular expression engines consume characters as they match, meaning they can easily jump right past overlapping structural targets. For example, in a sequence like `NNST`, a naive search would match the first `NST` pattern and advance the cursor past the second `N`, completely missing the secondary `NST` overlap starting at index 1. 

To safely intercept overlapping indices, we use a specialized **Positive Lookahead Assertion (`(?=...)`)**. This allows our regular expression pattern to test for the motif structure down the line without shifting the engine's main tracking index forward.

---

## Problem Statement

Given a list of at most 15 UniProt Protein Accession IDs. Return the Accession ID alongside the 1-based start positions where the N-glycosylation motif occurs for each protein. Omit proteins that do not contain the motif.

---

## Approach

1.  **Resolve Accession IDs:** Read the list of target strings. Note that some IDs include structural modification details (e.g., `B5ZC00_CLOPE`), so we isolate the core index boundary to fetch data while preserving the full label string for output mapping.
2.  **Execute Network Requests:** Query `https://rest.uniprot.org/uniprotkb/{accession_id}.fasta` using Python's `requests` library.
3.  **Sanitize FASTA Content:** Discard the header descriptor line and join the remaining lines into a continuous amino acid sequence string.
4.  **Perform Overlap Search:**
    * Compile the lookahead pattern: `(?=(N[^P][ST][^P]))`.
    * Use `re.finditer` to locate matches, extracting the 1-based start coordinates via `.start() + 1`.

---

## Solution
See the [Python Solution](solution.py) for this problem.

---

## Key Python Concepts Used
-requests.get(): Handles external API connection pooling natively, cleanly managing content extraction without manual buffer loops.

-re.finditer() with (?=...): A lookahead structural frame that inspects the upcoming character array without advancing the string scanner index, ensuring no overlapping entries drop out.

---

Related Problems
SUBS -- Prerequisite: Finding a simple static DNA pattern inside a larger sequence template.

PROT -- Prerequisite: Translating RNA matrices straight into clear amino acid strings.