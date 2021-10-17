from __future__ import annotations
from typing import List

'''
TrieNode class definition
'''
class TrieNode:
    def __init__(self, prefix: str = "", isTerminal: bool = False):
        self._prefix = prefix
        self._isTerminal = isTerminal
        self._children = [None for _ in range(26)]

    def getPrefix(self) -> str:
        return self._prefix

    def getIsTerminal(self) -> bool:
        return self._isTerminal

    def getChildAt(self, idx: int) -> TrieNode:
        assert 0 <= idx < 26, f"Bad index provided: {idx}"
        return self._children[idx]

    def setTerminal(self):
        self._isTerminal = True

    def setNonTerminal(self):
        self._isTerminal = False

    def setPrefix(self, newPrefix:str):
        self._prefix = newPrefix

    def setChildAt(self, idx: int, newChild: TrieNode):
        assert 0 <= idx < 26, f"Bad index provided: {idx}"
        self._children[idx] = newChild


'''
"Private" utilities
'''


def _idx(a: str):
    assert len(a) == 1, "We can only feed one character into the ord() function."
    return ord(a) - 97


def _getCommonPrefixLen(str1: str, str2: str) -> int:
    assert str1 is not None and str2 is not None, "Please give us a decent pair of strings to work with"
    i = 0
    while i < min(len(str1), len(str2)) and str1[i] == str2[i]:
        i += 1
    return i


def _splitInsert(node: TrieNode, key: str) -> TrieNode:
    storedPrefix = node.getPrefix()
    commonPrefixLen = _getCommonPrefixLen(storedPrefix, key)
    node.setPrefix(storedPrefix[0:commonPrefixLen])
    node.setNonTerminal()
    node.setChildAt(_idx(storedPrefix[commonPrefixLen]), TrieNode(storedPrefix[commonPrefixLen:], True))
    node.setChildAt(_idx(key[commonPrefixLen]), TrieNode(key[commonPrefixLen:], True))
    return node


'''
Interface methods
'''


def search(node: TrieNode, key: str) -> bool:
    if node is None or key is None:
        return False
    storedPrefix = node.getPrefix()
    prefixLength = len(storedPrefix)
    if prefixLength < len(key):     # If the prefix is of shorter length than the key
        if storedPrefix == key[0:prefixLength]:      # and it's an actual prefix of the key as well
            return search(node.getChildAt(_idx(key[prefixLength])), key[prefixLength:]) # Then chop the input key and look at the appropriate child.
        else:   # Otherwise, if it's NOT an actual prefix of the key...
            return False   # It's not in the trie; return False
    elif prefixLength == len(key):  # Otherwise, if the prefix of the key is actually of the same length as the key
        return storedPrefix == key and node.getIsTerminal()  # Then return True if the prefix is equal to the key and the node is a terminal node.
    else:   # If the stored prefix is greater in length than the input key...
        return False    # There's no way we can have the key stored in the trie.


def insert(node: TrieNode, key: str) -> TrieNode:
    if node is None:    # Leaf node; insert the key.
        node = TrieNode(key, True)
    else:
        prefix = node.getPrefix()
        prefixLen = len(prefix)
        keyLen = len(key)
        if key == prefix:   # If the key matches the prefix exactly
            node.setTerminal()
        elif keyLen < prefixLen and prefix[0:keyLen] == key:   # If the key is a proper prefix of the stored prefix, split node in 2, making a new parent.
            temp = node
            temp.setPrefix(prefix[keyLen:])
            node = TrieNode(key, True)
            node.setChildAt(_idx(prefix[keyLen]), temp)
        elif keyLen > prefixLen and key[0:prefixLen] == prefix: # If the stored prefix is a proper prefix of the key, chop string and recurse into appropriate node!
            residualKey = key[prefixLen:]
            targetChildIdx = _idx(key[prefixLen])
            node.setChildAt(targetChildIdx, insert(node.getChildAt(targetChildIdx), residualKey))
        else:       # If neither string is a strict prefix of the other AND they are not equal, this means that they have a shared prefix. Split into 3 nodes.
            node = _splitInsert(node, key)
    return node

if __name__ == '__main__':
    '''
      I will test with some hand-drawn tries I have available.
    '''
    trie = None
    stringList = ["biq", "bir"]
    for key in stringList:
        trie = insert(trie, key)
    for key in stringList:
        print(f"Key {key} was found: {search(trie, key)}")

