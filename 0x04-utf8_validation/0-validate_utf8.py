#!/usr/bin/python3
"""UTF-8 validation module."""


def validUTF8(data):
    """Validate utf-8 encoding returns True if data
    is a valid UTF-8 encoding, else return False"""
    n_bytes = 0

    for num in data:
        byte = num & 0xFF
        if n_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            if n_bytes == 0:
                continue
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        n_bytes -= 1

    return n_bytes == 0
