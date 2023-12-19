from classes.DL.menu import Menu
from models.Linkedlist import *
# Assuming Menu._food_list is a linked list

def sortedMerge(self, a, b):
        result = None
         
        # Base cases
        if a == None:
            return b
        if b == None:
            return a
             
        # pick either a or b and recur..
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
     
def mergeSort(self, h):
         
        # Base case if head is None
        if h == None or h.next == None:
            return h
 
        # get the middle of the list 
        middle = self.getMiddle(h)
        nexttomiddle = middle.next
 
        # set the next of middle node to None
        middle.next = None
 
        # Apply mergeSort on left list 
        left = self.mergeSort(h)
         
        # Apply mergeSort on right list
        right = self.mergeSort(nexttomiddle)
 
        # Merge the left and right lists 
        sortedlist = self.sortedMerge(left, right)
        return sortedlist
     
    # Utility function to get the middle 
    # of the linked list 
def getMiddle(self, head):
        if (head == None):
            return head
 
        slow = head
        fast = head
 
        while (fast.next != None and
               fast.next.next != None):
            slow = slow.next
            fast = fast.next.next
             
        return slow


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