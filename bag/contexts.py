"""
    This function makes the below dictionary available to all templates across
    the application
"""

def bag_contents(request):
    """ A function / context processor that returns a dictionary"""

    bag_items = []
    total = 0
    product_count = 0

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
