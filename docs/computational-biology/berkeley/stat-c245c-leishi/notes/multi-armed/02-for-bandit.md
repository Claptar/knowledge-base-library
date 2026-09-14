---
title: for bandit
source: https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd
source_file: sources/berkeley-stat-c245c-leishi/notes/multi-armed.Rmd
licence: unresolved
route: markdown
fidelity: lossless
converted: '2026-09-14'
---

# for bandit

**Source:** [`notes/multi-armed.Rmd`](https://leishi-rocks.github.io/courses/ph240c/notes/multi-armed.Rmd) · **Licence:** unresolved · Converted 2026-09-14 from `.Rmd` (lossless)

if(!require("devtools")){
  install.packages("devtools")
  library("devtools")
}

if(!require("contextual")){
  devtools::install_github('Nth-iteration-labs/contextual')
  library(contextual)
}

```

## Quick Review

### Reference used
1. The Multi-Armed Bandit Problem and Its Solutions: https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html#%CE%B5-greedy-algorithm

2. Multi-Armed Bandit with Thompson Sampling: https://www.r-bloggers.com/2020/09/multi-armed-bandit-with-thompson-sampling/

3. Multi-Armed Bandits as an A/B Testing Solution: https://www.r-bloggers.com/2019/09/multi-armed-bandits-as-an-a-b-testing-solution/

4. Reinforcement Learning: An Introduction: http://incompleteideas.net/book/the-book-2nd.html

5. Exploration vs Exploitation & the Multi Armed Bandit: https://rpubs.com/OttoP/478713

### Multi-armed bandit, Exploration & Exploitation

Imagine you are in a casino facing multiple slot machines and each is configured with an unknown probability of how likely you can get a reward at one play. The question is: What is the best strategy to achieve highest long-term rewards?

This is the motivating scenario, which can be generalized to a lot of other interesting real-life problems:

- Clinical trials: how to randomize patients to different treatment(say different drugs) options?
- Recommendation systems: what advertisement should a company serves among several possible options(traditionally termed as A/B test)? What videos (or types of videos) should youtube recommmend so that you can stay for five more minutes?

Some terminology:

- agent : the component that makes the decision of what action to take
- action(variant, policy) : the choice made, e.g. which offer to present from a number of alternatives (impression)
- reward : the result of doing a certain action, i.e. the “outcome” (e.g. a click)
- regret : the loss of not selecting the optimal action
- batch : in oline setting, the data comes in batches.


We focus on the bernoulli steup we used in the lectures: suppose there are $K$ actions, and when played, any action yields either a success or a failure. Action $k \in {1, \cdots, K}$ produces a success with probability $\theta_k \in [0, 1]$. The success probabilities $\theta_1, \cdots, \theta_K$ are unknown to the agent, but are fixed over time. Therefore, these probabilities can be learned by experimentation. The objective(reward), roughly speaking, is to maximize the cumulative number of successes over $T$ periods, where $T$ is relatively large compared to the number of arms $K$.

Now we are faced with the **exploration vs exploitation dilemma**. A nice restaurant I've tried vs a new restaurant I've never visited, which one should I go? We hope to make use of the resources that we have learned so far and maximize the greedy reward, while leave open the possibility of learning potentially more rewarding actions. In other word, exploitation serves for now, while exploration serves for future.

### Solutions for Multi-armed bandit

1. Epsilon-greedy

The $\epsilon$-greedy algorithm takes the best action most of the time, but does random exploration occasionally. According to the $\epsilon$-greedy algorithm, with a small probability $\epsilon$ we take a random action, but otherwise (which should be the most of the time, probability 1-$\epsilon$) we pick the best action that we have learnt so far.

2. UCB algorithm(not our focus, will do if we have time)

See https://lilianweng.github.io/lil-log/2018/01/23/the-multi-armed-bandit-problem-and-its-solutions.html#%CE%B5-greedy-algorithm.

3. Thompson sampling

- Bayesian statistics: prior & posterior distribution, conjugate distribution(https://en.wikipedia.org/wiki/Conjugate_prior?id="Table_of_conjugate_distributions"), inference(MAP, Bayesian confidence region)

- Beta distribution

Some basics about beta distribution $\text{Beta}(\alpha, \beta)$:


1. has a ugly pdf and a even worse cdf, though looks nice from plots:

```r
Beta_density <- data.frame(
  x = 0.01*(1:99),
  beta_density1 = dbeta(0.01*(1:99), 1, 1),
  beta_density2 = dbeta(0.01*(1:99), 0.5, 1.5),
  beta_density3 = dbeta(0.01*(1:99), 1.5, 0.5)
)

df <- gather(Beta_density, key = density, value = y,
c("beta_density1", "beta_density2", "beta_density3"))

beta_plot <- ggplot(df, aes(x=x, y = y, group = density, colour = density)) +
geom_line()

beta_plot


```

2. If $B\sim \text{Beta}(\alpha, \beta)$,
$$
\text{E}(B) = \frac{\alpha}{\alpha+\beta}, ~\text{Var}(B) = \frac{\alpha\beta}{(\alpha+\beta)^2(\alpha+\beta+1)}.
$$

Note although the mean is scale invariant, the variance is not. If we visualize the change of Beta distribution:
```r
x <- 0.01*1:99
alpha <- 0.2*1:20
beta <- 0.2*1:20

frame <- c()
x_val <- c()
beta_den <- c()
alpha_val <- c()
beta_val <- c()

for (i in 1:length(alpha)){
  frame <- c(frame, rep(i,length(x)))
  x_val <- c(x_val, x)
  alpha_val <- c(alpha_val, rep(alpha[i],length(x)))
  beta_val <- c(beta_val, rep(beta[i],length(x)))
  beta_den <- c(beta_den, dbeta(x, alpha[i], beta[i]))
}

Beta_den <- data.frame(
  frame = frame,
  x_val = x_val,
  alpha_val = alpha_val,
  beta_val = beta_val,
  beta_den = beta_den
)

Beta_den_plot <- ggplot(Beta_den, aes(x = x_val, y = beta_den)) +
  geom_line() +
  transition_time(frame) +
  ease_aes('linear')

Beta_den_plot
```


3. Uniform distribution is a special Beta distribution, with parameter $(1,1)$.

4. Beta distribution is the conjugate prior for the bernoulli distribution(more generally the binomial distribution family):

$$
\text{Beta}(\alpha,\beta) \to p \to \text{i.i.d Bernoulli(p) } X_i  \to \text{Beta}(\alpha+\sum X_i, ~\beta+n-\sum X_i) \to \cdots
$$


- For Thompson sampling it serves as a prior belief for the distribution of the reward. For simplicity suppose we only have one observation in each batch. The agent samples a $\hat{p}_k\sim \text{Beta}(\alpha_k, \beta_k)$ each time an individual arrives, and assigns her to the treatment corresponding to the highest $p_k$(say $k^\star$). Then we observe an outcome(success or failure) $Y$ and update the prior:
$$
\alpha_{k^\star} \leftarrow \alpha_{k^\star} + Y, ~\beta_{k^\star} \leftarrow \beta_{k^\star} + 1 - Y.
$$

## Programming perspective

### Resources

1. R package: contextual https://www.rdocumentation.org/packages/contextual/versions/0.9.8.4

- If you are using R3.0, then install.packages should work fine.
- If you are using R4.0, install it from github(see the first code chulk). Also need to update Rstudio to the newest version to make the parallel package compatible.
this package uses parallel computing.

2. some implementation: https://rpubs.com/OttoP/478713

### Implement Thompson sampling


Let’s assume that the ground truth success rates of the 4 treatments are:

Trt 1: 10%
Trt 2: 11%
Trt 3: 12%
Trt 4: 13%


```r
output <- {}
b_Probs <- c(0.10, 0.11, 0.12, 0.13)
b_Sent <- rep(0, length(b_Probs))
b_Reward <- rep(0, length(b_Probs))

batch_size<-1000
N<-10000
steps<-floor(N/batch_size)
msgs<-length(b_Probs)

for (i in 1:steps) {
  B<-matrix(rbeta(1000*msgs, b_Reward+1, (b_Sent-b_Reward)+1),1000, byrow = TRUE)
  P<-table(factor(max.col(B), levels=1:ncol(B)))/dim(B)[1]
  # tmp are the weights for each time step
  tmp<-round(P*batch_size,0)

  # Update the Rewards
  b_Reward<-b_Reward+rbinom(rep(1,msgs), size=tmp, prob = b_Probs)

  #Update the Sent
  b_Sent<-b_Sent+tmp

  #print(P)
  output<-rbind(output, t(matrix(P)))
}

---

[← for visualization](01-for-visualization.md) · [Up: contents](index.md) · [the weights of every step →](03-the-weights-of-every-step.md)
