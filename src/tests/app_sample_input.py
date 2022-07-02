"""
Sample inputs for the validation tests
"""

validation_case_1 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi bag",
            "quantity": 1,
            "category": "Bags",
            "unit_price_net": "2.00"
        }
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}

validation_case_2 = {
    "payments": [
        {
            "id": 1,
            "amount": "50.00"
        },
        {
            "id": 2,
            "amount": "200.00"
        }
    ]
}

validation_case_3 = {
    "invoice_lines": [],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}

validation_case_4 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi bag",
            "quantity": 1,
            "category": "Bags",
            "unit_price_net": "2.00"
        }
    ],
    "payments": []
}

validation_case_5 = {
    "invoice_lines": [
        {
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.00"
        }
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}

validation_case_6 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.00"
        }
    ],
    "payments": [
        {
            "amount": "4.45"
        }
    ]
}

validation_case_7 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": "1",
            "category": "Clothes",
            "unit_price_net": "2.00"
        }
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}
