import ast

from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict
from packages_dir.tools_modules.def_dict_form_module import deserialize_from_dict


class JsonSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str, globals_from_main: dict) -> None:
        '''
        Сериализация объекта в файл
        '''
        with open(file_path, 'w+') as file:
            file.write(JsonSerializer.dumps(self, target_item, globals_from_main))
            file.close()

    def dumps(self, target_item, globals_from_main: dict) -> str:
        '''
        Сериализация объекта в строку
        '''
        return str(serialize_to_dict(target_item, globals_from_main))

    def load(self, file_path: str, globals_from_main) -> all:
        '''
        Возвращает объект из файла
        '''
        with open(file_path, 'r+') as file:
            json_str = file.read()
            file.close()
        dict_from_str = ast.literal_eval(json_str)
        return deserialize_from_dict(dict_from_str, globals_from_main)

    def loads(self, target_str, globals_from_main) -> all:
        '''
        Возвращает объект из строки
        '''
        dict_from_str = ast.literal_eval(target_str)
        return deserialize_from_dict(dict_from_str, globals_from_main)
