import unittest
import os

import models


class TodoTest(unittest.TestCase):
    def setUp(self):
        self.name = 'Test Todo App'
        models.Todo.create(name=self.name)

    def test_db_initialize(self):
        models.initialize()
        self.assertTrue(os.path.isfile('todo.db'))

    def test_add_todo(self):
        self.assertEqual(models.Todo.name, self.name)

if __name__ == '__main__':
    unittest.main()