## Determinants
The determinant of a matrix can take one of two values, either zero, or some other number. If the determinant is not zero, then it can be said to be equal to the area scale factor of the transformation represented by the matrix. If the matrix is a 3x3 matrix, then this is the volume scale factor of the relavent transformation. If the determinant is zero, then the transformation maps all points on to either a point or a line, thus a shape with no volume or area. 

### 2x2
The determinant of a matrix $M$, $\begin{pmatrix}a&&b\newline c&&d\end{pmatrix}$ is denoted as $\det M $. For a 2x2 matrix, the determinant is calculated by the following formula: $\det M = ad-bc$. The determinant of a 2x2 matrix is equal to the area scale factor of the transformation it represents.

### 3x3
The determinant of a matrix $M$, 
$\begin{pmatrix}
a && b && c\newline
d && e && f\newline
g && h && i\newline
\end{pmatrix}$ is denoted as $\det M$. For a 3x3 matrix, the determinant is calculated by the following formula: $\det M = a\det\begin{pmatrix}e&&f\newline h&&i\end{pmatrix} - b\det\begin{pmatrix}d&&f\newline g&&i\end{pmatrix} + c\det\begin{pmatrix}d&&e\newline g&&h\end{pmatrix}$. The determinant of a 3x3 matrix is equal to the volume scale factor of the transformation it represents.

## Inverses
A matrix can only have it's inverse taken, if and only if, it has a non-zero determinant. Else, when the determinant is zero, effectively, information has been lost by applying the transformation, in the same way that by computing $y = x^2$, there are times where for a given y-value, it is impossible to know the x-value that was transformed into it.

### 2x2
The inverse of a 2x2 matrix $M$, $\begin{pmatrix}a&&b\newline c&&d\end{pmatrix}$ is denoted as $M^{-1}$ and can be calculated using the following formula: $\frac{1}{\det M}\begin{pmatrix}d && -b \newline -c && a \end{pmatrix}$

### 3x3
The inverse of a 3x3 matrix $M$, 
$\begin{pmatrix}
a && b && c\newline
d && e && f\newline
g && h && i\newline
\end{pmatrix}$ is denoted as $M^{-1}$. It is such a royal pain in the arse to calculate (source: I made a calculator for this). Just get your calculator to do it. It won't lose any marks.

### Checking your calculations
A good way to check if your determinant is correct is by multiplying it by the original matrix. This should result in the identity matrix for the given number of dimensions that the original matrix had.