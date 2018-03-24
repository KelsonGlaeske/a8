"""
Name: Kelson Glaeske
NSID: kjg659
Student Number: 11205487
Course: CMPT 145
Lecture Section: 04
Lab Section: 14
"""

import treenode as TN

def complete(tnode):
    """
    :param tnode: A node tree according to treenode ADT
    :return: Tuple of (True, depth) if complete and (False, None) otherwise
    """
    def cmplt(tnode):
        if tnode is None:
            flag = True
            depth = 0
            return flag, depth
        else:
            ldepth = cmplt(TN.get_left(tnode))
            rdepth = cmplt(TN.get_right(tnode))

            if (rdepth[1] is not None) and (ldepth[1] is not None) and ldepth == rdepth:
                flag = True
                depth = rdepth[1]+1
                return flag, depth
            else:
                flag, depth = False, None
                return flag, depth
    flag, depth = cmplt(tnode)
    return (depth is not None) and flag

