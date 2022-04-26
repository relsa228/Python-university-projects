from work_modules.abstractserializer import AbstractSerializer
import toml


class TomlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            toml.dump(target_item, file)
            file.close()

    def dumps(self, target_item) -> str:
        return toml.dumps(target_item)

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            return toml.load(file)

    def loads(self, target_item) -> all:
        return toml.loads(target_item)
