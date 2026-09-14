---
title: Plot the function
source: https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb
source_file: sources/berkeley-stat153/spring-2025/CodeLectureTwentyFive153248Spring2025.ipynb
licence: CC BY 4.0
route: notebook
fidelity: lossless
converted: '2026-09-14'
---

# Plot the function

**Source:** [`CodeLectureTwentyFive153248Spring2025.ipynb`](https://github.com/berkeley-stat153/spring-2025/blob/60232ff1b10a6e871e4de968015b36891a606030/CodeLectureTwentyFive153248Spring2025.ipynb) · **Licence:** CC BY 4.0 · Converted 2026-09-14 from `.ipynb` (lossless)

plt.figure(figsize = (12, 6))
plt.plot(x_vals, y_vals, label = 'True function g')
plt.plot(x_vals, ghat_nar, color = 'red', label = 'Fitted function by the Nonlinear AR model')
plt.plot(x_vals, ar_vals, color = 'green', label = 'Fitted function by the AR(1) model')
plt.title(r'$g(x) = \frac{2x}{1 + 0.8x^2}$')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.grid(True)
plt.show()
```

```
[-0.03280141  0.81247368]
```

*(1 figure omitted — see the original notebook.)*

We plot these fitted functions on the data $(y_{t-1}, y_t)$.

```python
plt.figure(figsize = (12, 6))
plt.scatter(y_sim[:-1], y_sim[1:], s = 5)
plt.plot(x_vals, y_vals, label = 'True function g')
plt.plot(x_vals, ghat_nar, color = 'red', label = 'Fitted function by the Nonlinear AR model')
plt.plot(x_vals, ar_vals, color = 'green', label = 'Fitted function by the AR(1) model')
plt.xlabel('y[t-1]')
plt.ylabel('y[t]')
plt.show()
```

*(1 figure omitted — see the original notebook.)*

Now we obtain predictions for future observations. We obtain predictions with the fitted nonlinear AR(1) model as well as the model where we use the true $g$ function.

```python
#Predictions:
#with fitted model
last_val = torch.tensor([[y_sim[-1]]], dtype = torch.float32)
future_preds = []
k_future = 100
for _ in range(k_future):
    next_val = nar(last_val)
    future_preds.append(next_val.item())
    last_val = next_val.detach()
future_preds_array = np.array(future_preds)

#with actual g
actual_preds = []
for _ in range(k_future):
    next_val = ((2*last_val)/(1 + 0.8 * (last_val ** 2)))
    actual_preds.append(next_val.item())
    last_val = next_val.detach()
actual_preds_array = np.array(actual_preds)
```

```python
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
fcast = ar.get_prediction(start = n_y, end = n_y+k_future-1).predicted_mean
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(1))', color = 'green')
plt.plot(tme_future, future_preds_array, label = 'Forecast - NAR', color = 'red')
plt.plot(tme_future, actual_preds_array, label = 'Forecast - True NAR', color = 'black')
plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

It is clear that the predictions obtained by the NAR(1) model are very close to those obtained by using the true $g$ function. Also these predictions are quite different from the predictions of the linear AR(1) model.

## Example Two

Below we change the data generation model to:
\begin{equation*}
   y_t = \frac{2 y_{t-5}}{1 + 0.8 y_{t-5}^2} + \epsilon_t.
\end{equation*}
In other words, $y_{t-1}$ is replaced by $y_{t-5}$.

```python
n = 1450
rng = np.random.default_rng(seed = 40)
eps = rng.uniform(low = -1.0, high = 1.0, size = n)

truelag = 5
y_sim = np.full(n, 0, dtype = float)
y_sim[:(truelag - 1)] = rng.uniform(low = -1, high = 1, size = truelag - 1)
for i in range(truelag, n):
    y_sim[i] = ((2*y_sim[i-truelag])/(1 + 0.8 * (y_sim[i-truelag] ** 2))) + eps[i]

plt.figure(figsize = (12, 6))
plt.plot(y_sim)
plt.show()
```

*(1 figure omitted — see the original notebook.)*

We will use the single hidden layer neural network model with $p = 5$ for this data.

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

