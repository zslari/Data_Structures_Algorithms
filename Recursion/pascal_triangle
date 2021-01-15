"""
Recursion
Created By: Zafir Lari
Application: Pascal's Triangle

Description: This application takes in a row
corresponding to a row of Pascal's Triangle
and returns the values of the row as a list.
"""


def pascaltriangle(n: int):
    if n < 0:
        return print("Input value may not be negative")
    if n == 0:
        return [1]
    else:
        row = [1]
        previous_row = pascaltriangle((n-1))
        for i in range(len(previous_row) - 1):
            row.append(previous_row[i] + previous_row[i+1])
        row += [1]
    return row
