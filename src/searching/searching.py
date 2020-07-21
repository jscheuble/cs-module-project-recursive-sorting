# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    #
    if start > end:
        return -1
    # declare middle variable
    middle = (start + end) // 2
    # base case
    if arr[middle] == target:
        return middle
    # if target is in left subtree
    if arr[middle] < target:
        return binary_search(arr, target, middle, end)
    # if target is in right subtree
    else:
        return binary_search(arr, target, start, middle)

    # STRETCH: implement an order-agnostic binary search
    # This version of binary search should correctly find
    # the target regardless of whether the input array is
    # sorted in ascending order or in descending order
    # You can implement this function either recursively
    # or iteratively


def agnostic_binary_search(arr, target):
    # Your code here
    pass
