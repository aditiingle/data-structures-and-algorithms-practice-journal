""" You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n. """

num1 = list(map(int, input("Enter numbers in your first array spaced by space: ").split()))
num2 = list(map(int, input("Enter numbers in your second array spaced by space: ").split()))

m = len(num1)
n = len(num2)

print("\nThe arrays you entered and their sizes are: ")
print("num1: ", num1, "\nm:", m)
print("num2: ", num2, "\nn:", n)

list()


# My attempt using Quick Sort O(n log n)
def quick_sort(arr):
    if len(arr) <= 1: # If array has 1 or 0 elements, it is already sorted.
        return arr
    pivot = arr[len(arr) // 2] # Choose the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) # Recursively applying the same steps to the left and right sub-arrays.

def merge_sorted_array(arr1, arr2):
    arr1 = quick_sort(quick_sort(arr1) + quick_sort(arr2))
    return arr1


num1 = merge_sorted_array(num1, num2)

print("New num1 array: ", num1)













