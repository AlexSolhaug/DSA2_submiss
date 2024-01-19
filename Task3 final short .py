def quicksort(arr, low, high):
    # Check if the low index is less than the high index
    if low < high:
        # Partition the array and get the index of the pivot
        pivot_index = partition(arr, low, high)

        # Recursively sort the elements before the pivot
        quicksort(arr, low, pivot_index - 1)

        # Recursively sort the elements after the pivot
        quicksort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    # Swap the pivot (second element) with the first element
    arr[low], arr[low + 1] = arr[low + 1], arr[low]
    pivot = arr[low]  # Now the pivot is the first element

    # Initialize pointers
    i = low + 1  # Start from the element after the pivot
    j = high     # Start from the end of the array

    while True:
        # Move i to the right until an element larger than the pivot is found
        while i <= j and arr[i] <= pivot:
            i += 1
        # Move j to the left until an element smaller than the pivot is found
        while i <= j and arr[j] > pivot:
            j -= 1

        # If the pointers have crossed, exit the loop
        if i > j:
            break

        # Swap the elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

    # Swap the pivot element back to its correct position
    arr[low], arr[j] = arr[j], arr[low]

    return j  # Return the pivot's final position

# Example usage
if __name__ == "__main__":
    example_array = [3, 5, 1, 2, 4, 6]
    quicksort(example_array, 0, len(example_array) - 1)
    print("Sorted array:", example_array)
