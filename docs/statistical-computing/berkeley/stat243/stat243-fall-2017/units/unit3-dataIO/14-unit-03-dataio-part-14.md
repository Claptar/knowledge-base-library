---
title: Unit 03 — dataIO Part 14 —
source: https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf
source_file: sources/berkeley-stat243/stat243-fall-2017/units/unit3-dataIO.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — dataIO Part 14 —

**Source:** [`units/unit3-dataIO.pdf`](https://github.com/berkeley-stat243/stat243-fall-2017/blob/0e9c7fe58194834b0d43b3dbf152d28a37044d05/units/unit3-dataIO.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.2 XML**

XML is a markup language used to store data in self-describing (no metadata needed) format, often with a hierarchical structure. It consists of sets of elements (also known as nodes because they generally occur in a hierarchical structure and therefore have parents, children, etc.) with tags that identify/name the elements, with some similarity to HTML. Some examples of the use of XML include serving as the underlying format for Microsoft Office and Google Docs documents and for the KML language used for spatial information in Google Earth.

Here’s a brief example. The book with id attribute _bk101_ is an element; the author of the book is also an element that is a child element of the book. The id attribute allows us to uniquely identify the element.

<?xml version="1.0"?>

<catalog>

<book id="bk101"> <author>Gambardella, Matthew</author> <title>XML Developer's Guide</title> <genre>Computer</genre> <price>44.95</price> <publish_date>2000-10-01</publish_date>

<description>An in-depth look at creating applications with XML.</description> </book> <book id="bk102"> <author>Ralls, Kim</author> <title>Midnight Rain</title> <genre>Fantasy</genre> <price>5.95</price> <publish_date>2000-12-16</publish_date>

<description>A former architect battles corporate zombies, an evil </book> </catalog>

15

We can read XML documents into R using _xmlToList()_ or _xmlToDataFrame()_ . Here’s an example of working with lending data from the Kiva lending non-profit. You can see the XML format in a browser at http://api.kivaws.org/v1/loans/newest.xml.

doc <- **xmlParse** ("http://api.kivaws.org/v1/loans/newest.xml") data <- **xmlToList** (doc, addAttributes = FALSE) **names** (data) ## [1] "paging" "loans" **length** (data$loans) ## [1] 20 data$loans[[2]][ **c** ('name', 'activity', 'sector', 'location', 'loan_amount')] ## $name ## [1] "Gulrukhsor" ## ## $activity ## [1] "Cafe" ## ## $sector ## [1] "Food" ## ## $location ## $location$country_code ## [1] "TJ" ## ## $location$country ## [1] "Tajikistan" ## ## $location$town ## [1] "Vahdat" ## ## $location$geo ## $location$geo$level ## [1] "town"

16

|##||
|---|---|
|##|$location$geo$pairs|
|##|[1] "39 71"|
|##||
|##|$location$geo$type|
|##|[1] "point"|
|##||
|##||
|##||
|##|$loan_amount|
|##|[1] "575"|
|_## _|_let's try to get the loan data into a data frame_|
|lo|ansNode <- **xmlRoot**(doc)[["loans"]]|
|**le**|**ngth**(**xmlChildren**(loansNode))|
|##|[1] 20|
|lo|ans <- **xmlToDataFrame**(**xmlChildren**(loansNode))|
|**di**<br>|**m**(loans)<br>|
|##|[1] 20 20|
|**he**<br>|**ad**(loans)<br><br>|
|##|id<br>name description|
|##|1 1364518<br>Solomboahirana<br>fren|
|##|2 1363041<br>Gulrukhsor<br>ruen|
|##|3 1364504<br>Elisabeth<br>fren|
|##|4 1364508<br>Papa Samba<br>fren|
|##|5 1365895 Maria Auxiliadora Group<br>esen|
|##|6 1365892<br>Luis Alfredo<br>esen|
|##|status funded_amount basket_amount<br>image|
|##|1 fundraising<br>0<br>25 26187111|
|##|2 fundraising<br>0<br>0 26169081|
|##|3 fundraising<br>0<br>0 26186831|
|##|4 fundraising<br>0<br>0 26186931|
|##|5 fundraising<br>0<br>0 26204751|


17

|##|6|fundraising<br>0<br>0 26204651|
|---|---|---|
|##||activity<br>sector|
|##|1|Pigs Agriculture|
|##|2|Cafe<br>Food|
|##|3|Fruits & Vegetables<br>Food|
|##|4|Cleaning Services<br>Services|
|##|5|Clothing Sales<br>Clothing|
|##|6|Cattle Agriculture|
|##|||
|##|1|to purchase|
|##|2|to buy a toaster oven and exp|
|##|3|to purchase fruits and vegetables to be resold at|
|##|4|to purchase an automobile pressure washer, mats,|
|##|5|to buy assorted clot|
|##|6|purchase cattle to raise and to provide another source of income when h|
|##||location|
|##|1|MGMadagascarTalatatown-20 47point|
|##|2|TJTajikistanVahdattown39 71point|
|##|3|SNSenegalcountry14 -14point|
|##|4|SNSenegalcountry14 -14point|
|##|5|PYParaguayCoronel Oviedotown-25.416667 -56.45point|
|##|6|SVEl SalvadorCiudad El Triunfotown13.833333 -88.916667point|
|##||partner_id<br>posted_date|
|##|1|359 2017-09-01T15:30:05Z|
|##|2|63 2017-09-01T15:30:02Z|
|##|3|108 2017-09-01T15:20:03Z|
|##|4|108 2017-09-01T15:20:03Z|
|##|5|58 2017-09-01T15:20:03Z|
|##|6|199 2017-09-01T15:10:06Z|
|##||planned_expiration_date loan_amount borrower_count|
|##|1|2017-10-01T15:30:05Z<br>150<br>1|
|##|2|2017-10-01T15:30:02Z<br>575<br>1|
|##|3|2017-10-01T15:20:03Z<br>200<br>1|
|##|4|2017-10-01T15:20:03Z<br>200<br>1|
|##|5|2017-10-01T15:20:02Z<br>4025<br>20|
|##|6|2017-10-01T15:10:05Z<br>1000<br>1|


18

---

[← Unit 03 — dataIO Part 13 —](13-unit-03-dataio-part-13.md) · [Up: contents](index.md) · [Unit 03 — dataIO Part 15 — →](15-unit-03-dataio-part-15.md)
