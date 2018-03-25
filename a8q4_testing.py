"""
Name: Kelson Glaeske
NSID: kjg659
Student Number: 11205487
Course: CMPT 145
Lecture Section: 04
Lab Section: 14
"""

import treenode as Tn
import a8q4 as T_ordered

orderedTestCases = [
    #0
    {
        "Input"     : None,
        "Output"    : True,
        "Reason"    : "The tree is empty and therefore ordered"
    },
    #1
    {
        "Input"     : Tn.create(1),
        "Output"    : True,
        "Reason"    : "A single leaf tree is ordered"
    },
    #2
    {
        "Input"     : Tn.create(1, Tn.create(2)),
        "Output"    : False,
        "Reason"    : "The tree is disordered because the left leaf is greater than the root"
    },
    #3
    {
        "Input"     : Tn.create(2, Tn.create(1), Tn.create(3)),
        "Output"    : True,
        "Reason"    : "The tree has a depth of two and is ordered"
    },
    #4
    {
        "Input"     : Tn.create(1, Tn.create(2), Tn.create(3)),
        "Output"    : False,
        "Reason"    : "The tree is disordered because the value at the left subtree is larger than the root value"
    },
    #5
    {
        "Input"     : Tn.create(4,
                                Tn.create(2,
                                          Tn.create(1),
                                          Tn.create(3)),
                                Tn.create(6,
                                          Tn.create(5),
                                          Tn.create(7))
                                ),
        "Output"    : True,
        "Reason"    : "The tree is in order with a depth of 3"
    },
    #6
    {
        "Input"     : Tn.create(4,
                                Tn.create(2,
                                          Tn.create(1),
                                          Tn.create(3)),
                                Tn.create(6,
                                          Tn.create(7),
                                          Tn.create(5))
                                ),
        "Output"    : False,
        "Reason"    : "The left leaf of the left branch is larger than the branch"
    },
    #7
    {
        "Input"     : Tn.create(4,
                                Tn.create(2,
                                          Tn.create(1),
                                          Tn.create(3)),
                                Tn.create(6,
                                          Tn.create(5),)
                                ),
        "Output"    : True,
        "Reason"    : "The tree is incomplete but still ordered"
    }
]

for test in orderedTestCases:
    testOut = T_ordered.ordered(test["Input"])
    testPrint = "Expected " + str(test["Output"]) + " returned " + str(testOut) + ", " + test["Reason"]
    assert test["Output"] is testOut, testPrint