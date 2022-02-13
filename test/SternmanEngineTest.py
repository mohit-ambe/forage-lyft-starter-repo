import unittest
from engine.SternmanEngine import SternmanEngine


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        sternman_engine = SternmanEngine(True)
        self.assertEqual(sternman_engine.needs_service(), True)

    def test_does_not_need_service(self):
        sternman_engine = SternmanEngine(False)
        self.assertEqual(sternman_engine.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
