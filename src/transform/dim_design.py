def dim_design(design_df):
    """
    This function takes the design dataframe
    and returns amended dim_design dataframe.

    Args:
    'design_df' - pandas dataframe

    Returns:
    dim_design_df - pandas dataframe with ammendments
    """
    design_copy = design_df.copy(deep=True)
    design_copy = design_copy.drop(columns=["last_updated", "created_at"])
    return design_copy
