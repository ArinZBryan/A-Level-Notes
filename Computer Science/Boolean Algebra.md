Boolean algebra is the process of making circuits more efficient.  There are two main ways of doing this at A-Level
- Using a Karnaugh Map
- Applying *the* law

### Karnaugh Maps
A Karnaugh map is a graphical representation of a circuit, used in logic design  for the simplification of boolean algebra expressions. In general, a Karnaugh map is another way of representing a truth table.
1. They are represented on a 2D grid
2. Binary values are entered into the grid.
##### Some Examples:
![[Karnaugh-AorB.png]] 
($A \vee B$)

![[Karnaugh-AandB.png]] ($A\wedge B$)
![[Karnaugh-AxorB.png]]
($A\underline{\vee}B$)
##### More Inputs
So far, only Karnaugh maps with two inputs have been shown, but it is possible to construct Karnaugh maps that are arbitrarily large. To do this, two or more inputs can be 'combined'. An example is shown below:
![[Karnaugh-4Inputs.png]]
### Simplifying Boolean Expressions using Karnaugh maps
### Boolean Operators
There are five main operators that can come up at A-Level:
$\wedge$ : AND 
$\vee$ : OR
$¬$ : NOT
$\underline{\vee}$ : XOR
$.$ : NAND

There is an order of precedence to be careful of:
NAND $\rightarrow$ NOT $\rightarrow$ XOR $\rightarrow$ AND $\rightarrow$ OR

### Rules of Boolean Algebra
##### Annulment
$A\wedge 0 = 0$
$A\vee 1 = 1$
##### Identity
$A\wedge 1= A$
$A\vee 0 = A$
##### Idempotent
$A\vee A = A$
$A\wedge A = A$
##### Complement
$A\vee¬A = 1$
$A\wedge¬A=0$
##### Double Negation
$¬(¬A) = A$
##### De Morgan's
$¬(A\wedge B) = ¬A \vee ¬B$
$¬(A\vee B) = ¬A \wedge ¬B$
##### Associative
$(A\vee B)\vee C = A\vee(B\vee C)$
$(A\wedge B)\wedge C = A\wedge(B \wedge C)$
##### Commutative
$A\vee B = B\vee A$
$A\wedge B = B\wedge A$
##### Distributive
$A\wedge (B\vee C) = (A \wedge B) \vee (A\wedge C)$
$A\vee (B\wedge C) = (A \vee B) \wedge (A\vee C)$
##### Absorptive
$A \vee (A \wedge B) = A$
$A\wedge(A\vee B) = A$

