from binaryTree import TreeNode
from binaryTree import is_bst
import unittest

class BinaryTreeValidationTest(unittest.TestCase):

    def test_validBinaryTreeIsValid(self):

        root = TreeNode(5)
        root.left = TreeNode(3)
        root.right = TreeNode(7)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(4)
        root.right.left = TreeNode(6)

        self.assertTrue(is_bst(root))

    def test_emptyTree(self):
        self.assertTrue(is_bst(None))

    def test_invalidTreeIsNotBST(self):

        root = TreeNode(20)
        root.left = TreeNode(10)
        root.right = TreeNode(30)
        root.right.left = TreeNode(5)
        root.right.right = TreeNode(40)

        self.assertFalse(is_bst(root))


if __name__ == '__main__':
    unittest.main()