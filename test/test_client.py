import unittest
from part1.toolbox.client import Client

class TestClient(unittest.TestCase):

    def test_init(self):
        # 创建一个Client实例
        client = Client(1, 'John Doe', 'johndoe@example.com', 10000)
        # 确认实例的属性被正确设置
        self.assertEqual(client.client_id, 1)
        self.assertEqual(client.name, 'John Doe')
        self.assertEqual(client.contact_info, 'johndoe@example.com')
        self.assertEqual(client.budget, 10000)

    def test_repr(self):
        # 创建一个Client实例
        client = Client(1, 'John Doe', 'johndoe@example.com', 10000)
        # 确认__repr__方法返回正确的字符串表示
        self.assertEqual(repr(client), "Client(1, 'John Doe', 'johndoe@example.com', 10000)")

    def test_init_with_valid_name(self):
    # 测试构造函数是否接受有效的名称
        client = Client(1, 'John Doe', 'johndoe@example.com', 10000)
        self.assertEqual(client.name, 'John Doe')


    def test_init_with_non_negative_budget(self):
    # 测试构造函数是否接受非负预算
       client = Client(1, 'John Doe', 'johndoe@example.com', 10000)
       self.assertGreaterEqual(client.budget, 0)


if __name__ == '__main__':
    unittest.main()
