from decimal import Decimal
from collections import Counter
import json


def get_bookkipping(payload):
    validate(payload)
    products = payload["invoice_lines"]
    payments = payload["payments"]

    categories = get_categories(products)
    all_products_total = get_products_total(products)
    total_per_category = get_total_per_category(products, categories)
    percentage_per_category = get_percentage_per_category(total_per_category, all_products_total)
    categorizations = calculate_categorizations(payments, percentage_per_category)
    return json.dumps(categorizations)


def get_categories(products: list) -> list[str]:
    """
    Get a list of all products
    """
    return {i["category"] for i in products}


def get_products_total(products: list) -> Decimal:
    """
    Get all the products total by adding each item price * quantity
    """
    return sum(Decimal(prod["unit_price_net"]) * Decimal(prod["quantity"]) for prod in products)


def get_total_per_category(products: list, categories: list) -> dict:
    """
    Get category total by adding each item price * quantity of the same category and return it as a dict
    """
    # Counter will contain the total sum of each category. Ex: {'Clothes': 5.00}, {'Bags': 10.00}, etc
    counter = Counter()
    for prod in products:
        if prod["category"] in categories:
            # This sums all items price of the same category
            counter.update({prod["category"]: Decimal(prod["unit_price_net"]) * Decimal(prod["quantity"])})
    return dict(counter)


def get_percentage_per_category(total_per_category: dict, all_products_total: Decimal) -> dict:
    percentage_per_category = total_per_category.copy()

    for category, total in total_per_category.items():
        percentage_per_category[category] = total/all_products_total
    return percentage_per_category

# Original
# def calculate_categorizations(payments: list, percentage_per_category: dict) -> dict:
#     categorizations = []
#     for paymnt in payments:
#         dictionary = {"id": paymnt["id"], "categorizations": []}
#         for category, percentage in percentage_per_category.items():
#             # Each category dictionary looks like this: {'category': 'Clothes', 'net_amount': '18.00'}
#             result = get_category_dictionary(category, percentage, paymnt["amount"])
#             dictionary["categorizations"].append(result)
#         categorizations.append(dictionary)

#     print(f"{categorizations=}")
#     return categorizations


def calculate_categorizations(payments: list, percentage_per_category: dict) -> dict:
    categorizations = []

    for paymnt in payments:
        print(f"Type?: {type(paymnt['amount'])}")
        estimated_amount = Decimal(0)
        dictionary = {"id": paymnt["id"], "categorizations": []}

        for index, (category, percentage) in enumerate(percentage_per_category.items()):
            print(f"index: {index}, key: {category}, value: {percentage}")
            net_amount = decimal_to_str((percentage * Decimal(paymnt['amount'])))
            estimated_amount += Decimal(net_amount)

            if index == len(percentage_per_category) - 1 and estimated_amount != Decimal(paymnt['amount']):
                net_amount = rounder(paymnt['amount'], net_amount, estimated_amount)

            dictionary["categorizations"].append({"category": category, "net_amount": net_amount})

        categorizations.append(dictionary)

    print(f"{categorizations=}")
    return categorizations


def rounder(total_amount, net_amount, estimated_amount):
    offset = Decimal(total_amount) - estimated_amount
    net_amount = Decimal(net_amount) + offset
    return str(net_amount)


# def get_category_dictionary(category, percentage, payment_amount):
#     print(f"{percentage=}")
#     net_amount = decimal_to_str((percentage * Decimal(payment_amount)))
#     return {"category": category, "net_amount": net_amount}


def decimal_to_str(amount: Decimal) -> str:
    return f"{amount:.2f}"


# def round_categorization(categorizations: list, payments: list) -> list:
#     # [print(f"{i['categorizations']=}") for i in categorization]
#     [[print(f"{j['net_amount']}") for j in i['categorizations']] for i in categorizations]
#     # [[j for j in range(5)] for i in range(5)]

#     for each_id in categorizations:
#         amounts = []
#         for category in each_id["categorizations"]:
#             print(category['net_amount'])
#             amounts.append(category['net_amount'])

#     return categorizations


def validate(payload):
    pass


def print_list(lista):
    for i in lista:
        print(f"{i=}")
