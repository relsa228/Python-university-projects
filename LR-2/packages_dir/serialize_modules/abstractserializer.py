from abc import abstractmethod


class AbstractSerializer:
    @abstractmethod
    def dump(self, target_item, file_path: str) -> None:
        """
        Cериализует Python объект в файл
        """
        pass

    @abstractmethod
    def dumps(self, target_item) -> str:
        """
        Cериализует Python объект в строку
        """
        pass

    @abstractmethod
    def load(self, file_path: str) -> all:
        """
        Десериализует Python объект из файла
        """
        pass

    @abstractmethod
    def loads(self, target_str) -> all:
        """
        Десериализует Python объект из строки
        """
        pass