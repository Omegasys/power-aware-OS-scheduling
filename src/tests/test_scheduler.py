import unittest
from src.scheduler.cpu_scheduler import CPUScheduler, Task

class TestCPUScheduler(unittest.TestCase):
    def test_allocate_cpu(self):
        cpu_scheduler = CPUScheduler()
        task = Task(cpu_usage=60)
        cpu_scheduler.allocate(task)
        self.assertEqual(cpu_scheduler.cpu_usage, 60)
    
    def test_deallocate_cpu(self):
        cpu_scheduler = CPUScheduler()
        cpu_scheduler.deallocate()
        self.assertEqual(cpu_scheduler.cpu_usage, 0)

if __name__ == "__main__":
    unittest.main()
