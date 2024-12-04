import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from cluster_maker.dataframe_builder import define_dataframe_structure, non_globular_cluster

def test_non_globular_cluster():
    # Define the seed DataFrame structure
    seed_df = define_dataframe_structure()
    
    # Simulate non-globular clusters
    num_points = 100
    cluster_shape = 'spiral'
    noise_level = 0.05
    
    # Call the non-globular cluster function
    result_df = non_globular_cluster(seed_df, num_points, cluster_shape, noise_level)
    
    # Check if the result DataFrame has the correct number of points
    assert len(result_df) == num_points, f"Expected {num_points} points, got {len(result_df)}."
    
    # Check if the DataFrame has the correct columns
    expected_columns = ['x', 'y', 'cluster_label']
    assert all(col in result_df.columns for col in expected_columns), "DataFrame does not have the expected columns."
    
    # Check if the cluster label is correctly assigned
    assert all(result_df['cluster_label'] == 'non-globular'), "Cluster label is not correctly assigned."
    
    # Check if the points are within a reasonable range (for spiral)
    assert np.all(np.abs(result_df['x']) <= 2), "X values are out of expected range."
    assert np.all(np.abs(result_df['y']) <= 1), "Y values are out of expected range."
    
    # Plotting the results
    plt.figure(figsize=(8, 6))
    plt.scatter(result_df['x'], result_df['y'], c='blue', label='Non-Globular Cluster', alpha=0.6)
    plt.title('Non-Globular Cluster Simulation')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.axhline(0, color='black',linewidth=0.5, ls='--')
    plt.axvline(0, color='black',linewidth=0.5, ls='--')
    plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
    plt.legend()
    plt.show()

    print("Test passed successfully!")

# Run the test
if __name__ == "__main__":
    test_non_globular_cluster()