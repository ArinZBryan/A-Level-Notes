The t-formulae are a set of equivalences that let us express $\sin\theta$, $\cos\theta$ and $\tan\theta$ in terms of $\tan\frac\theta 2$. Why would we want to do that though?
- Proving trig identities
- Solving equations involving multiple different trig functions
- Simplifying modelling problems
- As a substitution when integrating (the Weierstrauss substitution)

Let $t = \tan\frac\theta 2$, then after some rearrangement
$$\sin\theta = \frac{2t}{1+t^2}$$
$$\cos\theta = \frac{1-t^2}{1+t^2}$$
$$\tan\theta = \frac{2t}{1-t^2}$$
### The Weierstrauss Substitution
Quite simply, this is just doing integration by substitution, except the substitution made is $t = \tan\frac x2$. This results in the following:
$$\int 1dx = \int1\cdot\frac{2}{1+t^2}dt$$ Generally, this substitution is used when the top of a fraction can be reduced to some multiple of $(1 + t^2)$ which can then be cancelled.