## Standard Normal Distribution
The standard normal distribution is one where the mean is zero, and the standard deviation is 1. This can be represented in two ways:
$X\sim N(0,1^2)$ or $\phi(Z)$, where $Z = \frac{X -\mu}{\sigma}$

This coding, $Z = \frac{X -\mu}{\sigma}$ is required to transform any normal distribution into the standard normal distribution.

It is common to be given this normal distribution in a table on the formula sheet. The table supplied will be quite small though, as you are expected to do everything using the CG-50, eliminating the need to code for the standard normal distribution.

## Approximating a binomial distribution
To approximate a binomial distribution, $X \sim B(n,p)$, you can use a normal distribution modelled as $Y\sim N(np, np(1-p))$ . If $N$ is large, and $p \approx 0.5$ then this approximation is generally applicable.  There may also be questions given where despite one or both of these requirements not being met, you will be asked to use a 'suitable approximation'. This means use the normal distribution.
> Note that the variance and mean of a binomial distribution is given in the formula sheet. It is also important to remember that when inputting this into a calculator, that the *standard deviation* is required *rather than the deviance*.
### Correcting Bounds
When converting bounds from being used in the **discrete** binomial distribution to being used in the **continuous** normal distribution, the actual bounds must be adjusted due to the rounding present in the binomial distribution

$P(X < x) \rightarrow P(Y < x-0.5)$
$P(X > x)\rightarrow P(Y > x+0.5)$
$P(X \le x)\rightarrow P(Y \le x+0.5)$
$P(X \ge x)\rightarrow P(Y \ge x - 0.5)$ 

***Note that $x \in \mathbb{Z}$ , as it was from the binomial distribution