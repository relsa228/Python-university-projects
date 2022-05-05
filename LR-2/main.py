import math

from packages_dir.serialize_modules.json_serialize_module import JsonSerializer
from packages_dir.serialize_modules.toml_serialize_module import TomlSerializer
from packages_dir.serialize_modules.yaml_serialize_module import YamlSerializer
from packages_dir.serialize_modules.serialize_factory import SerializeFactory

from test_files.funct_file import f
from test_files.funct_file import take_globals as tg2

test_list = ['1', '2', '3']
test_tuple = ('1', '2', '3')
test_dict = {'1': 1, '2': 2, '3': 3}

class TestClassS:
    def __init__(self):
        self.s = "d"
        self.d = 1

    def funct1(self):
        return 2+1

    def funct2(self):
        return "jojo"

if __name__ == '__main__':
    json_s = SerializeFactory.create_serializer("json")
    toml_s = SerializeFactory.create_serializer("toml")
    yaml_s = SerializeFactory.create_serializer("yaml")

    test_item = TestClassS()
    print("Tests:")
    print("1. JSON tests:")
    print("\nClass serialize: ")
    json_s.dump(TestClassS, "results/ForClass.json", globals())
    print(" " + str(json_s.load("results/ForClass.json", globals())))
    print("\n\nClass object: ")
    jj = TestClassS()
    json_s.dump(jj, "results/ForObject.json", globals())
    print(" " + str(json_s.load("results/ForObject.json", globals())))



