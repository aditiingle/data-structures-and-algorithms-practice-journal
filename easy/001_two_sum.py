"""
Problem: Two Sum
Difficulty: Easy
Description: Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

# My attempt
int_array = [4, 2, 11, 7, 15]
target = 19
array_subset = 5

# Loop through the array
for i in range(array_subset - 1):
    for j in range(i + 1, array_subset):
        if int_array[i] + int_array[j] == target:
            print(f"Integers are at indices: {i} and {j}.")
            break  # Ends the loop when a match is found


# Solution using Hashmaps (idea is to use complements)
def two_sum(nums, target):
    num_map = {}  # Dictionary to store number and its index

    for i, num in enumerate(nums):
        complement = target - num  # Calculate the complement
        if complement in num_map:
            # If the complement exists in the map, return its index and the current index
            return [num_map[complement], i]
        # Otherwise, store the current number and its index
        num_map[num] = i

    return []  # Return empty list if no solution is found


nums = [4, 2, 7, 11, 15]
target = 19
result = two_sum(nums, target)

# Output the result
if result:
    print(f"Indices: [{result[0]}, {result[1]}]")
else:
    print("No solution found!")
