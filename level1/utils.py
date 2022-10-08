from tasks.bidirect_list_dummy_nodes import DoublyLinkedList


def print_all_nodes(s_list: DoublyLinkedList):
    """Debug print"""
    node = s_list.head.next
    while not node.dummy:
        prev, next = node.prev, node.next
        print(prev.value if prev is not None else None,
              '<--',
              node.value if node is not None else None, end=' | ')
        print(node.value if node is not None else None,
              '-->',
              next.value if next is not None else None)
        node = node.next