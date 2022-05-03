import yaml

from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict


class YamlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            file.write(yaml.dump(serialize_to_dict(target_item)))
            file.close()

    def dumps(self, target_item) -> str:
        return yaml.safe_dump(serialize_to_dict(target_item))

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            load_str = file.read()
            file.close()
            return yaml.safe_load(load_str)

    def loads(self, target_item) -> all:
        return yaml.safe_load(target_item)
