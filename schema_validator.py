import json
import jsonschema
import argparse
import sys

def validate_json(data_filepath, schema_filepath):
    """
    Validates a JSON data file against a JSON schema.
    
    Args:
        data_filepath (str): The path to the JSON file to validate.
        schema_filepath (str): The path to the JSON schema file.
        
    Returns:
        bool: True if validation is successful, False otherwise.
    """
    try:
        # Load the schema from the specified file
        with open(schema_filepath, 'r') as schema_file:
            schema = json.load(schema_file)
            
        # Load the JSON data to validate
        with open(data_filepath, 'r') as data_file:
            data_to_validate = json.load(data_file)
            
        # Validate the data against the schema
        jsonschema.validate(instance=data_to_validate, schema=schema)
        
    except FileNotFoundError as e:
        print(f"Error: File not found - {e.filename}")
        return False
    except json.JSONDecodeError as e:
        print(f"Error: Could not decode JSON. Please check the file for syntax errors. Details: {e}")
        return False
    except jsonschema.ValidationError as e:
        print("JSON is INVALID.")
        # Provide a clear, actionable error message
        print(f"Validation Error: '{e.message}' in instance path '{'/'.join(map(str, e.path))}'")
        return False
    except jsonschema.SchemaError as e:
        print("The provided SCHEMA is invalid.")
        print(f"Schema Error: {e.message}")
        return False
    
    print("JSON is VALID.")
    return True

# This block ensures the following code only runs when the script is executed directly
if __name__ == "__main__":
    # Set up the command-line argument parser
    parser = argparse.ArgumentParser(description="Validate a JSON file against a JSON schema.")
    
    # Add arguments for the data file and schema file
    parser.add_argument("data_file", help="The path to the JSON file to validate.")
    parser.add_argument("schema_file", help="The path to the JSON schema file.")
    
    # Parse the arguments provided by the user
    args = parser.parse_args()
    
    # Run the validation function with the provided file paths
    is_valid = validate_json(args.data_file, args.schema_file)
    
    # Exit with a status code indicating success (0) or failure (1)
    if is_valid:
        sys.exit(0)
    else:
        sys.exit(1)