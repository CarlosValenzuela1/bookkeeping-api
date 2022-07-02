import json
from collections import Counter
from decimal import Decimal


def calculate_bookkeeping(payload: dict) -> dict:
    """
    Main method to calculate the bookkeeping (categorisations)
    """
    products = payload['invoice_lines']
    payments = payload['payments']

    categories = get_categories(products)
    products_total = sum_products_total(products)
    total_per_category = calculate_total_per_category(products, categories)
    percentage_per_category = calculate_percentage_per_category(total_per_category, products_total)

    categorisations = calculate_categorisations(payments, percentage_per_category)

    return json.dumps(categorisations)


def get_categories(products: list) -> list[str]:
    """
    Get a list of all categories
    """
    return {i['category'].capitalize() for i in products}


def sum_products_total(products: list) -> Decimal:
    """
    Sum the total amount of all products by adding each item price * quantity
    """
    return sum(Decimal(prod['unit_price_net']) * Decimal(prod['quantity']) for prod in products)


def calculate_total_per_category(products: list, categories: list) -> dict:
    """
    Calculates the sum of all products' amount, by adding each item price * quantity of the same category and return it as a dict. Ex: {'Clothes': 5.00, 'Bags': 10.00}
    """
    counter = Counter()
    for prod in products:
        if prod['category'].capitalize() in categories:
            # This sums all items price of the same category
            counter.update({prod['category'].capitalize(): Decimal(prod['unit_price_net']) * Decimal(prod['quantity'])})
    return dict(counter)


def calculate_percentage_per_category(total_per_category: dict, all_products_total: Decimal) -> dict:
    """
    Calculates the percentage needed for categorization for each category, by dividing the category total by all products total. Ex: {'Clothes': '0.05..8', 'Posters': '0.05..8'}
    """
    percentage_per_category = total_per_category.copy()

    for category, total in total_per_category.items():
        percentage_per_category[category] = total/all_products_total
    return percentage_per_category


def calculate_categorisations(payments: list, percentage_per_category: dict) -> dict:
    """
    Calculates the payment of each categorization and for each category, rounding where needed
    """
    categorisations = []

    for paymnt in payments:
        estimated_amount = Decimal(0)
        dictionary = {'id': paymnt['id'], 'categorisations': []}

        for index, (category, percentage) in enumerate(percentage_per_category.items()):
            current_category_amount = '{:.2f}'.format(percentage * Decimal(paymnt['amount']))
            estimated_amount += Decimal(current_category_amount)

            # At the last category of the current payment, we verify that our estimated amount and the expected amount (paymnt['amount']) is the same, otherwise we round it
            if index == len(percentage_per_category) - 1 and estimated_amount != Decimal(paymnt['amount']):
                current_category_amount = rounder(paymnt['amount'], current_category_amount, estimated_amount)

            dictionary['categorisations'].append({'category': category, 'net_amount': current_category_amount})

        categorisations.append(dictionary)

    return categorisations


def rounder(total_amount: str, current_amount: str, estimated_amount: Decimal) -> str:
    """
    Sums the offset needed to have an exact match between the expected amount and the calculated amount
    """
    offset = Decimal(total_amount) - estimated_amount
    return str(Decimal(current_amount) + offset)
