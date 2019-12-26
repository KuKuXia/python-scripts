import json


def dict_raise_on_duplicates(ordered_pairs):
    """reject duplicate keys"""
    my_dict = dict()
    for key, values in ordered_pairs.items():
        if key in my_dict:
            raise ValueError("Duplicate key: {}".format(key, ))
        else:
            my_dict[key] = values
    return my_dict


with open('./data/demo_json.json') as jf:
    data = json.load(jf)
    print(data)
    dict_data = dict_raise_on_duplicates(data)
    print(dict_data)
