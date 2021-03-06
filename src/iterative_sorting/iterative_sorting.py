# Runtime complexity: O(n ^ 2) - Quadratic
# Nested for-loop
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for x in range(cur_index, len(arr)):
            if arr[x] < arr[smallest_index]:
                smallest_index = x
            
        # Swapping the values
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]
        

    return arr


# Runtime complexity: O(n ^ 2) - Quadratic
def bubble_sort(arr):

    needs_swapping = True

    while needs_swapping:
        # Change to false and change back to true only if a swap occurs
        # If a swap doesn't occur, it stays on false and the loop ends
        needs_swapping = False
        for x in range(len(arr) - 1):
            # If the current value is greater than the next value, swap the values
            if arr[x] > arr[x + 1]:
                arr[x], arr[x + 1] = arr[x + 1], arr[x]
                needs_swapping = True

    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr
