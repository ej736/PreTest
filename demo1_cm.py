# demo1_cm.py

import pandas as pd
from cluster_maker import define_dataframe_structure, simulate_data, export_to_csv

def main():
    # Step 1: Define the DataFrame structure
    column_specs = [
        {'name': 'Feature1', 'reps': [1.0, 2.0, 3.0]},
        {'name': 'Feature2', 'reps': [4.0, 5.0]},
        {'name': 'Feature3', 'reps': [6.0, 7.0, 8.0, 9.0]}
    ]
    
    # Create the DataFrame structure
    df_structure = define_dataframe_structure(column_specs)
    print("Defined DataFrame Structure:")
    print(df_structure)

    # Step 2: Simulate data based on the defined structure
    col_specs_simulation = {
        'Feature1': {'distribution': 'normal', 'variance': 0.5},
        'Feature2': {'distribution': 'uniform', 'variance': 1.0},
        'Feature3': {'distribution': 'normal', 'variance': 0.2}
    }
    
    simulated_data = simulate_data(seed_df=df_structure, n_points=10, col_specs=col_specs_simulation, random_state=42)
    print("\nSimulated Data:")
    print(simulated_data)

    # Step 3: Export the simulated data to a CSV file
    output_filename = 'simulated_data.csv'
    export_to_csv(simulated_data, output_filename)
    print(f"\nSimulated data exported to {output_filename}")

if __name__ == "__main__":
    main()