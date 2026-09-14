---
title: Load audio here
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture15.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Load audio here

**Source:** [`public/lectures/Lecture15.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture15.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

SR = 22050  # target sample rate (librosa default)

def load_clip(path, duration=60, offset=0):
    """Load an audio file. Returns (waveform, sample_rate)."""
    import librosa
    y, sr = librosa.load(path, sr=SR, duration=duration, offset=offset)
    print(f'Loaded: {path}  ({len(y)/sr:.1f}s, {len(y):,} samples, fs={sr} Hz)')
    return y, sr

---

[← Quick poll - Guess the category](02-quick-poll---guess-the-category.md) · [Up: contents](index.md) · [Change these paths if you have other sounds you want to use →](04-change-these-paths-if-you-have-other-sounds-you-want-to-use.md)
