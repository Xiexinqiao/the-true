import unittest
from realestate.toolbox.Client import Client
from realestate.toolbox.Queue import Queue
import unittest

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.clients = [
            Client(1, "Alice Johnson", "alice@example.com","HOUSE", 350000),
            Client(2, "Bob Miller", "bob@example.com", "APARTMENT",250000),
        ]

def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        for client in self.clients:
            self.queue.enqueue(client)
        self.assertFalse(self.queue.is_empty())