from transform.dim_date import dim_date
import copy

def fact_sales_order(sales_order):
    sales_order_copy = copy.deepcopy(sales_order)
    sales_order_table, dim_date_table = dim_date(sales_order_copy)
    fact_sales_order_table = {"fact_sales_order": sales_order_table["sales_order"]}
    for sale in fact_sales_order_table["fact_sales_order"]:
        sale["sales_record_id"] = sale["sales_order_id"]
        sale["sales_staff_id"] = sale["staff_id"]
        del sale["staff_id"]


    return  fact_sales_order_table, dim_date_table
    