```python
import unittest
from flask import json
from backend.app import create_app, db

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client
        self.headers = {'Content-Type': 'application/json'}

    def test_upload_file(self):
        response = self.client().post('/api/upload', headers=self.headers, data=json.dumps({'filename': 'test.mp3'}))
        self.assertEqual(response.status_code, 200)

    def test_list_files(self):
        response = self.client().get('/api/files', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_get_file(self):
        response = self.client().get('/api/files/test.mp3', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_delete_file(self):
        response = self.client().delete('/api/files/test.mp3', headers=self.headers)
        self.assertEqual(response.status_code, 200)

    def test_transcribe_file(self):
        response = self.client().post('/api/transcribe', headers=self.headers, data=json.dumps({'filename': 'test.mp3'}))
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

if __name__ == "__main__":
    unittest.main()
```