# Bubble Sort is the simplest sorting algorithm that works by 
# repeatedly swapping the adjacent elements if they are in wrong order.

def bubbleSort(arr):
    n = len(arr) 
    # Traverse through all array elements 
    for i in range(0, n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# The above function always runs O(n^2) time even if the array is sorted. 
# It can be optimized by stopping the algorithm if inner loop didn’t 
# cause any swap.
 

# An optimized version of Bubble Sort 
def bubbleSort(arr): 
	n = len(arr) 
	# Traverse through all array elements 
	for i in range(n): 
		swapped = False
		# Last i elements are already in place 
		for j in range(0, n-i-1): 
			# traverse the array from 0 to n-i-1. Swap if the element 
			# found is greater than the next element 
			if arr[j] > arr[j+1] : 
				arr[j], arr[j+1] = arr[j+1], arr[j] 
				swapped = True
		# If no two elements were swapped by inner loop, then break 
		if swapped == False: 
			break
		
# Worst and Average Case Time Complexity: O(n*n). 
# Worst case occurs when array is reverse sorted.

# Best Case Time Complexity: O(n). 
# Best case occurs when array is already sorted.

# Auxiliary Space: O(1) 

# Sorting In Place: Yes




# test 
arr = [64, 34, 25, 12, 22, 11, 90]  
bubbleSort(arr) 
  
print("Sorted array is:") 
for i in range(len(arr)): 
    print("{}".format(arr[i]) ) 