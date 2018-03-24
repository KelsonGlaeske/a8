"""
Name: Kelson Glaeske
NSID: kjg659
Student Number: 11205487
Course: CMPT 145
Lecture Section: 04
Lab Section: 14
"""

import a8q3 as complt
import treenode as Tn

testcasesComplete = [
    #0
    {
        "Input"     : None,
        "Output"    : True,
        "Reason"    : "There is no tree to evaluate"
    },
    #1
    {
        "Input"     : Tn.create(1),
        "Output"    : True,
        "Reason"    : "The tree is only a root"
    },
    #2
    {
        "Input"     : Tn.create(1, Tn.create(2)),
        "Output"    : False,
        "Reason"    : "The tree is incomplete"
    },
    #3
    {
        "Input"     : Tn.create(1, Tn.create(2), Tn.create(3)),
        "Output"    : True,
        "Reason"    : "The tree is complete with a depth of 2"
    },
    #4
    {
        "Input"     : Tn.create(1,
                                Tn.create(2,
                                          Tn.create(3),
                                          Tn.create(4)
                                          ),
                                Tn.create(5,
                                          Tn.create(6))
                                ),
        "Output"    : False,
        "Reason"    : "The is not complete"
    },
    #5
    {
        "Input"     : Tn.create(1,
                                Tn.create(2,
                                          Tn.create(3),
                                          Tn.create(4)
                                          ),
                                Tn.create(5,
                                          Tn.create(6),
                                          Tn.create(7))
                                ),
        "Output"    : True,
        "Reason"    : "The tree is complete with a depth of 3"
    }
]

for test in testcasesComplete:
    testOut = complt.complete(test["Input"])
    testPrint = "Expected " + str(test["Output"]) + " returned " + str(testOut) + ", " + test["Reason"]
    assert testOut == test["Output"], testPrint