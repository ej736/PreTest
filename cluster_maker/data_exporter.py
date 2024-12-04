###
## cluster_maker
## A package to simulate clusters of data points.
## J. Foadi - University of Bath - 2024
##
## Module data_exporter
###

## Function to export to CSV
def export_to_csv(data, filename, delimiter=",", include_index=False):
    """
    Export the DataFrame to a CSV file.

    Parameters:
        data (pd.DataFrame): The DataFrame to export.
        filename (str): Name f the output CSV file.
        delimiter (str): Delimiter for the CSV file (default: ',').
        include_index (bool): Whether to include the DataFrame index (default: False).

    Returns:
        None
    """
    try:
        data.to_csv(filename, sep=delimiter, index=include_index)
        print(f"Data successfully exported to {filename}")
    except Exception as e:
        print(f"Error exporting data to CSV: {e}")

def export_formatted(data, filename='exported_data.txt'):
    """
    Exports the provided data to a formatted text file.

    Parameters:
    - data: List of dictionaries containing the data to export.
    - filename: The name of the file to which the data will be exported.
    """
    try:
        with open(filename, 'w') as file:
            # Write a header
            file.write("=== Exported Data ===\n")
            file.write(f"Total Records: {len(data)}\n")
            file.write("=====================\n\n")

            # Write each record in a formatted way
            for index, record in enumerate(data):
                file.write(f"Record {index + 1}:\n")
                for key, value in record.items():
                    file.write(f"  {key}: {value}\n")
                file.write("\n")  # Add a newline for better separation between records

            print(f"Data successfully exported to {filename}")

    except Exception as e:
        print(f"An error occurred while exporting data: {e}")

