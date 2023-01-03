#!/usr/bin/python3
"""LockedClass Module"""


class LockedClass:
    """A locked class that permits only the instance
    attribut 'first_name'"""
    __slots__ = ['first_name']
