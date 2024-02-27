from datetime import datetime
import pandas as pd


# def dim_date(sales_order):

#     """
#     This function takes a dictionary from the design table and return amended  dictionary for the dim_design table.

#     Args:
#     'design' table_list

#     Returns:
#     dim_design table dict

#     """
#     sales_order = copy.deepcopy(sales_order)
#     dim_date_set = set()
#     for sale in sales_order["sales_order"]:
#         created_date_time = sale["created_at"].split("T")
#         sale["created_date"] = created_date_time[0]
#         sale["created_time"] = created_date_time[1]
#         del sale["created_at"]
#         last_updated_date_time = sale["last_updated"].split("T")
#         sale["last_updated_date"] = last_updated_date_time[0]
#         sale["last_updated_time"] = last_updated_date_time[1]
#         del sale["last_updated"]
#         sale_date_set = set(
#             (
#                 sale["created_date"],
#                 sale["last_updated_date"],
#                 sale["agreed_delivery_date"],
#                 sale["agreed_payment_date"],
#             )
#         )
#         dim_date_set.update(sale_date_set)

#     dim_date_table = {"dim_date": []}
#     for date in dim_date_set:
#         split_date = date.split("-")
#         dt = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
#         dim_date_table["dim_date"].append(
#             {
#                 "date_id": date,
#                 "year": int(split_date[0]),
#                 "month": int(split_date[1]),
#                 "day": int(split_date[2]),
#                 "day_of_week": dt.isoweekday(),
#                 "day_name": calendar.day_name[dt.weekday()],
#                 "month_name": calendar.month_name[int(split_date[1])],
#                 "quarter": int(f"{(int(split_date[1])-1)//3+1}"),
#             }
#         )

#     return sales_order, dim_date_table


def dim_date(sales_order_dataframe):
    dates_df = sales_order_dataframe.copy(deep=True)
    dates_df = dates_df.drop(
        columns=[
            "sales_order_id",
            "design_id",
            "staff_id",
            "counterparty_id",
            "units_sold",
            "unit_price",
            "currency_id",
            "agreed_delivery_location_id",
        ]
    )
    dates_df["created_date"] = dates_df["created_at"].map(lambda x: x.split("T")[0])
    dates_df["updated_date"] = dates_df["last_updated"].map(lambda x: x.split("T")[0])
    dates_df = dates_df.drop(columns=["created_at", "last_updated"])

    dates_df = pd.melt(
        dates_df,
        value_vars=[
            "agreed_delivery_date",
            "agreed_payment_date",
            "created_date",
            "updated_date",
        ],
        value_name="date_id",
        var_name=None,
    )
    dates_df = dates_df.drop(columns=["variable"]).drop_duplicates()

    dates_df["year"] = dates_df["date_id"].map(lambda x: x.split("-")[0])
    dates_df["month"] = dates_df["date_id"].map(lambda x: x.split("-")[1])
    dates_df["day"] = dates_df["date_id"].map(lambda x: x.split("-")[2])
    dates_df["day_of_week"] = dates_df["date_id"].map(lambda x: get_day_of_week(x))
    dates_df["day_name"] = dates_df["date_id"].map(lambda x: get_name_of_day(x))
    dates_df["month_name"] = dates_df["date_id"].map(lambda x: get_name_of_month(x))
    dates_df["quarter"] = dates_df["date_id"].map(
        lambda x: ((int(x.split("-")[1]) - 1) // 3) + 1
    )

    return dates_df


def get_day_of_week(date):
    split_date = date.split("-")
    dt = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    return dt.isoweekday()


def get_name_of_day(date):
    split_date = date.split("-")
    dt = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    return dt.strftime("%A")


def get_name_of_month(date):
    split_date = date.split("-")
    dt = datetime(int(split_date[0]), int(split_date[1]), int(split_date[2]))
    return dt.strftime("%B")
