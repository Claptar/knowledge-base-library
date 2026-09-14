---
title: Reproducing this work
source: https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/clm.pdf
source_file: sources/berkeley-stat243/stat243-fall-2019/ps/clm.pdf
licence: unresolved
route: pdf
fidelity: lossy
converted: '2026-09-14'
---

# Reproducing this work

**Source:** [`ps/clm.pdf`](https://github.com/berkeley-stat243/stat243-fall-2019/blob/b2795324dec367a50f578b01c67d907994ff40f5/ps/clm.pdf) · **Licence:** unresolved · Converted 2026-09-14 from `.pdf` (lossy)

!!! warning "Converted from PDF — mathematics may be mangled"
    Prose survives a PDF; equations do not. Check anything symbolic against the
    original before relying on it, and mark repairs `**Unverified.**`

This research has been conducted in a full reproducible manner. ‘Reproducibility’ in this context means that the empirical results presented in this work can be fully and exactly recreated by other parties using the data and workflow documentation which we have made publicly available. Reproducibility is necessary for the verification of empirical work and, as a result, has been defined as a ‘cornerstone’ (Mccullough, 2009) or a ‘fundamental tenet’ (Crick et al., 2014) of good scientific practice. Additionally, research conducted in a reproducible manner has been shown to contain fewer errors (Camfield and Palmer-Jones, 2013), completed more efficiently (Donoho, 2010) and garner more citations (King, 1995).

All code used to create the data and analysis in this paper is available at https:// github.com/andykrause/hhLocation. The documentation on this site will provide complete instructions for downloading and executing the necessary code to reproduce our analysis. The raw data (census geographic data and SF1 data) for this analysis are many gigabytes in size. The code will download, extract and clean these data. Users wishing to skip the time-consuming data download and cleaning process may download the cleaned set of data from Harvard’s DataVerse repository – available at https://dataverse.harvard.edu/dataverse/ repHHLoc. Users are encouraged to use our cleaned data for related research, provided the data are cited.

The model we propose here is also reproducible in other contexts. However, when thinking about external validity of the CLM, one should refer the two basic assumptions that this model was developed upon. Our first assumption that housing career increases over a household’s life span should hold globally. Yet, our second assumption about how housing services are being offered across metropolitan regions is US-based and in order for this model to work in other context, this assumption needs to be modified accordingly. Once this assumption is modified, the model in Figure 1 can be reproduced in intersection of the two assumptions and we expect its geometric form to be different for different regions in the world. Future work can reproduce this model in other parts of the world, add more detailed age intervals, or incorporate other proxies for housing career change over time.

### Acknowledgements

We thank the three anonymous reviewers for their careful reading and constructive comments.

### Funding

This research received no specific grant from any funding agency in the public, commercial, or notfor-profit sectors.

### Notes

1. To simplify the model, we consider housing provision to refer to structural utilitygenerating assets such as home size, number of bathrooms, lot size, etc. Location specific amenities – which vary in utility depending on household preference – are ignored.

2. http://www.census.gov/prod/cen2010/doc/sf1 .pdf.

3. https://dataverse.harvard.edu/dataverse/repH HLoc.

4. Jittering is a function that adds an amount of random noise to the data in order to break ties, and is often used to avoid overplotting.

Estiri and Krause

17

### References

- Abramsson M and Andersson EK (2012) Residential mobility patterns of elderly – Leaving the house for an apartment. Housing Studies 27(5): 582–604.

- Abu-Lughod JL and Foley MM (1960) Consumer strategies. In: Foote NN, et al. (eds) Housing Choices and Housing Constraints. New York: McGraw-Hill, pp. 71–271.

- Bailey AJ (2008) Population geography: Lifecourse matters. Progress in Human Geography 33(3): 407–418.

- Banks J, Blundell R, Oldfield Z, et al. (2007) Housing price volatility and downsizing in later life. National Bureau of Economic Research Working Paper Series, No. 13496. Available

   - at: http://www.nber.org/papers/w13496\n http://www.nber.org/papers/w13496.pdf.

- Beige S and Axhausen KW (2012) Interdependencies between turning points in life and longterm mobility decisions. Transportation 39(4): 857–872.

- Boehm TP and Ihlanfeld KR (1986) Residential mobility and neighborhood quality. Journal of Regional Science 26: 411–424.

- Brown LA and Moore EG (1970) The intra-urban migration process: A perspective. Geografiska Annaler. Series B 52(1): 1–13.

- Camfield L and Palmer-Jones R (2013) Three ‘Rs’ of econometrics: Repetition, reproduction and replication. Journal of Development Studies 49(12): 1607–1614.

- Cervero R and Duncan M (2006) Which reduces vehicle travel more: Jobs–housing balance or retail–housing mixing? Journal of the American Planning Association 72: 475–490.

- Clark WAV (2013) Life course events and residential change: Unpacking age effects on the probability of moving. Journal of Population Research 30(4): 319–334.

- Clark WAV and Coulter R (2015) Who wants to move? The role of neighbourhood change. Environment and Planning A 47(12): 2683–2709.

- Clark WAV and Dieleman FM (1996) Households and Housing: Choice and Outcomes in the Housing Market. New Brunswick, NJ: Center for Urban Policy Research, Rutgers.

- Clark WAV and Huang Y (2003) The life course and residential mobility in British housing markets. Environment and Planning A 35: 323–339.

- Clark WAV and Maas R (2015) Spatial mobility and opportunity in Australia: Residential selection and neighbourhood connections. Urban Studies 53(6): 1317–1331.

- Clark WAV and Morrison PS (2012) Socio-spatial mobility and residential sorting: Evidence from a large-scale Survey. Urban Studies 49(15): 3253–3270.

- Clark WAV and Onaka J (1983) Life cycle and housing adjustment as explanations of residential mobility. Urban Studies 20: 47–57.

- Clark WAV and Withers SD (2007) Family migration and mobility sequences in the United States. Demographic Research 17(20): 591–622. Available at: http://www.demographic-research.org/volumes/vol17/20/ (accessed 4 January 2014).

- Clark WAV, Deurloo MC and Dieleman FM (2002) Housing consumption and residential crowding in US housing market. Journal of Urban Affairs 22(1): 49–63.

- Clark WAV, Deurloo M and Dieleman F (2006) Residential mobility and neighbourhood outcomes. Housing Studies 21(3): 323–342.

- Clark WAV, van Ham M and Coulter R (2014) Spatial mobility and social outcomes. Journal of Housing and the Built Environment 29: 699–727.

- Coulter R and van Ham M (2013) Following people through time: An analysis of individual residential mobility biographies. Housing Studies 28(7): 1037–1055.

- Crick T, Hall BA and Ishtiaq S (2014) ‘‘Can I implement your algorithm?’’: A model for reproducible research software. arXiv Preprint arXiv:1407.5981.

- de Groot C, Mulder C, Das M, et al. (2011) Life events and the gap between intention to move and actual mobility. Environment and Planning A 43: 48–66.

- Denton NA and Massey DS (1991) Patterns of neighborhood transition in a multiethnic world: US metropolitan areas, 1970–1980. Demography 28(1): 41–63.

- Dieleman FM (2001) Modelling residential mobility; a review of recent trends in research. Journal of Housing and the Built Environment 16: 249–265.

- Dieleman FM, Clark WAV and Deurloo MC (2000) The geography of residential

18

Urban Studies

turnover in twenty-seven large US metropolitan housing markets, 1985–95. Urban Studies 37: 223–245.

- Donoho DL (2010) An invitation to reproducible computational research. Biostatistics 11(3): 385–388.

- Durlauf SN (2004) Neighborhood effects. In: Henderson JV and Thisse J-F (eds) Handbook of Regional and Urban Economics. Amsterdam: Elsevier, pp. 2147–2234.

- Estiri H, Krause A and Heris MP (2015) ‘Phasic’ metropolitan settlers: A phase-based model for the distribution of households in US metropolitan regions. Urban Geography 36(5): 777–794.

- Ewing R and Rong F (2008) The impact of urban form on U.S. residential energy use. Housing Policy Debate 19(1): 1–30.

- Frey WH (1978) Mover’s life-cycle stage and choice of destination neighborhood: Implications for urban social structure. In: Clark WAV and Moore EG (eds) Population Mobility and Residential Change. Evanston, IL: Northwestern University, pp. 99–148.

- Geist C and Mcmanus PA (2008) Geographical mobility over the life course: Motivations and implications. Population, Space And Place 14: 283–303.

- Gober P, Larson KL, Quay R, et al. (2013) Why land planners and water managers don’t talk to one another and why they should! Society & Natural Resources 26(3): 356–364.

- Gobillon L and Wolff F-C (2011) Housing and location choices of retiring households: Evidence from France. Urban Studies 48(2): 331–347.

- Hedman L, van Ham M and Manley D (2011) Neighbourhood choice and neighbourhood reproduction. Environment and Planning A 43(6): 1381–1399.

- Hunt B and Balachandran B (2015) Black: White disparities in lung cancer mortality in the 50 largest cities in the United States. Cancer Epidemiology 39(6): 908–916.

- Ihrke D (2014) Reason for Moving: 2012 to 2013. Available at: http://www.census.gov/prod/ 2014pubs/p20–574.pdf.

- Ioannides YM and Zabel JE (2008) Interactions, neighborhood selection and housing demand. Journal of Urban Economics 63: 229–252.

- Judd B, Liu E, Easthope H, et al. (2014) Downsizing amongst older Australians. AHURI Final Report 214: 1–197.

- King G (1995) Replication, replication. PS: Political Science and Politics 28(3): 443–499.

- King M, Steven Ruggles J, Alexander T, et al. (2010) Integrated public use microdata series, current population survey: Version 3.0. (Machine-readable database). Available at: https://cps.ipums.org/cps.

- Kulu H and Milewski N (2007) Family change and migration in the life course. Demographic Research 17: 567–590. Available at: http: //www.demographic-research.org/volumes/vol17/19/ (accessed 1 December 2013).

- Landale NS and Guest AM (1985) Constraints, satisfaction and residential mobility: Speare’s model reconsidered. Demography 22: 199–222.

- Lang RE (2002) Open spaces, bounded places: Does the American West’s arid landscape yield dense metropolitan growth? Housing Policy Debate 13(4): 755–778.

- Lee BA, Oropesa RS and Kanan JW (1994) Neighborhood context and residential mobility. Demography 31: 249–270.

- Lichter DT, Parisi D and Taquino MC (2015) Toward a new macro-segregation? Decomposing segregation within and between metropolitan cities and suburbs. American Sociological Review 80(4): 843–873.

- Mccullough BD (2009) Open access economics journals and the market for reproducible economic research. Economic Analysis & Policy 39(1): 117–126.

- Markusen A and Schrock G (2006) The distinctive city: Divergent patterns in growth, hierarchy and specialisation. Urban Studies 43(8): 1301–1323.

- Moos M (2015) From gentrification to youthification? The increasing importance of young age in delineating high-density living. Urban Studies 54(13): 2903–2920.

- Nechyba TJ and Walsh RP (2004) Urban sprawl. Journal of Economic Perspectives 18: 177–200.

- Quigley JM and Weinberg DH (1977) Intraurban residential mobility: A review and synthesis. International Regional Science Review 2: 41–66.

- Simmons JW (1968) Changing residence in the city: A review of intraurban mobility. Geographical Review 58: 622–651.

19

Estiri and Krause

- Sivak M (2008) Where to live in the United States: Combined energy demand for heating and cooling in the 50 largest metropolitan areas. Cities 25(6): 396–398.

- Speare A (1970) Home ownership, life cycle stage, and residential mobility. Demography 7: 449–458.

- Speare A (1974) Residential satisfaction as an intervening variable in residential mobility. Demography 11: 173–188.

- van der Vlist AJ, Gorter C, Nijkamp P, et al. (2002) Residential mobility and local housing-market differences. Environment and Planning A 34: 1147–1164.

- van Ham M (2012) Housing behaviour. In: Clapham DF, Clark WAV and Gibb K (eds) The

SAGE Handbook of Housing Studies. London: SAGE Publications, pp. 47–65.

- Waddell P, Bhat C, Eluru N, et al. (2007) Modeling interdependence in household residence and workplace choices. Transportation Research Record: Journal of the Transportation Research Board 2003(11): 84–92.

- Winstanley A, Thorns DC and Perkins HC (2002) Moving house, creating home: Exploring residential mobility. Housing Studies 17(6): 813–832.

- Wulff M, Champion A and Lobo M (2010) Household diversity and migration in mid-life: Understanding residential mobility among 45– 64 year olds in Melbourne, Australia. Population, Space and Place 16(4): 307–321.

Appendix 1. List of the 50 most populated CBSAs in the US according to the 2010 US Census.

|CBSA Name|States|2010 Population|
|---|---|---|
|New York-Northern New Jersey-Long Island|NY-NJ-PA|18,897,109|
|Los Angeles-Long Beach-Santa Ana|CA|12,828,837|
|Chicago-Joliet-Naperville|IL-IN-WI|9,461,105|
|Dallas-Fort Worth-Arlington|TX|6,371,773|
|Philadelphia-Camden-Wilmington|PA-NJ-DE-MD|5,965,343|
|Houston-Sugar Land-Baytown|TX|5,946,800|
|Washington-Arlington-Alexandria|DC-VA-MD-WV|5,582,170|
|Miami-Fort Lauderdale-Pompano Beach|FL|5,564,635|
|Atlanta-Sandy Springs-Marietta|GA|5,268,860|
|Boston-Cambridge-Quincy|MA-NH|4,552,402|
|San Francisco-Oakland-Fremont|CA|4,335,391|
|Detroit-Warren-Livonia|MI|4,296,250|
|Riverside-San Bernardino-Ontario|CA|4,224,851|
|Phoenix-Mesa-Glendale|AZ|4,192,887|
|Seattle-Tacoma-Bellevue|WA|3,439,809|
|Minneapolis-St. Paul-Bloomington|MN-WI|3,279,833|
|San Diego-Carlsbad-San Marcos|CA|3,095,313|
|St. Louis|MO-IL|2,812,896|
|Tampa-St. Petersburg-Clearwater|FL|2,783,243|
|Baltimore-Towson|MD|2,710,489|
|Denver-Aurora-Broomfield|CO|2,543,482|
|Pittsburgh|PA|2,356,285|
|Portland-Vancouver-Hillsboro|OR-WA|2,226,009|
|Sacramento- -Arden-Arcade- -Roseville|CA|2,149,127|
|San Antonio-New Braunfels|TX|2,142,508|
|Orlando-Kissimmee-Sanford|FL|2,134,411|
|Cincinnati-Middletown|OH-KY-IN|2,130,151|
|Cleveland-Elyria-Mentor|OH|2,077,240|


(continued)

20

Urban Studies

#### Appendix 1. Continued

|CBSA Name|States|2010 Population|
|---|---|---|
|Kansas City|MO-KS|2,035,334|
|Las Vegas-Paradise|NV|1,951,269|
|San Jose-Sunnyvale-Santa Clara|CA|1,836,911|
|Columbus|OH|1,836,536|
|Charlotte-Gastonia-Rock Hill|NC-SC|1,758,038|
|Indianapolis-Carmel|IN|1,756,241|
|Austin-Round Rock-San Marcos|TX|1,716,289|
|Virginia Beach-Norfolk-Newport News|VA-NC|1,671,683|
|Providence-New Bedford-Fall River|RI-MA|1,600,852|
|Nashville-Davidson- -Murfreesboro- -Franklin|TN|1,589,934|
|Milwaukee-Waukesha-West Allis|WI|1,555,908|
|Jacksonville|FL|1,345,596|
|Memphis|TN-MS-AR|1,316,100|
|Louisville/Jefferson County|KY-IN|1,283,566|
|Richmond|VA|1,258,251|
|Oklahoma City|OK|1,252,987|
|Hartford-West Hartford-East Hartford|CT|1,212,381|
|New Orleans-Metairie-Kenner|LA|1,167,764|
|Buffalo-Niagara Falls|NY|1,135,509|
|Raleigh-Cary|NC|1,130,490|
|Birmingham-Hoover|AL|1,128,047|
|Salt Lake City|UT|1,124,197|

---

[← Conclusion and discussion](16-conclusion-and-discussion.md) · [Up: contents](index.md)
