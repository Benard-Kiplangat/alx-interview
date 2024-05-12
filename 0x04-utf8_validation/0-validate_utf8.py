#!/usr/bin/python3
"""
UTF-8 validator
"""

def validUTF8(data):
    for i in data:
        if ((not isinstance(i, int)) or i > 128 or i < 0):
            return False
    return True
