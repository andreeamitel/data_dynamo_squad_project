import copy

def dim_staff(staff_table_data, department_table_data):
    staff_dict = copy.deepcopy(staff_table_data)
    dep_dict = copy.deepcopy(department_table_data)
    dim_staf = {"dim_staff": []}
    for staff in staff_dict['staff']:
        dim_staff_obj = {
                'staff_id': staff['staff_id'],
                'first_name': staff['first_name'],
                'last_name': staff['last_name'],
                'email_address': staff['email_address'],
            }
        for dep in dep_dict['department']:
            if staff['department_id'] == dep['department_id']:
                dim_staff_obj['department_name'] = dep['department_name']
                dim_staff_obj['location'] = dep['location']
        dim_staf['dim_staff'].append(dim_staff_obj)
    return dim_staf
