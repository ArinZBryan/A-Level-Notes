Radioactive decay is completely spontaneous and random. However, with larger nuclei, we can use statistics to find the expected number of nuclei that have decayed after a given time.

Assuming that the rate of disintegration of a given nuclide at any given time is proportional to the total number of ($N$) of nuclei present at that time.
$$A = -\frac{dN}{dt}\propto N \Rightarrow \frac{dN}{dt} = \lambda N$$
> $A$, Activity in Becquerels ($Bq$)
> $N$, Number of nuclei present
> $t$, Time in seconds ($s$)
> $\lambda$, Nuclear Decay Constant

##### An Example
Americum-241 is an artificially produced radioactive element that emits alpha particles. A sample of americum-241 of mass 5.1$\mu g$ is found to have an activity of $5.9\times 10^5\space\text{Bq}$.
Determine the number of nuclei in the sample of americum-241:
	$\text{Number of Nuclei} = \frac{\text{mass} \times N_A}{\text{molecular mass}}$ 
	$\text{Number of Nuclei} = \frac{(5.1\times 10^{-6})(6.02\times 10^{23})}{241} = 1.27\times 10^16$
Determine the decay constant of americum-241
	$\lambda = \frac AN = \frac{5.9\times 10^5}{1.27\times 10^{16}} = 4.65\times10^{-11}\space\text{s}^{-1}$
> Note that the unit for the decay constant is $\text{s}^{-1}$, which is the same as $\text{Hz}$

### Solving the differential equation
By solving the above differential equation, we can come to the following equation:
$$N = N_0e^{-\lambda t}$$
>$N$, Number of nuclei after time $t$
>$N_0$, Number of nuclei at time $t=0$
>$\lambda$, Nuclear decay constant ($\text{s}^{-1}$)
>$t$, Time spent decaying ($s$)

Thus, we get to a decay law: a radioactive substance decays exponentially  with time. It *does not* tell us *when* a particular nucleus will decay, but only that after a certain time a fraction will have decayed

### Half Life
The half life $T_{0.5}$ can be calculated by using the nuclear decay constant.
$$T_{0.5} = \frac{\ln 2}{\lambda}$$
