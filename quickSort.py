Like Merge Sort, QuickSort is a Divide and Conquer algorithm. 

The algorithm can be broken down into three parts​​:

1. Partition the array about the pivot.
2. Passing the smaller arrays to the recursive calls.
3. Joining the sorted arrays that are returned from the recursive call and the pivot.


 
QuickSort is an in-place sorting algorithm with worst-case time complexity of O(n^2).


T(n) = T(k) + T(n-k-1) + θ(n)
 
def quickSort(arr):   
    n = len(arr)  
    
    # Base case
    if n <= 1:
        return arr  
    
    pi = 0     # positioning index
    for i in range(1, n): 
        if arr[i] <= arr[0]: 
            pi += 1         
            arr[i], arr[pi] = arr[pi], arr[i]    
    arr[0], arr[pi] = arr[pi], arr[0]      # Brings pivot to it's appropriate position  
     
    left = quickSort(arr[0:pi])            # Sorts the elements to the left of pivot
    right = quickSort(arr[pi+1:n])         # sorts the elements to the right of pivot

    arr = left + [arr[pi]] + right         # Merging everything together
    return arr


# Test
test1 = [4,2,7,3,1,6]
print("Original Array: ", test1)
print("Sorted Array: ", quickSort(test1))

test2 = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print("Original Array: ", test2)
print("Sorted Array: ", quickSort(test2))

test3 = [4, 3, 2, 1, 0, 10, 9, 8, -1, 7]
print("Original Array: ", test3)
print("Sorted Array: ", quickSort(test3))

test4 = [4, 10, 9, 8, 7, 3, 2, 1, 20, 7, -1]
print("Original Array: ", test4)
print("Sorted Array: ", quickSort(test4))