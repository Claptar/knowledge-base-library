---
title: Fit the model
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb
source_file: sources/berkeley-stat153/spring-2025/Lab13.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Fit the model

**Source:** [`Lab13.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/Lab13.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

armod = AR1Model()
optimizer = optim.Adam(armod.parameters(), lr=0.001)

for epoch in range(3000):
    # Zero gradient
    optimizer.zero_grad()

    # Compute loss
    loss = armod(ylogdiff_tensor)

    # Compute gradient
    loss.backward()

    # Update parameters
    optimizer.step()

    if epoch % 100 == 0:
        print(f"Epoch {epoch}: phi0={armod.phi0.item():.4f}, phi1={armod.phi1.item():.4f}, sigma={torch.exp(armod.log_sigma).item():.4f}, loss={loss.item():.4f}")
```

```
Epoch 0: phi0=-0.0010, phi1=0.4990, sigma=0.9990, loss=754.7678
Epoch 100: phi0=-0.0008, phi1=0.3977, sigma=0.9057, loss=708.1990
Epoch 200: phi0=-0.0009, phi1=0.2938, sigma=0.8257, loss=664.1494
Epoch 300: phi0=-0.0010, phi1=0.1895, sigma=0.7572, loss=623.2971
Epoch 400: phi0=-0.0011, phi1=0.0874, sigma=0.6989, loss=586.7548
Epoch 500: phi0=-0.0011, phi1=-0.0099, sigma=0.6502, loss=555.8716
Epoch 600: phi0=-0.0012, phi1=-0.0992, sigma=0.6108, loss=531.7949
Epoch 700: phi0=-0.0011, phi1=-0.1778, sigma=0.5804, loss=514.9111
Epoch 800: phi0=-0.0013, phi1=-0.2431, sigma=0.5587, loss=504.4892
Epoch 900: phi0=-0.0014, phi1=-0.2943, sigma=0.5445, loss=498.8905
Epoch 1000: phi0=-0.0014, phi1=-0.3318, sigma=0.5362, loss=496.2641
Epoch 1100: phi0=-0.0014, phi1=-0.3575, sigma=0.5318, loss=495.1721
Epoch 1200: phi0=-0.0014, phi1=-0.3742, sigma=0.5298, loss=494.7625
Epoch 1300: phi0=-0.0015, phi1=-0.3844, sigma=0.5289, loss=494.6224
Epoch 1400: phi0=-0.0014, phi1=-0.3904, sigma=0.5286, loss=494.5786
Epoch 1500: phi0=-0.0014, phi1=-0.3936, sigma=0.5285, loss=494.5660
Epoch 1600: phi0=-0.0014, phi1=-0.3954, sigma=0.5285, loss=494.5628
Epoch 1700: phi0=-0.0014, phi1=-0.3962, sigma=0.5285, loss=494.5621
Epoch 1800: phi0=-0.0015, phi1=-0.3967, sigma=0.5285, loss=494.5620
Epoch 1900: phi0=-0.0014, phi1=-0.3968, sigma=0.5285, loss=494.5618
Epoch 2000: phi0=-0.0014, phi1=-0.3969, sigma=0.5285, loss=494.5619
Epoch 2100: phi0=-0.0014, phi1=-0.3969, sigma=0.5285, loss=494.5619
Epoch 2200: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2300: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2400: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2500: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2600: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2700: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5618
Epoch 2800: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
Epoch 2900: phi0=-0.0014, phi1=-0.3970, sigma=0.5285, loss=494.5619
```

```python
ar1_pars = np.array([armod.phi0.detach().numpy(),
                     armod.phi1.detach().numpy(),
                     np.exp(2 * armod.log_sigma.detach().numpy())])

---

[← the parameter estimates are quite close to each other](12-the-parameter-estimates-are-quite-close-to-each-other.md) · [Up: contents](index.md) · [mu, theta and sigma^2 →](14-mu-theta-and-sigma-2.md)
