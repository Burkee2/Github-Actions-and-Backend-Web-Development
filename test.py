import unittest
from app import app

class TestApp(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)

    def test_home_page_with_gif(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Home Page', response.data)
        self.assertIn(b'epic skyrim gif', response.data)  # Check for alt text

    def test_page1(self):
        response = self.app.get('/page1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Page 1', response.data)

    def test_page2(self):
        response = self.app.get('/page2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Page 2', response.data)

if __name__ == '__main__':
    unittest.main()
