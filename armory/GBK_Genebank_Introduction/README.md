# GBK -- GenBank Introduction

**Section:** Bioinformatics Armory
**Difficulty:** Easy
**Topics:** `biopython` `databases` `entrez`
**Rosalind Link:** https://rosalind.info/problems/gbk/
**Date Solved:** 2026-07-01

---

## Biological Background

Modern biological research relies heavily on centralized repositories to archive public genetic data. The primary international archive for nucleotide sequences is **GenBank**, curated by the National Center for Biotechnology Information (NCBI). 

Every entry in GenBank is cataloged with strict metadata parameters including its source organism, submission date, geographic origin, and molecule classification. Rather than downloading large sequence archives or scraping web views manually, bioinformaticians query the database programmatically via NCBI's **Entrez Utilites (E-utilities)** API engine.



---

## Problem Statement

Given a genus name, a start date, and an end date, return the total number of Nucleotide GenBank entries matching the specified genus that were uploaded or modified between those date bounds.

The dates are presented in standard `YYYY/MM/DD` formats, and the search must isolate entries matching the molecule class `mRNA`.

---

## Approach

1. **API Identification:** Set the mandatory `Entrez.email` parameter. This informs NCBI's tracking engine who is making the request, which prevents IP throttling or permanent firewall blocks.
2. **Search Term Composition:** Build a targeted NCBI query string combining biological fields and Boolean operators:
   * `"{genus}"[Organism]` -> Restricts searches to the target genus clade.
   * `("{start_date}"[MDAT] : "{end_date}"[MDAT])` -> Enforces a closed modification timeline window.
   * `"mRNA"[Molecule Type]` -> Filters out genomic DNA and structural protein records.
3. **Remote Server Request (`esearch`):** Execute `Bio.Entrez.esearch()`, targeting the `nucleotide` database with the constructed term string.
4. **Structured Object Parsing:** Pass the returning server text handle through `Bio.Entrez.read()`. This automatically converts the incoming XML metadata schema directly into a standard native Python dictionary matrix.
5. **Count Extraction:** Query the record dictionary using the `"Count"` key to pull the frequency count string.

---

## Solution

See the [Python Solution](solution.py) for this problem.

---

## Key Python & Biopython Concepts Used
-E-Utilities Interface (Entrez.esearch): A lightweight API endpoint designed to discover matching record metrics or structural ID indices quickly without transmitting raw sequence sequences.

-XML-to-Object Data Mapping (Entrez.read): Converts complex hierarchical XML payload blocks returned by government servers into accessible, native Python nested hash maps on the fly.

## Related Problems
-INI -- Prerequisite: Initial environment configuration and basic Biopython sequence object interaction.
-DBPR -- Next step: Connecting to UniProt databases to collect protein functional annotation blocks remotely.