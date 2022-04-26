from work_modules.abstractserializer import AbstractSerializer
import yaml


class YamlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as file:
            dump_str = yaml.dump(target_item)
            file.write(dump_str)
            file.close()

    def dumps(self, target_item) -> str:
        return yaml.safe_dump(target_item)

    def load(self, file_path: str) -> all:
        with open(file_path, 'r+') as file:
            load_str = file.read()
            file.close()
            return yaml.safe_load(load_str)

    def loads(self, target_item) -> all:
        return yaml.safe_load(target_item)
