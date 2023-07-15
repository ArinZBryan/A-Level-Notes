### Bubble Sort
Time: O($n^2$), Space: O($1$)
*  Bubble sort takes every pair of adjacent items, and swaps them if they are in the wrong order.
* It can only do this for two items at a time.
* It does this for every pair of items in the list, until the list is sorted.
* Usually a nested loop is used to do this. This is slow.
The only main upside to Bubble sort is that it sorts in place, and therefore has a space complexity of O(1)

### Insertion Sort 
Time: O($n^2$), Space: O($n$)
* Insertion Sort creates a secondary list, which it places elements of the original in.
* They are always placed in the right order, thus the new list is sorted, and can be copied to the original.
* Though this is O(n^2) in time, it is much faster than bubble sort to begin with, and such is still preferable in most situations.

### Quick Sort
Time: O($n\log n$) Space: O($n$)
* It is unlikely that in an exam, you will be asked to give the exact algorithm or code for this. However, it is vey likely that you will have to quick sort a short list.
* This method of sorting makes use of recursion (pain) so for longer lists (really really long) may require a maximum stack depth redefinition to prevent a stack overflow.
* This method of sorting can involve parallelism, if it is too slow. For small lists, the time to start a new thread may be too great to make it worth it.  
* Quick sort can be said to work on a divide and conquer basis.

#### How to quick sort
> 1. Set a left pointer and right pointer to each end of the list
> 2. Check the value pointed to by the right pointer is larger than that pointed to by the left pointer
> 3. If the above check returns true, increment the left pointer. Else, swap the values, and decrement the right pointer
> 4. Repeat steps 2 and 3 until the left and right pointers meet (are in the same place). Place the 'pivot' pointer at this position. Every value to the left of the pivot should be less than the value pointed to by the left pointer and the opposite for the values to the right.
> 5. This is where the parallelism comes in. The above steps (1-4) should be repeated for the sub lists (all elements to the left of pivot, all elements to the right of pivot. Pivot is not included in these sub lists.)
> 6. The base case of the recursion is if no swaps were made, or the sub lists are of length one.