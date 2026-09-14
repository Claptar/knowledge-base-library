---
title: On your laptop
source: https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/howtos/RandRStudioInstall.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2021/howtos/RandRStudioInstall.Rmd
licence: CC0-1.0
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# On your laptop

**Source:** [`howtos/RandRStudioInstall.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2021/blob/c918dcc56a197cc539e270f1f7d076010b175c52/howtos/RandRStudioInstall.Rmd) · **Licence:** CC0-1.0 · Converted 2026-09-14 from `.Rmd` (lossless)

If your version of R is older than 4.0.0, please install the latest version. For the most part R 3.5 or 3.6 would be fine but there are a couple topics in Unit 5 that will assume you are using R 4.0.0 or later.

To install R, see:

  * MacOS: install the R-4.1.0.pkg from https://cran.rstudio.com/bin/macosx
  * Windows: https://cran.rstudio.com/bin/windows/base/
  * Linux: https://cran.rstudio.com/bin/linux/

Then install RStudio. To do so, see https://www.rstudio.com/ide/download/desktop, scrolling down to the "Installers for Supported Platforms" section and selecting the Installer for your operating system.

Verify that you can install add-on R packages by installing the 'fields' package. In RStudio, go to 'Tools->Install Packages'. In the resulting dialog box, enter 'fields' (without quotes) in the 'Packages' field. Depending on the location specified in the 'Install to Library' field, you may need to enter your administrator password. To be able to install packages to the directory of an individual user, you may need to do the following:

  * In R, enter the command `Sys.getenv()['R_LIBS_USER']`.
  * Create the directory specified in the result that R returns, e.g., on a Mac, this might be `~/Library/R/4.0/library`.

For more detailed installation instructions for Windows, see the windowsInstall.html file.

---

[Up: contents](index.md) · [Via DataHub →](02-via-datahub.md)
