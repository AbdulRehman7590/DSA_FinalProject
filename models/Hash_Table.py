# ----------------------- HashTable -------------------------------- #
class HashTable:
    def __init__(self, size=30):
        self._size = size
        self._table = [None] * self._size
        self._count = 0
        self._threshold = 0.7


    # ------------------------ Methods ---------------------------- #
    def size(self):
        return self._count

    def keys(self):
        keys = []
        for item in self._table:
            if item:
                for user in item:
                    keys.append(user.order_id)
        return keys

    # ------------------------ Hash Function --------------------- #
    def _hash_function(self, key):
        sum = 0
        for ch in key:
            sum += ord(ch)
        return sum % self._size
    
    # ------------------------ Rehash ---------------------------- #
    def _rehash(self):
        self._size *= 2
        self._table = [None] * self._size
        oldTable = self._table
        self._count = 0

        for item in oldTable:
            if item:
                for user in item:
                    self.insert(user)

    # ------------------------ Insert ---------------------------- #
    def insert(self, order):
        index = self._hash_function(order.order_id)
        if not self._table[index]:
            self._table[index] = [order]
            self._count += 1
        else:
            for user in self._table[index]:
                if user.order_id == order.order_id:
                    user = order
                    return
            self._table[index].append(order)
            self._count += 1
        
        if self._count / self._size >= self._threshold:
            self._rehash()

    # ------------------------ Remove ---------------------------- #
    def remove(self, order):
        index = self._hash_function(order.order_id)
        if self._table[index]:
            for user in self._table[index]:
                if user.order_id == order.order_id:
                    self._table[index].remove(user)
                    self._count -= 1
                    return
    
    # ------------------------ Search ---------------------------- #
    def search(self, order_id):
        index = self._hash_function(order_id)
        if self._table[index]:
            for order in self._table[index]:
                if order.order_id == order_id:
                    return order
        return None
    
    