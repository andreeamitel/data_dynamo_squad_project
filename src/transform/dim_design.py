import copy

def dim_design(table_list):
    """
    This function takes a list of dictionary from the design table and return amended list of dictionaries for the dim_design table.

    Args:
    'design' table_list

    Returns:
    dim_design table list of dict

    """
    dim_design_table = copy.deepcopy(table_list)
    for design in dim_design_table:
        del design["created_at"]
        del design["last_updated"]
    return dim_design_table