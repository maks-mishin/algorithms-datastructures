from .linked_list import Node, LinkedList


def sum_linked_lists(s_list1: LinkedList, s_list2: LinkedList):
    if s_list1.len() != s_list2.len():
        return None

    result_s_list = LinkedList()
    node1, node2 = s_list1.head, s_list2.head
    while node1 is not None:
        new_node = Node(node1.Value + node2.Value)
        result_s_list.add_in_tail(new_node)
        node1, node2 = node1.next, node2.next
    return result_s_list
