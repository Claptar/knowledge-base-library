---
title: Unit 03 — Rinput Part 14 —
source: https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf
source_file: sources/berkeley-stat243/stat243-fall-2015/units/unit3-Rinput.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Unit 03 — Rinput Part 14 —

**Source:** [`units/unit3-Rinput.pdf`](https://github.com/berkeley-stat243/stat243-fall-2015/blob/ee3c3c2c523a96eefceddf8703d4938396730993/units/unit3-Rinput.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

### **3.2 XML**

XML is a markup language used to store data in self-describing (no metadata needed) format, often with a hierarchical structure. It consists of sets of elements (also known as nodes) with tags that identify/name the elements, with some similarity to HTML. Some examples of the use of XML include serving as the underlying format for Microsoft Office and Google Docs documents and for the KML language used for spatial information in Google Earth.

Here’s a brief example. The book with id attribute _bk101_ is an element; the author of the book is also an element that is a child element of the book. The id attribute allows us to uniquely identify the element.

<?xml version="1.0"?>

<catalog>

<book id="bk101"> <author>Gambardella, Matthew</author> <title>XML Developer's Guide</title> <genre>Computer</genre> <price>44.95</price> <publish_date>2000-10-01</publish_date>

<description>An in-depth look at creating applications with XML.</description> </book> <book id="bk102"> <author>Ralls, Kim</author> <title>Midnight Rain</title> <genre>Fantasy</genre> <price>5.95</price> <publish_date>2000-12-16</publish_date>

<description>A former architect battles corporate zombies, an evil </book> </catalog>

14

We can read XML documents into R using _xmlToList()_ or _xmlToDataFrame()_ . Here’s an example of working with lending data from the Kiva lending non-profit. You can see the XML format in a browser at http://api.kivaws.org/v1/loans/newest.xml.

doc <- **xmlParse** ("http://api.kivaws.org/v1/loans/newest.xml") data <- **xmlToList** (doc, addAttributes = FALSE) **names** (data) ## [1] "paging" "loans" **length** (data$loans) ## [1] 20 data$loans[[2]][ **c** ('name', 'activity', 'sector', 'location', 'loan_amount')] ## $name ## [1] "Alice" ## ## $activity ## [1] "Farming" ## ## $sector ## [1] "Agriculture" ## ## $location ## $location$country_code ## [1] "KE" ## ## $location$country ## [1] "Kenya" ## ## $location$town ## [1] "Kisii" ## ## $location$geo ## $location$geo$level ## [1] "town"

15

|##<br>##|$location$geo$pairs|
|---|---|
|##|[1] "-0.683333 34.766667"|
|##||
|##|$location$geo$type|
|##|[1] "point"|
|##||
|##||
|##||
|##|$loan_amount|
|##|[1] "250"|
|_#_|_et'strytogettheloandataintoadataframe_|
|<br>lo<br>lo<br>**he**<br>|<br>ansNode <- **xmlRoot**(doc)[["loans"]]<br>ans <- **xmlToDataFrame**(**xmlChildren**(loansNode))<br>**ad**(loans)<br><br><br>|
|##|id<br>name description<br>status|
|##|1 941854<br>Nzara<br>en fundraising|
|##|2 941853<br>Alice<br>en fundraising|
|##|3 941852<br>Zeqirja<br>en fundraising|
|##|4 941922 Regina Lisbeth<br>esen fundraising|
|##|5 942082<br>Mwanamisi<br>en fundraising|
|##|6 942114<br>Felismina<br>en fundraising|
|##|funded_amount basket_amount<br>image|
|##|1<br>0<br>0 19696811|
|##|2<br>0<br>0 19668581|
|##|3<br>0<br>0 19682991|
|##|4<br>0<br>0 19698391|
|##|5<br>0<br>0 19700811|
|##|6<br>0<br>0 19593491|
|##|activity<br>sector|
|##|1<br>Butcher Shop<br>Food|
|##|2<br>Farming Agriculture|
|##|3<br>Dairy Agriculture|
|##|4<br>Retail<br>Retail|
|##|5 Fruits & Vegetables<br>Food|


16

|## <br>##<br>##|6<br> 1|Agriculture Agriculture<br>|
|---|---|---|
|##|2|to buy certified fertilizers for top dressing her nappier grass in orde|
|##|3||
|##|4|to invest|
|##|5||
|##|6||
|##||location|
|##|1|KEKenyaTiribetown1 38point|
|##|2|KEKenyaKisiitown-0.683333 34.766667point|
|##|3|XKKosovocountry42.583333 21point|
|##|4|SVEl Salvadorcountry13.833333 -88.916667point|
|##|5|KEKenyaTiribetown1 38point|
|##|6|TLTimor-LesteOe-cussetown-8.833333 125.75point|
|##||partner_id<br>posted_date|
|##|1|164 2015-09-04T01:30:03Z|
|##|2|133 2015-09-04T01:30:02Z|
|##|3|240 2015-09-04T01:20:05Z|
|##|4|81 2015-09-04T01:20:03Z|
|##|5|164 2015-09-04T01:10:05Z|
|##|6|243 2015-09-04T01:10:05Z|
|##||planned_expiration_date loan_amount borrower_count|
|##|1|2015-10-04T01:30:03Z<br>200<br>1|
|##|2|2015-10-04T01:30:02Z<br>250<br>1|
|##|3|2015-10-04T01:20:04Z<br>2050<br>1|
|##|4|2015-10-04T01:20:03Z<br>500<br>1|
|##|5|2015-10-04T01:10:05Z<br>200<br>1|
|##|6|2015-10-04T01:10:05Z<br>600<br>1|
|##||lender_count bonus_credit_eligibility|
|##|1|0<br>1|
|##|2|0<br>0|
|##|3|0<br>1|
|##|4|0<br>1|
|##|5|0<br>1|
|##|6|0<br>1|


17

---

[← [1] "Migrant Chaos\nMounts While\nEurope Gropes\nfor a Response"](13-1-migrant-chaos-nmounts-while-neurope-gropes-nfor-a-response.md) · [Up: contents](index.md) · [Unit 03 — Rinput Part 15 — →](15-unit-03-rinput-part-15.md)
