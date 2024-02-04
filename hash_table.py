

class HT: #Hash table class
    def __init__(self, size):
        # Constructor method that initializes a new instance of the HT class.
        # It takes a `size` parameter, which specifies the size of the hash table.
        self.size = size
        # The `self.table` attribute is a list of length `size`, initially filled with `None` values.
        # This list represents the array of buckets or slots in the hash table.
        self.table = [None] * size

    def hash_function(self, key):
        # This method implements the hash function.
        # It takes a `key` parameter, computes its hash using the built-in `hash()` function,
        # and then takes the modulus of the hash with the size of the table to ensure the result fits within the table.
        return hash(key) % self.size
    
    def insert(self, key, value):
        # This method inserts a key-value pair into the hash table.
        # It first computes the index for the key using the hash function,
        # and then stores the value at that index in the table.
        index = self.hash_function(key)
        self.table[index] = value

    def get(self, key):
        # This method retrieves a value from the hash table by its key.
        # It computes the index for the key using the hash function,
        # and then returns the value stored at that index in the table.
        index = self.hash_function(key)
        return self.table[index]
    

if __name__ == '__main__':
    ht = HT(10)
    ht.insert('a', 1)
    ht.insert('b', 2)
    ht.insert('c', 3)
    print(ht.get('b'))  # Should return 2
    print(ht.get('z'))  # Should return None
    print(ht.table)  # Should print a list of 10 `None` values with ['b', 'c', 'a'] in the correct positions