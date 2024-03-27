A magnetic field is a field that interacts with various magnetic substances, as well as with charges. It is important to note that the field lines, when dealing with magnetic fields travel from a north pole to a south pole.
When current passes through a wire, a magnetic field is [induced](Physics/Electricity/Induction). This applies to any current carrying conductor. 
When current is flowing through the conductor, the magnetic field produced has field lines that form concentric rings around the conductor.
![Induced Magnetic Field](Images/InducedMagneticField.png)
#### Magnetic Flux Density
The magnetic flux density ($B$) of a magnetic field is a measure of the strength of a field at a given point, and is measured in *Tesla*. One *Tesla* is defined as a force of a Newton per meter of wire per ampere of current carried in the wire. It is important to note that this force is perpendicular to the magnetic field.

If you place such a current carrying wire in a magnetic field, the wire will feel a force exerted on it. However, if the current being carried is moving parallel to the magnetic field, the force exerted on the conductor is zero. This is because no component of the field is perpendicular to the current.

To find the magnitude of the force ($F$) on a wire of length $l$, carrying a current $I$, in a field of flux density $B$, we use the formula:
$$F = BIl\sin\theta$$
Note that theta is the angle between the conductor and the external flux lines.
#### Fleming's Left Hand Rule
To find the direction of the force, a simple physical rule exists: using your left hand, when positioned as shown the thumb, first and second finger point in the correct directions
![FlemingsLeftHandRule.png](FlemingsLeftHandRule.png)
### Moving Charges in a Magnetic Field
There is a force that acts on charged particles moving through a magnetic field. This is actually the reason that a current-carrying conductor experiences a force when it moves through a magnetic field.
The magnitude of this force ($F$) exerted on a given particle with charge $Q$, moving with a velocity $v$ at an angle $\theta$ relative to the field can be calculated with the following formula:
$$F = \frac{BQV}{\sin\theta}$$
To get the direction of the force, we can still use *Fleming's Left Hand Rule*. Instead of using the second finger as the current (which it technically still is), we say it is the direction of travel for a positively charged particle. If the particle is negatively charged, the direction should be flipped (effectively, this is done by mirroring everything to the right hand).

As the force applied to the particle is always perpendicular to the particle, said particle will move on a circular path, thus following [circular motion](Physics/Mechanics/Circular%20Motion).
The most common application of this is in a type of [particle accelerator](Physics/Fields/Particle%20Accelerators) called a *cyclotron*.
### Solenoids
A solenoid is a coil of wire, that when powered will create a magnetic field, similar to that of a bar magnet.
![Solenoid Magnetic Field](Solenoid.png)
By looking at the way that the current flows from the end of a coil, we can determine which pole of the coil you are looking at.
If the current is flowing clockwise, then it is a south pole, and if the current is flowing anticlockwise, then the pole is a north pole. This can be remembered using the following simple graphic.
![Solenoid Polarity](./../Images/SolenoidPolarity.png)