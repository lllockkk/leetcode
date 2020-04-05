import algorithm.tree.bst as bst
import unittest


# left leaning red black tree
# 左倾红黑树 (2-3树)
# TODO: 刪除
class LLRBTree(bst.BinarySearchTree):
    def put(self, key, value):
        self.root, addNode = self._put(self.root, key, value)
        if (addNode != None):
            self.n = self.n + 1
        self.root.isRed = False

    def _put(self, node, key, value):
        # 只有一个节点
        if (node == None):
            addNode = RedBlackTreeNode(key, value, True)
            return addNode, addNode
        elif (node.key == key):
            node.value = value
            return node, None
        elif (node.key < key):
            node.rightChild, addNode = self._put(node.rightChild, key, value)
        else:
            node.leftChild, addNode = self._put(node.leftChild, key, value)

        # 1、左旋  2、右旋  3、修改颜色
        if (node.rightChild and node.rightChild.isRed and (node.leftChild == None or not node.leftChild.isRed)):
            node = self.rotateLeft(node)
        if (node.leftChild and node.leftChild.isRed and node.leftChild.leftChild and node.leftChild.leftChild.isRed):
            node = self.rotateRight(node)
        if (node.leftChild and node.leftChild.isRed and node.rightChild and node.rightChild.isRed):
            self.flipColor(node)

        return node, addNode

    def deleteMin(self):
        if (self.root == None):
            return None, None
        if (not self.isRed(self.root.leftChild) and not self.isRed(self.root.rightChild)):
            self.root.isRed = True
        self.root, delNode = self._deleteMin(self.root)
        if (delNode):
            self.n = self.n - 1
        if (self.root):
            self.root.isRed = False

    def _deleteMin(self, node):
        if (node.left == None):
            return None
        if (not self.isRed(node.leftChild) and not self.isRed(node.leftChild.leftChild)):
            self.moveRedLeft(node)
        node.leftChild = self._deleteMin(node.leftChild)

    def moveRedLeft(self, node):
        pass

    def rotateLeft(self, node):
        r = node.rightChild
        node.rightChild = r.leftChild
        r.leftChild = node
        r.isRed = node.isRed
        node.isRed = True
        return r

    def rotateRight(self, node):
        l = node.leftChild
        node.leftChild = l.rightChild
        l.rightChild = node
        l.isRed = node.isRed
        node.isRed = True
        return l

    def flipColor(self, node):
        node.isRed = True
        node.leftChild.isRed = False
        node.rightChild.isRed = False

    def isRed(self, node):
        return node != None and node.isRed


class RedBlackTreeNode(bst.TreeNode):
    def __init__(self, key, value, isRed=False):
        super().__init__(key, value)
        self.isRed = isRed

    def __str__(self):
        return super().__str__() + "(" + ("red" if self.isRed else "black") + ")"


class TreeTest(unittest.TestCase):

    def test_random(self):
        tree = LLRBTree()
        with open('nums.txt', 'r') as f:
            lines = [line.strip('\n') for line in f.readlines()]

        for line in lines:
            tree.put(line, line)

        print(tree.size())
        self.isBlackRedTree(tree)

        # deleteMin
        for i in range(30):
            tree.deleteMin()
        print(tree.size())
        self.isBlackRedTree(tree)

        # delete
        # 刪除索引是3的倍数的
        # for index,line in enumerate(lines):
        #     if (index % 3 == 0):
        #         tree.delete(line)

        # print(tree.size())
        # self.isBlackRedTree(tree)

    def atest_test(self):
        tree = LLRBTree()
        self.assertEqual(tree.size(), 0)
        self.assertEqual(tree.deleteMin(), (False, None))

        tree.put(1, 'a')
        self.assertEqual(tree.size(), 1)
        tree.put(1, 'a')
        self.assertEqual(tree.size(), 1)
        tree.put(2, 'b')
        self.assertEqual(tree.size(), 2)
        self.assertEqual(tree.get(1), 'a')
        self.assertEqual(tree.get(2), 'b')
        self.assertEqual(tree.deleteMin(), (True, 'a'))
        self.assertEqual(tree.size(), 1)
        self.assertEqual(tree.delete(4), (False, None))
        self.assertEqual(tree.delete(2), (True, 'b'))
        self.assertEqual(tree.size(), 0)
        tree.put(20, 'a')
        tree.put(10, 'b')
        tree.put(30, 'c')
        tree.put(25, 'd')
        tree.put(35, 'e')
        self.assertEqual(tree.delete(30), (True, 'c'))
        self.assertEqual(tree.delete(25), (True, 'd'))
        self.assertTrue(self.isBlackRedTree(tree))

        # 10 b
        # 20 a
        # 25 d
        # 35 e
        tree.printNodes()

    def isBlackRedTree(self, tree):
        if (tree.root == None):
            return True
        if (tree.root.isRed):
            raise AssertionError("test")
        self.redLink(tree.root)
        self.down([tree.root])
        self.order(tree.root)

    def order(self, node):
        if node is None:
            return True
        if node.leftChild and node.leftChild.key > node.key:
            raise AssertionError('left child greater than parent')
        if node.rightChild and node.rightChild.key < node.key:
            raise AssertionError('right child less than parent')
        self.order(node.leftChild)
        self.order(node.rightChild)

    def down(self, nodes):
        # 判断是否存在
        exists = nodes[0].rightChild is not None

        allChilds = []
        for node in nodes:
            childs = self.getChilds(node)
            for child in childs:
                if (child is not None) != exists:
                    raise AssertionError('test')

            allChilds += childs
        if exists:
            self.down(allChilds)

    def getChilds(self, node):
        if not node.leftChild:
            return [node.rightChild]
        if node.leftChild.isRed:
            return [node.leftChild.leftChild, node.leftChild.rightChild, node.rightChild]
        else:
            return [node.leftChild, node.rightChild]

    def redLink(self, node):
        if self.isRed(node.leftChild) and self.hasChildRed(node.leftChild):
            raise AssertionError("test")
        if self.isRed(node.rightChild) and self.hasChildRed(node.rightChild):
            raise AssertionError("test")
        if self.isRed(node.leftChild) and self.isRed(node.rightChild):
            raise AssertionError("test")

    def isRed(self, node):
        return node and node.isRed

    def hasChildRed(self, node):
        return self.isRed(node.leftChild) or self.isRed(node.rightChild)


if __name__ == "__main__":
    # unittest.main()
    TreeTest().test_random()
