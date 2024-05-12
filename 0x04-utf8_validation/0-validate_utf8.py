#!/usr/bin/python3
"""
UTF-8 validator
"""

def validUTF8(data):
    for i in data:
        if i > 128:
            return False
    return True
