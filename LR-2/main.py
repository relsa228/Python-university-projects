from test_files.test_functions.test_for_json import test_for_json
from test_files.test_functions.test_for_toml import test_for_toml
from test_files.test_functions.test_for_yaml import test_for_yaml


if __name__ == '__main__':
    while True:
        print("1. Test for JSON\n2. Test for TOML\n3. Test for YAML\n0. Exit\n")
        choose = input("Your choose: ")
        match choose:
            case "1":
                test_for_json()
                input()
            case "2":
                test_for_toml()
                input()
            case "3":
                test_for_yaml()
                input()
            case "0":
                break
