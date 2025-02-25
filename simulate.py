# Simulate.py

import numpy as np

class Vehicle:
    def __init__(self, position, velocity, max_velocity, min_velocity):
        self.position = position
        self.velocity = velocity
        self.max_velocity = max_velocity
        self.min_velocity = min_velocity
    
    def update_velocity(self, other_vehicle, time_step):
        # Rule 1: Acceleration if the distance is large and speed is below max
        distance_to_other = other_vehicle.position - self.position
        if self.velocity < self.max_velocity and distance_to_other > self.velocity + 1:
            self.velocity += 1  # Accelerate

        # Rule 2: Slowing down if the distance is too small
        elif distance_to_other < 5:  # Adjust this threshold as needed
            self.velocity = max(self.velocity - 1, self.min_velocity)  # Slow down

        # Rule 3: Randomization factor (small chance to randomly slow down)
        if np.random.rand() < 0.1:  # Random factor for slow down
            self.velocity = max(self.velocity - 1, self.min_velocity)
        
        # Rule 4: Move by velocity (simulate movement)
        self.position += self.velocity * time_step

def simulate_traffic(time_steps=100):
    # Initialize vehicles
    A = Vehicle(position=0, velocity=5, max_velocity=10, min_velocity=1)
    B = Vehicle(position=20, velocity=3, max_velocity=10, min_velocity=1)

    # Simulation parameters
    time = np.arange(time_steps)
    speed_A = []
    speed_B = []
    distance_A = []
    distance_B = []

    # Simulate the traffic system
    for t in time:
        A.update_velocity(B, 1)  # Vehicle A interacts with Vehicle B
        B.update_velocity(A, 1)  # Vehicle B interacts with Vehicle A
        
        speed_A.append(A.velocity)
        speed_B.append(B.velocity)
        distance_A.append(A.position)
        distance_B.append(B.position)

    return time, speed_A, speed_B, distance_A, distance_B
