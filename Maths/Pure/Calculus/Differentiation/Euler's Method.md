### First Order Differential Equations
When defining differentiation from first principals, we get that
$$f'(x) = \lim_{h\to 0}\frac{f(x+h)- f(x)}{h}$$
Euler's method is an approximation, where we remove the limit and set $h$ to some arbitrary, small value (usually less than 1).
By doing this, we can rearrange to get that:
$$f(x + h) \approx f(x) + hf'(x)$$
This, in a nutshell is Euler's method. This can be more usefully written as:
$$y_{n+1} = y_n + h\begin{pmatrix}\frac{dy}{dx}\end{pmatrix}_n$$
This method has aa few obvious issues:
1. The more steps we take with this method, the larger the error against the real value at that point.
2. The larger the steps we take, the less accuracy the values have.
3. Rapidly changing functions ($|\frac{d^2y}{dx^2}|$ is large) are likely to have little accuracy.
The best way to do this is to use the **Table Method**

| $n$ | $x_n$ | $y_n$ | $(\frac{dy}{dx})_n$ |
| --- | ----- | ----- | ------------------- |
| 0   | 2     | 5     | -11                 |
| 1   | ...   | ...   | ...                 |
| 2   | ...   | ...   | ...                 |
| 3   | ...   | ...   | ...                 |

### Second Order Differential Equations
