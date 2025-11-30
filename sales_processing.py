# sales_processing.py

def calc_total_sales(orders):
    """
    REQ-01:
    Calculate the total sales amount.
    Each order dict contains: {"item": "...", "qty": X, "price": Y}
    Total sales = sum of (qty * price) for all orders.
    If list is empty, return 0.
    """
    # Add your implementation here
    sales = 0 
    if len(orders) == 0:
        return 0
    for item in orders:
        sales += item['qty'] * item['price']

    return sales    


def calc_average_order_value(orders):
    """
    REQ-02:
    Calculate the average order value.
    Order value = qty * price for each record.
    Return a float.
    If list is empty, return None.
    """
    # Add your implementation here
    sales = 0
    if len(orders)==0:
        return None
    for item in orders:
        sales += item['qty'] * item['price']
    return sales/len(orders)    


def find_max_order(orders):
    """
    REQ-03:
    Return the order dictionary with the highest order value (qty * price).
    If list is empty, return None.
    """
    # Add your implementation here
    
    if len(orders) ==0:
        return None
    longest = orders[0]
    for item in orders:
        item_value = item['qty'] * item['price']
        longest_value = longest['qty'] * longest['price']
        if item_value > longest_value:
            longest = item
    return longest

def filter_items_above_threshold(orders, threshold):
    """
    REQ-04:
    Return a list of orders where (qty * price) > threshold.
    If none match, return an empty list [].
    """
    # Add your implementation here
    result = []
    for item in orders:
        total_value = item['qty'] * item['price']
        if total_value > threshold:
            result.append(item)
    return result