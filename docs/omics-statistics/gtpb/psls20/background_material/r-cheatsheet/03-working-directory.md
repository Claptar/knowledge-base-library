---
title: Working Directory
source: https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf
source_file: sources/gtpb-psls20/background_material/r-cheatsheet.pdf
licence: CC BY 4.0
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Working Directory

**Source:** [`background_material/r-cheatsheet.pdf`](https://github.com/GTPB/PSLS20/blob/55acd654e639f1d5297dc0f2e46d8fd6855b5bad/background_material/r-cheatsheet.pdf) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

```
getwd()
```

Find the current working directory (where inputs are found and outputs are sent). **`setwd(‘C://file/path’)`** Change the current working directory.

**Use projects in RStudio to set the working directory to the folder you are working in.**

### **Programming**

### **Vectors**

#### **Creating Vectors**

#### **While Loop**

#### **For Loop**

|`c(2, 4, 6)`|`2 4 6`|Join elements into<br>a vector|`for (variable insequence){`|
|---|---|---|---|
|`2:6`|`2 3 4 5 6`|An integer<br>sequence|`Do something`<br>`}`|
|`seq(2, 3, by=0.5)`|`2.0 2.5 3.0`|A complex<br>sequence|**Example**<br>`for (i in 1:4){`|
|`rep(1:2, times=3)`|`1 2 1 2 1 2`|Repeat a vector|`j <- i + 10`|
|`rep(1:2, each=3)`|`1 1 1 2 2 2`|Repeat elements<br>of a vector|`print(j)`|


```
while (condition){
Do something
```

```
}
```

##### **Example**

```
while (i < 5){
print(i)
```

```
i <- i + 1
```

```
}
```

```
}
```

#### **Vector Functions**

#### **Functions**

#### **If Statements**

**`sort(x)`** Return x sorted. **`table(x)`** See counts of values.

**`rev(x)`** Return x reversed. **`unique(x)`** See unique values.

```
function_name <- function(var){
Do something
return(new_variable)
```

```
if (condition){
Do something
} else {
Do something different
```

```
}
```

```
}
```

#### **Selecting Vector Elements**

##### **Example**

##### **Example**

**By Position**

```
square <- function(x){
squared <- x*x
return(squared)
```

```
if (i > 3){
print(‘Yes’)
} else {
print(‘No’)
```

|**`x[4]`**|The fourth element.|`print(‘Yes’)`<br>`} else {`|||`squared <- x*x`|
|---|---|---|---|---|---|
|**`x[-4]`**|All but the fourth.|`print(‘No’)`<br>`}`||<br>`}`|`return(squared)`|
|**`x[2:4]`**|Elements two to four.|**Re**|**ading a**|**nd Writ**|**ing Data**|
|**`x[-(2:4)]`**|All elements except<br>two to four.|**Input**|**Ouput**||**Description**|
|**`x[c(1, 5)]`**|Elements one and<br>five.|`df <- read.table(‘file.txt’)`|`write.t`|`able(df,`|`‘file.txt’)`<br>Read and write a delimited text<br>file.|
|**B**|**y Value**||||Read and write a comma|
|**`x[x ==10]`**|Elements which<br>are equal to 10.|`df <- read.csv(‘file.csv’)`|`write.`|`csv(df,‘`|`file.csv’)`<br>separated value file. This is a<br>special case of read.table/<br>write.table.|
|**`x[x <0]`**<br>**`x[x %in%`**<br>**`c(1, 2, 5)]`**|All elements less<br>than zero.<br>Elements in the set<br>1, 2, 5.|`load(‘file.RData’)`|`save(df,`|`file =’`|`file.Rdata’)`<br>Read and write an R data file, a<br>file type special for R.|
|**Nam**|**ed Vectors**|`a == b`<br>Are equal<br>**Conditions**|`a > b`|Greater than|<br>`a >= b`<br>Greater than<br>or equal to<br>`is.na(a)`<br>Is missing|
|**`x[‘apple’]`**|Element with<br>name ‘apple’.|`a != b`<br>Not equal|`a < b`|Less than|`a <= b`<br>Less than or<br>equal to<br>`is.null(a)`<br>Is null|


RStudio® is a trademark of RStudio, Inc.  • <u>CC BY Mhairi McNeill  •  mhairihmcneill@gmail.com</u>

Learn more at web page or vignette  •  package  version  •  Updated: 3/15

---

[← Using Libraries](02-using-libraries.md) · [Up: contents](index.md) · [Types →](04-types.md)
