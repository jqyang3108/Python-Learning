#! /user/local/bin/python3.4

from inspect import getmembers, isfunction


def print_success(module_name):
    print("-------------------------------")
    print("Code file '{}' imported successfully.".format(module_name))
    print("-------------------------------")
    print()


def fail_safe(module_name):
    print("-------------------------------")
    print("Cannot import '{}'. File is missing or cannot be compiled.".format(module_name))
    print("-------------------------------")
    print()
    exit(-1)


def load_module(function_names):

    # Obtain all functions in the code.
    present_functions = [fn_name for fn_name, _ in getmembers(student, isfunction)]

    # Check whether each function is present or missing, and print out the result.
    for fn_index, fn_name in enumerate(function_names):

        if fn_name in present_functions:
            print('{:02d}- Function "{}" located.'.format(fn_index + 1, fn_name))
        else:
            print('{:02d}- =======> Unable to locate the function "{}".'.format(fn_index + 1, fn_name))


# Define desired functions that should be present.
function_names = ["check_network", "is_ok", "load_data_from", "is_bounded"]
module_name = "module_tasks"

# Attempt to import the code, and fail otherwise.
try:
    import module_tasks as student
except:
    fail_safe(module_name)
else:
    print_success(module_name)

load_module(function_names)

print("\n" * 3)

# Define desired functions that should be present.
function_names = ["load_multiple", "save_data"]
module_name = "signals"

# Attempt to import the code, and fail otherwise.
try:
    import signals as student
except:
    fail_safe(module_name)
else:
    print_success(module_name)

load_module(function_names)

