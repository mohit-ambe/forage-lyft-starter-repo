import unittest
from engine.NubbinBattery import NubbinBattery


class MyTestCase(unittest.TestCase):
    def test_needs_service(self):
        nubbin_battery = NubbinBattery(10, 2000)
        self.assertEqual(nubbin_battery.needs_service(), True)

    def test_does_not_need_service(self):
        nubbin_battery = NubbinBattery(10, 365)
        self.assertEqual(nubbin_battery.needs_service(), False)


if __name__ == '__main__':
    unittest.main()
