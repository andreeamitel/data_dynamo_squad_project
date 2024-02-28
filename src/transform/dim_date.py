from datetime import datetime
import pandas as pd


def dim_date(sales_order_dataframe):
    """
    This function takes a sales order dataframe
    and returns an amended dim_dates dataframe.

    Args:
    'sales_order_dataframe' pandas dataframe

    Returns:
    dim_date_df pandas dataframe

    """
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
    dates_df["created_date"] = dates_df["created_at"].map(
        lambda x: x.split("T")[0]
        )
    dates_df["updated_date"] = dates_df["last_updated"].map(
        lambda x: x.split("T")[0]
        )
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
    dates_df["day_of_week"] = dates_df["date_id"].map(
        lambda x: get_day_of_week(x)
        )
    dates_df["day_name"] = dates_df["date_id"].map(
        lambda x: get_name_of_day(x)
        )
    dates_df["month_name"] = dates_df["date_id"].map(
        lambda x: get_name_of_month(x)
        )
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
