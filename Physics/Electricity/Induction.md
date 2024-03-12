6### Fleming's Right Hand Rule
When a conductive wire is moved through a magnetic field, a current is induced in the wire. The direction of the current is given by Fleming’s right-hand rule for generators. As with Fleming’s left-hand rule, the thumb is the direction of the motion of the wire, or equivalently, the force exerted on the wire, F, the first finger is the direction of the magnetic field, B, and the second finger is the direction of the induced conventional current, I.
![[FlemingsRightHandRule.png]]
## Lenz's Law
Consider the following scenario:
![[Lenzs_Law_1.svg]]
This scenario will induce a force in the opposite direction via the motor effect ([Fleming's Left Hand Rule](Physics/Fields/Magnetic%20Fields)).
![[Lenzs_Law_2.svg]]
As it happens, the effect will be the same if we start with Fleming's Left Hand Rule, and find Fleming's Right Hand Rule creating the same scenario.

This leads to Lenz's Law:
	**The current induced in a wire due to electromagnetic induction will oppose the change that created it.**
In other words: the force moving a charge through the electromagnetic field will be opposed by the force created via the induced current.

Lenz's law is, despite it's seemingly complex wording, actually just an extension of conservation of energy: if the converse were true, an object would accelerate up to high speeds just by being lightly pushed into a magnetic field.

This can be shown by just dropping a magnet through a copper pipe or coil: the magnet falls much slower than it would falling down a plastic pipe. This is due to the force acting against gravity, caused by Lenz's Law.

### Faraday's Law
There is an expression for the EMF $\epsilon$ created by a wire in a magnetic field, which we can derive using conservation of energy.
Consider the following diagram. We are exerting a force $F$ on a wire of length $l$, acting downwards for a distance $\Delta s$. The induced current in the wire is $I$.
![[FaradaysLawDerivation.svg]]
Now by conservation of energy:
	Work done on the wire = electrostatic energy gained by the wire.
Now, we can make this an equation.
$E = \epsilon Q$ ($E$ here is the electrostatic energy, though it might look a little weird, this is actually just $E = QV$, but for EMFs.)
Hence, $$F\Delta s = \epsilon Q$$
Now we know that $F$ is equal and opposite to the force given by the [motor effect equation](Physics/Fields/Magnetic%20Fields#Magnetic%20Flux%20Density). (Except we use $-F$ here as opposed to $F$, as our force is in the opposite direction and as $\theta = 90^\circ$, the sine term becomes one.)
$$-BIl\Delta s = \epsilon Q$$
Rearranging for $\epsilon$, and substituting $Q = I\Delta t$ we get that
$$\epsilon = -\frac{BIl\Delta s}{I\Delta t}$$
Cancelling $I$, 
$$\epsilon = -\frac{Bl\Delta s}{\Delta t}$$
Here we can note that $\frac{\Delta s}{\Delta t} = v$.
$$\epsilon = -Blv$$
However, we can also note that $l\Delta s = \Delta A$, where $A$ is the 'area swept out by the wire'. Additionally, we note that in our example, we used a change in distance, but a changing magnetic field would have produced the same effect. Thus, we can rearrange to the following derivative:
$$\epsilon = -\frac{\Delta (BA)}{\Delta t} = -\frac{d (BA)}{dt} $$
#### Magnetic Flux
Here, we introduce a new variable, *magnetic flux* ($\phi$), which is linked to the [*magnetic flux density*](Physics/Fields/Magnetic%20Fields#Magnetic%20Flux%20Density), by the following equation, $\phi = BA$. 
Magnetic flux is measured in *webers* (*Wb*), which is equal to one Tesla meter squared.
In essence, magnetic flux can be thought of as the total number of magnetic field lines in an area of the magnetic field, which should be natural extension based on the definition of [*magnetic flux density*](Physics/Fields/Magnetic%20Fields#Magnetic%20Flux%20Density).
> The number of field lines per unit area

This leads the above equation to become:
$$\epsilon = -\frac{d\phi}{dt}$$
**This** is called *Faraday's Law of induction*. In the case that we are dealing with a coil, as we usually are, we use
$$\epsilon = -\frac{d(N\phi)}{dt}$$
Where $N$ is the number of turns in the coil. The term $N\phi$ actually has a special name in this context: *magnetic flux linkage*.