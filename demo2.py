import os

# Assuming the export_formatted function is in data_exporter.py
from cluster_maker.data_exporter import export_formatted

def test_export_formatted():
    # Sample data to export
    sample_data = [
        {"name": "Alice", "age": 30, "city": "New York"},
        {"name": "Bob", "age": 25, "city": "Los Angeles"},
        {"name": "Charlie", "age": 35, "city": "Chicago"}
    ]
    
    # Define the output filename
    output_filename = 'test_exported_data.txt'
    
    # Call the export function
    export_formatted(sample_data, output_filename)
    
    # Check if the file was created
    assert os.path.exists(output_filename), "Output file was not created."
    
    # Read the contents of the file and verify the format
    with open(output_filename, 'r') as file:
        contents = file.read()
    
    # Expected output format
    expected_output = (
        "=== Exported Data ===\n"
        "Total Records: 3\n"
        "=====================\n\n"
        "Record 1:\n"
        "  name: Alice\n"
        "  age: 30\n"
        "  city: New York\n\n"
        "Record 2:\n"
        "  name: Bob\n"
        "  age: 25\n"
        "  city: Los Angeles\n\n"
        "Record 3:\n"
        "  name: Charlie\n"
        "  age: 35\n"
        "  city: Chicago\n\n"
    )
    
    # Assert that the contents match the expected output
    assert contents == expected_output, "Output file contents do not match expected format."

    print("Test passed successfully!")

# Run the test
if __name__ == "__main__":
    test_export_formatted()