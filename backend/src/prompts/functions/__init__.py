# import yaml
# import json
# import os

# _current_dir = os.path.dirname(__file__)
# _config_file = os.path.join(_current_dir, "config.yaml")

# def read_yaml_file(file_path):
#     with open(file_path, 'r') as file:
#         return yaml.safe_load(file)

# def filter_allowed_functions(data):
#     allowed_functions = []
#     for function in data.get('functions', []):  # Ensure data['functions'] is a list
#         if function.get('allow', False):
#             # Remove the 'allow' key-value pair
#             function.pop('allow', None)

#             allowed_functions.append(function)
#     return allowed_functions

# def convert_to_json(data):
#     print(data)
#     return json.dumps(data, indent=4)

# def write_to_json_file(data, file_path):
#     with open(file_path, 'w') as file:
#         file.write(data)

# yaml_data = read_yaml_file(_config_file)
# allowed_functions = filter_allowed_functions(yaml_data)
# ALL_ALLOWED_FUNCTIONS = convert_to_json(allowed_functions)  # Wrap in a dictionary under 'functions' key

# write_to_json_file(ALL_ALLOWED_FUNCTIONS, os.path.join(_current_dir, 'signatures.json'))

import yaml
import json
import os

_current_dir = os.path.dirname(__file__)
_config_file = os.path.join(_current_dir, "config.yaml")

def read_yaml_file(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def filter_allowed_functions(data):
    allowed_functions = []
    for function in data.get('functions', []):  # Ensure data['functions'] is a list
        if function.get('allow', False):
            # Remove the 'allow' key-value pair
            function.pop('allow', None)
            allowed_functions.append(function)
    return allowed_functions

def write_to_json_file(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

yaml_data = read_yaml_file(_config_file)
ALL_ALLOWED_FUNCTIONS = filter_allowed_functions(yaml_data)

write_to_json_file(ALL_ALLOWED_FUNCTIONS, os.path.join(_current_dir, 'signatures.json'))