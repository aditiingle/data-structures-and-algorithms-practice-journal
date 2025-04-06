# Merge two sorted arrays

# My attempt using Quick Sort O(n log n)
nums1 = list(map(int, input("Enter numbers in your first array spaced by space: ").split()))
nums2 = list(map(int, input("Enter numbers in your second array spaced by space: ").split()))

m = len(nums1)
n = len(nums2)

print("\nThe arrays you entered and their sizes are: ")
print("nums1: ", nums1, "\nm:", m)
print("nums2: ", nums2, "\nn:", n)

def quick_sort(arr):
    if len(arr) <= 1: # If array has 1 or 0 elements, it is already sorted.
        return arr
    pivot = arr[len(arr) // 2] # Choose the middle element
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right) # Recursively applying the same steps to the left and right sub-arrays.

def merge_sorted_array(arr1, arr2):
    arr1 = quick_sort(arr1 + arr2)
    return arr1


nums1 = merge_sorted_array(nums1, num2)

print("New nums1 array: ", nums1)


# Solution using the three-pointer approach
def merge(nums1, m, nums2, n):
    i = m - 1       # Pointer for nums1's actual elements
    j = n - 1       # Pointer for nums2
    k = m + n - 1   # Pointer for placement in nums1

    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1















