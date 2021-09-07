"""
Python implementation of Leetcode Question #146:
https://leetcode.com/problems/lru-cache/

The implementation of LRUCache is based in a combination of a circular list, as well as a hash map that maps
the keys to nodes inside the list. The nodes contain the values.
"""


class LRUCache:

    ###########################################
    # Inner class for Doubly Linked List Node #
    ###########################################

    class _CLNode:

        ############################
        # Constructor for _CLNode: #
        ############################
        def __init__(self, key=None, value=None):
            self.key = key
            self.value = value
            self.prev = None
            self.next = None

    ############################
    # Constructor for LRUCache #
    ###########################
    def __init__(self, capacity: int):
        assert capacity > 0, f"Provided bad capacity: {capacity}"
        self._capacity = capacity
        self._cache = dict()
        self._num_elements = 0
        self._prepare_list()

    ##################
    # List utilities #
    ##################

    def _prepare_list(self) -> None:
        self._head = self._CLNode()  # dummy node
        self._tail = self._CLNode()  # dummy node
        self._head.next = self._tail
        self._head.prev = self._tail
        self._tail.next = self._head
        self._tail.prev = self._head

    def _move_to_head(self, node: _CLNode) -> None:
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        node.prev = self._head
        node.next = self._head.next
        self._head.next.prev = node
        self._head.next = node

    def _pop_from_tail(self) -> _CLNode:
        assert self._num_elements > 0, "You cannot pop the tail of an empty list!"
        lru_el = self._tail.prev
        lru_el.prev.next = lru_el.next            # tail
        self._tail.prev = lru_el.prev
        return lru_el

    def _add_to_head(self, key, value) -> None:
        node = self._CLNode(key, value)
        self._move_to_head(node)

    ##################################
    # LRU cache public functionality #
    ##################################

    def get(self, key: int) -> int:
        node = self._cache.get(key)
        if node is None:
            return -1
        else:
            self._move_to_head(node)                                            # O(1)
            return node.value

    def put(self, key: int, value: int) -> None:
        node = self._cache.get(key)
        if node is None:
            if self._num_elements == self._capacity:                            # pop LRU if full
                lru_el = self._pop_from_tail()                                  # O(1), unlike bounded heaps that are O(log_2n)
                del self._cache[lru_el.key]                                     # Also O(1), because hash function.
            else:
                self._num_elements = self._num_elements + 1                     # Increase only if not at capacity.
            new_node = self._CLNode(key, value)
            self._cache[key] = new_node                                         # O(1)
            self._move_to_head(new_node)                                        # Most recently used object always moves up front
        else:
            node.value = value
            self._move_to_head(node)

