import sys
import random
import string


def unique(s):
    return list(set(s))

def intersect(a, b):
    return list(set(a) & set(b))

def union(a, b):
    return list(set(a) | set(b))

def jaccard(a, b):
    return (len(intersect(a,b))) / float(len(union(a,b)))
