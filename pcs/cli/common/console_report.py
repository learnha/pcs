from __future__ import (
    absolute_import,
    division,
    print_function,
    unicode_literals,
)

import sys


def warn(message):
    write_message(message, "Warning: ")

def write_message(message, prefix):
    sys.stdout.write("{0}{1}\n".format(prefix, message))

def error(message):
    write_message(message, "Error: ")
    return SystemExit(1)

def indent(line_list, indent_step=2):
    """
    return line list where each line of input is prefixed by N spaces
    list of string line_list are original lines
    int indent_step is count of spaces for line prefix
    """
    return [
        "{0}{1}".format(" "*indent_step, line) if line else line
        for line in line_list
    ]
