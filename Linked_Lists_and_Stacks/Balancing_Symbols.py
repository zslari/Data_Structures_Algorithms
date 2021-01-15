"""
Linked Lists and Stacks
Created By: Zafir Lari
Application: Balancing Symbols

Description: This application processes a string of symbols
and checks whether the given expression has balanced symbols.

Requires Stack and Node from stack_ADT.py and node_ADT.py
"""

from stack_ADT import Stack


def charParser(symbolstring: str):
    """ Processes string of symbols to determine
     string is balanced
    """
    s = Stack()
    index = 0

    while index < len(symbolstring):
        symbol = symbolstring[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                return False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    return False
        index += 1
    return True if s.isEmpty() else False


def matches(openvalue, closevalue):
    """ Helper method to check if symbols align in symbolstring """
    openers = "([{"
    closers = ")]}"
    if openvalue not in openers:
        return False
    if closevalue not in closers:
        return False
    return openers.index(openvalue) == closers.index(closevalue)


def test_run():
    """ Test Cases """
    testcase_one = "([|)]"
    print(charParser(testcase_one))
    testcase_two = "()(()[()])"
    print(charParser(testcase_two))
    testcase_three = "{{([][])}}()"
    print(charParser(testcase_three))
    testcase_four = "(())"
    print(charParser(testcase_four))
    testcase_five = "$$"
    print(charParser(testcase_five))
    testcase_six = ""
    print(charParser(testcase_six))
    testcase_seven = "{)"
    print(charParser(testcase_seven))
    print("Time and space complexity is O(n) dependent on the length of "
          "the size of the string of symbols passed in.")


if __name__ == "__main__":
    test_run()
