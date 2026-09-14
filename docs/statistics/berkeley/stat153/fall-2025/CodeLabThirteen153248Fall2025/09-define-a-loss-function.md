---
title: Define a loss function
source: https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb
source_file: sources/berkeley-stat153/fall-2025/CodeLabThirteen153248Fall2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Define a loss function

**Source:** [`CodeLabThirteen153248Fall2025.ipynb`](https://github.com/berkeley-stat153/fall-2025/blob/df8e8e972b95eb1235ce8a17f88722e852802200/CodeLabThirteen153248Fall2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

loss_fn = nn.MSELoss()
loss_values = []

for epoch in range(300000):
    # Zero out gradients
    optimizer.zero_grad()
    # Without zeroing the gradients before each iteration,
    # gradients from previous iterations would accumulate,
    # leading to incorrect updates of the model's parameters.

    # Compute loss
    y_pred = md_nn(x_raw_torch)
    loss = loss_fn(y_pred, y_raw_torch)

    # Compute gradients
    loss.backward()
    # The .backward() method calculates the gradients of that tensor
    # with respect to all the parameters in the network that contributed to its computation.

    # Update parameters
    optimizer.step()
    # The .step() method performs a single optimization step,
    # updating the model's parameters based on the gradients computed during the backward pass.

    loss_values.append(loss.item())
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item():.4f}")

