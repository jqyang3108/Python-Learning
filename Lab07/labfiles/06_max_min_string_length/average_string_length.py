#!/usr/local/bin/python3.4
'''
This module provides two functions:

    calculate_max_string_length(strings)
     - Returns the length of the longest string
     - Argument is a sequence of strings

    calculate_min_string_length(a)
     - Returns the length of the longest string
     - Argument is a sequence of strings
'''

# ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓  ↓ 
#‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
# Calculates the maximum string length
def calculate_max_string_length(strings):
    max_length = None  # will hold the minimum length
    for s in strings:
        if not max_length or len(s) > max_length:
            max_length = len(s)
    return max_length

# Calculates the minimum string length
def calculate_min_string_length(strings):
        minLength = None  # will hold the minimum length
        for s in strings:
                if not minLength or len(s) < minLength:
                        minLength = len(s)
        return minLength


def calculate_max_string_length_OLD_VERSION(strings):
    max_length = -1  # will hold the minimum length
    for i in range(len(strings)):
        s = strings[i]
        if max_length is None or len(string) >= max_length:
            max_length = len(string)
    return max_length
#____________________________________________________________
# ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  ↑  


if __name__ == "__main__":
    def _test_lightly():
        # These tests are not comprehensive.  They are here to avoid simple mistakes
        # and misunderstandings.  Passing these does NOT guarantee a perfect score.
        assert calculate_max_string_length(["a", "ab", "abc"]) == 3
        assert calculate_min_string_length(["a", "ab", "abc"]) == 1

    _test_lightly()

#____________________________________________________________
#
# CODE QUALITY CLEAN-UP
#
# This code is sloppy and has one bug.
# 
# Fix the bug and improve the code quality of everything above so that it
# follows the code quality standards used in this course.
#
# Make only the MINIMUM changes necessary to make it correct and compliant.
# There may be penalties for over-zealous clean-up or other changes which are
# not related to code quality.
#
# You may ignore the doc string at the top and everything below
# if __name__ == "__main__" sections.
#
# CLARIFICATION:  To clarify a point in the code quality standards, only the specific
# single-letter names listed in that document are allowed for code in this course.
#
# vim: set fileencoding=utf8 expandtab tabstop=4 shiftwidth=4:
