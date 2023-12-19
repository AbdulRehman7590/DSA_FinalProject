from classes.DL.menu import Menu

# Assuming Menu._food_list is a linked list

def merge_sort_linked_list(linked_list):
    if len(linked_list) <= 1:
        return linked_list

    mid = len(linked_list) // 2 
    left_half = linked_list[:mid]
    right_half = linked_list[mid:]

    left_half = merge_sort_linked_list(left_half)
    right_half = merge_sort_linked_list(right_half)

    return merge_linked_lists(left_half, right_half)

def merge_linked_lists(left, right):
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:  # Assuming sorting based on some property
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged

# Example usage:
sorted_food_list = merge_sort_linked_list(Menu._food_list)
print(sorted_food_list)


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