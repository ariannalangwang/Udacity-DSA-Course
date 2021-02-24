
# For merge sort, it's particularly worth reading up on 
# top-down and bottom-up merge sort.

# Merge Sort is a Divide and Conquer algorithm. 
# It divides input array in two halves, calls itself for the two halves 
# and then merges the two sorted halves. 
# The merge() function is used for merging two halves. 
# The merge(arr, l, m, r) is key process that assumes that arr[l..m] 
# and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one.

# merge left subarray & right subarray into arr (in place):
def merge(arr, left, right):           
    i = j = k = 0   # initial index of left, right, merged subarrays 
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Checking if any element was left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        # Recursive call on each half
        mergeSort(left)
        mergeSort(right)
        merge(arr, left, right)

# Time Complexity: Sorting arrays on different machines. 
# Merge Sort is a recursive algorithm and time complexity can be 
# expressed as following recurrence relation. 
# T(n) = 2T(n/2) + θ(n)

# The above recurrence can be solved either using the Recurrence Tree method 
# or the Master method. 
# Time complexity of Merge Sort is  θ(n logn) in all 3 cases 
# (worst, average and best) as merge sort always divides the array 
# into two halves and takes linear time to merge two halves.

# Auxiliary Space: O(n)
# because have to make new left & right arrays.

# Algorithmic Paradigm: Divide and Conquer
# Sorting In Place: No in a typical implementation



# Test
arr = [12, 11, 13, 5, 6, 7]
mergeSort(arr) 
for i in range(len(arr)):
    print(arr[i], end=" ")
print()
 