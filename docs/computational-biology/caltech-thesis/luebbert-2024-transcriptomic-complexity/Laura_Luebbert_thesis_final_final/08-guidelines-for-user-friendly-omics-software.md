---
title: Guidelines for User-Friendly Omics Software
source: https://thesis.library.caltech.edu/16368/
source_file: sources/luebbert-2024-transcriptomic-complexity/Laura_Luebbert_thesis_final_final.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Guidelines for User-Friendly Omics Software

**Source:** `Laura_Luebbert_thesis_final_final.pdf` from [luebbert-2024-transcriptomic-complexity](https://thesis.library.caltech.edu/16368/) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The below is a checklist of simple yet effective guidelines for user-friendly omics software curated based on the analyses performed in part I of the introduction:

- Devise a memorable and distinctive name for the tool that is compatible with Google and GitHub searches (good example: kallisto, poor example: bio)

   - Tip: For increased searchability on GitHub, include GitHub keywords and a short “About” description

- If possible, the computational resources (e.g., memory and disk space) to run the software should not exceed those of a standard laptop

   - If this is not feasible, consider supplying a simplified version of the software (for example, the widely used _gget alphafold_ module (see Chapter 2) allows users to run a simplified version of AlphaFold2 without requiring 3 TB of disk space and a modern NVIDIA GPU)

- Provide users with a functional installation (including package dependencies) using a single line of code, ideally through the widely used package managers PyPI, Bioconda, and/or Bioconductor (e.g., “pip install gget”)

- Keep package dependencies to a minimum (ideally limited to standard libraries or widely used third-party libraries, e.g., numpy), and specify dependency versions if necessary (avoid this or provide version ranges to avoid package version conflicts)

- Provide clear and coherent documentation through various media:

   - Provide function descriptions in Python/R/etc.

   - Add help (-h / --help) methods to shell scripts

   - Write a GitHub README that includes the documentation or links to the documentation

   - Write extensive documentation that includes installation instructions and ideally a “quick start” or “getting started” guide, and describe the function and the data type (e.g., int) of each argument with input examples

      - 8

   - Write tutorials spanning different use cases of the software, ideally in the form of immediately executable Google Colab notebooks, and link to them in the documentation

   - To increase accessibility, use alt text for images and provide the documentation in different languages, e.g., English and Spanish

- Keep required arguments to a minimum: The simplest use case of the software tool should require as little user input as possible to simplify the process of getting started

- Write extensive unit tests and use GitHub Actions to automatically run the tests when changes to the code are committed AND in specified time intervals, e.g., once a week

   - Include a badge in the GitHub README and/or the documentation to inform users of the current test status (fail/pass)

- Maintain the software tool:

   - Maintain backward compatibility when implementing changes

   - Document the changes for each new release in the software documentation

   - Update the software when the unit tests break (Tip: Set up E-mail notifications through GitHub for failing unit tests)

   - Respond to GitHub issues raised by users (I do not recommend the use of bots that automatically close “stale” GitHub issues)

   - Update dependencies to the most recent versions as updates are released

- Facilitate and promote user feedback and contribution:

   - Set up GitHub issue templates to facilitate communication between users and software developers

   - Include contributing guidelines in the software documentation, including a detailed checklist for contributors (examples: <u>https://docs.github.com/en/communities/setting-up-your-project-for-healthycontributions/setting-guidelines-for-repository-contributors, https://pachterlab.github.io/gget/en/contributing.html)</u>

9

_C h a p t e r 2_

---

[← INTRODUCTION – PART II](07-introduction-part-ii.md) · [Up: contents](index.md) · [SOFTWARE FOR BIOLOGISTS BY BIOLOGISTS - PART I →](09-software-for-biologists-by-biologists---part-i.md)
