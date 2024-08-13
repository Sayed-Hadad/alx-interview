#!/usr/bin/python3
"""
This module provides functions to generate Pascal's Triangle.
"""

def calculate_row(prev_row):
    """
    Generates the next row in Pascal's Triangle based on the previous row.
    Args:
        prev_row (list): The previous row in Pascal's Triangle.
    Returns:
        list: The next row in Pascal's Triangle.
    """
    row = [1]
    for i in range(1, len(prev_row)):
        row.append(prev_row[i] + prev_row[i - 1])
    row.append(1)
    return row

def pascal_triangle(n):
    """
    Generates Pascal's Triangle up to the nth row.
    Args:
        n (int): The number of rows in Pascal's Triangle to generate.
    Returns:
        list of lists: Pascal's Triangle up to the nth row.
    """
    if n <= 0:
        return []

    triangle = [[1]]  # Start with the first row
    for i in range(1, n):
        triangle.append(calculate_row(triangle[-1]))

    return triangle

