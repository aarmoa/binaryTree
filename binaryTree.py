class TreeNode:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    result = False
    min = float('-inf')
    max = float('inf')

    return is_bst_recursive(root, min, max)

def is_bst_recursive(root, min, max):

    result = False

    result = root == None or (
            isRootKeyValid(root, min, max) and \
            is_bst_recursive(root.left, min, root.key-1) and \
            is_bst_recursive(root.right, root.key + 1, max))

    return result

def isRootKeyValid(root, min, max):
    return root.key >= min and root.key <= max


