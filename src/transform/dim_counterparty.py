import pandas as pd


def dim_counterparty(address_df, counterparty_df):
    """
    This function takes a two dataframes,
    counterparty and address returns
    dim_counterparty dataframe.

    Args:
    'counterparty' and 'address' dataframes
    Returns:
    dim_counterparty dataframe
    """
    address_copy = address_df.copy(deep=True)
    counterparty_copy = counterparty_df.copy(deep=True)
    counterparty_copy = counterparty_copy.rename(
        columns={"legal_address_id": "address_id"}
    )

    dim_counterparty_df = pd.merge(
        address_copy, counterparty_copy, on="address_id"
        )

    dim_counterparty_df = dim_counterparty_df.rename(
        columns={
            "address_line_1": "counterparty_legal_address_line_1",
            "address_line_2": "counterparty_legal_address_line_2",
            "district": "counterparty_legal_district",
            "city": "counterparty_legal_city",
            "postal_code": "counterparty_legal_postal_code",
            "country": "counterparty_legal_country",
            "phone": "counterparty_legal_phone_number",
        }
    )
    dim_counterparty_df = dim_counterparty_df.drop(
        columns=[
            "address_id",
            "last_updated_x",
            "last_updated_y",
            "created_at_x",
            "created_at_y",
            "commercial_contact",
            "delivery_contact",
        ]
    )
    dim_counterparty_df = dim_counterparty_df[
        [
            "counterparty_id",
            "counterparty_legal_name",
            "counterparty_legal_address_line_1",
            "counterparty_legal_address_line_2",
            "counterparty_legal_district",
            "counterparty_legal_city",
            "counterparty_legal_postal_code",
            "counterparty_legal_country",
            "counterparty_legal_phone_number",
        ]
    ]
    return dim_counterparty_df
