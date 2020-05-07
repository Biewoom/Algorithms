import os
import sys

class BinaryTree:

    class Node:
        def __init__(self, x, y, value):
            self.x = x
            self.y = y
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, info):
        node = self.Node(info[0], info[1], info[2])

        if self.root is None: self.root = node; return
        cur = self.root
        while True:
            if node.x < cur.x:
                if cur.left: cur = cur.left
                else: cur.left = node; break
            else:
                if cur.right: cur = cur.right
                else: cur.right = node; break

    def preorder(self):
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, cur, result):
        result.append(cur.value)
        if cur.left: self._preorder(cur.left, result)
        if cur.right: self._preorder(cur.right, result)

    def postorder(self):
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, cur, result):
        if cur.left: self._postorder(cur.left, result)
        if cur.right: self._postorder(cur.right, result)
        result.append(cur.value)

def solution(nodeinfo):
    sys.setrecursionlimit(10**4)
    result = []
    binary_tree = BinaryTree()

    nodeinfos = [(x[0], x[1], i+1) for i, x in enumerate(nodeinfo)]
    nodeinfos.sort(key = lambda x: x[1], reverse = True)

    for info in nodeinfos:
        binary_tree.insert(info)

    result.append(binary_tree.preorder())
    result.append(binary_tree.postorder())
    return result

if __name__ == '__main__':
    nodeinfo = []
    for line in sys.stdin:
        line = line.rstrip('\n')
        info = list(map(int, line.split(",")))
        nodeinfo.append(info)

    result = solution(nodeinfo)
    print(result)
