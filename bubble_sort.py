def bubble_sort(lst):
    """Time complexity - O(N^2 - N) = O(N^2)"""

    sorted = False
    while not sorted:
        sorted = True
        for idx in range(len(lst) - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]
                sorted = False

    return lst

def bubble_sort_optimized(lst):
    """Time complexity - O(N^2 - N) / 2 = O(N^2)
       The algorithm can somewhat be optimized as it takes less comparisons, however the time complexity remains
       the same when we drop constants"""

    for i in range(len(lst)):
        for idx in range(len(lst) - i - 1):
            if lst[idx] > lst[idx + 1]:
                lst[idx], lst[idx + 1] = lst[idx + 1], lst[idx]

    return lst


print(bubble_sort([5, 4, 3, 2, 1]))
print(bubble_sort_optimized([5, 4, 3, 2, 1]))