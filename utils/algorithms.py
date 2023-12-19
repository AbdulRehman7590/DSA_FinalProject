from classes.DL.menu import Menu
from models.Linkedlist import *
# Assuming Menu._food_list is a linked list

def merge_sort_linked_list(linked_list):
    if not linked_list or not linked_list.head or not linked_list.head.next:
        return linked_list

    mid = find_midpoint(linked_list)
    left_half = LinkedList()
    left_half.head = linked_list.head
    right_half = LinkedList()
    right_half.head = mid.next
    mid.next = None             # Disconnect the two halves

    left_half = merge_sort_linked_list(left_half)
    right_half = merge_sort_linked_list(right_half)

    return merge_linked_lists(left_half, right_half)

def find_midpoint(linked_list):
    slow = linked_list.head
    fast = linked_list.head

    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge_linked_lists(left, right):
    merged = LinkedList()
    current = merged.head

    left_ptr = left.head
    right_ptr = right.head

    while left_ptr and right_ptr:
        if left_ptr.value < right_ptr.value:
            if not current:
                merged.head = Node(left_ptr.value)
                current = merged.head
            else:
                current.next = Node(left_ptr.value)
                current = current.next
            left_ptr = left_ptr.next
        else:
            if not current:
                merged.head = Node(right_ptr.value)
                current = merged.head
            else:
                current.next = Node(right_ptr.value)
                current = current.next
            right_ptr = right_ptr.next

    if left_ptr:
        current.next = left_ptr
    elif right_ptr:
        current.next = right_ptr

    return merged

# # Example usage:
# sorted_food_list = merge_sort_linked_list(Menu._food_list)
# print(sorted_food_list)


# ---------------------- Data filters ------------------------ #
def starts_With(value, search_key):
        size = len(str(search_key))
        for i in range(size):
            if value[i] != search_key[i]:
                return False
        return True

def ends_With(value, search_key):
        n = len(str(search_key))
        for i in range(len(value) - n, len(value)):
            if search_key[i - (len(value) - n)] != value[i]:
                return False
        return True


# ---------------------- Searching ------------------------------- #
def LinearSearch(df, columnName, search_key, filter_type):
        indexList = []
        for index, value in enumerate(df):
            row = str(value[columnName])
            if filter_type == 0 and search_key in row:
                indexList.append(value)
            elif filter_type == 1 and row.startswith(search_key):
                indexList.append(value)
            elif filter_type == 2 and row.endswith(search_key):
                indexList.append(value)
        
        return indexList