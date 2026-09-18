---
title: 'Application Two: Southern Oscillation Index Dataset'
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLectureFifteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-18'
---

> **Converted source.** [`CodeLectureFifteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLectureFifteen153248Fall2025.ipynb) — berkeley-stat153 · fall-2025, licensed CC BY 4.0. Converted 2026-09-18 from `.ipynb`. The same text in markdown, split so that every part has a URL; nothing here is rewritten.

# Application Two: Southern Oscillation Index Dataset

This dataset can be downloaded from http://www.bom.gov.au/climate/enso/soi/. El Niño (see wiki entry) is a climate pattern that describes the unusual warming of surface waters in the eastern tropical Pacific Ocean. It is believed to occur irregularly at two to seven year intervals. Closely related to the fluctuations in oceanic temperatures are large-scale changes in atmospheric pressure. El Nino events are associated with sustained negative Southern Oscillation Index (SOI) values. The SOI is computed from fluctuations in the surface air pressure difference between Tahiti and Darwin. See the paper "The definition of El Nino" by Trenberth 1997 for more details.

Wikipedia article for El Niño Southern Oscillation has this sentence: "El Niño and Li Niña last a year or so and typically occur every two to seven years with varying intensity, with neutral periods of lower intensity interspersed."

```python
def load_soi_data(filepath):
    data = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue  # skip blank lines if any

            date_str, soi_str = line.split(',')
            date_code = int(date_str)   # e.g. 187601
            year = date_code // 100     # e.g. 1876
            month = date_code % 100     # e.g. 1
            soi_val = float(soi_str)

            data.append([year, month, soi_val])

    # Create a DataFrame from parsed rows
    df = pd.DataFrame(data, columns=['Year', 'Month', 'SOI'])

    # Convert Year, Month to a datetime; assume day=1 for each month
    df['Date'] = pd.to_datetime(df[['Year', 'Month']].assign(DAY=1))

    # Make Date the index
    df.set_index('Date', inplace=True)

    # Sort by date just in case (and drop the now-redundant Year/Month columns)
    df.sort_index(inplace=True)

    return df[['SOI']]

# Usage
df_soi = load_soi_data("soi_monthly.txt")
print(df_soi)
```

```
SOI
Date
1876-01-01  11.3
1876-02-01  11.0
1876-03-01   0.2
1876-04-01   9.4
1876-05-01   6.8
...          ...
2024-10-01   4.2
2024-11-01   6.5
2024-12-01  10.8
2025-01-01   3.7
2025-02-01   3.0

[1790 rows x 1 columns]
```

```python
y = df_soi['SOI']
n = len(y)
plt.figure(figsize = (12, 6))
plt.plot(y)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, pgram = periodogram(y)
plt.figure(figsize = (12, 6))
plt.plot(freqs, pgram)
plt.title('Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
freqs, pgram = periodogram(y)
plt.figure(figsize = (12, 6))
plt.plot(freqs, np.log(pgram))
plt.title('Log Periodogram')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
alpha_opt_ridge, freq = spectrum_estimator_ridge(y, 50000)
power_ridge = (2/n)*(np.exp(2*alpha_opt_ridge))
alpha_opt_lasso, freq = spectrum_estimator_lasso(y, 100)
power_lasso = (2/n)*(np.exp(2*alpha_opt_lasso))

plt.figure(figsize = (12, 6))
markerline, stemline, baseline = plt.stem(freq, pgram, linefmt = 'lightblue', basefmt = '')
markerline.set_marker("None")
plt.title('Periodogram and the Power Spectrum')
plt.plot(freq, power_ridge, color = 'red', label = 'Ridge')
plt.plot(freq, power_lasso, color = 'black', label = "LASSO")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
plt.figure(figsize = (12, 6))
#markerline, stemline, baseline = plt.stem(freq, np.log(pgram), linefmt = 'lightblue', basefmt = '')
#markerline.set_marker("None")
plt.plot(freq, np.log(pgram), color = 'lightblue')
plt.title('Log Periodogram and Log Power Spectrum')
plt.plot(freq, np.log(power_ridge), color = 'red', label = 'Ridge')
plt.plot(freq, np.log(power_lasso), color = 'black', label = "LASSO")
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
from scipy.signal import find_peaks
# Find peaks
peaks, _ = find_peaks(np.log(power_ridge))
print("Peaks:", peaks)
print(1/freq[peaks])
```

```
Peaks: [ 33 186 257 318 423 560 631 710 782 857]
[52.64705882  9.57219251  6.9379845   5.61128527  4.22169811  3.19073084
  2.83227848  2.51758087  2.28607918  2.08624709]
```

The peak therefore corresponds to the period of about 52.64 months, which is about 4.5 years.

---

[← Application One: Sunspots Dataset](01-application-one-sunspots-dataset.md) · [Up: contents](index.md) · [Application Three: Quake Vibration Dataset →](03-application-three-quake-vibration-dataset.md)
