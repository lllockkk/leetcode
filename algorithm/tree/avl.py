import algorithm.tree.bst as bst


class AVLTree (bst.BinarySearchTree):

    def _put(self, node, key, value):
        if node is None:
            addNode = AVLTreeNode(key, value, 1)
            return addNode, addNode
        if (node.key == key):
            node.value = value
            return node, None
        if node.key < key:
            node.rightChild, addNode = self._put(node.rightChild, key, value)
        else:
            node.leftChild, addNode = self._put(node.leftChild, key, value)

        if addNode:
            # 如果添加成功
            node = self.balance(node)
        return node, addNode

    def _deleteMin(self, node):
        node, delNode = super()._deleteMin(node)
        if delNode:
            node = self.balance(node)
        return node, delNode

    def _delete(self, node, key):
        node, delNode = super()._delete(node, key)
        if delNode:
            node = self.balance(node)
        return node, delNode

    def rotateLeft(self, node):
        r = node.rightChild
        node.rightChild = r.leftChild
        r.leftChild = node
        self.setHeight(node)
        self.setHeight(r)
        return r

    def rotateRight(self, node):
        l = node.leftChild
        node.leftChild = l.rightChild
        l.rightChild = node
        self.setHeight(node)
        self.setHeight(l)
        return l

    def balance(self, node):
        if not node:
            return node
        # 先矫正高度，然后根据高度判断是否需要旋转
        self.setHeight(node)
        diff = self.getHeight(node.leftChild) - self.getHeight(node.rightChild)
        if diff == 2:  # 左子树高
            if self.getHeight(node.leftChild.rightChild) > self.getHeight(node.leftChild.leftChild):
                # 如果是内测高，需要多一次左旋
                node.leftChild = self.rotateLeft(node.leftChild)
            node = self.rotateRight(node)
        if diff == -2:  # 右子树高
            if self.getHeight(node.rightChild.leftChild) > self.getHeight(node.rightChild.rightChild):
                node.rightChild = self.rotateRight(node.rightChild)
            node = self.rotateLeft(node)
        return node

    def setHeight(self, node):
        node.height = max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1

    def getHeight(self, node):
        return node.height if node else 0

    def is_balance(self):
        self._is_balance(self.root)

    def _is_balance(self, node):
        if not node:
            return True

        if not node.height == max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1:
            return False

        return self._is_balance(node.leftChild) and self._is_balance(node.rightChild)

    def check(self):
        self.check_balance()
        self.check_order()

    def check_balance(self):
        self._check_balance(self.root)

    def _check_balance(self, node):
        if not node:
            return

        assert node.height == max(self.getHeight(node.leftChild), self.getHeight(node.rightChild)) + 1
        self._check_balance(node.leftChild)
        self._check_balance(node.rightChild)

class AVLTreeNode(bst.TreeNode):
    def __init__(self, key, value, height):
        super().__init__(key, value)
        self.height = height


if __name__ == "__main__":
    tree = AVLTree()

    with open('../../nums.txt', 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]
    for line in lines:
        tree.put(line, line)
        tree.put(line, line)

    addCount = 10000
    deleteCount = 30

    assert tree.size() == addCount
    tree.check()

    # deleteMin
    for i in range(deleteCount):
        tree.deleteMin()
    assert tree.size() == addCount - deleteCount
    tree.check()

    # delete
    for i, line in enumerate(lines):
        if i % 3:
            tree.delete(line)

    print(tree.size())
    tree.check()





