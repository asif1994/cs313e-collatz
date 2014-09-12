#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]
    
# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    if (i > j):
      i, j = j, i
    m = (j // 2) + 1
    if (m > i):
      i = m
    cashe = {}
    max = 0
    for k in range (i, j+1):
      n = k
      assert n > 0
      c = 1
      if n in cashe:
         c = cashe[n]
      else:
        while n > 1 :
            if (n % 2) == 0 :
              n = (n // 2)
              c += 1 
            else :
              n = n + (n // 2) + 1
              c += 2
        cashe[n] = c
        
      assert c > 0
      if (c > max):
        max = c
    return max

# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)