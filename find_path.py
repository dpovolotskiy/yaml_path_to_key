import yaml
import argparse


def get_full_path_to_value(value, dictionary, path=""):
    if isinstance(dictionary, (dict, list, tuple)):
        if value in dictionary:
            print(path[1:] + ":" + str(value))
            return
        elif value not in dictionary and (not isinstance(dictionary, dict) or len(dictionary.keys()) == 0):
            return
        else:
            for key in dictionary.keys():
                get_full_path_to_value(value, dictionary[key], path=path + ":" + str(key))
    elif type(value) == type(dictionary) and value == dictionary:
        print(path[1:] + ":" + str(value))
        return
    else:
        return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_path", help="path to yaml file", type=str)
    parser.add_argument("value", help="desired value", type=str)
    args = parser.parse_args()
    with open(args.file_path, "r") as stream:
        try:
            data = yaml.safe_load(stream)
            get_full_path_to_value(args.value, data)
            if args.value.isdigit():
                get_full_path_to_value(int(args.value), data)
        except yaml.YAMLError as error:
            print(error)
