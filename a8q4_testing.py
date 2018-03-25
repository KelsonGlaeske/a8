"""
Name: Kelson Glaeske
NSID: kjg659
Student Number: 11205487
Course: CMPT 145
Lecture Section: 04
Lab Section: 14
"""

import treenode as Tn

orderedTestCases = [
    #0
    {
        "Input"     : None,
        "Output"    : False,
        "Reason"    : "There is no tree node"
    },
    #1
    {
        "Input"     : Tn.create(1),
        "Output"    : False,
        "Reason"    : "There is only one item so it can't be ordered"
    },
    #2
    {
        "Input"     : Tn.create(1, Tn.create(2)),
        "Output"    : False,
        "Reason"    : "The tree is incomplete and therefore disordered"
    },
    #3
    {
        "Input"     : Tn.create(2, Tn.create(1), Tn.create(3)),
        "Output"    : True,
        "Reason"    : "The tree has has a depth of two and is complete and in order"
    },
    #4
    {
        "Input"     : Tn.create(1, Tn.create(2), Tn.create(3)),
        "Output"    : False,
        "Reason"    :
    }
]