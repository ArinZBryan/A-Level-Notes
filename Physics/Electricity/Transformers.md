### Transformers
Transformers are a circuit element used to change the voltage of an AC power supply. A transformer is represented with the following symbol
![[IronCoreTransformer.png|200]]
A transformer is made of two coils of wire. Usually, these are wrapped around an iron core. The above symbol is more specifically the symbol for an iron-cored transformer. 

The number of windings in each coil determine the multiplicative factor on the voltage the transformer provides. More specifically the voltages on the primary and secondary coils and the windings on the coils is related as follows:
$$\frac{N_s}{N_p} = \frac{V_s}{V_p}$$
### How do transformers work?
When AC current is passed through the primary coil, this causes a changing magnetic field (by the motor effect), which passes through the iron core and interacts with the secondary coil [inducing](Induction) a voltage in the secondary coil.

### The Efficiency of a Transformer
The efficiency of a transformer can be measured in the same way as any other electrical device: useful power out against total power in. With transformers specifically, this can be reduced to the following equation:
$$E_{fficiency} = \frac{I_sV_s}{I_pV_p}$$
One of the main causes of efficiency loss in transformers is *eddy currents*. These are induced in the alternating magnetic field in the primary coil and form a loop. Due to [Lenz's law](Induction#Lenz's%20Law), this current will oppose the magnetic field that created it, thus reducing the field's overall flux density and generating heat. By using a *laminated iron core*, such eddy currents can be reduced.
Energy can also be lost to resistance in the coils, which is solved by using thicker, and less resisting conductors for the coils.
Finally, the core can reduce efficiency if it is not made of sufficiently easy to magnetise substance. Thus, magnetically soft iron is generally used.