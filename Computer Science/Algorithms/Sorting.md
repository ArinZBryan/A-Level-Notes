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
1. Set a left pointer and right pointer to the first and last elements of the array
2. Set the *pivot* pointer to the middle element of the array
3. Walk the left pointer right until it hits a value greater than the pivot's value
4. Walk the right pointer left until it hits a value smaller than the pivot's value
5. Swap the values at the left and right pointers
6. Repeat steps 3-5 until the left and right pointers are at the pivot.
7. Divide the array into two sub-arrays, one each side of the pivot. This can be done by pre-setting the left and right pointers to points in the original array
8. Run all above steps on each of the sub-arrays recursively.