import yaml

from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict
from packages_dir.tools_modules.def_dict_form_module import deserialize_from_dict


class YamlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            file.write(yaml.dump(serialize_to_dict(target_item)))
            file.close()

    def dumps(self, target_item) -> str:
        return yaml.safe_dump(serialize_to_dict(target_item))

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            wrk_str = file.read()
            wrk_str = yaml.safe_load(wrk_str)
            file.close()
        return deserialize_from_dict(wrk_str)

    def loads(self, target_str) -> all:
        wrk_str = yaml.safe_load(target_str)
        return deserialize_from_dict(wrk_str)
