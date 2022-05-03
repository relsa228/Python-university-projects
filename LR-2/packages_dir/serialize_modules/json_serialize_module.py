from packages_dir.serialize_modules.abstractserializer import AbstractSerializer
from packages_dir.tools_modules.def_dict_form_module import serialize_to_dict


class JsonSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            file.write(JsonSerializer.dumps(self, target_item))
            file.close()

    def dumps(self, target_item) -> str:
        return str(serialize_to_dict(target_item))

    def load(self, file_path: str) -> all:
        return ""

    def loads(self, target_item) -> all:
        return ""
