import copy


def dim_staff(staff_table_data, department_table_data):
    staff_dict = copy.deepcopy(staff_table_data)
    dep_dict = copy.deepcopy(department_table_data)
    dim_staff = {
        "dim_staff": [
            {
                "staff_id": staff["staff_id"],
                "first_name": staff["first_name"],
                "last_name": staff["last_name"],
                "email_address": staff["email_address"],
                "department_name": dep["department_name"],
                "location": dep["location"],
            }
            for staff in staff_dict["staff"]
            for dep in dep_dict["department"]
            if staff["department_id"] == dep["department_id"]
        ]
    }
    return dim_staff
