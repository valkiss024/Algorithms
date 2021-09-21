"""Tree traversal with Depth-First Search algorithm"""

from Data_structures.tree import TreeNode


def depth_first_search(root_node, target_value, path=tuple()):
    new_path = path + (root_node.value, )

    if root_node.value == target_value:
        return new_path

    for child in root_node.children:
        path_found = depth_first_search(child, target_value, new_path)  # Recursive call
        if path_found:
            return path_found

    return None


if __name__ == "__main__":

    root_node = TreeNode("Python")
    java_node = TreeNode("Java")
    c_node = TreeNode("C")
    javascript_node = TreeNode("Javascript")
    angular_node = TreeNode("AngularJS")
    react_node = TreeNode("React")
    c_plus_node = TreeNode("C++")
    c_sharp_node = TreeNode("C#")

    root_node.add_child(java_node)
    root_node.add_child(c_node)

    java_node.add_child(javascript_node)

    c_node.add_child(c_plus_node)
    c_node.add_child(c_sharp_node)

    javascript_node.add_child(angular_node)
    javascript_node.add_child(react_node)

    print(depth_first_search(root_node, "AngularJS"))
