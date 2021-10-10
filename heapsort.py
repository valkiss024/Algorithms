import random

from Data_structures.max_heap import MaxHeap
from Data_structures.min_heap import MinHeap


def heap_sort_descending(lst):
    """Heap sort algorithm implementing a max-heap"""
    sorted_lst = []
    max_heap = MaxHeap()
    for element in lst:
        max_heap.add(element)

    while max_heap.get_root_node():
        max_value = max_heap.retrieve_max()
        sorted_lst.append(max_value)

    return sorted_lst


def heap_sort_ascending(lst):
    """Heap sort algorithm implementing a min-heap"""
    sorted_lst = []
    min_heap = MinHeap()
    for element in lst:
        min_heap.add(element)

    while min_heap.get_root_node():
        min_value = min_heap.retrieve_min()
        sorted_lst.append(min_value)

    return sorted_lst


if __name__ == "__main__":

    my_list = [random.randint(1, 50) for _ in range(10)]

    sorted_list_1 = heap_sort_descending(my_list)
    sorted_list_2 = heap_sort_ascending(my_list)

    print(f"Descending order: {sorted_list_1}")
    print(f"Ascending order: {sorted_list_2}")
