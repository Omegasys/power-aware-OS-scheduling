import time

class GPUScheduler:
    def __init__(self):
        # Initialize GPU scheduling parameters
        self.gpu_usage = 0
        self.gpu_clock_speed = 1500  # in MHz, just an example value

    def allocate(self, task):
        """
        Allocate GPU resources based on task needs.
        """
        task_gpu_usage = task.get_gpu_usage()

        # Example allocation logic
        if task_gpu_usage > 70:
            self.gpu_clock_speed = 1800  # Boost GPU clock for high-demand tasks
        elif task_gpu_usage < 30:
            self.gpu_clock_speed = 1200  # Reduce GPU clock for light tasks

        # Simulate GPU allocation by adjusting the usage
        self.gpu_usage = task_gpu_usage
        print(f"Allocating GPU with {self.gpu_usage}% usage at {self.gpu_clock_speed}MHz")

    def deallocate(self):
        """
        Free GPU resources.
        """
        self.gpu_usage = 0
        print("Deallocated GPU resources")

class Task:
    def __init__(self, gpu_usage):
        self.gpu_usage = gpu_usage  # % GPU usage this task requires
    
    def get_gpu_usage(self):
        return self.gpu_usage

# Example usage
if __name__ == "__main__":
    gpu_scheduler = GPUScheduler()
    task = Task(gpu_usage=85)  # Task requiring 85% GPU usage
    gpu_scheduler.allocate(task)
    time.sleep(1)
    gpu_scheduler.deallocate()
