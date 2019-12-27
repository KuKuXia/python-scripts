import json

import yaml

"""
Example usage:

$ python 29_json_to_yaml.py 29_json_test.json
"""

# load json data
json_data = json.loads(open('data/demo_json.json').read())
# convert unicode to string
converted_json_data = json.dumps(json_data)
# output yaml
print(yaml.dump(yaml.load(converted_json_data), default_flow_style=False))
