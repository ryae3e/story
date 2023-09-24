```python
import unittest
from app import create_app, db
from api.models import User, Entry

class TestModels(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_user_model(self):
        user = User(username='test', password='test')
        db.session.add(user)
        db.session.commit()
        self.assertIsNotNone(User.query.filter_by(username='test').first())

    def test_entry_model(self):
        user = User(username='test', password='test')
        db.session.add(user)
        db.session.commit()
        entry = Entry(user_id=user.id, text='test entry', date='2022-01-01')
        db.session.add(entry)
        db.session.commit()
        self.assertIsNotNone(Entry.query.filter_by(user_id=user.id).first())

if __name__ == '__main__':
    unittest.main()
```