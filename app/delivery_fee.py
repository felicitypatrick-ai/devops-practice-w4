"""Harbor Street Bakery: delivery fee (demonstration code for the walkthrough video)."""

DELIVERY_FEE = 400  # delivery fee in cents ($4.00)
FREE_DELIVERY_FROM_CENTS = 2000  # orders of $20.00 or more deliver free


def delivery_total(order_cents):
    """Return the order total with delivery, in cents."""
    if order_cents >= FREE_DELIVERY_FROM_CENTS:
        return order_cents
    return order_cents + DELIVERY_FEE
