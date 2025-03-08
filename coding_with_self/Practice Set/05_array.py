def find_subarray_with_sum(arr, target):
    start = 0
    current_sum = 0

    for end in range(len(arr)):
        current_sum += arr[end]

        # Shrink the window while the sum is greater than the target
        while current_sum > target and start <= end:
            current_sum -= arr[start]
            start += 1

        # Check if we found the target sum
        if current_sum == target:
            return (start, end)

    return None  # No subarray found


# Input from user
arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))
# arr = [int(x) for x in input("Enter the array elements separated by spaces: ").split()]
target = int(input("Enter the target sum: "))

# Find and display result
result = find_subarray_with_sum(arr, target)
if result:
    print(f"Subarray with target sum found between indexes: {result}")
else:
    print("No subarray with the given target sum found.")
