---
title: Data Frames
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Data Frames

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

##### **dplyr** library.

`df <- data.frame(x = 1:3, y = c('a', 'b', 'c'))` A special case of a list where all elements are the same length.

##### **List subsetting**


<!-- Start of picture text -->
x y<br>df$x df[[2]]<br>1 a<br>2 b<br>Understanding a data frame<br>See the full data<br>View(df)<br>3 c frame.<br>See the first 6<br>Matrix subsetting head(df)<br>rows.<br><!-- End of picture text -->


```
df[ , 2]
df[2, ]
df[2, 2]
```

`nrow(df)` **`cbind`** - Bind columns. Number of rows. `ncol(df)` Number of columns. **`rbind`** - Bind rows. `dim(df)` Number of columns and rows.

---

[← Lists](09-lists.md) · [Up: contents](index.md) · [Strings →](11-strings.md)
