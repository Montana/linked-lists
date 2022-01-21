from typing import List


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


def convert_to_multilevel_lst(node_lst: List) -> List[List]:

    node_lst.append(None)
    multi_node_lst = []
    is_new_level = True
    for i, val in enumerate(node_lst):
        if is_new_level:
            temp = []
            is_new_level = False
        temp.append(val)
        if val is None and node_lst[i - 1] is not None: 
            is_new_level = True
            multi_node_lst.append(temp)
    return multi_node_lst


def create_doubly_linked_list(node_lst: List) -> Node:
    def print_multilevel_linked_list() -> None:

        for i, root in enumerate(levels):
            num_nones = 0
            for j in range(i + 1):
                for val in multilevel_lst[j]:
                    if val is None:
                        num_nones += 1
                    else:
                        break
            print("   " * num_nones, end="")
            curr = root
            while curr:
                print(f"{curr.val}->", end="")
                curr = curr.next
            print(None)
            print("   " * num_nones, end="")
            curr = root
            while curr:
                if curr.child:
                    print("|  ", end="")
                else:
                    print("   ", end="")
                curr = curr.next
            print()

    multilevel_lst = convert_to_multilevel_lst(node_lst)
    levels = []
    for single_level in multilevel_lst:
        idx = 0
        while not single_level[idx]:
            idx += 1
        root = Node(single_level[idx], None, None, None)
        idx += 1
        pre = root
        while single_level[idx]:
            curr = Node(single_level[idx], pre, None, None)
            pre.next = curr
            pre = curr
            idx += 1
        levels.append(root)

    for i, root in enumerate(levels[1:], 1):
        num_nones = 0
        for val in multilevel_lst[i]:
            if val is None:
                num_nones += 1
            else:
                break
        pre_lvl_node = levels[i - 1]

        for _ in range(num_nones):
            pre_lvl_node = pre_lvl_node.next
        pre_lvl_node.child = root

    print_multilevel_linked_list()

    return levels[0] if levels else None


# Sample usage

node_lst = [1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12]
root = create_doubly_linked_list(node_lst)
