# Main.py

from simulate import simulate_traffic
from plot import plot_graphs
from save_data import save_to_excel

def main():
    # Run the traffic simulation
    time, speed_A, speed_B, distance_A, distance_B = simulate_traffic()

    # Plot the graphs for speed vs. time and distance vs. time
    plot_graphs(time, speed_A, speed_B, distance_A, distance_B)

    # Save the data to an Excel file
    save_to_excel(time, speed_A, speed_B, distance_A, distance_B)

if __name__ == "__main__":
    main()
