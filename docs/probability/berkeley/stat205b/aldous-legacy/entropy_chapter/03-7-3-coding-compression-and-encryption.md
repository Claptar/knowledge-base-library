---
title: 7.3 Coding, compression and encryption
source: https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf
source_file: sources/berkeley-stat205b/aldous-legacy/entropy_chapter.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# 7.3 Coding, compression and encryption

**Source:** [`entropy_chapter.pdf`](https://www.stat.berkeley.edu/~aldous/205B/entropy_chapter.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

The word _coding_ nowadays primarily means “writing computer code” but here we are concerned with representing data in some convenient form. A simple example is the original ASCII scheme (section 7.6) for representing letters and typewriter symbols in binary. In choosing how to code a particular type of data there are several issues one might consider.

- _Compression_ : coding to make a text shorter

is useful both in data storage and in data transmission, because there is some “cost” both to storage space and transmission time.

_• Encryption_ : coding for secrecy

is familiar from old spy novels and from modern concerns about security of information sent over the internet. These di↵er in an obvious way. Compressing files on your computer will produce, say, a `.zip` file, and the algorithms for compressing and decompressing are public. Encryption algorithms in widespread use are commonly like public-key cryptography in that the logical form of the algorithms for encryption and decryption are public, but a private key (like a password) is required to actually perform decryption. In contrast, intelligence agencies presumably use algorithms whose

> 3The solution of _E_ ( **p** ) = log _N_ e↵, typically not actually an integer.

_7.3. CODING, COMPRESSION AND ENCRYPTION_

107

form is secret. For concreteness, in this lecture I talk in terms of coding English language text, but the issues are the same for any kind of data. A third issue I will not discuss is

- robustness under errors in data transmission: **error-correcting code**

Intuitively there seems no particular connection between encryption and compression – if anything, they seem opposites, involving secrecy and openness. But a consequence of the mathematical theory outlined in this lecture is that

- (*) finding good codes for encryption is the same as finding good codes for compression.

Here is a verbal argument for (*). A code or cipher transforms _plaintext_ into _ciphertext_ . The simplest substitution cipher transforms each letter into another letter. Such codes – often featured as puzzles in magazines – are easy to break using the fact that di↵erent letters and letter-pairs occur in English (and other natural languages) with di↵erent frequencies. A more abstract viewpoint is that there are 26! possible “codebooks” but that, given a moderately long ciphertext, only one codebook corresponds to a meaningful plaintext message.

Now imagine a hypothetical language in which _every_ string of letters like QHSKUUC . . . had a meaning. In such a language, a substitution cipher would be unbreakable, because an adversary seeing the ciphertext would know only that it came from of 26! possible plaintexts, and if all these are meaningful then there would be no way to pick out the true plaintext. Even though the context of secrecy would give hints about the general nature of a message – say it has military significance, and only one in a million messages has military significance – that still leaves 10<sup>_−_6</sup> _⇥_ 26! possible plaintexts.

Returning to English language plaintext, let us think about what makes a _compression_ code good. It is intuitively clear that for an ideal coding we want each possible sequence of ciphertext to arise from some meaningful plaintext (otherwise we are wasting an opportunity); and it is also intuitively plausible that we want the possible ciphertexts to be approximately equally likely (this is the key issue that the mathematics deals with).

Suppose there are 2<sup>1000</sup> possible messages, and we’re equally likely to want to communicate each of them. Then an ideal code would encode each as a di↵erent 1000-bit (binary digit) string, and this could be a public algorithm for encoding and decoding. Now consider a substitution code based on the 32 word “alphabet” of 5-bit strings. Then we could encrypt a message by

_CHAPTER 7. CODING AND ENTROPY_

108

(i) apply the public algorithm to get a 1000-bit string; (ii) then use the substitution code, separately on each 5-bit block. An adversary would know we had used one of the 32! possible codebooks and hence know that the message was one of a certain set of 32! plaintext messages. But, by the “approximately equally likely” part of the ideal coding scheme, these would be approximately equally likely, and again the adversary has no practical way to pick out the true plaintext.

**Conclusion:** given a good public code for compression, one can easily convert it to a good code for encryption.

---

[← 7.2 Entropy as a measure of unpredictability](02-7-2-entropy-as-a-measure-of-unpredictability.md) · [Up: contents](index.md) · [7.4 The asymptotic equipartition property →](04-7-4-the-asymptotic-equipartition-property.md)
