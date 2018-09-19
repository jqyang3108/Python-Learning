#! /user/local/bin/python3.4

from inspect import getmembers, isfunction

# Define desired functions that should be present.
function_names = ['get_distinct_words', 'get_first_appearances', 'get_word_to_first_idx', 'get_word_to_frequency','get_word_to_frequency_ordered_by_first_idx']

# Attempt to import the code, and fail otherwise.
try:
    import text_utils as student
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
present_functions = [fn_name for fn_name, _ in getmembers(student, isfunction)]

# Check whether each function is present or missing, and print out the result.
for fn_index, fn_name in enumerate(function_names):

    if fn_name in present_functions:
        print('{:02d}- Function "{}" located.'.format(fn_index + 1, fn_name))
    else:
        print('{:02d}- =======> Unable to locate the function "{}".'.format(fn_index + 1, fn_name))
