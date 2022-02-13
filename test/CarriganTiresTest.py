import unittest
from engine.CarriganTires import CarriganTires


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        carrigan_tires = CarriganTires([0.9, 0, 1, 2])
        self.assertEqual(carrigan_tires.needs_service(), True)

    def test_does_not_need_service(self):
        carrigan_tires = CarriganTires([0, 1, 2, 3])
        self.assertEqual(carrigan_tires.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
