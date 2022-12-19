#!/usr/bin/python3
def safe_print_division(a, b):
    try:
       return (a / b)
    except (ZeroDivisionError, ValueError):
        return None
    finally:
        pass
