### Half Adders
Processors can only do three major operations: addition, shifting and flipping. A binary half adder is a circuit which adds two single bit binary numbers. Below is the truth table for such a circuit.

| A   | B   | Carry | Sum |
| --- | --- | ----- | --- |
| 0   | 0   | 0     | 0   |
| 0   | 1   | 0     | 1   |
| 1   | 0   | 0     | 1   |
| 1   | 1   | 1     | 0   | 

It is plain to see that the carry column can be produced by $A \wedge B$. It is also clear to see that the sum column is equal to the results of $A \underline{\vee} B$ (xor). Using this information, we can draw the circuit diagram of this logic.

![[HalfAdder.png]]
### Full Adders
A half adder can only add two single bit numbers together, to add slightly bigger numbers, it is needed to make a circuit that can be chained one after another. Thus, it is possible to join two half-adders to make a 'full adder'. The truth table of this circuit is shown below:

| A   | B   | Cin | Cout | S   |
| --- | --- | --- | ---- | --- |
| 0   | 0   | 0   | 0    | 0   |
| 0   | 0   | 1   | 0    | 1   |
| 0   | 1   | 0   | 0    | 1   |
| 0   | 1   | 1   | 1    | 0   |
| 1   | 0   | 0   | 0    | 1   |
| 1   | 0   | 1   | 1    | 0   |
| 1   | 1   | 0   | 1    | 0   |
| 1   | 1   | 1   | 1    | 1   | 

You can build the circuit using two half-adders: use the first half adder to add $A+B$, then use the second to add the result of $A+B$ with $C_{in}$, giving the final sum. Finally, OR'ing the carry outs from the two adders gives $C_{out}$.

![[Full_Adder.png]]
### D-Type Flip-Flops
A D-Type flip flop is a circuit as shown below:
![[D-Type_Flip_Flop.png]]
It is not required that you know the circuit diagram of this circuit, and as such it will often be represented as just a single component. 
It is important to know what this circuit does:
- When CLK is high, Q = D and NOT Q = !D
- When CLK is not high, the values of Q and NOT Q are maintained.
On some versions, called *rising edge* D-Type Flip Flops, the D=Q step only occurs on the rising edge. When CLK is maintained high, Q and NOT Q are not affected by D.