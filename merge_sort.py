def merge_sort(lst):
    """Time complexity - O(N * log N) for best, average, and worst, Space complexity - O(N)"""
    if len(lst) <= 1:
        return lst

    middle_index = len(lst) // 2
    left_split = lst[:middle_index]
    right_split = lst[middle_index:]
    # Recursive call of merge_sort():
    left_split_all = merge_sort(left_split)
    right_split_all = merge_sort(right_split)

    return merge(left_split_all, right_split_all)


def merge(left, right):
    merged_list = []
    while left and right:
        if left[0] < right[0]:
            merged_list.append(left.pop(0))
        else:
            merged_list.append(right.pop(0))
    if left:
        merged_list += left
    if right:
        merged_list += right
    return merged_list


unordered_list = [15, 65, 8, 17, 150, 1]
print(merge_sort(unordered_list))
