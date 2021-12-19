#!/usr/bin/python3
"""
Module that parses a log and prints status
"""
from sys import stdin

status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

size = 0


def print_log():
    """Prints the logs"""
    print("File size: {}".format(size))
    for status in sorted(status_codes.keys()):
        if status_codes[status]:
            print("{}: {}".format(status, status_codes[status]))


if __name__ == "__main__":
    count = 0
    try:
        for line in stdin:
            try:
                log = line.split()
                size += int(log[-1])
                if log[-2] in status_codes:
                    status_codes[log[-2]] += 1
            except Exception:
                pass
            if count == 9:
                print_log()
                count = -1
            count += 1
    except KeyboardInterrupt:
        print_log()
        raise
    print_log()
