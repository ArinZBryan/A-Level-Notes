### Magnitude and Angle
Assume the following situation, a particle of mass $m$ travelling at a speed $u$ m/s hits a smooth immovable plane at an angle $\alpha$. It then rebounds at an angle $\beta$ with speed $v$.
![](./../Images/ObliqueCollision1.svg)
In this situation, we can calculate some important values.
As momentum is conserved parallel to the plane, we know that:
$$mu\cos\alpha = mv\cos\beta$$
$$\therefore u\cos\alpha = v\cos\beta$$
We also know, that if the plane and particle have a coefficient of restitution of $e$, where $0 \lt e \leq 1$ we can calculate the speed in the perpendicular component.
$$eu\sin\alpha = v\sin\beta$$
Using these two equations, we can make two more useful ones.
$$e\tan\alpha = \tan\beta$$
$$(u\cos\alpha)^2 + (eu\cos\alpha)^2 = v^2$$
Using these equations, we can now solve for all the possible needed values.
### Vectors
Consider a particle moving with velocity $\underline u\text{ ms}^{-1}$ that hits a smooth plane with direction vector $\underline W$ and rebounds with a velocity $\underline v\text{ ms}^{-1}$.
![](./../Images/vector_collisions.drawio.svg)
It is known that the impulse $\underline I$ is perpendicular to the vector $\underline W$.

By the definition of the [dot product](./../Pure/Vectors/Vector%20Operations.md#Dot%20(scalar)%20Product):
$$\underline u \cdot \underline{\hat{W}} = |u| |\underline{\hat W}| = u\cos\alpha$$ $$\underline v \cdot \underline{\hat{W}} = |v| |\underline{\hat W}| = v\cos\alpha$$
We can substitute this into the CoLM equation ($u\cos\alpha = v\cos\beta$) as:
$$\underline u\cdot\underline{\hat{W}} = \underline v\cdot\underline{\hat{W}}$$
$$\implies \underline u \cdot \underline W = \underline v \cdot \underline W$$
In a similar process, we can get that:
$$\underline v \cdot \underline{\hat{I}} = -e(\underline u \cdot \underline{\hat{I}})$$
which can also be given without using unit vectors.