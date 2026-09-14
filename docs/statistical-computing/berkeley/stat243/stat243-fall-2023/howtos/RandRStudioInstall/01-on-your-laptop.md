---
title: On your laptop
source: https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/howtos/RandRStudioInstall.md
source_file: sources/berkeley-stat243/stat243-fall-2023/howtos/RandRStudioInstall.md
licence: BSD-3-Clause
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# On your laptop

**Source:** [`howtos/RandRStudioInstall.md`](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/howtos/RandRStudioInstall.md) · **Licence:** BSD-3-Clause · Converted 2026-09-14 from `.md` (lossless)

If your version of R is older than 4.0.0, please install the latest version.

To install R, see:

  * MacOS: install the R-4.2.1.pkg from [https://cran.rstudio.com/bin/macosx](https://cran.rstudio.com/bin/macosx)
  * Windows: [https://cran.rstudio.com/bin/windows/base/](https://cran.rstudio.com/bin/windows/base/)
  * Linux: [https://cran.rstudio.com/bin/linux/](https://cran.rstudio.com/bin/linux/)

Then install RStudio. To do so, see
[https://www.rstudio.com/ide/download/desktop](https://www.rstudio.com/ide/download/desktop), scrolling down to the "Installers
for Supported Platforms" section and selecting the Installer for your operating
system.

Verify that you can install add-on R packages by installing the 'fields'
package. In RStudio, go to 'Tools->Install Packages'. In the resulting dialog
box, enter 'fields' (without quotes) in the 'Packages' field. Depending on the
location specified in the 'Install to Library' field, you may need to enter your
administrator password. To be able to install packages to the directory of an
individual user, you may need to do the following:

  * In R, enter the command `Sys.getenv()['R_LIBS_USER']`.
  * Create the directory specified in the result that R returns, e.g., on a Mac, this might be `~/Library/R/4.0/library`.

For more detailed installation instructions for Windows, see [Using R, RStudio, and LaTeX on Windows](https://github.com/berkeley-stat243/stat243-fall-2023/blob/14ac5335a61c8e78d9c36ec381d606a22cb95bf9/howtos/windowsInstall.Rmd) file.

---

[Up: contents](index.md) · [Via DataHub →](02-via-datahub.md)
