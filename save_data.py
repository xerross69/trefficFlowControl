# Save_Data.py

import pandas as pd

def save_to_excel(time, speed_A, speed_B, distance_A, distance_B, filename="traffic_simulation_data.xlsx"):
    # Create a DataFrame
    data = {
        "Time": time,
        "Speed_A": speed_A,
        "Speed_B": speed_B,
        "Distance_A": distance_A,
        "Distance_B": distance_B
    }
    df = pd.DataFrame(data)

    # Save to Excel
    df.to_excel(filename, index=False)
    print(f"Data saved to {filename}")
