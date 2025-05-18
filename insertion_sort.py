def insertion_sort_monotonically(numbers_array):
    for index in range(1, len(numbers_array)):
        key = numbers_array[index]
        left_index = index - 1

        # iterate using while loop, moving elements smaller than key to the right
        while left_index >= 0 and numbers_array[left_index] < key:
            numbers_array[left_index + 1] = numbers_array[left_index]
            left_index -= 1
        numbers_array[left_index + 1] = key

if __name__ == "__main__":
    test_data = [5, 2, 9, 1, 5, 6]
    print("Unordered list:", test_data)
    insertion_sort_monotonically(test_data)
    print("Sorted in decreasing order:", test_data)
