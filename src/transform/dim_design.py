import copy


def dim_design(table_dict):
    """
    This function takes a dictionary from the design table and return amended  dictionary for the dim_design table.

    Args:
    'design' table_list

    Returns:
    dim_design table dict

    """
    dim_design_table = copy.deepcopy(table_dict["design"])
    for design in dim_design_table:
        del design["created_at"]
        del design["last_updated"]
    return {"dim_design": dim_design_table}
