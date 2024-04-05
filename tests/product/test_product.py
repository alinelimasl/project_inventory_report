from inventory_report.product import Product


def test_create_product() -> None:
    data = Product(
        id="6511",
        product_name="ad",
        company_name="Silveira Peixoto - EI",
        manufacturing_date="2023-09-15",
        expiration_date="2083-10-08",
        serial_number="SX80 B8JR 3709 27JT 7736 LJSS 2X1R",
        storage_instructions="Voluptatem eius quaerat veritatis "
        "facere fuga.",
    )

    assert data.id == "6511"
    assert data.product_name == "ad"
    assert data.company_name == "Silveira Peixoto - EI"
    assert data.manufacturing_date == "2023-09-15"
    assert data.expiration_date == "2083-10-08"
    assert data.serial_number == "SX80 B8JR 3709 27JT 7736 LJSS 2X1R"
    assert (
        data.storage_instructions
        == "Voluptatem eius quaerat veritatis facere fuga."
    )
