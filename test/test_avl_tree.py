import unittest
from part1.toolbox.avl_tree import AVLTree

class TestAVLTree(unittest.TestCase):

    def setUp(self):
        self.avl = AVLTree()

    def test_insert(self):
        self.avl.root = self.avl.insert(self.avl.root, 10, "value10")
        self.assertEqual(self.avl.root.key, 10)
        self.assertEqual(self.avl.root.value, "value10")

        self.avl.root = self.avl.insert(self.avl.root, 20, "value20")
        self.assertEqual(self.avl.root.right.key, 20)
        self.assertEqual(self.avl.root.right.value, "value20")

        self.avl.root = self.avl.insert(self.avl.root, 5, "value5")
        self.assertEqual(self.avl.root.left.key, 5)
        self.assertEqual(self.avl.root.left.value, "value5")

    def test_left_rotate(self):
        self.avl.root = self.avl.insert(self.avl.root, 10, "value10")
        self.avl.root = self.avl.insert(self.avl.root, 20, "value20")
        self.avl.root = self.avl.insert(self.avl.root, 30, "value30")
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.root.left.key, 10)
        self.assertEqual(self.avl.root.right.key, 30)

    def test_right_rotate(self):
        self.avl.root = self.avl.insert(self.avl.root, 30, "value30")
        self.avl.root = self.avl.insert(self.avl.root, 20, "value20")
        self.avl.root = self.avl.insert(self.avl.root, 10, "value10")
        self.assertEqual(self.avl.root.key, 20)
        self.assertEqual(self.avl.root.left.key, 10)
        self.assertEqual(self.avl.root.right.key, 30)

    def test_get_height(self):
        self.avl.root = self.avl.insert(self.avl.root, 10, "value10")
        self.avl.root = self.avl.insert(self.avl.root, 20, "value20")
        self.avl.root = self.avl.insert(self.avl.root, 30, "value30")
        self.assertEqual(self.avl.get_height(self.avl.root), 2)
        self.assertEqual(self.avl.get_height(self.avl.root.left), 1)
        self.assertEqual(self.avl.get_height(self.avl.root.right), 1)

    def test_get_balance(self):
        self.avl.root = self.avl.insert(self.avl.root, 10, "value10")
        self.avl.root = self.avl.insert(self.avl.root, 20, "value20")
        self.assertEqual(self.avl.get_balance(self.avl.root), -1)

        self.avl.root = self.avl.insert(self.avl.root, 5, "value5")
        self.assertEqual(self.avl.get_balance(self.avl.root), 0)

if __name__ == '__main__':
    unittest.main()
