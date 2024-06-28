import unittest
from realestate.toolbox.Queue import Queue
from realestate.toolbox.Client import Client
class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.clients = [
            Client(1, "Alice Johnson", "alice@example.com","HOUSE", 350000),
            Client(2, "Bob Miller", "bob@example.com", "APARTMENT",250000),
            Client(3, "Charlie Davis", "charlie@example.com", "COMMERCIAL",400000),
        ]

    def test_enqueue(self):
        for client in self.clients:
            self.queue.enqueue(client)
        self.assertEqual(self.queue.queue[0], self.clients[0])

    def test_dequeue(self):
        for client in self.clients:
            self.queue.enqueue(client)
        self.queue.dequeue()
        self.assertEqual(self.queue.queue[0], self.clients[1])

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        for client in self.clients:
            self.queue.enqueue(client)
        self.assertFalse(self.queue.is_empty())

# 运行测试
if __name__ == '__main__':
    unittest.main()