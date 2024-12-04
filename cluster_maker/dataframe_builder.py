###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module dataframe_builder
###

## Libraries needed
import pandas as pd
import numpy as np

## Function to define the wanted data structure
def define_dataframe_structure(column_specs):
    """
    Define the structure of a DataFrame.

    Parameters:
    columns (list of str): A list of column names for the DataFrame.
    dtypes (dict): A dictionary mapping column names to their respective data types.
    index (str or None): The name of the index column (default: None).

    Returns:
    pd.DataFrame: A DataFrame with the specified structure.
    """
    # Prepare data dictionary
    data = {}
    max_length = 0

    # Find the maximum length of representative points
    for spec in column_specs:
        max_length = max(max_length, len(spec.get('reps', [])))

    for spec in column_specs:
        name = spec['name']
        reps = spec.get('reps', [])
        # Extend numerical columns with NaN to match max_length
        extended_points = reps + [np.nan] * (max_length - len(reps))
        data[name] = extended_points

    return pd.DataFrame(data)

## Function to simulate data
def simulate_data(seed_df, n_points=100, col_specs=None, random_state=None):
    """
    Simulate data points based on representative points from a seed DataFrame.

    Parameters:
    seed_df (pd.DataFrame): A DataFrame containing representative points for simulation.
    n_points (int): The number of simulated data points to generate for each representative (default: 100).
    col_specs (dict): A dictionary specifying the distribution and variance for each column (default: None).
    random_state (int or None): Seed for the random number generator for reproducibility (default: None).

    Returns:
    pd.DataFrame: A DataFrame containing the simulated data points.
    """
    if random_state is not None:
        np.random.seed(random_state)
    
    simulated_data = []

    for _, representative in seed_df.iterrows():
        for _ in range(n_points):
            simulated_point = {}
            for col in seed_df.columns:
                # Numerical columns: apply column-specific specifications
                if col_specs and col in col_specs:
                    dist = col_specs[col].get('distribution', 'normal')
                    variance = col_specs[col].get('variance', 1.0)

                    if dist == 'normal':
                        simulated_point[col] = representative[col] + np.random.normal(0, np.sqrt(variance))
                    elif dist == 'uniform':
                        simulated_point[col] = representative[col] + np.random.uniform(-variance, variance)
                    else:
                        raise ValueError(f"Unsupported distribution: {dist}")
                else:
                    raise ValueError(f"Column {col} has no specifications in col_specs.")
            simulated_data.append(simulated_point)
    
    return pd.DataFrame(simulated_data)

import numpy as np
import pandas as pd

def define_dataframe_structure():
    """
    Define the structure of the DataFrame to be used for simulation.
    This function returns an empty DataFrame with predefined columns.
    """
    return pd.DataFrame(columns=['x', 'y', 'cluster_label'])

def non_globular_cluster(seed_df, num_points, cluster_shape='spiral', noise_level=0.1):
    """
    Simulates non-globular clusters of data points.

    Parameters:
    - seed_df: DataFrame structure created by define_dataframe_structure().
    - num_points: Number of points to simulate.
    - cluster_shape: The shape of the cluster ('spiral', 'elongated', etc.).
    - noise_level: The level of noise to add to the points.

    Returns:
    - DataFrame containing the simulated non-globular cluster points.
    """
    np.random.seed(42)  # For reproducibility
    points = []

    if cluster_shape == 'spiral':
        # Generate points in a spiral shape
        theta = np.linspace(0, 4 * np.pi, num_points)  # Angle
        r = np.linspace(0, 1, num_points)  # Radius
        x = r * np.sin(theta) + np.random.normal(0, noise_level, num_points)
        y = r * np.cos(theta) + np.random.normal(0, noise_level, num_points)
        points = np.column_stack((x, y))

    elif cluster_shape == 'elongated':
        # Generate points in an elongated shape
        t = np.linspace(0, 2 * np.pi, num_points)
        x = 2 * np.sin(t) + np.random.normal(0, noise_level, num_points)  # Elongated in x
        y = np.cos(t) + np.random.normal(0, noise_level, num_points)  # Regular in y
        points = np.column_stack((x, y))

    else:
        raise ValueError("Unsupported cluster shape. Choose 'spiral' or 'elongated'.")

    # Create a DataFrame from the points
    cluster_df = pd.DataFrame(points, columns=['x', 'y'])
    cluster_df['cluster_label'] = 'non-globular'

    # Combine with the seed DataFrame if needed
    result_df = pd.concat([seed_df, cluster_df], ignore_index=True)

    return result_df