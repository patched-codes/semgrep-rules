# License: Apache 2.0 (c) PyCQA
# source: https://github.com/PyCQA/bandit/blob/master/examples/yaml_load.py
# hash:  8eee173

import json
import yaml

def test_yaml_load():
    ystr = yaml.dump({'a': 1, 'b': 2, 'c': 3})
    # ruleid: python_deserialization_rule-yaml-load
    y = yaml.load(ystr, Loader=yaml.FullLoader)
    yaml.dump(y)
    try:
        yaml.load(ystr, Loader=yaml.CSafeLoader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load(ystr, Loader=yaml.Loader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load(ystr, Loader=yaml.CLoader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load(ystr, Loader=yaml.UnsafeLoader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load_all(ystr, Loader=yaml.Loader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load_all(ystr, Loader=yaml.CLoader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load_all(ystr, Loader=yaml.UnsafeLoader)
        # ruleid: python_deserialization_rule-yaml-load
        yaml.load_all(ystr, Loader=yaml.FullLoader)
    except AttributeError:
        # CSafeLoader only exists if you build yaml with LibYAML
        y = yaml.load(ystr, Loader=yaml.SafeLoader)

def test_json_load():
    # no issue should be found
    j = json.load("{}")
