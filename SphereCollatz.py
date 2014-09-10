def collatz_read (r) :
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]
    
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
      while n > 1 :
          if n in cashe:
              c = cashe[n]
          else:
              if (n % 2) == 0 :
                n = (n // 2)
                c += 1 
              else :
                n = n + (n // 2) + 1
                c += 2
      assert c > 0
      if (c > max):
        max = c
    return max

def collatz_print (w, i, j, v) :
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

def collatz_solve (r, w) :
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)


import sys

collatz_solve(sys.stdin, sys.stdout)


