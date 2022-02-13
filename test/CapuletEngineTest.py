import unittest
from engine.CapuletEngine import CapuletEngine


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        capulet_engine = CapuletEngine(20, 30300)
        self.assertEqual(capulet_engine.needs_service(), True)

    def test_does_not_need_service(self):
        capulet_engine = CapuletEngine(20, 21)
        self.assertEqual(capulet_engine.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
