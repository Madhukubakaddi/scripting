#!/tools/bin/python
# Program to convert yml file to python dictionary

import yaml
with open("yamlfile.yml", 'r') as stream:
    try:
        x = (yaml.load(stream))
    except yaml.YAMLError as exc:
        print(exc)

