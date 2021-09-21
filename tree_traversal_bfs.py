"""Tree traversal with breadth-first search algorithm"""

from Data_structures.tree import TreeNode
from collections import deque
import os


def breadth_first_search(root_node, value):
    path_queue = deque()
    initial_path = [root_node]
    path_queue.appendleft(initial_path)
    findings = []
    while path_queue:
        current_path = path_queue.pop()
        current_node = current_path[-1]

        if value in current_node.value[0]:
            findings.append(current_path)

        for child in current_node.children:
            new_path = current_path[:]
            new_path.append(child)

            path_queue.appendleft(new_path)

    if findings:
        return findings

    return None


BASE_PATH = "C:\\"  # Define a base path to the root directory of the search

root_node = TreeNode(["Root Dir"])  # Assign the chosen directory where hte search starts to be the tree root


def iterate_directory_tree(node, path_):
    path = path_ + node.value[0] + "\\"
    for element in os.listdir(path):
        if os.path.isfile(path + element):
            filename, ext = os.path.splitext(element)
            new_node = TreeNode([filename, ext])
        else:
            new_node = TreeNode([element])
        node.add_child(new_node)
        if os.path.isdir(path + element):
            try:
                iterate_directory_tree(new_node, path)
            except PermissionError:
                continue


if __name__ == "__main__":

    iterate_directory_tree(root_node, BASE_PATH)

    path = breadth_first_search(root_node, "DATA STRUCTURES")
    if path:
        for p in path:
            print(" >> ".join([node.value[0] for node in p]))
