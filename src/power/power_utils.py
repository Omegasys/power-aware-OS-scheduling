import time

class PowerEstimator:
    def __init__(self, cpu_usage, gpu_usage, ram_usage, battery_level):
        self.cpu_usage = cpu_usage
        self.gpu_usage = gpu_usage
        self.ram_usage = ram_usage
        self.battery_level = battery_level

    def estimate_power_consumption(self):
        """
        Estimate power consumption based on CPU, GPU, RAM usage, and battery level.
        This is a simplified approach and can be made more sophisticated with real power data.
        """
        # These factors would depend on the system hardware and real power consumption data
        cpu_power_factor = 0.02  # Example value: 2% power per 10% CPU usage
        gpu_power_factor = 0.03  # Example value: 3% power per 10% GPU usage
        ram_power_factor = 0.01  # Example value: 1% power per GB RAM usage

        power_consumption = (
            (self.cpu_usage * cpu_power_factor) +
            (self.gpu_usage * gpu_power_factor) +
            (self.ram_usage * ram_power_factor)
        )
        power_consumption *= (1 - self.battery_level * 0.01)  # Adjust for battery level

        print(f"Estimated Power Consumption: {power_consumption:.2f} W")
        return power_consumption

    def optimize_for_battery(self):
        """
        Estimate an optimal setting for saving power based on the current resource usage.
        """
        if self.battery_level < 20:
            # In a real case, you would adjust system components like CPU frequency, GPU, etc.
            print("Battery level low, optimizing for power saving!")
            return "Lowering CPU/GPU frequency"
        else:
            print("Battery level sufficient, running at full performance.")
            return "Running at full performance"

# Example usage
if __name__ == "__main__":
    power_estimator = PowerEstimator(cpu_usage=75, gpu_usage=50, ram_usage=4, battery_level=15)
    power_estimator.estimate_power_consumption()
    power_estimator.optimize_for_battery()
