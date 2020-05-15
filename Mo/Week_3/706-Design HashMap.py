"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value): Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key): Remove the mapping for the value key if this map contains the mapping for the key.

Example:

    MyHashMap hashMap = new MyHashMap();
    hashMap.put(1, 1);          
    hashMap.put(2, 2);         
    hashMap.get(1);            // returns 1
    hashMap.get(3);            // returns -1 (not found)
    hashMap.put(2, 1);          // update the existing value
    hashMap.get(2);            // returns 1 
    hashMap.remove(2);          // remove the mapping for 2
    hashMap.get(2);            // returns -1 (not found) 
"""
class MyHashMap:
    class ListNode: 
        def __init__(self, x):
            self.val = x
            self.next = None

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 15000
        self.bucket = [None] * self.size

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        idx = key % self.size
        if self.bucket[idx] is None: 
            curr = ListNode([key, value])
            self.bucket[idx] = curr
        else: 
            curr = self.bucket[idx]
            prev = None
            while curr is not None: 
                if curr.val[0] == key: 
                    curr.val[1] = value
                    break 
                prev = curr
                curr = curr.next
                
            if curr is None: 
                prev.next = ListNode([key, value])

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        idx = key % self.size
        curr = self.bucket[idx]
        while curr is not None: 
            if curr.val[0] == key: 
                value = curr.val[1]
                return value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        idx = key % self.size
        curr = self.bucket[idx] # bucket[idx] is the head
        # If it's the head
        if curr and curr.val[0] == key:
            self.bucket[idx] = curr.next
            curr = None
            return
        
        prev = None
        while curr and curr.val[0] != key: 
            prev = curr
            curr = curr.next
        # If current is None that means no node has the key needed
        if curr is None: 
            return
        
        prev.next = curr.next
        curr = None
                
# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)