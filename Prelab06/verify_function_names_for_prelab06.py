#! /user/local/bin/python3.4

from inspect import getmembers, isfunction

# Define desired functions that should be present.
functionNames = ["get_url_parts", "get_query_parameters", "get_special", "get_real_mac", "get_rejected_entries",
                 "get_employees_with_ids", "get_employees_without_ids", "get_employees_with_phones", "get_employees_with_states",
                 "get_complete_entries"]

# Attempt to import the code, and fail otherwise.
try:
    import regex_app as student
except:
    print("-------------------------------")
    print("Unable to find expected file.")
    print("-------------------------------")
    print()
    exit(-1)
else:
    print("-------------------------------")
    print("Code file imported successfully.")
    print("-------------------------------")
    print()

# Obtain all functions in the code.
presentFunctions = [fnName for fnName, _ in getmembers(student, isfunction)]

# Check whether each function is present or missing, and print out the result.
for fnIndex, fnName in enumerate(functionNames):

    if fnName in presentFunctions:
        print('{:02d}- Function "{}" located.'.format(fnIndex + 1, fnName))
    else:
        print('{:02d}- =======> Unable to locate the function "{}".'.format(fnIndex + 1, fnName))
