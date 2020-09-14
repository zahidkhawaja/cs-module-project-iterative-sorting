def linear_search(arr, target):

    for x in range(len(arr)):
        if arr[x] == target:
            return x
        
    return -1 # Not found

# Write an iterative implementation of Binary Search
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
            # Toss out the left side of the array
            # Since the midpoint is also irrelevant, we can +1 to start from the next value
            right = midpoint - 1
        else:
            left = midpoint + 1

    # Did not find what we're looking for
    return -1
