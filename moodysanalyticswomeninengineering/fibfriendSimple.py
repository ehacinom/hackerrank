#!/bin/python

import sys
from collections import defaultdict

# get fibonacci numbers into fibdict
fibdict = defaultdict(int)
def fibonacci(n):
  # n is upper limit
  a, b = 0, 1
  
  while a <= n:
    fibdict[a] = 1
    a, b = b, a+b

fibonacci(10**19)

# friend generator
def friend(n):
    max_i = n*n
    count = 1110
    for i in xrange(count + 1): 
        yield i, i
    
    i = count + 1
    while i < max_i:
        freq = [0,0,0,0,0,0,0,0,0,0]
        s = str(i)
        found = True
        
        for c in s:
            d = int(c)
            freq[d] = freq[d] + 1
        
        for f in freq:
            if not fibdict[f]:
                found = False
                break
        if found: 
            count += 1
            yield count, i
        
        i += 1


# input
q = int(raw_input().strip())
queries = []
for _ in xrange(q):
  n = int(raw_input().strip())
  queries.append(n)

# generate friends
maxQuery = max(queries)
sortedquery = sorted(queries)
friendsdict = dict()
index = 0
nextQuery = sortedquery[index]

for res in friend(maxQuery):
  if nextQuery == res[0]:
    friendsdict[res[0]] = res[1]
    index += 1
    if index < q:
      nextQuery = sortedquery[index]

# return
#map(friendsdict.get, queries)
for q in queries:
  print friendsdict[q]

