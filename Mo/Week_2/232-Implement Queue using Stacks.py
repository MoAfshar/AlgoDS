"""
Implement the following operations of a queue using stacks.

    push(x) -- Push element x to the back of queue.
    pop() -- Removes the element from in front of queue.
    peek() -- Get the front element.
    empty() -- Return whether the queue is empty.
    
Example:

    MyQueue queue = new MyQueue();

    queue.push(1);
    queue.push(2);  
    queue.peek();  // returns 1
    queue.pop();   // returns 1
    queue.empty(); // returns false
    
Notes:

You must use only standard operations of a stack -- which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, stack may not be supported natively. You may simulate a stack by using a list or deque (double-ended queue), as long as you use only standard operations of a stack.
You may assume that all operations are valid (for example, no pop or peek operations will be called on an empty queue).
"""
class MyQueue2:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []

    # Every new element should be pushed to the bottom of the stack 
    # Transfer all s1 elements to auxiliary stack s2 
    # Then the newly arrived element is pushed on top of s2 and all its elements are popped and pushed to s1
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        while self.s1: 
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2: 
            self.s1.append(self.s2.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        return self.s1.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.s1[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1
    
    
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s1 = []
        self.s2 = []
        self.front = None

    # Every new element should be pushed to the bottom of the stack 
    # Transfer all s1 elements to auxiliary stack s2 
    # Then the newly arrived element is pushed on top of s2 and all its elements are popped and pushed to s1
    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.s1: 
            self.front = x
        self.s1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.s2: 
            while self.s1: 
                self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s2: 
            return self.s2[-1]
        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.s1 and not self.s2

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()