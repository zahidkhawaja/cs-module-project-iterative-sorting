# Runtime complexity O(n) - Linear
def linear_search(arr, target):

    for x in range(len(arr)):
        if arr[x] == target:
            return x
        
    return -1 # Not found

# Runtime complexity O(log n) - Logarithmic
# Requires sorted data
def binary_search(arr, target):

    # Find the middle element
    left = 0
    right = len(arr) - 1

    # Keep iterating so long as the left index is <= right

    while left <= right:

        midpoint = (right + left) // 2

        if arr[midpoint] == target:
            return midpoint

        elif arr[midpoint] > target:
            right = midpoint - 1
        else:
            left = midpoint + 1

    # Did not find what we're looking for
    return -1
