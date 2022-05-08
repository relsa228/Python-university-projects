import os

from serialize_factory import SerializeFactory

to_toml_serializer = SerializeFactory.create_serializer('toml')
to_yaml_serializer = SerializeFactory.create_serializer('yaml')
to_json_serializer = SerializeFactory.create_serializer('json')


def transfer_to_another_format(input_file: str, input_file_format: str, output_file_format: str,
                               globals_from_main: dict) -> bool:
    """
    Конвертирует один формат сериализации в другой
    """
    if output_file_format.lower() == 'yaml':
        if input_file_format.lower() == 'toml' and 'toml' in input_file:
            with open(input_file, 'r') as file:
                restored_class_toml = to_toml_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'yaml', 'toml_to_yaml.yaml'), 'w') as file:
                to_yaml_serializer.dump(restored_class_toml, file, globals_from_main)
            return True

        elif input_file_format.lower() == 'json' and 'json' in input_file:
            with open(input_file, 'r') as file:
                restored_class_json = to_json_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'yaml', 'json_to_yaml.yaml'), 'w') as file:
                to_yaml_serializer.dump(restored_class_json, file, globals_from_main)
            return True

        elif input_file_format.lower() == 'yaml' and 'yaml' in input_file:
            return True

        return False

    elif output_file_format.lower() == 'toml':
        if input_file_format.lower() == 'yaml' and 'yaml' in input_file:
            with open(input_file, 'r') as file:
                restored_class_yaml = to_yaml_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'toml', 'yaml_to_toml.toml'), 'w') as file:
                to_toml_serializer.dump(restored_class_yaml, file, globals_from_main)
            return True

        elif input_file_format.lower() == 'json' and 'json' in input_file:
            with open(input_file, 'r') as file:
                restored_class_json = to_json_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'toml', 'json_to_toml.toml'), 'w') as file:
                to_toml_serializer.dump(restored_class_json, file, globals_from_main)
            return True

        elif input_file_format.lower() == 'toml' and 'toml' in input_file:
            return True

        return False

    elif output_file_format.lower() == 'json':
        if input_file_format.lower() == 'toml' and 'toml' in input_file:
            with open(input_file, 'r') as file:
                restored_class_toml = to_toml_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'json', 'toml_to_json.json'), 'w') as file:
                to_json_serializer.dump(restored_class_toml, file, globals_from_main)
            return True

        elif input_file_format.lower() == 'yaml' and 'yaml' in input_file:
            with open(input_file, 'r') as file:
                restored_class_yaml = to_yaml_serializer.load(file, globals_from_main)
            with open(os.path.join('serialized_results', 'json', 'yaml_to_json.json'), 'w') as file:
                to_json_serializer.dump(restored_class_yaml, file, globals_from_main)
            return True
        elif input_file_format.lower() == 'json' and 'json' in input_file:
            return True

        return False
