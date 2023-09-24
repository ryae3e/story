```python
import unittest
from backend.api.auth import generate_token, verify_token

class TestAuth(unittest.TestCase):

    def setUp(self):
        self.token = generate_token()

    def test_token_generation(self):
        self.assertIsNotNone(self.token, "Token generation failed")

    def test_token_verification(self):
        self.assertTrue(verify_token(self.token), "Token verification failed")

    def test_invalid_token_verification(self):
        self.assertFalse(verify_token("invalid_token"), "Invalid token verification failed")

if __name__ == '__main__':
    unittest.main()
```