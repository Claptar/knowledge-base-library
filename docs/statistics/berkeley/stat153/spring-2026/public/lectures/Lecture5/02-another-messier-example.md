---
title: Another (messier) example
source: https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb
source_file: sources/berkeley-stat153/spring-2026/public/lectures/Lecture5.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`public/lectures/Lecture5.ipynb`](https://github.com/berkeley-stat153/spring-2026/blob/c08dd12c146698bb6ea1d0c6887d1898a8d98c6e/public/lectures/Lecture5.ipynb) — berkeley-stat153 · spring-2026, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Another (messier) example

Now let's load some data from `astsa`, for example, the price of chicken over time, from 2001 to 2016. As pointed out in your book, commodities (such as raw materials, basic resources, agricultural, or mining products) show specific fluctuations in their prices over time. For this example, we'll fit a regression model for chicken prices as our response $y$ and time as our predictor $x$.

```python
chicken_data = astsa.load_chicken()
print(chicken_data)
```

```
Time   Value
0    2001-08   65.58
1    2001-09   66.48
2    2001-10   65.70
3    2001-11   64.33
4    2001-12   63.23
..       ...     ...
175  2016-03  111.56
176  2016-04  111.55
177  2016-05  111.98
178  2016-06  111.84
179  2016-07  111.46

[180 rows x 2 columns]
```

```python
plt.plot(chicken_data['Time'], chicken_data['Value'])
```

```
[<matplotlib.lines.Line2D at 0x1690fc790>]
```

*(1 figure omitted — see the original notebook.)*

```python
chicken_data['Time'] = pd.to_datetime(chicken_data['Time'])
chicken_data.set_index('Time', inplace=True)
print(chicken_data)
```

```
Value
Time
2001-08-01   65.58
2001-09-01   66.48
2001-10-01   65.70
2001-11-01   64.33
2001-12-01   63.23
...            ...
2016-03-01  111.56
2016-04-01  111.55
2016-05-01  111.98
2016-06-01  111.84
2016-07-01  111.46

[180 rows x 1 columns]
```

```python
plt.figure(figsize=(8,6))
plt.plot(chicken_data.index, chicken_data['Value'], label='Value')
plt.xlabel('Year', fontsize=18)
plt.ylabel('Value', fontsize=18)
plt.title('Chicken prices (U.S. cents/pound)', fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16);
```

*(1 figure omitted — see the original notebook.)*

---

[← Introduction](01-introduction.md) · [Up: contents](index.md) · [Chicken price regression →](03-chicken-price-regression.md)
