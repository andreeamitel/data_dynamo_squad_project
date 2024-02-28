# import copy
import pandas as pd


def dim_staff(staff_df, department_df):
    staff_copy = staff_df.copy(deep=True)
    department_copy = department_df.copy(deep=True)
    dim_staff = pd.merge(staff_copy, department_copy, on="department_id")
    dim_staff = dim_staff.drop(
        columns=[
            "department_id",
            "created_at_x",
            "last_updated_x",
            "created_at_y",
            "last_updated_y",
            "manager",
        ]
    )
    dim_staff = dim_staff[
        [
            "staff_id",
            "first_name",
            "last_name",
            "department_name",
            "location",
            "email_address",
        ]
    ]
    return dim_staff
