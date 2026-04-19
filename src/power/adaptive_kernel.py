import random

class AdaptivePowerKernel:
    def __init__(self):
        # Initializing the kernel layer with default power management states
        self.kernel_state = "Normal"
        self.cpu_frequency = 2.5  # GHz, for example
        self.gpu_clock = 1500  # MHz, for example
        self.is_battery_saving = False

    def adjust_kernel_state(self, battery_level, system_activity):
        """
        Adjust the system power state based on battery level and system activity.
        """
        if battery_level < 20:
            self.is_battery_saving = True
            self.kernel_state = "Power Saving"
            self.cpu_frequency = 1.2  # Reduce CPU frequency for power saving
            self.gpu_clock = 800  # Reduce GPU clock
            print("Battery is low. Switching to power-saving mode.")
        else:
            self.is_battery_saving = False
            self.kernel_state = "Normal"
            self.cpu_frequency = 2.5  # Normal frequency
            self.gpu_clock = 1500  # Normal GPU clock
            print("Battery level is sufficient. Running at normal performance.")

        # Simulate a change in system activity
        if system_activity == "High":
            print("High system activity detected. Allocating more resources.")
            self.cpu_frequency = 3.0  # Boost CPU frequency during high activity
        elif system_activity == "Low":
            print("Low system activity detected. Lowering resource usage.")
            self.cpu_frequency = 2.0  # Lower CPU frequency during low activity

        print(f"Kernel state: {self.kernel_state}")
        print(f"CPU Frequency: {self.cpu_frequency} GHz")
        print(f"GPU Clock: {self.gpu_clock} MHz")

# Example usage
if __name__ == "__main__":
    adaptive_kernel = AdaptivePowerKernel()
    battery_level = random.randint(10, 100)  # Simulating battery level
    system_activity = random.choice(["High", "Low"])

    adaptive_kernel.adjust_kernel_state(battery_level, system_activity)
