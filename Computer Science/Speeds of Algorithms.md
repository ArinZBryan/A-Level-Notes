Algorithms in the wild should have competitive advantage if they are to be widely used. This often requires that the algorithm is well optimized.  
It is required that you are able to measure and understand how each algorithm performs. There are 2 main things that are measured when comparing algorithms: time and space complexity.

This is generally shown using 'big O notation' eg. as O(n)

### Some common complexities
- **O($1$)** - Constant no matter the size of the dataset.
- **O($\log(n)$)** - Binary Search. Generally associated with 'divide and conquer' algorithms
- **O($n$)** - Linear Search. The complexity is just a direct function of the size of the data set
- **O($n log(n)$)** - Quick Sort + Binary Search. Generally used on large unordered datasets, where a large penalty for sorting need only be incurred once, and more efficient searches (binary search) can be used many times later.
- **O($n^2$) / O($n^3$)** - Iterating through a 2d or 3d array (where the power is the number of dimensions). This also applies to any algorithm involving nested loops. Again, the depth of the loops is the power that n is to. As such, insertion and bubble sort also fit here.
- **O($2^n$)** - Travelling salesman solved with dynamic programming. This is the first intractable algorithm. These such algorithms are those where a modest increase in the dataset size results in massive increases in the number of operations required by the algorithms.
- **O($n!$)** - Bogo Sort / Travelling salesman solved with brute force / most brute force algorithms. (This is also an intractable algorithm)

![A graph of the common complexities](./Images/Speeds_of_algorithms/Graph.jpeg "Big-O complexity Chart")

>__A side note on BOGO sort.__
>This is the Russian roulette of sorting algorithms. The best case scenario is O(n), if it gets it after one randomization.  
> The worst case scenario is O(infinity), where it randomizes over and over, but never randomizes how it wants to.  
> The average scenario is O(n!), where it randomizes to visit each permutation of the list once.