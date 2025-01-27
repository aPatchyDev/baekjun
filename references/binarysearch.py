#!/usr/bin/python3

def binsearch(lo, hi, check):
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if check(mid):
            lo = mid
        else:
            hi = mid
    
    # check(lo), check(hi) remains constant throughout
    return lo