import time
import random

# Simulate performance benchmarking
def benchmark_cpu_performance():
    # Simulate CPU load benchmark
    cpu_load = random.randint(10, 100)
    print(f"Simulating CPU load: {cpu_load}%")
    time.sleep(1)
    return cpu_load

def benchmark_gpu_performance():
    # Simulate GPU load benchmark
    gpu_load = random.randint(10, 100)
    print(f"Simulating GPU load: {gpu_load}%")
    time.sleep(1)
    return gpu_load

def benchmark_ram_performance():
    # Simulate RAM load benchmark
    ram_load = random.randint(1, 16)  # Assuming system has 16GB RAM
    print(f"Simulating RAM load: {ram_load}GB")
    time.sleep(1)
    return ram_load

def benchmark_system():
    print("Starting performance benchmarks...\n")
    cpu_load = benchmark_cpu_performance()
    gpu_load = benchmark_gpu_performance()
    ram_load = benchmark_ram_performance()

    # Simulate a performance score based on loads
    performance_score = (cpu_load + gpu_load + ram_load) / 3
    print(f"\nSystem Performance Score: {performance_score:.2f}")

if __name__ == "__main__":
    benchmark_system()
