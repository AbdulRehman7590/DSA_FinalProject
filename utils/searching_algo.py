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
def LinearSearch(data_list, columnName, search_key, filter_type):
        indexList = []
        for i in range(data_list.size()):
            value = data_list.get_item_at_index(i)
            row = getattr(value, columnName)
            if filter_type == 0 and search_key in row:
                indexList.append(value)
            elif filter_type == 1 and row.startswith(search_key):
                indexList.append(value)
            elif filter_type == 2 and row.endswith(search_key):
                indexList.append(value)
        
        return indexList