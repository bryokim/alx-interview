#!/usr/bin/python3
"""Log parsing module"""

import re
import sys

# Regex for matching logs.
log_regex = re.compile(
    r"(\d{1,3}\.*){4}\s-\s\[\d{4}(-\d{1,2}){2}\s(\d{1,2}:*){3}.\d{6}\]\s" +
    r'"GET /projects/260 HTTP/1.1"\s(\d{3})\s(\d{1,4})'
)


def main():
    """Reads stdin line by line and computes metrics.

    The input must be of the format: `<IP Address> - [<date>] \
    "GET /projects/260 HTTP/1.1" <status code> <file size>`
    """

    line_count, total_file_size = 0, 0
    status_codes = {}
    accepted_status_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    try:
        for line in sys.stdin:
            match_obj = log_regex.match(line)

            if not match_obj:
                line_count += 1
                continue

            status_code = int(match_obj.group(4))

            file_size = int(match_obj.group(5))

            if status_code in accepted_status_codes:
                status_codes.setdefault(status_code, 0)
                status_codes[status_code] += 1

            total_file_size += file_size

            line_count += 1

            if line_count == 10:
                print("File size: {}".format(total_file_size), flush=True)
                print_status_codes(status_codes)
                line_count = 0
    except KeyboardInterrupt:
        print("File size: {}".format(total_file_size))
        print_status_codes(status_codes)


def print_status_codes(status_codes: dict):
    """Print the status codes in ascending order.

    Args:
        status_codes (dict): Dictionary of the status codes to print.
    """
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]), flush=True)


if __name__ == "__main__":
    main()
