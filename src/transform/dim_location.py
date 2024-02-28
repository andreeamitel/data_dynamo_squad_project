def dim_location(address_df):
    """
    This function takes one dataframe,
    address and returns
    dim_location dataframe.

    Args:
    'address' dataframe
    Returns:
    dim_location dataframe
    """
    dim_location_df = address_df.copy(deep=True)
    dim_location_df = dim_location_df.drop(
        columns=["created_at", "last_updated"])
    dim_location_df = dim_location_df.rename(
        columns={"address_id": "location_id"}
    )
    dim_location_df = dim_location_df[
        ["location_id",
         "address_line_1",
         "address_line_2",
         "district",
         "city",
         "postal_code",
         "country",
         "phone"
         ]
    ]
    return dim_location_df
