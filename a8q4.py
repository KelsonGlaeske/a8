"""
Name: Kelson Glaeske
NSID: kjg659
Student Number: 11205487
Course: CMPT 145
Lecture Section: 04
Lab Section: 14
"""

import treenode as Tn
import queue as queue
import treefunctions as Tf

def ordered(tnode):
    """
    Purpose: Establish if binary tree defined by treenode ADT is ordered
    Pre-condition: :param tnode: tree-node defined by treenode ADT
    Post-condition: none
    :return: True if tnode is ordered, False otherwise

    A binary search tree is ordered if and only if all the following conditions are true:
        0. The left subtree is ordered
        1. The right subtree is ordered
        2. If the left subtree is not empty and all values in said subtree are less than the root value
        3. If the right subtree is not empty and all values in said subtree are greater than the root value
    """
    # Check for no tree
    print()
    if tnode is None:
        return True
    # Check for tree end
    elif Tn.get_left(tnode) is None and Tn.get_right(tnode) is None:
        return True
    # Check for proper tree order
    elif ordered(Tn.get_left(tnode)) < Tn.get_data(tnode) and ordered(Tn.get_right(tnode)) > Tn.get_data(tnode):
        return True
    else:
        return False