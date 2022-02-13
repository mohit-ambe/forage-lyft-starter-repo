import unittest
from engine.SpindlerBattery import SpindlerBattery


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        spindler_battery = SpindlerBattery(10, 1000)
        self.assertEqual(spindler_battery.needs_service(), True)

    def test_does_not_need_service(self):
        spindler_battery = SpindlerBattery(10, 365)
        self.assertEqual(spindler_battery.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
