# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.linked_list = None

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Part 1: Hash collisions should be handled with an error warning.

        Part 2: Change this so that hash collisions are handled with Linked List Chaining.

        Fill this in.
        '''
        

        idx = self._hash_mod(key)
            
        node = LinkedPair(key, value)
        node.next = self.linked_list
        self.linked_list = node

        if self.storage[idx]:
            print("warning index collision")
        else:
            self.storage[idx] = node
        



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)

        # self.storage[idx]

        cur_node = self.linked_list

        if cur_node is None:
            print("key not found")
            return

        if cur_node.key == key:
            self.linked_list = cur_node.next
            return

        while cur_node.next:
            if cur_node.next.key == key:
                cur_node.next = cur_node.next.next
                return

            cur_node = cur_node.next

        print("key not found")


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        idx = self._hash_mod(key)

        # if self.storage[idx] == None:
        #     return None

        # node = self.storage[idx]

        node = self.linked_list

        while node:
            if node.key == key:
                return node.value
            node = node.next


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        self.storage += [None] * self.capacity
        self.capacity *= 2


if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
