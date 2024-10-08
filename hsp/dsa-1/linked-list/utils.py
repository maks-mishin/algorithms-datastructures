from bidirect_list_dummy_nodes import DoublyLinkedList
from bidirect_linked_list import Node, LinkedList2
from linked_list import LinkedList


def print_bidirectional_list_dummy(s_list: DoublyLinkedList):
    """Debug print for bidirectional linked list with dummy nodes"""
    node = s_list.head.next
    while isinstance(node, Node):
        prev, next = node.prev, node.next
        print(prev.Value if prev is not None else None,
              '<--',
              node.Value if node is not None else None, end=' | ')
        print(node.Value if node is not None else None,
              '-->',
              next.Value if next is not None else None)
        node = node.next


def print_bidirectional_list(s_list: LinkedList2):
    """Debug print for bidirectional linked list"""
    node = s_list.head
    while node is not None:
        prev, next = node.prev, node.next
        print(prev.Value if prev is not None else None,
              '<--',
              node.Value if node is not None else None, end=' | ')
        print(node.Value if node is not None else None,
              '-->',
              next.Value if next is not None else None)
        node = node.next

def print_all_nodes(s_list: LinkedList):
    """Debug print for single linked list"""
    node = s_list.head
    while node is not None:
        if node.next is None:
            print(node.value, '-->', node.next)
        else:
            print(node.value, '-->', node.next.Value)
        node = node.next