import unittest
from src.power.battery import BatteryManager
from src.power.power_utils import PowerEstimator

class TestBatteryManager(unittest.TestCase):
    def test_battery_status(self):
        battery_manager = BatteryManager()
        status = battery_manager.get_battery_status()
        self.assertTrue('percentage' in status)
        self.assertTrue('plugged_in' in status)
        self.assertTrue('time_left' in status)

    def test_estimate_remaining_time(self):
        battery_manager = BatteryManager()
        time_left = battery_manager.estimate_remaining_time()
        self.assertIsInstance(time_left, int)

class TestPowerEstimator(unittest.TestCase):
    def test_estimate_power_consumption(self):
        power_estimator = PowerEstimator(cpu_usage=50, gpu_usage=60, ram_usage=4, battery_level=75)
        power = power_estimator.estimate_power_consumption()
        self.assertGreater(power, 0)

if __name__ == "__main__":
    unittest.main()
