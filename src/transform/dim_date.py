import copy
import re
from datetime import datetime
import calendar


def dim_date(sales_order):
    """
    This function takes a dictionary from the design table and return amended  dictionary for the dim_design table.

    Args:
    'design' table_list

    Returns:
    dim_design table dict

    """
    sales_order = copy.deepcopy(sales_order)
    dim_date_set = set()
    dim_date = {"dim_date": []}
    # format_date = "%Y-%m-%d"
    for sale in sales_order["sales_order"]:
        created_date_time = sale["created_at"].split("T")
        sale["created_date"] = created_date_time[0]
        sale["created_time"] = created_date_time[1]
        del sale["created_at"]
        last_updated_date_time = sale["last_updated"].split("T")
        sale["last_updated_date"] = last_updated_date_time[0]
        sale["last_updated_time"] = last_updated_date_time[1]
        del sale["last_updated"]
        sale_date_set = set((
            sale["created_date"],
            sale["last_updated_date"],
            sale["agreed_delivery_date"],
            sale["agreed_payment_date"],
        ))
        dim_date_set.update(sale_date_set)
    
    for date in dim_date_set:
        foo = date.split('-')
        dt = datetime(int(foo[0]), int(foo[1]), int(foo[2]))
        dim_date["dim_date"].append({
            'date_id': date,
            'year': int(foo[0]),
            'month': int(foo[1]),
            'day': int(foo[2]),
            'day_of_week': dt.isoweekday(),
            'day_name': calendar.day_name[dt.weekday()],
            'month_name': calendar.month_name[int(foo[1])],
            'quarter': int(f'{(int(foo[1])-1)//3+1}')
        })
        
        

        

    return sales_order, dim_date
