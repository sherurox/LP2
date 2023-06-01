def selectionSort(arr):
    for i in range(len(arr)):
        min_idx = i  # Assume the current element is the minimum
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:  # If we find a smaller element
                min_idx = j  # Update the index of the minimum element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap the minimum element with the current element
    return arr

print(selectionSort([89, 56, 45, 34, 65, 76]))

# Explanation:
# The selection sort algorithm sorts an array by repeatedly finding the minimum 
# element from the unsorted part of the array and placing it at the beginning. 
# Here's a step-by-step breakdown of the algorithm:

# 1. The `selectionSort` function takes an array `arr` as input.
# 2. It iterates through each element of the array using the outer loop, 
# controlled by the variable `i`.
# 3. Within the outer loop, the variable `min_idx` is initialized as `i`, 
# assuming that the current element is the minimum.
# 4. The inner loop, controlled by the variable `j`, starts from `i + 1`
#  and iterates until the end of the array.
# 5. Within the inner loop, it compares each element `arr[j]` with the 
# assumed minimum element `arr[min_idx]`.
# 6. If `arr[j]` is found to be smaller than `arr[min_idx]`, it updates `min_idx` 
# with the index `j`, indicating that `arr[j]` is the new minimum element.
# 7. Once the inner loop completes, it swaps the minimum element (`arr[min_idx]`) 
# with the current element (`arr[i]`).
# 8. This process continues for each element in the array until the array is completely sorted.
# 9. Finally, the sorted array is returned.

# The selection sort algorithm has a time complexity of O(n^2) in the worst case, as it involves nested loops. It is an in-place sorting algorithm, meaning it doesn't require additional memory beyond the input array. However, it is not considered efficient for large arrays and is mainly used for educational purposes or for sorting small lists.


# Selection Sort is a simple comparison-based sorting algorithm. It works by dividing the input array into two parts: the sorted part and the unsorted part. The algorithm repeatedly selects the smallest (or largest) element from the unsorted part and moves it to the sorted part. This process is repeated until the entire array is sorted.

# Here's how the selection sort algorithm works:

# 1. Start with an unsorted array of elements.
# 2. Set the first element as the minimum (or maximum) value.
# 3. Find the minimum (or maximum) element from the remaining unsorted part of the array.
# 4. Swap the found minimum (or maximum) element with the first element of the unsorted part.
# 5. Move the boundary of the sorted part one element to the right.
# 6. Repeat steps 2-5 until the entire array is sorted.

# The selection sort algorithm sorts the array in-place, meaning it modifies the 
# original array without requiring additional memory. However, it is not an efficient 
# algorithm for large lists as its time complexity is O(n^2), where n is the number of 
# elements in the array.

# Despite its inefficiency, selection sort has some advantages. It is easy to understand 
# and implement, making it a suitable choice for small lists or educational purposes. 
# Additionally, it has the property of minimizing the number of swaps, which can be beneficial 
# in certain situations where the cost of swapping elements is high.

# Overall, selection sort is a basic sorting algorithm that can be used when simplicity and 
# minimal memory usage are more important than sorting speed.