import unittest
from realestate.toolbox.AVLTree import AVLTree
from realestate.toolbox.Property import Property
from realestate.toolbox.PropertyType import PropertyType


# 测试AVL树
class TestAVLTree(unittest.TestCase):
    # 设置测试用例
    def setUp(self):
        # 创建一个AVL树实例
        self.tree = AVLTree()
        # 创建一个房产列表
        self.properties = [
            Property(1, "123 Main St", 250000, PropertyType.HOUSE),
            Property(2, "456 Maple Ave", 300000, PropertyType.APARTMENT),
            Property(3, "789 Oak Dr", 150000, PropertyType.LAND)
        ]

    # 测试插入操作
    def test_insert(self):
        # 循环遍历房产列表
        for prop in self.properties:
            # 在AVL树中插入每个房产
            self.tree.root = self.tree.insert(self.tree.root, prop.property_id, prop)
        # 检查AVL树根节点的值是否与房产列表中的第二个房产相匹配
        self.assertEqual(self.tree.root.value, self.properties[1])

    # 测试搜索操作
    def test_search(self):
        # 循环遍历房产列表
        for prop in self.properties:
            # 在AVL树中插入每个房产
            self.tree.root = self.tree.insert(self.tree.root, prop.property_id, prop)
        # 搜索第一个插入的房产
        self.assertEqual(self.tree.root.left.value, self.properties[0])

    # 测试删除操作
    def test_delete(self):
        # 循环遍历房产列表
        for prop in self.properties:
            # 在AVL树中插入每个房产
            self.tree.root = self.tree.insert(self.tree.root, prop.property_id, prop)
        # 从AVL树中删除第三个房产
        self.tree.root = self.tree.delete(self.tree.root, self.properties[2].property_id)
        # 检查AVL树根节点的值是否与房产列表中的第二个房产相匹配
        self.assertEqual(self.tree.root.value, self.properties[1])



# 运行测试
if __name__ == '__main__':
    unittest.main()