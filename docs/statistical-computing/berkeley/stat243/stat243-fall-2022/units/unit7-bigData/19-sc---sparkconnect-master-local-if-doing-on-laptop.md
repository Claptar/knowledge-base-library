---
title: 'sc <- sparkconnect(master = "local") # if doing on laptop'
source: https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd
source_file: sources/berkeley-stat243/stat243-fall-2022/units/unit7-bigData.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# sc <- sparkconnect(master = "local") # if doing on laptop

**Source:** [`units/unit7-bigData.Rmd`](https://github.com/berkeley-stat243/stat243-fall-2022/blob/34dee34760386ed7a0ea4f1fd1c9e7d088e637ff/units/unit7-bigData.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

sc <- spark_connect(master = Sys.getenv("SPARK_URL"),
                    config = conf)  # non-local

### read data in ###

cols <- c(date = 'numeric', hour = 'numeric', lang = 'character',
          page = 'character', hits = 'numeric', size = 'numeric')


## takes a while even with only 1.4 GB (zipped) input data (100 sec.)
wiki <- spark_read_csv(sc, "wikistats",
                       "/global/scratch/paciorek/wikistats/dated",
                       header = FALSE, delimiter = ' ',
                       columns = cols, infer_schema = FALSE)

head(wiki)
class(wiki)
dim(wiki)   # not all operations work on a spark dataframe

### some dplyr operations on the Spark dataset ###

library(dplyr)

wiki_en <- wiki %>% filter(lang == "en")
head(wiki_en)

table <- wiki %>% group_by(lang) %>% summarize(count = n()) %>%
    arrange(desc(count))
## note the lazy evaluation: need to look at table to get computation to run
table
dim(table)
class(table)

### distributed apply ###

## need to use spark_apply to carry out arbitrary R code
## the function transforms a dataframe partition into a dataframe
## see help(spark_apply)
##
## however this is _very_ slow, probably because it involves
## serializing objects between java and R
wiki_plus <- spark_apply(wiki, function(data) {
    data$obama = stringr::str_detect(data$page, "Barack_Obama")
    data
}, columns = c(colnames(wiki), 'obama'))

obama <- collect(wiki_plus %>% filter(obama))

### SQL queries ###

library(DBI)
## reference the Spark table (see spark_read_csv arguments)
## not the R tbl_spark interface object
wiki_en2 <- dbGetQuery(sc,
            "SELECT * FROM wikistats WHERE lang = 'en' LIMIT 10")
wiki_en2
```

---

[← Unit 07 — bigData Part 18 —](18-unit-07-bigdata-part-18.md) · [Up: contents](index.md) · [3. Databases →](20-3-databases.md)
