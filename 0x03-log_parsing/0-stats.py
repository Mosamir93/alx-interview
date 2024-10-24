#!/usr/bin/python3
"""
A script that reads stdin line by
line and computes metrics.
"""
import sys
import re


log_pattern = re.compile(
    r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3}) - '
    r'\[(?P<date>.*?)\] '
    r'"GET /projects/260 HTTP/1.1" '
    r'(?P<status>\d{3}) '
    r'(?P<size>\d+)'
    )
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
        line_count += 1
        match = log_pattern.match(line)
        if not match:
            continue

        try:
            status_code = int(match.group('status'))
            file_size = int(match.group('size'))
            total_size += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1

        except (ValueError, IndexError):
            continue
        if line_count == 10:
            line_count = 0
            print(f"File size: {total_size}")
            for key, value in sorted(status_codes.items()):
                if value > 0:
                    print(f"{key}: {value}")
except KeyboardInterrupt:
    print(f"File size: {total_size}")
    for key, value in sorted(status_codes.items()):
        if value > 0:
            print(f"{key}: {value}")
