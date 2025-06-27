
import json
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def update_json_file(file_path, new_data):
    """
    Update a JSON file with new data.

    Args:
        file_path (str): The path to the JSON file.
        new_data (dict): The new data to update the JSON file with.

    Returns:
        bool: True if the update was successful, False otherwise.
    """
    import json
    import os

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return False

    # Read the existing data from the JSON file
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            print(f"Error decoding JSON from file {file_path}.")
            return False

    # Update the data with new data
    data.update(new_data)

    # Write the updated data back to the JSON file
    with open(file_path, 'w') as file:
        try:
            json.dump(data, file, indent=4)
        except TypeError as e:
            print(f"Error writing JSON to file {file_path}: {e}")
            return False

    return True

def update_temp(simulation,channel,value):
    #write the json file
    """
    :param simulation: True or False
    :param channel: The channel number for the temperature sensor. ex: TS1
    :param value: The value to set if simulation is disabled.
    :return: The value set for the temperature sensor.
    """
    file_path = "files\\data.json"  # Update this path as needed
    channel = channel
    value = value
    if simulation:
         # Read the existing data from the JSON file
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
            except TypeError as e:
                print(f"Error writing JSON to file {file_path}: {e}")

   

if __name__ == "__main__":
    # Example usage
    file_path = "config\\approched_data.json"  # Update this path as needed
    channel = "TS1"  # Example channel
    with open(file_path, 'w') as file:
        try:
            data = json.load(file)
            # data = json.dump(data)
            # print(data["temperature"][channel]["simulation"])
            data["temperature"][channel]["simulation"] = 1
            data = json.dump(data,file, indent=4)
            # print(data["temperature"][channel]["simulation"])
            # print(data["temperature"])
        except TypeError as e:
            print(f"Error writing JSON to file {file_path}: {e}")
            
            # tempp1 text_box update check_box_enabled data.json 
            # tempp2
            # tempp3
            # tempp4
            
            
            # all simuktion
            # file1.json    
            # file2.json = file1.json