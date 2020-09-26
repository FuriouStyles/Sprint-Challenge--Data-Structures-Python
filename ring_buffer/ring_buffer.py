from doubly_linked_list import *

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.contents = DoublyLinkedList()


    def append(self, item):
        # Check if there's available capacity in the ring buffer
        if self.contents.length < self.capacity:
            self.contents.add_to_tail(item)
            self.current = self.contents.head
        else:
            # Remove the oldest item in the buffer
            oldest = self.contents.head
            self.contents.remove_from_head() 
            self.contents.add_to_tail(item)
            if oldest == self.current:
                self.current = self.contents.tail


    def get(self):
        buffer_contents = []

        current = self.current
        buffer_contents.append(current.value)

        if current.next:
            next_node = current.next
        else:
            next_node = self.contents.head

        while next_node is not current:
            buffer_contents.append(next_node.value)
            if next_node.next:
                next_node = next_node.next
            else:
                next_node = self.contents.head

        return buffer_contents