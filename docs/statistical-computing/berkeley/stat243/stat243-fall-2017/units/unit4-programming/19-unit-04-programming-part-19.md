---
title: Unit 04 — programming Part 19 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit4-programming.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 04 — programming Part 19 —

**Source:** [`units/unit4-programming.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit4-programming.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **4.2 Attributes**

_Attributes_ are information about an object attached to an object as something that looks like a named list. Attributes are often copied when operating on an object. This can lead to some weirdlooking formatting:

x <- **rnorm** (10 * 365) qs <- **quantile** (x, **c** (.025, .975)) qs ## 2.5% 97.5% ## -2.00 1.94 qs[1] + 3 ## 2.5% ## 1

Thus in an subsequent operations with _qs_ , the _names_ attribute will often get carried along. We can get rid of it:

**names** (qs) <- **NULL** qs ## [1] -2.00 1.94

14

A common use of attributes is that rows and columns may be named in matrices and data frames, and elements in vectors:

**row.names** (mtcars)[1:6] ## [1] "Mazda RX4" "Mazda RX4 Wag" ## [3] "Datsun 710" "Hornet 4 Drive" ## [5] "Hornet Sportabout" "Valiant" **names** (mtcars) ## [1] "mpg" "cyl" "disp" "hp" "drat" "wt" "qsec" ## [8] "vs" "am" "gear" "carb" **attributes** (mtcars) ## $names ## [1] "mpg" "cyl" "disp" "hp" "drat" "wt" "qsec" ## [8] "vs" "am" "gear" "carb" ## ## $row.names ## [1] "Mazda RX4" "Mazda RX4 Wag" ## [3] "Datsun 710" "Hornet 4 Drive" ## [5] "Hornet Sportabout" "Valiant" ## [7] "Duster 360" "Merc 240D" ## [9] "Merc 230" "Merc 280" ## [11] "Merc 280C" "Merc 450SE" ## [13] "Merc 450SL" "Merc 450SLC" ## [15] "Cadillac Fleetwood" "Lincoln Continental" ## [17] "Chrysler Imperial" "Fiat 128" ## [19] "Honda Civic" "Toyota Corolla" ## [21] "Toyota Corona" "Dodge Challenger" ## [23] "AMC Javelin" "Camaro Z28" ## [25] "Pontiac Firebird" "Fiat X1-9" ## [27] "Porsche 914-2" "Lotus Europa" ## [29] "Ford Pantera L" "Ferrari Dino" ## [31] "Maserati Bora" "Volvo 142E" ##

15

---

[← Unit 04 — programming Part 18 —](18-unit-04-programming-part-18.md) · [Up: contents](index.md) · [Unit 04 — programming Part 20 — →](20-unit-04-programming-part-20.md)
