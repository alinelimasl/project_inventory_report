import json
from typing import Dict, Type
import abc

from inventory_report.product import Product


class Importer(abc.ABC):
    def __init__(self, path: str):
        self.path = path

    @abc.abstractmethod
    def import_data(self) -> list[Product]:
        pass


class JsonImporter(Importer):
    def import_data(self) -> list[Product]:
        with open(self.path) as file:
            data = json.load(file)

        products = []
        for item in data:
            product = Product(
                id=item["id"],
                product_name=item["product_name"],
                company_name=item["company_name"],
                manufacturing_date=item["manufacturing_date"],
                expiration_date=item["expiration_date"],
                serial_number=item["serial_number"],
                storage_instructions=item["storage_instructions"],
            )
            products.append(product)

        return products


class CsvImporter:
    pass


# Não altere a variável abaixo

IMPORTERS: Dict[str, Type[Importer]] = {
    "json": JsonImporter,
    "csv": CsvImporter,
}
