import time
import algorithm.tree.bst as bst


class RedBlackTree(bst.BinarySearchTree):
    def put(self, key, value):
        addNode = self._insert(key, value)
        self._fixAfterInsert(addNode)

    def _insert(self, key, value):
        p = None
        c = self.root

        while c:
            if c.key == key:
                c.value = value
                return None
            elif c.key < key:
                p = c
                c = c.rightChild
            else:
                p = c
                c = c.leftChild
        
        addNode = RedBlackTreeNode(key, value, True, None)
        if not p:
            self.root = addNode
        elif p.key < key:
            p.rightChild = addNode
            addNode.parent = p
        else:
            p.leftChild = addNode
            addNode.parent = p

        self.n += 1
        return addNode

    def delete(self, key):
        delNode = self._delete(self.root, key)
        if delNode:
            self.n -= 1

    def _delete(self, node, key):
        if not node:
            return None

        # 2-node 转成 3/4-node
        if node.parent and self.is_2_node(node):
            if node.parent.leftChild == node:
                sib = node.parent.rightChild
                if sib.isRed:
                    # 说明这个元素和parent同一个节点，旋转，把父节点作为红色节点
                    node.parent.isRed = True
                    sib.isRed = False
                    self.leftRotate(node.parent)
                    sib = node.parent.rightChild

                if self.is_2_node(sib):
                    # 兄弟节点2-node，从父节点借一个键
                    sib.isRed = True
                    node.isRed = True
                    node.parent.isRed = False

                else:
                    # 兄弟节点非2-node，借一个键
                    if not self.isRed(sib.rightChild):
                        # 将兄弟节点的右键转成红色
                        sib.leftChild.isRed = False
                        sib.isRed = True
                        self.rightRotate(sib)
                        sib = node.parent.rightChild

                    sib.rightChild.isRed = False
                    sib.isRed = node.parent.isRed
                    node.parent.isRed = False
                    node.isRed = True
                    self.leftRotate(node.parent)
            else:
                # 对称
                sib = node.parent.leftChild
                if sib.isRed:
                    # 说明这个元素和parent同一个节点，旋转，把父节点作为红色节点
                    node.parent.isRed = True
                    sib.isRed = False
                    self.rightRotate(node.parent)
                    sib = node.parent.leftChild

                if self.is_2_node(sib):
                    # 兄弟节点2-node，从父节点借一个键
                    sib.isRed = True
                    node.isRed = True
                    node.parent.isRed = False

                else:
                    # 兄弟节点非2-node，借一个键
                    if not self.isRed(sib.leftChild):
                        # 将兄弟节点的右键转成红色
                        sib.rightChild.isRed = False
                        sib.isRed = True
                        self.leftRotate(sib)
                        sib = node.parent.leftChild

                    sib.leftChild.isRed = False
                    sib.isRed = node.parent.isRed
                    node.parent.isRed = False
                    node.isRed = True
                    self.rightRotate(node.parent)

        # 刪除
        if node.key == key:
            s = self.successor(node)
            if not s:
                # not have successor
                if node.leftChild:
                    node.leftChild.isRed = False
                    node.leftChild.parent = node.parent
                if not node.parent:
                    self.root = node.leftChild
                elif node.parent.leftChild == node:
                    node.parent.leftChild = node.leftChild
                else:
                    node.parent.rightChild = node.leftChild

                node.leftChild = None
                node.parent = None
                return node

            else:
                # have successor
                node.key, s.key = s.key, node.key
                node.value, s.value = s.value, node.value
                delNode = self._delete(node.rightChild, key)
                return delNode


        elif node.key < key:
            delNode = self._delete(node.rightChild, key)
        else:
            delNode = self._delete(node.leftChild, key)

        return delNode

    def is_leaf(self, node):
        return not node.leftChild or (node.leftChild.isRed and not node.leftChild.rightChild and node.leftChild.rightChild)

    def is_2_node(self, node):
        return not node.isRed and not self.isRed(node.leftChild) and not self.isRed(node.rightChild)

    def successor(self, node):
        if not node:
            return None
        if not node.rightChild:
            return None
        p = node.rightChild
        while p.leftChild:
            p = p.leftChild
        return p


    def _fixAfterInsert(self, node):
        while node and node.parent and node.parent.isRed:
            p = node.parent
            if p.parent.leftChild == p:
                # 父节点是左节点
                if self.isRed(self.rightOf(p.parent)):
                    p.parent.isRed = True
                    p.parent.rightChild.isRed = False
                    p.isRed = False
                    node = p.parent
                else:
                    if p.rightChild == node:
                        node = p
                        self.leftRotate(node)
                    node.parent.isRed = False
                    node.parent.parent.isRed = True
                    self.rightRotate(node.parent.parent)
            else:
                if self.isRed(self.leftOf(p.parent)):
                    p.parent.isRed = True
                    p.parent.leftChild.isRed = False
                    p.isRed = False
                    node = p.parent
                else:
                    if p.leftChild == node:
                        node = p
                        self.rightRotate(node)
                    node.parent.isRed = False
                    node.parent.parent.isRed = True
                    self.leftRotate(node.parent.parent)

        self.root.isRed = False

    def isRed(self, node):
        return node and node.isRed

    def rightOf(self, node):
        if node and node.rightChild:
            return node.rightChild

    def leftOf(self, node):
        if node and node.leftChild:
            return node.leftChild

    def rightRotate(self, node):
        if node:
            # 设置孩子节点
            l = node.leftChild
            node.leftChild = l.rightChild
            if node.leftChild:
                node.leftChild.parent = node
            l.rightChild = node
            # 设置父节点
            if not node.parent:
                self.root = l
            elif node.parent.rightChild == node:
                node.parent.rightChild = l
            else:
                node.parent.leftChild = l
            l.parent = node.parent
            node.parent = l

    def leftRotate(self, node):
        if node:
            # 设置孩子节点
            r = node.rightChild
            node.rightChild = r.leftChild
            if node.rightChild:
                node.rightChild.parent = node
            r.leftChild = node

            # 设置父节点
            if not node.parent:
                self.root = r
            elif node.parent.leftChild == node:
                node.parent.leftChild = r
            else:
                node.parent.rightChild = r
            r.parent = node.parent
            node.parent = r

    def check(self):
        assert not self.root or not self.root.isRed
        self.check_black_height()
        self.check_order()
        self.check_parent()

    def check_parent(self):
        self._check_parent(self.root)

    def _check_parent(self, node):
        if node:
            assert not node.leftChild or node.leftChild.parent == node
            assert not node.rightChild or node.rightChild.parent == node
            self._check_parent(node.leftChild)
            self._check_parent(node.rightChild)

    def check_black_height(self):
        self.root and self._check_black_height([self.root])

    def _check_black_height(self, nodes):
        # 判断是否存在
        exists = self.getChilds(nodes[0])[0] is not None

        allChilds = []
        for node in nodes:
            childs = self.getChilds(node)
            for child in childs:
                if (child is not None) != exists:
                    raise AssertionError('black height')

            allChilds += childs
        if exists:
            self._check_black_height(allChilds)

    def getChilds(self, node):
        children = []
        if node.leftChild and node.leftChild.isRed:
            children.append(node.leftChild.leftChild)
            children.append(node.leftChild.rightChild)
        else:
            children.append(node.leftChild)

        if node.rightChild and node.rightChild.isRed:
            children.append(node.rightChild.leftChild)
            children.append(node.rightChild.rightChild)
        else:
            children.append(node.rightChild)

        return children

