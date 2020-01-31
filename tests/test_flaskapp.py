import unittest
import json

from main import app


class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_unauthorized(self):
        response = self.app.get('/authorized')
        # Check if the request fails with authorization error
        self.assertEqual(response._status_code,401,'Unauthorized access to page without login')

    def test_multiply(self):
        response = self.app.get('/multiply?x=5&y=7')
        resp = json.loads(response.data.decode())
        self.assertEqual(resp['answer'],35,'Multiply endpoint failed known answer 7*5 = 35')

    # TODO DEFINE TWO MORE TESTS ON THE END POINTS
    def test_touppercase(self):
        response = self.app.get('/touppercase?s=hello')
        resp = response.data.decode()
        self.assertEqual(resp, 'HELLO', 'Failed to get uppercase of hello')

    def test_app(self):
        response = self.app.get('/')
        resp = response.data.decode()
        self.assertEqual(resp, 'Hello World!', 'Failed to return hello world')

if __name__ == '__main__':
    unittest.main()
