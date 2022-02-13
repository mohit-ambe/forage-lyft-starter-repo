import unittest
from engine.WilloughbyEngine import WilloughbyEngine


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        willoughby_engine = WilloughbyEngine(20, 60300)
        self.assertEqual(willoughby_engine.needs_service(), True)

    def test_does_not_need_service(self):
        willoughby_engine = WilloughbyEngine(20, 21)
        self.assertEqual(willoughby_engine.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