class RedBlackTreeNode(bst.TreeNode):
    def __init__(self, key, value, isRed, parent):
        super().__init__(key, value)
        self.isRed = isRed
        self.parent = parent

    def __str__(self):
        return super().__str__() + "(" + ("red" if self.isRed else "black") + ")"


def test(path):
    tree = RedBlackTree()

    with open(path, 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]
    for line in lines:
        tree.put(line, line)
        tree.put(line, line)

    tree.check()

    # delete
    for i, line in enumerate(lines):
        if i % 3 == 0:
            tree.delete(line)

    tree.check()


def testMap(path):
    m = {}
    with open(path, 'r') as f:
        lines = [line.strip('\n') for line in f.readlines()]
    for line in lines:
        m[line] = line
        m[line] = line

    print(len(m))
    for i, line in enumerate(lines):
        if i % 3 == 0:
            del m[line]
    print(len(m))


def buildTree():
    # 构建一个测试树，刪除10节点
    tree = RedBlackTree()
    tree.n = 21

    tree.root = node8 = RedBlackTreeNode(8, None, False, None)
    node8.leftChild = node4 = RedBlackTreeNode(4, None, False, node8)
    node8.rightChild = node12 = RedBlackTreeNode(12, None, False, node8)
    node4.leftChild = node2 = RedBlackTreeNode(2, None, False, node4)
    node4.rightChild = node6 = RedBlackTreeNode(6, None, False, node4)
    node2.leftChild = node1 = RedBlackTreeNode(1, None, False, node2)
    node2.rightChild = node3 = RedBlackTreeNode(3, None, False, node2)
    node6.leftChild = node5 = RedBlackTreeNode(5, None, False, node6)
    node6.rightChild = node7 = RedBlackTreeNode(7, None, False, node6)

    node12.leftChild = node10 = RedBlackTreeNode(10, None, False, node12)
    node12.rightChild = node16 = RedBlackTreeNode(16, None, True, node12)

    node10.leftChild = node9 = RedBlackTreeNode(9, None, False, node10)
    node10.rightChild = node11 = RedBlackTreeNode(11, None, False, node10)

    node16.leftChild = node14 = RedBlackTreeNode(14, None, False, node16)
    node16.rightChild = node20 = RedBlackTreeNode(20, None, False, node16)

    node14.leftChild = node13 = RedBlackTreeNode(13, None, False, node14)
    node14.rightChild = node15 = RedBlackTreeNode(15, None, False, node14)

    node20.leftChild = node18 = RedBlackTreeNode(18, None, True, node20)
    node20.rightChild = node21 = RedBlackTreeNode(21, None, False, node20)

    node18.leftChild = node17 = RedBlackTreeNode(17, None, False, node18)
    node18.rightChild = node19 = RedBlackTreeNode(19, None, False, node18)
    return tree


if __name__ == "__main__":
    begin = time.time()
    for i in range(10):
        tree = RedBlackTree()

        for i in range(10000):
            tree.put(i, i)
            tree.put(i, i)
        print(tree.size())
        # delete
        # for i in range(10000):
        #     if i % 3 == 0:
        #         tree.delete(i)
        # test('../../nums10000.txt')
        # testMap('../../nums10000.txt')
    end = time.time()

    print (end - begin)
    # test('../../nums100.txt')
    # tree = buildTree()
    # print(tree.size())
    # tree.check()
    # tree.delete(14)
    # print(tree.size())
    # tree.check()

