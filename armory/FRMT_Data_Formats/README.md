# FRMT -- Data Formats

**Section:** Bioinformatics Stronghold
**Difficulty:** Easy
**Topics:** `data-formats` `network-apis` `biopython` `ncbi`
**Rosalind Link:** https://rosalind.info/problems/frmt/
**Date Solved:** 2026-07-12

---

## Biological & Engineering Background

### Bioinformatics Data Ecosystems
Biological information is stored across hundreds of structured data profiles depending on its metadata focus:
* **FASTA:** Minimalist sequence structural framework containing a simple descriptor header token (`>`) followed by unformatted raw structural string arrays.
* **GenBank (`gb`):** Highly descriptive biological layout architecture tracking explicit taxonomy headers, publishing annotations, chromosome coordinate feature tables, and publication citations.

### Remote Access via NCBI Entrez E-utilities
Instead of parsing complex text engines manually, the National Center for Biotechnology Information (NCBI) exposes a suite of API utilities known as **E-utilities** (`efetch`, `esearch`). Using Biopython's abstraction module (`Bio.Entrez`), we can seamlessly pipe official cross-database queries straight into our local workflows.

---

## Problem Statement

Given a collection of at most 10 NCBI GenBank Accession IDs separated by spaces. 

Find the accession ID corresponding to the shortest sequence in the list, retrieve its complete entry from NCBI in FASTA format, and print it.

---

## Approach

1.  **Read and Parse Accession Targets:** Ingest the space-delimited ID line utilizing standard `pathlib` workspace files.
2.  **Establish Mailbox Authentication:** Assign a valid placeholder to `Entrez.email` as required by NCBI API throttling guidelines.
3.  **Execute Batch Query Loop (`efetch`):** 
    * Submit the complete array of Accession IDs concurrently inside a single connection pool request targeting the `nucleotide` database.
    * Mandate the response mapping profile using `rettype="fasta"`.
4.  **Identify the Shortest Sequence:** Iterate through the parsed FASTA sequences using `SeqIO.parse` to evaluate sequence lengths (`len(record.seq)`), keeping track of the minimum.
5.  **Output Format Alignment:** Print the absolute string contents of the shortest entry, keeping the original multiline structural layout completely intact.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python & Biopython Concepts Used

-Entrez.efetch(): An automated wrapper executing backend API requests. Passing multi-token comma-separated inputs compiles records into a single transport batch, bypassing strict rate limit flags.

-min(records, key=lambda x: len(x.seq)): Leverages Python's native functional sorting metrics to identify target elements in a clean O(n) sweep without array reallocation overhead.

-StringIO: Emulates traditional physical file descriptor hooks entirely inside volatile RAM memory blocks, letting string content flow through standard file-based parsers like SeqIO.

---

## Related Problems
-DNA -- Prerequisite: Understanding the absolute foundational layout of nucleotide strings.
-INI -- Core: Initial installation and sanity checking of the local working Biopython environment wrapper.