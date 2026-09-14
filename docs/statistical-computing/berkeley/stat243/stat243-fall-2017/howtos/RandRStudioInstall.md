---
title: RandRStudioInstall
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/howtos/RandRStudioInstall.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2017/howtos/RandRStudioInstall.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# RandRStudioInstall

**Source:** [`howtos/RandRStudioInstall.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/howtos/RandRStudioInstall.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

If your version of R is older than 3.2.0, please install the latest version, though you may be fine with older versions.

To install R, see:

  * Mac: install the R-3.4.1.pkg from http://cran.rstudio.com/bin/macosx/ if you have OS X 10.11 (El Capitan) or higher (or the R-3.3.3.pkg package if you have OS X 10.9 or 10.10)
  * Windows: http://cran.rstudio.com/bin/windows/base/
  * Linux: http://cran.rstudio.com/bin/linux/

Then install RStudio. To do so, see http://www.rstudio.com/ide/download/desktop.

Verify that you can install add-on R packages by installing the 'fields' package. In RStudio, go to 'Tools->Install Packages'. In the resulting dialog box, enter 'fields' (without quotes) in the 'Packages' field. Depending on the location specified in the 'Install to Library' field, you may need to enter your administrator password. To be able to install packages to the directory of an individual user, you may need to do the following:

  * In R, enter the command `Sys.getenv()['R_LIBS_USER']`.
  * Create the directory specified in the result that R returns, e.g., on a Mac, this might be `~/Library/R/3.4/library`.

For more detailed installation instructions for Windows, see the windowsInstall.html file.

---

[Up: contents](../index.md)
