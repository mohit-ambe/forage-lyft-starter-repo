import unittest
from engine.OctoprimeTires import OctoprimeTires


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        octoprime_tires = OctoprimeTires([0, 1, 2, 3])
        self.assertEqual(octoprime_tires.needs_service(), True)

    def test_does_not_need_service(self):
        octoprime_tires = OctoprimeTires([0.9, 0, 0.1, 1])
        self.assertEqual(octoprime_tires.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