The model is fit in the following way.

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
Epoch 0, Loss:  0.957468
Epoch 200, Loss:  0.416492
Epoch 400, Loss:  0.389080
Epoch 600, Loss:  0.338375
Epoch 800, Loss:  0.337272
Epoch 1000, Loss:  0.336349
Epoch 1200, Loss:  0.335065
Epoch 1400, Loss:  0.334118
Epoch 1600, Loss:  0.332721
Epoch 1800, Loss:  0.332244
Epoch 2000, Loss:  0.331803
Epoch 2200, Loss:  0.331380
Epoch 2400, Loss:  0.331162
Epoch 2600, Loss:  0.331000
Epoch 2800, Loss:  0.330908
Epoch 3000, Loss:  0.330862
Epoch 3200, Loss:  0.330896
Epoch 3400, Loss:  0.330697
Epoch 3600, Loss:  0.330606
Epoch 3800, Loss:  0.330560
Epoch 4000, Loss:  0.330592
Epoch 4200, Loss:  0.330519
Epoch 4400, Loss:  0.330571
Epoch 4600, Loss:  0.330325
Epoch 4800, Loss:  0.330287
Epoch 5000, Loss:  0.330349
Epoch 5200, Loss:  0.330291
Epoch 5400, Loss:  0.330297
Epoch 5600, Loss:  0.330337
Epoch 5800, Loss:  0.330293
Epoch 6000, Loss:  0.330287
Epoch 6200, Loss:  0.330297
Epoch 6400, Loss:  0.330288
Epoch 6600, Loss:  0.330314
Epoch 6800, Loss:  0.330307
Epoch 7000, Loss:  0.330318
Epoch 7200, Loss:  0.330294
Epoch 7400, Loss:  0.330281
Epoch 7600, Loss:  0.330333
Epoch 7800, Loss:  0.330292
Epoch 8000, Loss:  0.330287
Epoch 8200, Loss:  0.330287
Epoch 8400, Loss:  0.330287
Epoch 8600, Loss:  0.330288
Epoch 8800, Loss:  0.330465
Epoch 9000, Loss:  0.330285
Epoch 9200, Loss:  0.330288
Epoch 9400, Loss:  0.330291
Epoch 9600, Loss:  0.330399
Epoch 9800, Loss:  0.330337
```

Next we obtain predictions.

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
tensor([-0.6649, -0.9638,  0.0533,  ..., -0.1717,  1.1205, -1.6019])
tensor([-1.6860, -0.2503, -0.1717,  1.1205, -1.6019])
tensor(-1.6860)
-1.6860132
```

For comparison, here are the predictions with the true $g$.

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

Again for comparison, here are the predictions by the linear AR($p$) model with $p = 5$.

```python
ar = AutoReg(y_sim, lags = p).fit()
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
fcast = ar.get_prediction(start = n_y, end = n_y+k_future-1).predicted_mean
```

Below are the predictions by the three models (along with the observed data).

```python
n_y = len(y_sim)
tme = range(1, n_y+1)
tme_future = range(n_y+1, n_y+k_future+1)
plt.figure(figsize = (12, 7))
plt.plot(tme, y_sim, label = 'Data')
plt.plot(tme_future, fcast, label = 'Forecast (AR(p))', color = 'green')
plt.plot(tme_future, predictions, label = 'Forecast - NAR', color = 'red')
plt.plot(tme_future, actual_predictions, label = 'Forecast - True NAR', color = 'black')
plt.axvline(x=n_y, color='gray', linestyle='--')
plt.legend()
plt.show()
```

*(1 figure omitted — see the original notebook.)*

For better visualization, let us only plot the predictions obtained by the three models.

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

The closeness of predictions by the NAR($p$) model and AR($p$) model compared with the predictions obtained from the true value of $g$ are computed by the MSEs below.

```python
mse_ar = np.mean( (actual_predictions - fcast) ** 2)
mse_NAR = np.mean( (actual_predictions - predictions) ** 2)
print(mse_ar, mse_NAR, mse_ar/mse_NAR)
```

```
0.49578311371259687 0.0027808830340550596 178.28262017538012
```

Below we plot the data $(y_{t-5}, y_t)$ along with the actual function $g$, and the fitted values by the NAR($p$) model.

```python
nar_fits = nar_model(x_data)

print(x_data[:,0].shape)
print(nar_fits.shape)

---

[← Plot the function](03-plot-the-function.md) · [Up: contents](index.md) · [Sort xdata[:,0] and corresponding narfits →](05-sort-xdata-0-and-corresponding-narfits.md)
