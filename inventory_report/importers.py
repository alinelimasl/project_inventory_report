from typing import Dict, Type
import abc

from inventory_report.product import Product


class Importer(abc.ABC):
    def __init__(self, path: str):
        self.path = path

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter:
    pass


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
