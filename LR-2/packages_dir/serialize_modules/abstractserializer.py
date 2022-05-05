from abc import abstractmethod


class AbstractSerializer:
    @abstractmethod
    def dump(self, target_item, file_path: str, globals_from_main: dict) -> None:
        """
        Cериализует Python объект в файл
        """
        pass

    @abstractmethod
    def dumps(self, target_item, globals_from_main: dict) -> str:
        """
        Cериализует Python объект в строку
        """
        pass

    @abstractmethod
    def load(self, file_path: str, globals_from_main) -> all:
        """
        Десериализует Python объект из файла
        """
        pass

    @abstractmethod
    def loads(self, target_str, globals_from_main) -> all:
        """
        Десериализует Python объект из строки
        """
        pass