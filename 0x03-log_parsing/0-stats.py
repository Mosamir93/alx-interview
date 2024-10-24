#!/usr/bin/python3
"""
A script that reads stdin line by
line and computes metrics.
"""
from sys import stdin


def print_stats(total_size: int, codes_counts: dict) -> None:
    """Prints the stats."""
    print(f"File size: {total_size}")
    for key, value in sorted(codes_counts.items()):
        if value > 0:
            print(f"{key}: {value}")


if __name__ == "__main__":
    total_size = 0
    status_codes = {200: 0,
                    301: 0,
                    400: 0,
                    401: 0,
                    403: 0,
                    404: 0,
                    405: 0,
                    500: 0}
    line_count = 0

    try:
        for line in stdin:
            line_count += 1
            parts = line.split()

            try:
                status_code = int(parts[-2])
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            except (ValueError, IndexError):
                continue
            if line_count == 10:
                line_count = 0
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise
