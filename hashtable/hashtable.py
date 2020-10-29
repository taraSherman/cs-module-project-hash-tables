class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.capacity = capacity
        self.my_list = [None] * capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.my_list)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        # load factor = total number of items divided by number of buckets/cells/slots
        items = 0
        for item in self.list:
            if item != None:
                items += 1
        return items / self.capacity

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit
            hash := FNV_offset_basis
        for each byte_of_data to be hashed do
            hash := hash × FNV_prime
            hash := hash XOR byte_of_data
        return hash
        
        byte_of_data = an 8-bit unsigned integer
        XOR = 8-bit operation that modifies only the lower 8-bits of the hash value
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        """
        # Your code here
        self.key = key
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        hash = FNV_offset_basis
        for byte_of_data in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(byte_of_data)

        return hash

    # def djb2(self, key):
    #     """
    #     DJB2 hash, 32-bit

    #     Implement this, and/or FNV-1.
    #     """
    #     # Your code here


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        return self.fnv1(key) % self.capacity
        # return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        # Your code here
        ## 1. Hash our string/key, get out a number
        ## 2. Take this number and modulo it by the length of the array
        ## 3. This new number can be used as an index, so put the value at that index in our array
        idx = self.hash_index(key)
        self.my_list[idx] = value

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        # Delete: find the value, then set to None
        idx = self.hash_index(key)
        if self.my_list[idx] is None:
            print(f'{key} not found')
        else:
            self.my_list[idx] = None

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        ## 1. Hash our string/key, string --> number
        ## 2. Mod this number by length of array
        ## 3. Use this modded number / index to get the value there
        idx = self.hash_index(key)
        return self.my_list[idx]


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
