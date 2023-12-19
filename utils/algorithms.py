# ---------------------- Merge Sort ------------------------------- #
def MergeSort(array,column,start = 0,end = None):
    end = len(array) if end is None else end

    if start < end:
        mid = (start + end) // 2
        MergeSort(array,column, start, mid) 
        MergeSort(array,column, mid + 1, end)
        Merge(array, start, mid, end,column)

def Merge(arr, p, q, r, column):
    lefthalf = arr[p:q + 1]
    righthalf = arr[q + 1:r + 1]

    i = j = 0
    k = p 

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i][column] < righthalf[j][column]:
            arr[k] = lefthalf[i]
            i += 1
        else:
            arr[k] = righthalf[j]
            j += 1
        k += 1
        
    while i < len(lefthalf):
        arr[k] = lefthalf[i]
        i += 1
        k += 1

    while j < len(righthalf):
        arr[k] = righthalf[j]
        j += 1
        k += 1


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
    
    
    