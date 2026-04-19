import psutil  # psutil is a Python library for system and process utilities, used for battery monitoring.

class BatteryManager:
    def __init__(self):
        # Initialize battery manager parameters
        self.battery = psutil.sensors_battery()
        self.is_plugged = self.battery.power_plugged
        self.percent = self.battery.percent

    def get_battery_status(self):
        """
        Get the current battery status.
        """
        return {
            'percentage': self.percent,
            'plugged_in': self.is_plugged,
            'time_left': self.battery.secsleft // 60 if self.is_plugged else self.battery.secsleft // 60
        }

    def estimate_remaining_time(self):
        """
        Estimate remaining time on battery.
        Returns the time left in minutes.
        """
        if not self.is_plugged:
            time_left = self.battery.secsleft // 60
            print(f"Battery remaining time: {time_left} minutes.")
            return time_left
        return None  # Battery is plugged in, no estimate needed

    def is_battery_low(self, threshold=20):
        """
        Check if battery is below a specified threshold.
        """
        return self.percent < threshold

    def handle_low_battery(self):
        """
        Handle low battery scenarios by adjusting system behavior.
        E.g., lowering CPU/GPU frequencies, switching to battery saving modes, etc.
        """
        if self.is_battery_low():
            print("Battery is low! Switching to power-saving mode.")
            # Here you could call your kernel to adjust power settings, lower CPU frequency, etc.
        else:
            print("Battery level is sufficient.")

# Example usage
if __name__ == "__main__":
    battery_manager = BatteryManager()
    print(battery_manager.get_battery_status())
    battery_manager.estimate_remaining_time()
    battery_manager.handle_low_battery()
