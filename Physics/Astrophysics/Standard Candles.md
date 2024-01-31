When calculating the distance a star is from Earth, it is possible to use [stellar parallax](./Stellar%20Parallax.md) to find the distance by using simple trigonometry. However, when stars are further away than ~250 parsecs / ~820 light years, the angles become too small to measure accurately. There is however, a better way to measure long distances. This is through the use of 'standard candles'.
> A *standard candle* is a term referring to an object of known luminosity

### Measuring using standard candles
If we can know *exactly* how bright an object is we can do some neat equations. By measuring the intensity of the radiation from it that reaches Earth, we can use the inverse-square law to determine its distance. This is because the electromagnetic radiation (light) that is put off by such an object always follows the inverse-square law.

### Luminosity & Intensity
Luminosity ($L$) is defined as the total electromagnetic power output of an object across all frequencies. It is measured in Watts. It is important to take note of the fact that this includes all parts of the EM spectrum, so that must be taken into account.
Intensity ($I$) is defined as the total electromagnetic power received across all frequency of the EM spectrum per unit area. It is measured in $Wm^{-2}$. 

Deriving the exact relationship between luminosity and intensity should be largely straight forward. Assuming a star is a point source (for all intents and purposes it is at this kind of distance), the luminosity $L$ is radiated *uniformly in all directions*. Thus, we can say that the radiation spreads evenly across the surface area of a sphere. 
- If the observer is at a distance $d$, then the surface are of that sphere will be $A = 4\pi d^2$.
- The intensity on that sphere will simply be the area times luminosity.
$$I = \frac{L}{4\pi d^2}$$
### Standard Candles
The above is all well and good, but it relies on actually knowing the luminosity of the object precisely. How can we do that?
As it turns out there are are many types of standard candles used in astronomy, but the two seen at A-level are:
- Type 1A supernovae
- Cepheid variable stars
##### Type 1A supernovae
Many stars exist in a binary system, where two stars orbit each other, leading to chaotic planetary orbits. These such systems are very common, with an estimated third of all stars in the milky way being part of such a system.
Sometimes, these stars are white dwarf stars. Note that white dwarves are the final form of stars that weren't large enough to go supernova. Since such stars are generally much denser than the average star, the companion star in the binary system often has its mass 'sucked' into the white dwarf.
When this happens, the white dwarf slowly accumulates mass, until it reaches approximately 1.44 times the mass of the sun. This is known as the Chandrasekhar limit. This is the maximum mass a white dwarf can be before it will undergo a supernova. As we can know *precisely* what the mass will be when it goes supernova, we can predict exactly how luminous the supernova will be, every time.
##### Cepheid Variable Stars
Most main-sequence stars are not actually a constant brightness. Instead, luminosity pulses over time. Thus, these stars are called 'variable stars'.
A Cepheid variable star has much larger variations (the sun is not a Cepheid variable star, it varies by about 0.1% over an 11-year cycle). This is due to a changing diameter of the star (as much as up to 10% - 20%). This change in size causes a similar change in brightness.
In 1912, it was discovered that a Cepheid variable star's period of pulsation was directly linked to its maximum luminosity, and thus, a simple *logarithmic* pattern has been noticed. Thus, by measuring the time it takes for such a star to pulse, we can know with great certainty what its maximum luminosity is.