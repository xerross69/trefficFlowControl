# Plot.py

import matplotlib.pyplot as plt

def plot_graphs(time, speed_A, speed_B, distance_A, distance_B):
    # Plot Speed vs Time
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.plot(time, speed_A, label="Vehicle A", color="blue")
    plt.plot(time, speed_B, label="Vehicle B", color="red")
    plt.xlabel("Time")
    plt.ylabel("Speed")
    plt.title("Speed vs Time for Vehicle A and Vehicle B")
    plt.legend()

    # Plot Distance vs Time
    plt.subplot(1, 2, 2)
    plt.plot(time, distance_A, label="Vehicle A", color="blue")
    plt.plot(time, distance_B, label="Vehicle B", color="red")
    plt.xlabel("Time")
    plt.ylabel("Distance")
    plt.title("Distance vs Time for Vehicle A and Vehicle B")
    plt.legend()

    plt.tight_layout()
    plt.show()
