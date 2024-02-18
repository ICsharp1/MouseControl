import json
import os
import collections

def load_corner_data(filename):

    corners = []
    try:
        with open(filename) as f:
            data = json.load(f)
    except(FileNotFoundError):
        #we will throw the error back
        raise FileNotFoundError(f"File {filename} not found")

    Coordinates = collections.namedtuple('Point', 'number type left_x top_y right_x bottom_y keys file_to_execute')

    for corner in data:
        
        basic_attributes = {
            'number': corner['number'],
            'type': corner['type'],
            'left_x': corner['leftX'],
            'top_y': corner['topY'],
            'right_x': corner['rightX'],
            'bottom_y': corner['bottomY'],
        }
        if corner['type'] =='command':
            basic_attributes['file_to_execute'] = corner['file_to_execute']
            basic_attributes['keys'] = None
        elif corner['type'] =='shortcut':
            basic_attributes['keys'] = corner.get('keys', [])
            basic_attributes['file_to_execute'] = None

        corner_instance = Coordinates(**basic_attributes)

        corners.append(corner_instance)

    return corners  

def add_to_json(number, type, leftX, topY, rightX, bottomY, keys_or_file, json_file="mouse_actions.json"):

    if os.path.exists(json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
    else:
        # If the file doesn't exist, create an empty list
        data = []

    # Create a new entry based on the provided arguments
    
    entry = {
        "number": number,
        "type": type,
        "leftX": leftX,
        "topY": topY,
        "rightX": rightX,
        "bottomY": bottomY,
    }
    if type == 'command':
        entry["file_to_execute"] = keys_or_file
        entry["keys"] = None
    elif type == 'shortcut':
        entry["keys"] = keys_or_file
        entry["file_to_execute"] = None
    
    # Append the new entry to the existing data
    data.append(entry)

    # Write the updated data back to the JSON file
    with open(json_file, 'w') as f:
        json.dump(data, f, indent=2)

def get_last_corner_number(filename):
    corners = load_corner_data(filename)
    if corners:
        last_corner_number = corners[-1].number
        return last_corner_number
    else:
        return 0
    

def add_corner_to_json(rect, data, type, json_file="mouse_actions.json"):
    try:
        number = get_last_corner_number(json_file)
    except FileNotFoundError:
        number = -1

    leftX = rect.topLeft().x()
    topY = rect.topLeft().y()
    rightX = rect.bottomRight().x()
    bottomY = rect.bottomRight().y()


    add_to_json(number + 1, type, leftX, topY, rightX, bottomY, data, json_file)


