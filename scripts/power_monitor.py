import time
from src.power.battery import BatteryManager
from src.power.power_utils import PowerEstimator

def monitor_battery():
    # Create a BatteryManager instance
    battery_manager = BatteryManager()

    # Monitor battery status
    while True:
        status = battery_manager.get_battery_status()
        print(f"\nBattery Status: {status}")
        if battery_manager.is_battery_low():
            print("Warning: Battery level is low!")

        time.sleep(5)  # Sleep for 5 seconds before checking again

def monitor_power_consumption():
    # Simulate power consumption monitoring based on CPU, GPU, and RAM usage
    cpu_usage = 50  # Example values (could use actual monitoring data)
    gpu_usage = 60
    ram_usage = 4  # GB
    battery_level = 75  # Example battery level

    power_estimator = PowerEstimator(cpu_usage, gpu_usage, ram_usage, battery_level)
    power_estimator.estimate_power_consumption()
    
    # Monitor and optimize power for battery saving
    print(power_estimator.optimize_for_battery())

if __name__ == "__main__":
    print("Starting Power Monitor...\n")
    monitor_battery()
    # Uncomment the next line to monitor power consumption
    # monitor_power_consumption()
