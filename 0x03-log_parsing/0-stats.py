#!/usr/bin/python3
"""Log parsing module"""

import re
import sys


def get_size_and_code_nonstrict(line: str):
    """
    Read file size and status code from line.

    Reads the file size and code non-sparingly provided line is a
    valid string.\n
    Does not check validity of the file size or status code.\n
    That is whether file size is an integer between 1 and 1024(exclusive) or
    whether status code is found in status_codes dictionary.

    Therefore extra checks must be done on the values returned from this
    function to check their validity before being used.

    Args:
        line (str): Line of text as red from stdin.

    Returns:
        tuple: Tuple of both size and code.
    """
    size = ""
    code = ""
    i = 0

    for char in reversed(line):
        if char == " ":
            i += 1
        elif not i:
            size += char
        elif i:
            code += char

        if i == 2:
            break
    if size[0] == "\n":
        size = size[1:]
    return (code[-1::-1], size[-1::-1])


def get_size_and_code_strict(line):
    """
    Strictly matches the segment of line with the regex of the format
    required.\n
    This function is not used in matching the line since it skips lines which
    don't exactly adhere to the format or don't contain a portion that does.\n
    It can be used if format of lines being read is strictly required to
    follow the format.

    Format:\n
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" \
<status code> <file size>

        File size => 1 - 1024(exclusive)
        Status codes => [200, 301, 400, 401, 403, 404, 405, 500]

    The following lines pass the search:\n
        128.230.61.246 - [2017-02-05 23:31:23.258076] \
"GET /projects/260 HTTP/1.1" 301 292\n
        8.20.161.246 - [2013-01-05 23:31:23.138174] \
"GET /projects/260 HTTP/1.1" 400 1023\n
        18.0.1.2 - [2022-10-02 24:35:33.258076] \
"GET /projects/260 HTTP/1.1" 500 1

    Args:
        line (str): Line to search in.

    Returns:
        tuple: Tuple containing the file size and status code from the
                matched line if found or empty strings if not successfully
                matched.
    """
    # Regex for matching logs.
    log_regex = re.compile(
        r"(\d{1,3}\.*){4}\s-\s\[\d{4}(-\d{1,2}){2}\s(\d{1,2}:*){3}.\d{6}\]\s" +
        r'"GET /projects/260 HTTP/1.1"\s(\d{3})\s(\d{1,4})'
    )

    try:
        mo = log_regex.search(line)
        return mo.group(4, 5)
    except AttributeError:
        return ("", "")


def print_status_codes(status_codes: dict):
    """Print the status codes in ascending order.

    Args:
        status_codes (dict): Dictionary of the status codes to print.
    """
    for code in sorted(status_codes.keys()):
        if status_codes[code]:
            print("{}: {}".format(code, status_codes[code]), flush=True)


def main():
    """Reads stdin line by line and computes metrics.

    The input must be of the format: `<IP Address> - [<date>] \
    "GET /projects/260 HTTP/1.1" <status code> <file size>`
    """

    line_count, total_file_size = 0, 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    line = sys.stdin.readline()

    try:
        while line:
            code, file_size = get_size_and_code_nonstrict(line)
            # For strict matching instead use:
            # code, file_size = get_size_and_code_strict(line)

            try:
                total_file_size += int(file_size)
                if code in status_codes:
                    status_codes[code] += 1
                line_count += 1
            except ValueError:
                pass

            line = sys.stdin.readline()
            while line == "\n":
                line = sys.stdin.readline()

            if line_count == 10 or not line:
                print("File size: {}".format(total_file_size))
                print_status_codes(status_codes)
                line_count = 0

            code, file_size = "", ""
    except KeyboardInterrupt:
        print("File size: {}".format(total_file_size))
        print_status_codes(status_codes)


if __name__ == "__main__":
    main()