print(f"Epoch {epoch}, Loss: {loss.item():.4f}")
```

```
Epoch 0, Loss: 80948888.0000
Epoch 1000, Loss: 52399508.0000
Epoch 2000, Loss: 49242824.0000
Epoch 3000, Loss: 47964040.0000
Epoch 4000, Loss: 47336768.0000
Epoch 5000, Loss: 46942112.0000
Epoch 6000, Loss: 46699364.0000
Epoch 7000, Loss: 46517784.0000
Epoch 8000, Loss: 46565056.0000
Epoch 9000, Loss: 46373556.0000
Epoch 10000, Loss: 46316752.0000
Epoch 11000, Loss: 46285712.0000
Epoch 12000, Loss: 46241228.0000
Epoch 13000, Loss: 46203376.0000
Epoch 14000, Loss: 46175032.0000
Epoch 15000, Loss: 46153744.0000
Epoch 16000, Loss: 46137504.0000
Epoch 17000, Loss: 46124436.0000
Epoch 18000, Loss: 46136976.0000
Epoch 19000, Loss: 46105196.0000
Epoch 20000, Loss: 46374868.0000
Epoch 21000, Loss: 46591068.0000
Epoch 22000, Loss: 46439060.0000
Epoch 23000, Loss: 46085180.0000
Epoch 24000, Loss: 46090524.0000
Epoch 25000, Loss: 46396488.0000
Epoch 26000, Loss: 46078640.0000
Epoch 27000, Loss: 46105336.0000
Epoch 28000, Loss: 46142696.0000
Epoch 29000, Loss: 46072500.0000
Epoch 30000, Loss: 46098604.0000
Epoch 31000, Loss: 46076788.0000
Epoch 32000, Loss: 46080060.0000
Epoch 33000, Loss: 46071212.0000
Epoch 34000, Loss: 46128784.0000
Epoch 35000, Loss: 46166504.0000
Epoch 36000, Loss: 46104376.0000
Epoch 37000, Loss: 46125652.0000
Epoch 38000, Loss: 46082916.0000
Epoch 39000, Loss: 46079800.0000
Epoch 40000, Loss: 46089576.0000
Epoch 41000, Loss: 46073724.0000
Epoch 42000, Loss: 46086328.0000
Epoch 43000, Loss: 46133528.0000
Epoch 44000, Loss: 46057368.0000
Epoch 45000, Loss: 46136624.0000
Epoch 46000, Loss: 46070180.0000
Epoch 47000, Loss: 46080124.0000
Epoch 48000, Loss: 46078072.0000
Epoch 49000, Loss: 46063876.0000
Epoch 50000, Loss: 46091832.0000
Epoch 51000, Loss: 46073312.0000
Epoch 52000, Loss: 46071148.0000
Epoch 53000, Loss: 46065696.0000
Epoch 54000, Loss: 46072072.0000
Epoch 55000, Loss: 46075824.0000
Epoch 56000, Loss: 46060588.0000
Epoch 57000, Loss: 46137204.0000
Epoch 58000, Loss: 46074800.0000
Epoch 59000, Loss: 46058916.0000
Epoch 60000, Loss: 46091884.0000
Epoch 61000, Loss: 46085712.0000
Epoch 62000, Loss: 46180844.0000
Epoch 63000, Loss: 46055736.0000
Epoch 64000, Loss: 46069636.0000
Epoch 65000, Loss: 46076828.0000
Epoch 66000, Loss: 46054856.0000
Epoch 67000, Loss: 46089436.0000
Epoch 68000, Loss: 46229328.0000
Epoch 69000, Loss: 46081344.0000
Epoch 70000, Loss: 46144500.0000
Epoch 71000, Loss: 46156544.0000
Epoch 72000, Loss: 46079372.0000
Epoch 73000, Loss: 46123884.0000
Epoch 74000, Loss: 46077264.0000
Epoch 75000, Loss: 46116756.0000
Epoch 76000, Loss: 46114352.0000
Epoch 77000, Loss: 46087656.0000
Epoch 78000, Loss: 46054424.0000
Epoch 79000, Loss: 46049944.0000
Epoch 80000, Loss: 46080056.0000
Epoch 81000, Loss: 46062508.0000
Epoch 82000, Loss: 46064524.0000
Epoch 83000, Loss: 46054372.0000
Epoch 84000, Loss: 46064180.0000
Epoch 85000, Loss: 46052868.0000
Epoch 86000, Loss: 46057264.0000
Epoch 87000, Loss: 46057528.0000
Epoch 88000, Loss: 46086404.0000
Epoch 89000, Loss: 46065236.0000
Epoch 90000, Loss: 46050436.0000
Epoch 91000, Loss: 46062012.0000
Epoch 92000, Loss: 46063844.0000
Epoch 93000, Loss: 46080404.0000
Epoch 94000, Loss: 46056244.0000
Epoch 95000, Loss: 46065652.0000
Epoch 96000, Loss: 46086876.0000
Epoch 97000, Loss: 46062744.0000
Epoch 98000, Loss: 46112908.0000
Epoch 99000, Loss: 46074880.0000
Epoch 100000, Loss: 46055572.0000
Epoch 101000, Loss: 46056660.0000
Epoch 102000, Loss: 46120100.0000
Epoch 103000, Loss: 46072552.0000
Epoch 104000, Loss: 46056792.0000
Epoch 105000, Loss: 46073420.0000
Epoch 106000, Loss: 46050048.0000
Epoch 107000, Loss: 46080992.0000
Epoch 108000, Loss: 46048212.0000
Epoch 109000, Loss: 46211516.0000
Epoch 110000, Loss: 46048232.0000
Epoch 111000, Loss: 46098984.0000
Epoch 112000, Loss: 46065184.0000
Epoch 113000, Loss: 46091668.0000
Epoch 114000, Loss: 46058780.0000
Epoch 115000, Loss: 46134192.0000
Epoch 116000, Loss: 46097664.0000
Epoch 117000, Loss: 46082064.0000
Epoch 118000, Loss: 46062312.0000
Epoch 119000, Loss: 46084900.0000
Epoch 120000, Loss: 46102404.0000
Epoch 121000, Loss: 46461948.0000
Epoch 122000, Loss: 46080256.0000
Epoch 123000, Loss: 46061572.0000
Epoch 124000, Loss: 46079852.0000
Epoch 125000, Loss: 46057572.0000
Epoch 126000, Loss: 46125564.0000
Epoch 127000, Loss: 46049396.0000
Epoch 128000, Loss: 46062056.0000
Epoch 129000, Loss: 46140936.0000
Epoch 130000, Loss: 46054920.0000
Epoch 131000, Loss: 46104600.0000
Epoch 132000, Loss: 46052604.0000
Epoch 133000, Loss: 46081172.0000
Epoch 134000, Loss: 46147304.0000
Epoch 135000, Loss: 46070420.0000
Epoch 136000, Loss: 46050096.0000
Epoch 137000, Loss: 46098920.0000
Epoch 138000, Loss: 46053808.0000
Epoch 139000, Loss: 46079496.0000
Epoch 140000, Loss: 46194976.0000
Epoch 141000, Loss: 46123880.0000
Epoch 142000, Loss: 46080052.0000
Epoch 143000, Loss: 46090356.0000
Epoch 144000, Loss: 46108216.0000
Epoch 145000, Loss: 46077244.0000
Epoch 146000, Loss: 46099332.0000
Epoch 147000, Loss: 46091968.0000
Epoch 148000, Loss: 46059280.0000
Epoch 149000, Loss: 46110476.0000
Epoch 150000, Loss: 46111860.0000
Epoch 151000, Loss: 46077532.0000
Epoch 152000, Loss: 46049788.0000
Epoch 153000, Loss: 46068524.0000
Epoch 154000, Loss: 46094116.0000
Epoch 155000, Loss: 46054136.0000
Epoch 156000, Loss: 46088876.0000
Epoch 157000, Loss: 46093544.0000
Epoch 158000, Loss: 46049340.0000
Epoch 159000, Loss: 46104280.0000
Epoch 160000, Loss: 46121344.0000
Epoch 161000, Loss: 46107692.0000
Epoch 162000, Loss: 46060064.0000
Epoch 163000, Loss: 46109240.0000
Epoch 164000, Loss: 46048852.0000
Epoch 165000, Loss: 46124320.0000
Epoch 166000, Loss: 46080088.0000
Epoch 167000, Loss: 46052236.0000
Epoch 168000, Loss: 46049780.0000
Epoch 169000, Loss: 46068672.0000
Epoch 170000, Loss: 46081944.0000
Epoch 171000, Loss: 46081320.0000
Epoch 172000, Loss: 46057656.0000
Epoch 173000, Loss: 46048372.0000
Epoch 174000, Loss: 46058704.0000
Epoch 175000, Loss: 46049880.0000
Epoch 176000, Loss: 46054696.0000
Epoch 177000, Loss: 46048308.0000
Epoch 178000, Loss: 46130700.0000
Epoch 179000, Loss: 46053228.0000
Epoch 180000, Loss: 46067968.0000
Epoch 181000, Loss: 46075528.0000
Epoch 182000, Loss: 46048004.0000
Epoch 183000, Loss: 46054204.0000
Epoch 184000, Loss: 46075184.0000
Epoch 185000, Loss: 46047648.0000
Epoch 186000, Loss: 46117412.0000
Epoch 187000, Loss: 46071436.0000
Epoch 188000, Loss: 46063992.0000
Epoch 189000, Loss: 46054196.0000
Epoch 190000, Loss: 46047668.0000
Epoch 191000, Loss: 46088848.0000
Epoch 192000, Loss: 46158872.0000
Epoch 193000, Loss: 46048068.0000
Epoch 194000, Loss: 46087296.0000
Epoch 195000, Loss: 46068000.0000
Epoch 196000, Loss: 46085068.0000
Epoch 197000, Loss: 46064384.0000
Epoch 198000, Loss: 46049676.0000
Epoch 199000, Loss: 46062380.0000
Epoch 200000, Loss: 46067064.0000
Epoch 201000, Loss: 46094964.0000
Epoch 202000, Loss: 46132872.0000
Epoch 203000, Loss: 46141816.0000
Epoch 204000, Loss: 46053748.0000
Epoch 205000, Loss: 46066980.0000
Epoch 206000, Loss: 46289568.0000
Epoch 207000, Loss: 46050232.0000
Epoch 208000, Loss: 46098572.0000
Epoch 209000, Loss: 46058704.0000
Epoch 210000, Loss: 46094828.0000
Epoch 211000, Loss: 46314708.0000
Epoch 212000, Loss: 46176876.0000
Epoch 213000, Loss: 46105768.0000
Epoch 214000, Loss: 46051152.0000
Epoch 215000, Loss: 46054176.0000
Epoch 216000, Loss: 46055964.0000
Epoch 217000, Loss: 46071184.0000
Epoch 218000, Loss: 46051816.0000
Epoch 219000, Loss: 46056832.0000
Epoch 220000, Loss: 46048024.0000
Epoch 221000, Loss: 46073900.0000
Epoch 222000, Loss: 46049920.0000
Epoch 223000, Loss: 46115572.0000
Epoch 224000, Loss: 46146456.0000
Epoch 225000, Loss: 46057396.0000
Epoch 226000, Loss: 46087556.0000
Epoch 227000, Loss: 46050060.0000
Epoch 228000, Loss: 46066040.0000
Epoch 229000, Loss: 46083716.0000
Epoch 230000, Loss: 46068748.0000
Epoch 231000, Loss: 46052284.0000
Epoch 232000, Loss: 46094988.0000
Epoch 233000, Loss: 46084768.0000
Epoch 234000, Loss: 46061404.0000
Epoch 235000, Loss: 46051988.0000
Epoch 236000, Loss: 46050884.0000
Epoch 237000, Loss: 46067336.0000
Epoch 238000, Loss: 46051784.0000
Epoch 239000, Loss: 46100116.0000
Epoch 240000, Loss: 46064720.0000
Epoch 241000, Loss: 46057624.0000
Epoch 242000, Loss: 46063268.0000
Epoch 243000, Loss: 46074488.0000
Epoch 244000, Loss: 46047724.0000
Epoch 245000, Loss: 46087656.0000
Epoch 246000, Loss: 46048340.0000
Epoch 247000, Loss: 46100260.0000
Epoch 248000, Loss: 46057444.0000
Epoch 249000, Loss: 46056360.0000
Epoch 250000, Loss: 46050120.0000
Epoch 251000, Loss: 46466956.0000
Epoch 252000, Loss: 46060392.0000
Epoch 253000, Loss: 46053168.0000
Epoch 254000, Loss: 46054776.0000
Epoch 255000, Loss: 46049840.0000
Epoch 256000, Loss: 46092584.0000
Epoch 257000, Loss: 46096380.0000
Epoch 258000, Loss: 46047596.0000
Epoch 259000, Loss: 46105184.0000
Epoch 260000, Loss: 46104044.0000
Epoch 261000, Loss: 46072672.0000
Epoch 262000, Loss: 46061080.0000
Epoch 263000, Loss: 46061744.0000
Epoch 264000, Loss: 46127080.0000
Epoch 265000, Loss: 46049492.0000
Epoch 266000, Loss: 46049952.0000
Epoch 267000, Loss: 46063940.0000
Epoch 268000, Loss: 46064084.0000
Epoch 269000, Loss: 46213724.0000
Epoch 270000, Loss: 46056544.0000
Epoch 271000, Loss: 46050808.0000
Epoch 272000, Loss: 46063152.0000
Epoch 273000, Loss: 46078784.0000
Epoch 274000, Loss: 46053304.0000
Epoch 275000, Loss: 46350624.0000
Epoch 276000, Loss: 46049344.0000
Epoch 277000, Loss: 46114852.0000
Epoch 278000, Loss: 46080776.0000
Epoch 279000, Loss: 46062100.0000
Epoch 280000, Loss: 46063712.0000
Epoch 281000, Loss: 46062696.0000
Epoch 282000, Loss: 46047636.0000
Epoch 283000, Loss: 46059808.0000
Epoch 284000, Loss: 46065436.0000
Epoch 285000, Loss: 46295268.0000
Epoch 286000, Loss: 46086632.0000
Epoch 287000, Loss: 46110964.0000
Epoch 288000, Loss: 46094972.0000
Epoch 289000, Loss: 46068852.0000
Epoch 290000, Loss: 46047676.0000
Epoch 291000, Loss: 46053624.0000
Epoch 292000, Loss: 46050820.0000
Epoch 293000, Loss: 46064620.0000
Epoch 294000, Loss: 46074732.0000
Epoch 295000, Loss: 46072768.0000
Epoch 296000, Loss: 46096908.0000
Epoch 297000, Loss: 46050176.0000
Epoch 298000, Loss: 46063684.0000
Epoch 299000, Loss: 46049728.0000
Epoch 299999, Loss: 46055416.0000
```

Here are some points that can be verified:
1. When the learning rate is 0.01, the algorithm is moving too slowly and we get convergence after about 300000 epochs (the smallest loss is around 46047484).
2. When the learning rate is 0.1, the algorithm is still slow and convergence seems to be achieved at around 150000 epochs.
3. When the learning rate is 1, the algorithm does not seem to settle down, and is oscillating quite a bit even after reaching around the smallest loss.

```python
nn_fits_1 = md_nn(x_raw_torch).detach().numpy()

---

[← try lr = 0.01, 0.1 and 1](08-try-lr-0-01-0-1-and-1.md) · [Up: contents](index.md) · [CodeLabThirteen153248Fall2025 Part 10 — →](10-codelabthirteen153248fall2025-part-10.md)
