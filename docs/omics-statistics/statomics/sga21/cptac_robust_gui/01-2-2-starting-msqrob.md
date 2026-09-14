---
title: 2.2. Starting MSqRob
source: https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd
source_file: sources/statomics-sga21/cptac_robust_gui.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# 2.2. Starting MSqRob

**Source:** [`cptac_robust_gui.Rmd`](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/cptac_robust_gui.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

You can find the installation instructions for the installation of msqrob2 and the msqrob2gui graphical user interface (GUI)/shinyApp in [software](https://github.com/statOmics/SGA21/blob/0ad787d4cc2bb2f4636440840a8a923cf6c09839/software.html)

Upon installation

1. Open Rstudio, you will see the following login window

![Figure 1. RStudio](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/rstudio.png)


2. Copy and paste following commands in the console window and type enter

```
library(msqrob2gui)
launchMsqrob2App()
```

![Figure 2. Rstudio with launchcommand](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/rstudio2.png)


- The first line will load the msqrob2gui package and its dependencies
- The second line will launch the GUI/shinyApp

3. A new window will open with the shinyApp

![Figure 3. msqrob2 ShinyApp](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/shinyApp.png)

4. It is advicable to open the shiny app in a webbrowser. You can do that by clicking on the button `Open in Browser`, which you can find above the blue navigation bar and the shinyApp will pop up in a new browser tab/window.

![Figure 4. msqrob2gui in browser tab](https://raw.githubusercontent.com/statOmics/SGA21/0ad787d4cc2bb2f4636440840a8a923cf6c09839/figures/msqrob2gui.png)

---

[Up: contents](index.md) · [2.2.1. The Input tab →](02-2-2-1-the-input-tab.md)
