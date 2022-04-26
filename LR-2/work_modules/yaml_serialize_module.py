from work_modules.abstractserializer import AbstractSerializer
import yaml


class YamlSerializer(AbstractSerializer):
    def dump(self, target_item, file_path: str) -> None:
        with open(file_path, 'w+') as f:
            yaml.safe_dump(target_item, f)

    def dumps(self, target_item) -> str:
        return yaml.safe_dump(target_item)

    def load(self, file_path: str) -> None:
        with open(file_path, 'w+') as f:
            yaml.safe_load(f)

    def loads(self, target_item) -> str:
        return yaml.safe_load(target_item)
