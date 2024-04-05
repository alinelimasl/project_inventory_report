from inventory_report.product import Product


def test_product_report() -> None:
    data = Product(
        id="1234",
        product_name="farinha",
        serial_number="TY68 409C JJ43 ASD1 PL2F",
        manufacturing_date="01-05-2021",
        company_name="Farinini",
        expiration_date="02-06-2023",
        storage_instructions="protegido da luz",
    )

    assert str(data) == (
        "The product 1234 - farinha with serial number TY68 409C JJ43 ASD1 "
        "PL2F manufactured on 01-05-2021 by the company Farinini valid until "
        "02-06-2023 must be stored according to the following instructions: "
        "protegido da luz."
    )
