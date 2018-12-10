#!/usr/local/bin/python3.4
from inspect import isgeneratorfunction

def does_fn_consume_input_incrementally(fn):
    assert isgeneratorfunction(fn)
    # ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓ 
    #‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
    print(fn)
    return True # TODO: Replace this stub with real code.




    #____________________________________________________________
    # ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  

if __name__ == "__main__":
    def _test_lightly():
        # These tests are not comprehensive.  They are here to avoid simple mistakes
        # and misunderstandings.  Passing these does NOT guarantee a perfect score.
        assert does_fn_consume_input_incrementally(good_double) is True
        assert does_fn_consume_input_incrementally(bad_double)  is False

    def good_double(integers):  # GENERATOR FUNCTION
        for n in integers:
            yield n * 2

    def bad_double(integers):   # GENERATOR FUNCTION
        integers = list(integers)  # <--- BAD - needlessly converts input to list
        for n in integers:
            yield n * 2

    _test_lightly()

#____________________________________________________________
# NAME
#        does_fn_consume_input_incrementally(..) - Test whether a function
#        consumes its input (generator) incrementally
# 
# SYNOPSIS
#        does_fn_consume_input_incrementally(«FN»)
# 
# DESCRIPTION
#        When passing a generator to a generator function, it is usually most
#        efficient if the generator only consumes one item from its input for every
#        item that it yields.  Poorly written functions may needlessly convert
#        their input to a sequence (e.g., list or tuple).
#
#        does_fn_consume_input_incrementally(…) should return False if the function
#        consumes the entire generator to yield just one value.  Otherwise, return
#        True.  (See the examples.)
#
#        FN is a Python generator function which takes a generator of integers as
#        its sole parameter, and returns a generator of integers.
#
#
# DETAILS
#        ∙ No error handling is expected.  Assume all inputs are of the right type.
#        ∙ You may add helper functions if you wish, but that is not necessary.
#        ∙ This is a Python function, not a command line utility.
#        ∙ Instructor solution is 5 sloc / 293 characters
#____________________________________________________________
# vim: set fileencoding=utf8 expandtab tabstop=4 shiftwidth=4:
