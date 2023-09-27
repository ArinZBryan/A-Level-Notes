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

