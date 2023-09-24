```python
import os
import unittest
from flask import current_app
from backend.app import create_app, db
from backend.api.file_management import save_file, get_file, delete_file

class TestFileManagement(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_save_file(self):
        with self.app.test_request_context():
            response = save_file('test.mp3', 'audio/mpeg')
            self.assertEqual(response.status_code, 201)

    def test_get_file(self):
        with self.app.test_request_context():
            save_file('test.mp3', 'audio/mpeg')
            response = get_file('test.mp3')
            self.assertEqual(response.status_code, 200)

    def test_delete_file(self):
        with self.app.test_request_context():
            save_file('test.mp3', 'audio/mpeg')
            response = delete_file('test.mp3')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
```