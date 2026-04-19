import time

class CPUScheduler:
    def __init__(self):
        # Initialize CPU scheduling parameters
        self.cpu_usage = 0
        self.cpu_frequency = 2.5  # in GHz, just an example value

    def allocate(self, task):
        """
        Allocate CPU resources based on task priority and need.
        """
        task_cpu_usage = task.get_cpu_usage()

        # Example allocation logic
        if task_cpu_usage > 80:
            self.cpu_frequency = 3.0  # Increase CPU frequency for high-demand tasks
        elif task_cpu_usage < 20:
            self.cpu_frequency = 2.0  # Decrease CPU frequency for light tasks

        # Simulate CPU allocation by adjusting the usage
        self.cpu_usage = task_cpu_usage
        print(f"Allocating CPU with {self.cpu_usage}% usage at {self.cpu_frequency}GHz")

    def deallocate(self):
        """
        Free the CPU resources.
        """
        self.cpu_usage = 0
        print("Deallocated CPU resources")

class Task:
    def __init__(self, cpu_usage):
        self.cpu_usage = cpu_usage  # % CPU usage this task requires
    
    def get_cpu_usage(self):
        return self.cpu_usage

# Example usage
if __name__ == "__main__":
    cpu_scheduler = CPUScheduler()
    task = Task(cpu_usage=75)  # Task requiring 75% CPU usage
    cpu_scheduler.allocate(task)
    time.sleep(1)
    cpu_scheduler.deallocate()
