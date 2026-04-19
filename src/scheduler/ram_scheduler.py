import time

class RAMScheduler:
    def __init__(self):
        # Initialize RAM scheduling parameters
        self.ram_usage = 0
        self.ram_size = 8  # in GB, just an example value

    def allocate(self, task):
        """
        Allocate RAM resources based on task requirements.
        """
        task_ram_usage = task.get_ram_usage()

        # Example allocation logic
        if task_ram_usage > 60:
            print("Allocating more RAM to task.")
        elif task_ram_usage < 20:
            print("Releasing RAM for task.")
        
        # Simulate RAM allocation by adjusting the usage
        self.ram_usage = task_ram_usage
        print(f"Allocating RAM with {self.ram_usage}GB usage of {self.ram_size}GB available.")

    def deallocate(self):
        """
        Free the RAM resources.
        """
        self.ram_usage = 0
        print("Deallocated RAM resources")

class Task:
    def __init__(self, ram_usage):
        self.ram_usage = ram_usage  # GB of RAM required by this task
    
    def get_ram_usage(self):
        return self.ram_usage

# Example usage
if __name__ == "__main__":
    ram_scheduler = RAMScheduler()
    task = Task(ram_usage=4)  # Task requiring 4GB RAM
    ram_scheduler.allocate(task)
    time.sleep(1)
    ram_scheduler.deallocate()
