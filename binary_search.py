def binary_search(sorted_list, value):
    lower_bound = 0
    upper_bound = len(sorted_list)

    while lower_bound < upper_bound:
        middle_idx = (lower_bound + upper_bound) // 2
        middle_value = sorted_list[middle_idx]

        if middle_value == value:
            return middle_idx
        elif middle_value > value:
            upper_bound = middle_idx
        elif middle_value < value:
            lower_bound = middle_idx + 1

    else:
        return "Value not found!"


def binary_search_recursion(sorted_list, value):
    if not sorted_list:
        return "Value not found!"

    middle_idx = len(sorted_list) // 2
    middle_value = sorted_list[middle_idx]

    if middle_value == value:
        return middle_idx
    elif middle_value > value:
        left_half = sorted_list[:middle_idx]
        return binary_search_recursion(left_half, value)
    elif middle_value < value:
        right_half = sorted_list[middle_idx + 1:]
        result = binary_search_recursion(right_half, value)

        if result == "Value not found!":
            return result
        else:
            return result + middle_idx + 1


def binary_search_pointers(sorted_list, value, left_pointer=None, right_pointer=None):
    if not left_pointer:
        left_pointer = 0
    if not right_pointer:
        right_pointer = len(sorted_list) - 1

    if left_pointer > right_pointer:
        return "Value not found!"

    middle_idx = (left_pointer + right_pointer) // 2
    middle_value = sorted_list[middle_idx]

    if middle_value == value:
        return middle_idx
    elif middle_value > value:
        return binary_search_pointers(sorted_list, value, left_pointer, middle_idx)
    elif middle_value < value:
        return binary_search_pointers(sorted_list, value, middle_idx + 1, right_pointer)


if __name__ == "__main__":

    test_list = [8, 12, 21, 45, 69, 128, 244, 256, 311]

    # UNCOMMENT LINES BELOW TO TEST THE BINARY SEARCH FUNCTIONS

    print("---BINARY SEARCH WITH WHILE LOOP---\n")
    # print(binary_search(test_list, 12))
    # print(binary_search(test_list, 1200))

    print("\n\n---BINARY SEARCH WITH RECURSION---\n")
    # print(binary_search_recursion(test_list, 128))
    # print(binary_search_recursion(test_list, 1200))

    print("\n\n---BINARY SEARCH WITH POINTERS---\n")
    # print(binary_search_pointers(test_list, 311))
    # print(binary_search_pointers(test_list, 1200))
