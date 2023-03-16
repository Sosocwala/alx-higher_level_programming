#!/usr/bin/python3
def simple_delete(the_dic, key=""):
    if key in the_dic:
        del the_dic[key]
    return the_dic
