# 非平衡二叉查找树
class BinarySearchTree:
    '''
    测试用例
    >>> tree = BinarySearchTree()
    >>> tree.size()
    0
    >>> tree.deleteMin()
    (False, None)
    >>> tree.put(1, 'a')
    >>> tree.size()
    1
    >>> tree.put(1, 'a')
    >>> tree.size()
    1
    >>> tree.put(2, 'b')
    >>> tree.size()
    2
    >>> tree.get(1)
    'a'
    >>> tree.get(2)
    'b'
    >>> tree.deleteMin()
    (True, 'a')
    >>> tree.size()
    1
    >>> tree.delete(4)
    (False, None)
    >>> tree.delete(2)
    (True, 'b')
    >>> tree.size()
    0
    >>> tree.put(20, 'a')
    >>> tree.put(10, 'b')
    >>> tree.put(30, 'c')
    >>> tree.put(25, 'd')
    >>> tree.put(35, 'e')
    >>> tree.delete(30)
    (True, 'c')
    >>> tree.printNodes()
    10: b
    20: a
    25: d
    35: e
    '''
    
    def __init__(self):
        self.n = 0
        self.root = None
        
    def put(self, key, value):
        self.root, addNode =self._put(self.root, key, value)
        if (addNode != None):
            self.n = self.n + 1

    def _put(self, node, key, value): 
        if(node == None):
            addNode = TreeNode(key, value)
            return addNode, addNode
        if (node.key == key):
            node.value = value
            return node, None
        if (node.key > key):
            node.leftChild, addNode = self._put(node.leftChild, key, value)
        else:
            node.rightChild, addNode = self._put(node.rightChild, key, value)
        return node, addNode

    def size(self):
        return self.n

    def get(self, key):
        return self._get(self.root, key)

    def _get(self, node, key):
        if (node == None): 
            return None
        if (node.key == key):
            return node.value
        cnode = node.leftChild if key < node.key else node.rightChild
        return self._get(cnode, key)

    def deleteMin(self):
        self.root, delNode = self._deleteMin(self.root)
        if (delNode == None):
            return False, None
        self.n = self.n - 1
        return True,delNode.value

    def _deleteMin(self, node):
        if (node == None):
            return None,None
        if (node.leftChild == None):
            return node.rightChild, node
        node.leftChild, delNode = self._deleteMin(node.leftChild)
        return node, delNode

    def delete(self, key):
        self.root, delNode = self._delete(self.root, key)
        if (delNode == None):
            return False, None
        self.n = self.n - 1
        return True,delNode.value

    def _delete(self, node, key):
        if (node == None):
            return None, None
        if (node.key == key):
            if (node.leftChild == None):
                return node.rightChild, node
            if (node.rightChild == None):
                return node.leftChild, node
            rightChild, minNode = self._deleteMin(node.rightChild)
            minNode.leftChild = node.leftChild
            minNode.rightChild = rightChild
            node.leftChild = node.rightChild = None
            return minNode, node

        if (node.key < key):
            node.rightChild, delNode = self._delete(node.rightChild, key)
        else:
            node.leftChild, delNode = self._delete(node.leftChild, key)
        return node, delNode

    def printNodes(self):
        self._printNodes(self.root)

    def _printNodes(self, node):
        if (node == None):
            return
        if (node.leftChild != None):
            self._printNodes(node.leftChild)
        print(node)
        if (node.rightChild != None):
            self._printNodes(node.rightChild)

    def check_order(self):
        self._check_order(self.root)

    def _check_order(self, node):
        if node is None:
            return True
        if node.leftChild and node.leftChild.key > node.key:
          raise AssertionError('left child greater than parent')
        if node.rightChild and node.rightChild.key < node.key:
           raise AssertionError('right child less than parent')
        self._check_order(node.leftChild)
        self._check_order(node.rightChild)


class TreeNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.leftChild = None
        self.rightChild = None
    
    def __str__(self):
        return str(self.key) + ": " + str(self.value)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    

        

