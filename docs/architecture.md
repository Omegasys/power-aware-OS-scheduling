# System Architecture of Power-Aware OS Scheduling

This document explains the high-level architecture of the Power-Aware OS Scheduling project, which focuses on efficient resource scheduling using AI-assisted methods and adaptive power management techniques. The goal of this system is to optimize resource allocation across CPU, GPU, RAM, and battery, ensuring better power efficiency without compromising performance.

## Overview

The architecture is designed around a modular structure, consisting of multiple components that interact to dynamically schedule and manage system resources based on the current workload and available power.

### Key Components:
1. **Scheduler Layer**: This layer handles the resource scheduling for CPU, GPU, and RAM, ensuring that these components are efficiently allocated based on the current system state and power constraints.
2. **AI-Assisted Scheduler**: A machine learning-based scheduler that dynamically adjusts resource allocation based on historical performance data and predicted power consumption.
3. **Adaptive Power Kernel Layer**: This layer adapts the system's power management strategies by optimizing battery usage and regulating power states based on real-time system activity.
4. **Battery and Power Monitoring**: Continuous monitoring of battery life and power consumption, providing feedback to the scheduler and kernel for better decision-making.

## High-Level Flow

1. **System Monitoring**: The system continuously monitors CPU, GPU, RAM, and battery utilization. It also tracks the power consumption of these components.
2. **AI-based Predictions**: Using historical data and AI models, the system predicts the future workload and power needs of each component.
3. **Resource Allocation**: The AI-assisted scheduler allocates resources (CPU, GPU, RAM) based on predicted needs while considering power constraints. This allocation may change dynamically based on workload spikes or drops.
4. **Power Efficiency Adjustment**: The adaptive kernel layer adjusts the system’s power states (such as CPU frequency scaling, GPU throttling, and RAM power management) to ensure minimal energy usage while maintaining system performance.

### Future Improvements

The architecture can evolve to include more advanced AI models, additional power management techniques (e.g., dynamic voltage scaling), and better integration with hardware components. Future work could focus on refining power prediction models and enhancing the kernel layer for even more precise adaptive power management.
