import json
import sys
import os

def validate_json_file(file_path):
    """
    Checks if a file contains valid JSON.

    Args:
        file_path (str): The path to the file to check.

    Returns:
        bool: True if the file is valid JSON, False otherwise.
    """
    # Check if the file exists and is not empty
    if not os.path.exists(file_path):
        print(f"Error: File not found at '{file_path}'")
        return False
    if os.path.getsize(file_path) == 0:
        print(f"Error: File is empty at '{file_path}'")
        return False

    try:
        # Open the file and try to load the JSON data
        with open(file_path, 'r') as f:
            json.load(f)
    except json.JSONDecodeError as e:
        # If a JSONDecodeError is raised, the JSON is invalid
        print(f"Invalid JSON in file: {file_path}")
        print(f"Error details: {e}")
        return False
    except Exception as e:
        # Catch any other potential errors (e.g., permissions)
        print(f"An unexpected error occurred: {e}")
        return False
    else:
        # If no exception was raised, the JSON is valid
        print(f"Success: '{file_path}' contains valid JSON.")
        return True

if __name__ == "__main__":
    # The script expects one command-line argument: the path to the JSON file.
    if len(sys.argv) != 2:
        print("Usage: python validate_json.py <path_to_json_file>")
        sys.exit(1)

    # Get the file path from the command-line arguments
    json_file_path = sys.argv[1]
    
    # Call the validation function
    validate_json_file(json_file_path)
