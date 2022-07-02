"""
Sample inputs for the bookkipping tests
"""

bookkipping_case_1 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 2,
            "category": "Clothes",
            "unit_price_net": "25.00"
        },
        {
            "description": "Holvi hoodie",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "40.00"
        },
        {
            "description": "Holvi poster",
            "quantity": 4,
            "category": "Posters",
            "unit_price_net": "40.00"
        }
    ],
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


bookkipping_case_2 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.55"
        },
        {
            "description": "Holvi poster",
            "quantity": 1,
            "category": "Posters",
            "unit_price_net": "2.55"
        },
        {
            "description": "Holvi gift card",
            "quantity": 1,
            "category": "Gift cards",
            "unit_price_net": "43.90"
        }
    ],
    "payments": [
        {
            "id": 3,
            "amount": "3.00"
        }
    ]
}


bookkipping_case_3 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 1,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi poster",
            "quantity": 1,
            "category": "Posters",
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

bookkipping_case_4 = {
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
            "id": 4,
            "amount": "4.45"
        }
    ]
}

bookkipping_case_5 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 3,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi poster",
            "quantity": 9,
            "category": "Posters",
            "unit_price_net": "2.00"
        },
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}


bookkipping_case_6 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 3,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi T-shirt",
            "quantity": 9,
            "category": "Clothes",
            "unit_price_net": "5.00"
        }
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        }
    ]
}

bookkipping_case_7 = {
    "invoice_lines": [
        {
            "description": "Holvi T-shirt",
            "quantity": 3,
            "category": "Clothes",
            "unit_price_net": "2.00"
        },
        {
            "description": "Holvi poster",
            "quantity": 9,
            "category": "Posters",
            "unit_price_net": "3.00"
        }
    ],
    "payments": [
        {
            "id": 4,
            "amount": "4.45"
        },
        {
            "id": 5,
            "amount": "5.69"
        }
    ]
}
