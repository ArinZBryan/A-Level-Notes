*Errors*, also called *Uncertainties* come in two flavours:
- Random
	- Run-to-run variance
- Systematic
	- A consistent mistake or error from the real value (eg. incorrectly zeroing a scale)
*Systematic errors* are errors that should be attempted to be mitigated in the experiment itself. This then should be noted when planning and carrying out experiments.
*Random errors* are errors that cannot be accounted for, and can be due to any number of factors, chief of which being insufficient measuring apparatus.
### Calculating uncertainties
To calculate uncertainties, attempt to try the following in order. If one is not possible, then attempt the next.
##### 1. Range Testing
$\pm$ Half the range (This only applies when multiple readings have been taken for the same expected value)
##### 2. Digital Equipment
$\pm$ The least significant figure on the readout
##### 3. Analogue Equipment
$\pm$ Half the most precise figure on the readout
### Absolute vs Relative
An absolute uncertainty is given as the value $\pm$ some value with a unit.
A relative uncertainty is given as the value $\pm$ a percentage of that value without a unit.
> Remember: Uncertainties should not be given to more than 2 significant figures. Most of the time one significant figure is best.

### Propagating Uncertainties
- When adding or subtracting values, add the *absolute* uncertainties
- When multiplying or dividing values, add the *relative* uncertainties
- When raising a value to a power, multiply the *relative* uncertainties by the power
Make sure when dealing with relative uncertainties, to use the *actual* value, rather than the percentage value. Only convert to a percentage right at the end.
### Accuracy vs Precision
One of the most common confusions is the difference between accuracy and precision. In common English, these are practically synonyms, however, in physics, they have a specific meaning.
**Accuracy** refers to the distance from the true value. Thus, a high accuracy reading is close to the correct value, and a low accuracy reading is not.
**Precision** refers to the spread of the data points. In statistics, this would be the [variance / standard deviation](./../../Maths/Statistics/Measures%20of%20Location%20And%20Spread/Variance%20and%20Standard%20Deviation.md) of the measurements.
Put in the terms of statistics, accuracy is a measure of location, and would be represented by $\overline{x}$, the mean, whereas precision is a measure of spread and would be represented by $\sigma$ or $\sigma^2$, i.e. the variance or standard deviation.
![](AccuracyVsPrecision.png)