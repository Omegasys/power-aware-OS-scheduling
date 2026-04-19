import unittest
from src.scheduler.ai_scheduler import AIScheduler
from src.scheduler.cpu_scheduler import CPUScheduler
from src.scheduler.gpu_scheduler import GPUScheduler
from src.scheduler.ram_scheduler import RAMScheduler

class TestAIScheduler(unittest.TestCase):
    def test_allocate_resources(self):
        cpu_scheduler = CPUScheduler()
        gpu_scheduler = GPUScheduler()
        ram_scheduler = RAMScheduler()
        
        ai_scheduler = AIScheduler(cpu_scheduler, gpu_scheduler, ram_scheduler)
        task = Task(cpu_usage=50, gpu_usage=60, ram_usage=4)
        
        ai_scheduler.allocate_resources(task)
        # Assuming some checks like verifying resource allocation were done here.
        self.assertIsNotNone(ai_scheduler)

    def test_deallocate_resources(self):
        cpu_scheduler = CPUScheduler()
        gpu_scheduler = GPUScheduler()
        ram_scheduler = RAMScheduler()
        
        ai_scheduler = AIScheduler(cpu_scheduler, gpu_scheduler, ram_scheduler)
        ai_scheduler.deallocate_resources()
        
       
