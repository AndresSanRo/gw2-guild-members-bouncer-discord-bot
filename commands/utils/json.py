import json

def write_json(file_path: str, data: dict):
    try:
        # Read the existing content of the file
        existing_data = read_json(file_path)
        
        # Update the existing data with the new data
        existing_data.update(data)
        
        # Write the updated data back to the file
        with open(file_path, "w") as f:
            json.dump(existing_data, f, indent=4)
        
        print(f"Data written to {file_path}")
        
    except Exception as e:
        print(f"Error writing data: {e}")
        raise e
    
def read_json(file_path):
    try:
        with open(file_path, "r") as f:
            existing_data = json.load(f)
    except json.JSONDecodeError:
        existing_data = {}
    return existing_data