---
title: Sort xdata[:,0] and corresponding narfits
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyFive153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Sort xdata[:,0] and corresponding narfits

**Source:** [`CodeLectureTwentyFive153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

sorted_indices = torch.argsort(x_data[:,0])
x_sorted = x_data[:,0][sorted_indices]
nar_fits_sorted = nar_fits[sorted_indices]


def g(x):
    return 2 * x / (1 + 0.8 * x**2)

true_g_vals = g(x_sorted.detach().numpy())

plt.figure(figsize=(12, 6))
plt.plot(x_sorted.detach().numpy(), nar_fits_sorted.detach().numpy(), label = 'Fitted values')
plt.plot(x_sorted.detach().numpy(), true_g_vals, color = 'red', label = 'Actual g values')
plt.title('Plotting fitted values against y_{t-5}')
plt.xlabel('y_{t-5}')
plt.ylabel('Fitted values')
plt.show()
```

```
torch.Size([1445])
torch.Size([1445])
```

*(1 figure omitted — see the original notebook.)*

## Example Three

Now we repeat the exercise but we now change $y_{t-5}$ to $y_{t-20}$. We also fit NAR($p$) and AR($p$) models with $p = 20$. Now NAR($p$) becomes a model with many parameters so there will be the issue of overfitting.

```python
n = 1450
rng = np.random.default_rng(seed = 40)
eps = rng.uniform(low = -1.0, high = 1.0, size = n)

truelag = 20
y_sim = np.full(n, 0, dtype = float)
y_sim[:(truelag - 1)] = rng.uniform(low = -1, high = 1, size = truelag - 1)
for i in range(truelag, n):
    y_sim[i] = ((2*y_sim[i-truelag])/(1 + 0.8 * (y_sim[i-truelag] ** 2))) + eps[i]

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
class SingleHiddenLayerNN(nn.Module):
    def __init__(self, input_dim, hidden_dim):
        super().__init__()
        self.W = nn.Linear(input_dim, hidden_dim)
        self.beta = nn.Linear(hidden_dim, 1)
    def forward(self, x):
        s = self.W(x)
        #r = torch.sigmoid(s)
        r = torch.relu(s)
        #r = torch.tanh(s)
        mu = self.beta(r)
        return mu.squeeze()
```

```python
torch.manual_seed(3)

#Create x's and y's from the data (x is simply the lagged values). Also conversion to tensors.
p = truelag
y = torch.tensor(y_sim, dtype = torch.float32)
n = len(y)
x_list = []
y_list = []
for t in range(p, n):
    x_list.append(y[t-p : t]) #(y_{t-1}, \dots, y_{t-p})
    y_list.append(y[t]) #y_t
x_data = torch.stack(x_list) #shape: (n-p, p)
y_data = torch.stack(y_list) #shape: (n-p,)
```

```python
k = 6
nar_model = SingleHiddenLayerNN(input_dim=p, hidden_dim=k)

loss_fn = nn.MSELoss()
optimizer = optim.Adam(nar_model.parameters(), lr = 0.01)

num_epochs = 10000
for epoch in range(num_epochs):
    optimizer.zero_grad()
    mu_pred = nar_model(x_data)
    loss = loss_fn(mu_pred, y_data)
    loss.backward()
    optimizer.step()
    if epoch % 200 == 0:
        print(f"Epoch {epoch}, Loss: {loss.item(): .6f}")
```

```
Epoch 0, Loss:  1.454649
Epoch 200, Loss:  0.379441
Epoch 400, Loss:  0.373239
Epoch 600, Loss:  0.368197
Epoch 800, Loss:  0.367407
Epoch 1000, Loss:  0.367285
Epoch 1200, Loss:  0.367280
Epoch 1400, Loss:  0.367292
Epoch 1600, Loss:  0.367298
Epoch 1800, Loss:  0.367281
Epoch 2000, Loss:  0.367306
Epoch 2200, Loss:  0.367287
Epoch 2400, Loss:  0.367290
Epoch 2600, Loss:  0.367310
Epoch 2800, Loss:  0.367283
Epoch 3000, Loss:  0.367293
Epoch 3200, Loss:  0.367269
Epoch 3400, Loss:  0.367162
Epoch 3600, Loss:  0.367093
Epoch 3800, Loss:  0.364829
Epoch 4000, Loss:  0.364723
Epoch 4200, Loss:  0.364730
Epoch 4400, Loss:  0.364724
Epoch 4600, Loss:  0.364736
Epoch 4800, Loss:  0.364697
Epoch 5000, Loss:  0.364703
Epoch 5200, Loss:  0.364687
Epoch 5400, Loss:  0.364697
Epoch 5600, Loss:  0.364705
Epoch 5800, Loss:  0.364676
Epoch 6000, Loss:  0.364709
Epoch 6200, Loss:  0.364662
Epoch 6400, Loss:  0.364705
Epoch 6600, Loss:  0.364678
Epoch 6800, Loss:  0.364711
Epoch 7000, Loss:  0.364670
Epoch 7200, Loss:  0.364697
Epoch 7400, Loss:  0.364688
Epoch 7600, Loss:  0.364677
Epoch 7800, Loss:  0.364706
Epoch 8000, Loss:  0.364733
Epoch 8200, Loss:  0.364688
Epoch 8400, Loss:  0.364683
Epoch 8600, Loss:  0.364677
Epoch 8800, Loss:  0.364666
Epoch 9000, Loss:  0.364684
Epoch 9200, Loss:  0.364684
Epoch 9400, Loss:  0.364706
Epoch 9600, Loss:  0.364668
Epoch 9800, Loss:  0.364667
```

```python
#Predictions
nar_model.eval()
predictions = []
k_future = 40
current_input = y[-p:]
for i in range(k_future):
    with torch.no_grad():
        mu = nar_model(current_input.unsqueeze(0))
    predictions.append(mu.item())
    current_input = torch.cat([current_input[1:], mu.unsqueeze(0)])
predictions = np.array(predictions)
```

```python
current_input = y[-p:]
print(y)
print(current_input)
print(current_input[0])
print(current_input[0].detach().numpy())
```

```
tensor([-0.6649, -0.9638,  0.0533,  ...,  0.4710,  1.3228,  0.5566])
tensor([-0.1745,  1.3297,  1.6169, -1.3475, -1.9818, -1.4642,  1.4335, -0.4679,
         0.3011, -0.9683, -1.9576, -0.2013, -1.3051,  1.8167, -0.1115,  0.2793,
        -1.2411,  0.4710,  1.3228,  0.5566])
tensor(-0.1745)
-0.17447984
```

```python
#Actual predictions using the true function:
actual_predictions = []
current_input = y[-p:]
for i in range(k_future):
    lastval = current_input[0]
    next_val = ((2*lastval)/(1 + 0.8 * (lastval ** 2)))
    actual_predictions.append(next_val)
    current_input = np.concatenate([current_input[1:], np.array([next_val])])
actual_predictions = np.array(actual_predictions)
```

```python
ar = AutoReg(y_sim, lags = p).fit()
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
fcast = ar.get_prediction(start = n_y, end = n_y+k_future-1).predicted_mean
```

```python
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(1))', color = 'green')
plt.plot(tme_future, predictions, label = 'Forecast - NAR', color = 'red')
plt.plot(tme_future, actual_predictions, label = 'Forecast - True NAR', color = 'black')
plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

```python
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
plt.figure(figsize = (12, 7))
plt.plot(tme_future, fcast, label = 'Forecast (AR(p))', color = 'green')
plt.plot(tme_future, predictions, label = 'Forecast - NAR', color = 'red')
plt.plot(tme_future, actual_predictions, label = 'Forecast - True NAR', color = 'black')
#plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

The predictions by NAR($p$) model are not as close to the true predictions (i.e., obtained using the true function $g$) as in the previous case when $p$ is small. In fact now, the predictions for the linear AR($p$) model seem closer to the true predictions. This is a result of overfitting.

```python
mse_ar = np.mean( (actual_predictions - fcast) ** 2)
mse_NAR = np.mean( (actual_predictions - predictions) ** 2)
print(mse_ar, mse_NAR, mse_ar/mse_NAR)
```

```
0.15533280348971384 0.1627774080292371 0.9542651241984017
```

```python
nar_fits = nar_model(x_data)

print(x_data[:,0].shape)
print(nar_fits.shape)

---

[← Plot the function](04-plot-the-function.md) · [Up: contents](index.md) · [Sort xdata[:,0] and corresponding narfits →](06-sort-xdata-0-and-corresponding-narfits.md)
