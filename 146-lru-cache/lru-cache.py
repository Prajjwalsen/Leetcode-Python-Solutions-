class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        # Dummy nodes
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from linked list
    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    # Insert node at MRU side
    def insert(self, node):
        prev_node = self.right.prev
        next_node = self.right

        prev_node.next = node
        node.prev = prev_node

        node.next = next_node
        next_node.prev = node

    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]

            # This key is now recently used
            self.remove(node)
            self.insert(node)

            return node.value

        return -1

    def put(self, key: int, value: int) -> None:

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Store in hashmap
        self.cache[key] = node

        # New node becomes most recently used
        self.insert(node)

        # If capacity exceeded
        if len(self.cache) > self.capacity:

            # Remove least recently used node
            lru = self.left.next

            self.remove(lru)
            del self.cache[lru.key]