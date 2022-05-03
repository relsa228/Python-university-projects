import toml

from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict


class TomlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            toml.dump(serialize_to_dict(target_item), file)
            file.close()

    def dumps(self, target_item) -> str:
        return toml.dumps(serialize_to_dict(target_item))

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            return toml.load(file)

    def loads(self, target_item) -> all:
        return toml.loads(target_item)
