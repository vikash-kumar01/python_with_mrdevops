import json
import yaml


def json_to_yaml(json_file, yaml_file):
    with open(json_file, "r") as json_file:
        data = json.load(json_file)
        print(data)
    with open(yaml_file, "w") as yalm_file:
        yaml.dump(data, yalm_file, default_flow_style=False)
        

json_to_yaml("data.json", "data.yaml")
