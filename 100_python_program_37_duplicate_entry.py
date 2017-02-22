'''
Programs:100_python_program_37_duplicate_entry.py
Duplicate Entries in a List
'''

def duplicate_entries(list):
    new_list = set()
    duplicate_list = []
    for val in list:
        if not val in new_list:
            new_list.add(val)

        else:
            duplicate_list.append(val)


    print duplicate_list

duplicate_entries([1,2,3,4,5,6,5,4,3,55,66,7])
