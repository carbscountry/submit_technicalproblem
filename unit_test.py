import unittest
from app import app, fibonacci

class TestFibonacciAPI(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_fibonacci_function(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)

    def test_api_response(self):
        response = self.app.get('/fib?n=5')
        data = response.get_json()
        self.assertEqual(data["result"], 5)

    def test_api_bad_request(self):
        response = self.app.get('/fib?n=-1')
        data = response.get_json()
        self.assertEqual(data["status"], 400)
        self.assertEqual(data["message"], "Bad request.")

if __name__ == "__main__":
    unittest.main()
