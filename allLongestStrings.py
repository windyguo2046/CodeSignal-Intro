"""
Given an array of strings, return another array containing all of its longest strings.
Example
For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""


def allLongestStrings(inputArray):
    longestList = []
    max_length = max([len(x) for x in inputArray])

    for string in inputArray:
        if len(string) == max_length:
            longestList.append(string)
    return longestList
