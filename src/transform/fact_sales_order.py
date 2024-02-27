import pandas as pd


# def fact_sales_order(sales_order):
#     """
#     This function takes a dictionary from the sales
#     table and returns amended dictionary for the fact_sales_order table table.

#     Args:
#     'sales_order' table_list

#     Returns:
#     fact_sales_order table dict

#     """

#     sales_order_copy = copy.deepcopy(sales_order)
   

#     # sales_order_table, dim_date_table = dim_date(sales_order_copy)


#     fact_sales_order_table = {
#         "fact_sales_order": sales_order_copy["sales_order"]}
#     start3 = time.time()
#     for sale in fact_sales_order_table["fact_sales_order"]:
#         sale["sales_record_id"] = sale["sales_order_id"]
#         sale["sales_staff_id"] = sale["staff_id"]
#         del sale["staff_id"]
    
    
#     return fact_sales_order_table

def fact_sales_order(sales_df):
    sales_copy = sales_df.copy(deep=True)
    sales_copy["created_date"] = sales_copy["created_at"].map(lambda x: x.split("T")[0])
    sales_copy["created_time"] = sales_copy["created_at"].map(lambda x: x.split("T")[1])
    sales_copy = sales_copy.drop(columns= ["created_at", "last_updated"])
    sales_copy = sales_copy.rename(columns= {"staff_id": "sales_staff_id"})
    sales_copy = sales_copy[["sales_order_id", "created_date", "created_time", "sales_staff_id", "counterparty_id", "units_sold", "unit_price", "currency_id", "design_id", "agreed_payment_date", "agreed_delivery_date", "agreed_delivery_location_id"]]
    return sales_copy