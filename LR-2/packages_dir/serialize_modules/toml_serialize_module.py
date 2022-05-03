import toml

from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict
from packages_dir.tools_modules.def_dict_form_module import deserialize_from_dict


class TomlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            toml.dump(serialize_to_dict(target_item), file)
            file.close()

    def dumps(self, target_item) -> str:
        return toml.dumps(serialize_to_dict(target_item))

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            wrk_str = toml.load(file)
            file.close()
        return deserialize_from_dict(wrk_str)

    def loads(self, target_str) -> all:
        wrk_str = toml.loads(target_str)
        return deserialize_from_dict(wrk_str)
