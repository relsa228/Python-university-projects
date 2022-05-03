from packages_dir.serialize_modules.json_serialize_module import JsonSerializer
from packages_dir.serialize_modules.toml_serialize_module import TomlSerializer
from packages_dir.serialize_modules.yaml_serialize_module import YamlSerializer
from test_files.test_fie import TestClass

ffd = {'d': {'g': 1}}
ff = """
def govno(self):
    return 2+1
"""

# my_tree = ast.parse(ff)
# ii = ast.walk(my_tree)
# strin = ast_to_string_for_dict(my_tree)


# dic = eval(normilize_string(strin))
# print(json.dumps(dic))
# my_oo = ast.parse(normilize_string(strin))


# print(ast.unparse(my_tree))
# print(ast.unparse(my_oo))

ser = JsonSerializer()
#ser.dump(TestClass, "results/ForClass.json")

serr = TomlSerializer()
#serr.dump(TestClass, "results/ForClass.toml")

serrr = YamlSerializer()
#serrr.dump(TestClass, "results/ForClass.yml")

#tc = TestClass()
#ser.dump(TestClass, "results/ForObject.json")
#serr.dump(TestClass, "results/ForObject.toml")
#serrr.dump(TestClass, "results/ForObject.yml")

#test_list = ["aaa", "bbb", "ccc"]
#ser.dump(test_list, "results/ForList.json")
#serr.dump(test_list, "results/ForList.toml")
#serrr.dump(test_list, "results/ForList.yml")

#test_tuple = ("fff", "111", "999")
#ser.dump(test_tuple, "results/ForTuple.json")
#serr.dump(test_tuple, "results/ForTuple.toml")
#serrr.dump(test_tuple, "results/ForTuple.yml")

#test_dict = {'nnn': 1234, 'molchat': "doma", 'eee': 413}
#ser.dump(test_dict, "results/ForDict.json")
#serr.dump(test_dict, "results/ForDict.toml")
#serrr.dump(test_dict, "results/ForDict.yml")

mmm = serrr.load("results/ForDict.yml")
print(mmm)
