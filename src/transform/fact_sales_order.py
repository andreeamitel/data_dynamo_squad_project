import copy
import time


def fact_sales_order(sales_order):
    """
    This function takes a dictionary from the sales
    table and returns amended dictionary for the fact_sales_order table table.

    Args:
    'sales_order' table_list

    Returns:
    fact_sales_order table dict

    """
    start1 = time.time()
    sales_order_copy = copy.deepcopy(sales_order)
    end1 = time.time()
    print(end1 - start1, "this is how long deepcopy took")
    start2 = time.time()

    # sales_order_table, dim_date_table = dim_date(sales_order_copy)
    end2 = time.time()
    print(end2 - start2, "this is how dim dates took")

    fact_sales_order_table = {
        "fact_sales_order": sales_order_copy["sales_order"]}
    start3 = time.time()
    for sale in fact_sales_order_table["fact_sales_order"]:
        sale["sales_record_id"] = sale["sales_order_id"]
        sale["sales_staff_id"] = sale["staff_id"]
        del sale["staff_id"]
    end3 = time.time()
    print(end3 - start3)
    return fact_sales_order_table
