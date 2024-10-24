#!/usr/bin/python3
"""
A script that reads stdin line by
line and computes metrics.
"""
import sys


total_size = 0
status_codes = {'200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0}
line_count = 0

try:
    for line in sys.stdin:
        line.split()
        if len(line) > 4:
            try:
                status_code = int(match.group('status'))
                file_size = int(match.group('size'))
                line_count += 1
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            except (ValueError, IndexError):
                continue
            if line_count == 10:
                line_count = 0
                print("File size: {}".format(total_size))
                for key, value in sorted(status_codes.items()):
                    if value > 0:
                        print("{}: {}".format(key, value))
except KeyboardInterrupt:
    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print("{}: {}".format(key, value))
