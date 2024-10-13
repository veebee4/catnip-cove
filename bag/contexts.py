from decimal import Decimal
from django.conf import settings

def bag_contents(request):
    bag_items = []
    total = 0
    donation_count = 0
    
    # Determine if a cuddly toy should be added & how much to spend to get free toy
    if total < settings.DONATION_THRESHOLD:
        add_cuddly_toy = False
        amount_to_get_free_toy = settings.DONATION_THRESHOLD - total
    else:
        amount_to_get_free_toy = 0
        add_cuddly_toy = True

    # Return all relevant context information
    context = {
        'bag_items': bag_items,
        'total': total,
        'donation_count': donation_count,
        'add_cuddly_toy': add_cuddly_toy,
        'amount_to_get_free_toy': amount_to_get_free_toy,
        'donation_threshold': settings.DONATION_THRESHOLD,
    }

    return context
