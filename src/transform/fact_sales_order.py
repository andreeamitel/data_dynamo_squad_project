def fact_sales_order(sales_df):
    sales_copy = sales_df.copy(deep=True)
    sales_copy["created_date"] = sales_copy["created_at"].map(lambda x: x.split("T")[0])
    sales_copy["created_time"] = sales_copy["created_at"].map(lambda x: x.split("T")[1])
    sales_copy = sales_copy.drop(columns=["created_at", "last_updated"])
    sales_copy = sales_copy.rename(
        columns={
            "staff_id": "sales_staff_id",
            "counterparty_id": "counterparty_record_id",
            "currency_id": "currency_record_id",
            "design_id": "design_record_id",
        }
    )
    sales_copy = sales_copy[
        [
            "sales_order_id",
            "created_date",
            "created_time",
            "sales_staff_id",
            "counterparty_record_id",
            "units_sold",
            "unit_price",
            "currency_record_id",
            "design_record_id",
            "agreed_payment_date",
            "agreed_delivery_date",
            "agreed_delivery_location_id",
        ]
    ]
    return sales_copy
