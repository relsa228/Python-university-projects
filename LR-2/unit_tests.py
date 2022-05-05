import os
import unittest

from packages_dir.serialize_modules.formats_converter import transfer_to_another_format

from test_files.class_file import TestClassS
from test_files.class_file import take_globals as tg1

from test_files.funct_file import f
from test_files.funct_file import take_globals as tg2

from packages_dir.serialize_modules.serialize_factory import SerializeFactory
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict
from packages_dir.tools_modules.def_dict_form_module import deserialize_from_dict

test_list = ['1', '2', '3']
test_tuple = ('1', '2', '3')
test_dict = {'1': 1, '2': 2, '3': 3}


class TestClass(unittest.TestCase):

    def setUp(self):
        self.to_toml_serializer = SerializeFactory.create_serializer('toml')
        self.to_yaml_serializer = SerializeFactory.create_serializer('yaml')
        self.to_json_serializer = SerializeFactory.create_serializer('json')

    def test_serialization_class(self):
        serialized = serialize_to_dict(TestClassS, tg1())
        restored = deserialize_from_dict(serialized, tg1())
        instance_tmp1 = TestClassS()
        instance_tmp2 = restored

        self.assertEqual(instance_tmp1, instance_tmp2)

        tmp1 = instance_tmp1.funct1()
        tmp2 = instance_tmp2.funct1()

        self.assertEqual(tmp1, tmp2)

    def test_serialization_class_object(self):
        serialized = serialize_to_dict(TestClassS(), tg1())
        restored = deserialize_from_dict(serialized, tg1())
        self.assertEqual(TestClassS(), restored)

    def test_serialization_function(self):
        serialized = serialize_to_dict(f, tg2())
        restored = deserialize_from_dict(serialized, tg2())
        self.assertEqual(f(3), restored(3))

    def test_formats_serializer_class(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_class_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(TestClassS, file, tg1())

        with open(os.path.join('serialized_results', 'toml', 'serialized_class_to_toml.toml'), 'r') as file:
            restored_class_toml = self.to_toml_serializer.load(file, tg1())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_class_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(TestClassS, file, tg1())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_class_to_yaml.yaml'), 'r') as file:
            restored_class_yaml = self.to_yaml_serializer.load(file, tg1())

        with open(os.path.join('serialized_results', 'json', 'serialized_class_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(TestClassS, file, tg1())

        with open(os.path.join('serialized_results', 'json', 'serialized_class_to_json.json'), 'r') as file:
            restored_class_json = self.to_json_serializer.load(file, tg1())

        restored_class_object_from_class_toml = restored_class_toml()
        intial_class_object_toml = TestClassS()

        tmp_toml1 = restored_class_object_from_class_toml.funct1()
        tmp_toml2 = intial_class_object_toml.funct1()

        restored_class_object_from_class_yaml = restored_class_yaml()
        intial_class_object_yaml = TestClassS()

        tmp_yaml1 = restored_class_object_from_class_yaml.funct1()
        tmp_yaml2 = intial_class_object_yaml.funct1()

        restored_class_object_from_class_json = restored_class_json()
        intial_class_object_json = TestClassS()

        tmp_json1 = restored_class_object_from_class_json.funct1()
        tmp_json2 = intial_class_object_json.funct1()

        self.assertEqual(tmp_toml2, tmp_toml1)
        self.assertEqual(tmp_yaml1, tmp_yaml1)
        self.assertEqual(tmp_json1, tmp_json2)

    def test_formats_serializer_class_object(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_class_object_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(TestClassS(), file, tg1())

        with open(os.path.join('serialized_results', 'toml', 'serialized_class_object_to_toml.toml'), 'r') as file:
            restored_class_object_toml = self.to_toml_serializer.load(file, tg1())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_class_object_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(TestClassS(), file, tg1())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_class_object_to_yaml.yaml'), 'r') as file:
            restored_class_object_yaml = self.to_yaml_serializer.load(file, tg1())

        with open(os.path.join('serialized_results', 'json', 'serialized_class_object_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(TestClassS(), file, tg1())

        with open(os.path.join('serialized_results', 'json', 'serialized_class_object_to_json.json'), 'r') as file:
            restored_class_object_json = self.to_json_serializer.load(file, tg1())

        self.assertEqual(TestClassS(), restored_class_object_toml)
        self.assertEqual(TestClassS(), restored_class_object_yaml)
        self.assertEqual(TestClassS(), restored_class_object_json)

    def test_formats_serializer_function(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_function_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(f, file, tg2())

        with open(os.path.join('serialized_results', 'toml', 'serialized_function_to_toml.toml'), 'r') as file:
            restored_function_toml = self.to_toml_serializer.load(file, tg2())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_function_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(f, file, tg2())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_function_to_yaml.yaml'), 'r') as file:
            restored_function_yaml = self.to_yaml_serializer.load(file, tg2())

        with open(os.path.join('serialized_results', 'json', 'serialized_function_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(f, file, tg2())

        with open(os.path.join('serialized_results', 'json', 'serialized_function_to_json.json'), 'r') as file:
            restored_function_json = self.to_json_serializer.load(file, tg2())

        self.assertEqual(restored_function_toml(3), f(3))
        self.assertEqual(restored_function_yaml(3), f(3))
        self.assertEqual(restored_function_json(3), f(3))

    def test_formats_serializer_dict(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_test_dict_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(test_dict, file, globals())

        with open(os.path.join('serialized_results', 'toml', 'serialized_test_dict_to_toml.toml'), 'r') as file:
            restored_test_dict_toml = self.to_toml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_dict_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(test_dict, file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_dict_to_yaml.yaml'), 'r') as file:
            restored_test_dict_yaml = self.to_yaml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_dict_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(test_dict, file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_dict_to_json.json'), 'r') as file:
            restored_test_dict_json = self.to_json_serializer.load(file, globals())

        self.assertEqual(restored_test_dict_toml, test_dict)
        self.assertEqual(restored_test_dict_yaml, test_dict)
        self.assertEqual(restored_test_dict_json, test_dict)

    def test_formats_serializer_list(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_test_list_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(test_list, file, globals())

        with open(os.path.join('serialized_results', 'toml', 'serialized_test_list_to_toml.toml'), 'r') as file:
            restored_test_list_toml = self.to_toml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_list_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(test_list, file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_list_to_yaml.yaml'), 'r') as file:
            restored_test_list_yaml = self.to_yaml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_list_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(test_list, file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_list_to_json.json'), 'r') as file:
            restored_test_list_json = self.to_json_serializer.load(file, globals())

        self.assertEqual(restored_test_list_toml, test_list)
        self.assertEqual(restored_test_list_yaml, test_list)
        self.assertEqual(restored_test_list_json, test_list)

    def test_formats_serializer_tuple(self):
        with open(os.path.join('serialized_results', 'toml', 'serialized_test_tuple_to_toml.toml'), 'w') as file:
            self.to_toml_serializer.dump(test_tuple, file, globals())

        with open(os.path.join('serialized_results', 'toml', 'serialized_test_tuple_to_toml.toml'), 'r') as file:
            restored_test_tuple_toml = self.to_toml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_tuple_to_yaml.yaml'), 'w') as file:
            self.to_yaml_serializer.dump(test_tuple, file, globals())

        with open(os.path.join('serialized_results', 'yaml', 'serialized_test_tuple_to_yaml.yaml'), 'r') as file:
            restored_test_tuple_yaml = self.to_yaml_serializer.load(file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_tuple_to_json.json'), 'w') as file:
            self.to_json_serializer.dump(test_tuple, file, globals())

        with open(os.path.join('serialized_results', 'json', 'serialized_test_tuple_to_json.json'), 'r') as file:
            restored_test_tuple_json = self.to_json_serializer.load(file, globals())

        self.assertEqual(restored_test_tuple_toml, test_tuple)
        self.assertEqual(restored_test_tuple_yaml, test_tuple)
        self.assertEqual(restored_test_tuple_json, test_tuple)

    def test_change_formats(self):
        self.assertTrue(
            transfer_to_another_format('serialized_results/toml/serialized_class_object_to_toml.toml',
                                       'toml', 'yaml', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/json/serialized_class_object_to_json.json',
                                       'json', 'yaml', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/yaml/serialized_class_object_to_yaml.yaml',
                                       'yaml', 'yaml', globals()))

        self.assertTrue(
            transfer_to_another_format('serialized_results/yaml/serialized_class_object_to_yaml.yaml',
                                       'yaml', 'toml', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/json/serialized_class_object_to_json.json',
                                       'json', 'toml', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/toml/serialized_class_object_to_toml.toml',
                                       'toml', 'toml', globals()))

        self.assertTrue(
            transfer_to_another_format('serialized_results/yaml/serialized_class_object_to_yaml.yaml',
                                       'yaml', 'json', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/toml/serialized_class_object_to_toml.toml',
                                       'toml', 'json', globals()))
        self.assertTrue(
            transfer_to_another_format('serialized_results/json/serialized_class_object_to_json.json',
                                       'json', 'json', globals()))
