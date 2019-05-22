class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST(object):

    def __init__(self, node_list):
        self.root = Node(node_list[0])
        for node in node_list[1:]:
            self.insert(node)

    def search(self, node, parent, value):
        if not node:
            return False, node, parent

        if node.val == value:
            return True, node, parent

        if node.val < value:
            return self.search(node.right, node, value)

        else:
            return self.search(node.left, node, value)

    def insert(self, value):
        flag, node, parent = self.search(self.root, self.root, value)
        if not flag:
            new_node = Node(value)
            if value > parent.val:
                parent.right = new_node
            else:
                parent.left = new_node

    def delete(self, value):
        flag, node, parent = self.search(self.root, self.root, value)
        if not flag:
            return -1

        else:
            if node.left and node.right:
                successor = node.right
                if not successor.left:
                    parent.right = successor
                    del node

                else:
                    precursor = successor.left
                    while precursor.left:
                        precursor = precursor.left
                    node.val = precursor.val
                    del precursor

            elif not node.left:
                if node == parent.left:
                    parent.left = node.right
                else:
                    parent.right = node.right
                del node

            elif not node.right:
                if node == parent.left:
                    parent.left = node.left
                else:
                    parent.right = node.left
                del node

            else:
                if node == parent.left:
                    parent.left = None
                else:
                    parent.right = None
                del node

    def preOrderTraverse(self, node):
        if not node:
            print(node.val)
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)

    def inOrderTraverse(self, node):
        if not node:
            self.preOrderTraverse(node.left)
            print(node.val)
            self.preOrderTraverse(node.right)

    def inOrderTraverse(self, node):
        if not node:
            self.preOrderTraverse(node.left)
            self.preOrderTraverse(node.right)
            print(node.val)
