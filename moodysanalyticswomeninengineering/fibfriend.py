#!/bin/python

import sys
from collections import defaultdict
# import time

# get fibonacci numbers into fibdict
fibdict = defaultdict(int)
def fibonacci(n):
  # n is upper limit
  a, b = 0, 1
  
  while a <= n:
    fibdict[a] = 1
    a, b = b, a+b

fibonacci(10**19)

# string n
def frequency(n):
  freq = [0,0,0,0,0,0,0,0,0,0]
  for c in n:
    d = int(c)
    freq[d] = freq[d] + 1
  
  return freq

# friend generator
def friend(n):
    count = 1110
    for i in xrange(count): 
        yield i, i
    
    # start with known fib friend + 1
    i = count
    while count < n + 1:
      yield count, i
      
      # print 'finding next friend', count, i
      # find next friend
      # increment
      s = str(i+1)
      freq = frequency(s)
      i = find_next_friend(s, freq)
      
      count += 1

def find_next_friend(n, freq):
  
  # i, j are markers where i-- and j++
  def change_freq(i, j):
    newI = freq[i] - 1
    newJ = freq[j] + 1
    freq[i] = newI
    freq[j] = newJ

    if fibdict[newI]:
      if i in freqToChange:
        freqToChange.remove(i)
    else:
      if i not in freqToChange:
        freqToChange.add(i)
    if fibdict[newJ]:
      if j in freqToChange:
        freqToChange.remove(j)
    else:
      if j not in freqToChange:
        freqToChange.add(j)

  # n (str), num (arr of int)
  num, digits = map(int, n), len(n)
  
  # find non-true frequencies
  freqToChange = set()
  for i in xrange(10):
    if not fibdict[freq[i]]: freqToChange.add(i)

  # print 'freqToChange', freqToChange
  # print 'freq', freq

  # increment and change number
  while (freqToChange):
    i = num[-1]

    if i == 9:
      for i in xrange(digits - 2, -1, -1):
        if num[i] == 9:
          # increment
          num[i] = 0
          change_freq(9, 0)
          
          if i == 0: 
            # gonna have to mildly recurse
            n = '1' + ''.join(['0' for _ in xrange(digits)])
            freq = [digits, 1, 0,0,0,0,0,0,0,0]
            # print '\n\nRECURSING\n', n, freq, '\n'
            # RUNTIME ERROR FROM THIS
            return find_next_friend(n, freq)
        else: 
          j = num[i]
          # increment
          num[i] = j + 1
          change_freq(j, j+1)
          break
    else:
      # increment
      num[-1] = i + 1
      change_freq(i, i+1)

    # make sure you are incrementing right here!
    # print n, freq

  return int(''.join(map(str, num)))

# starttime = time.time()

# input
q = int(raw_input().strip())
queries = []
for _ in xrange(q):
  n = int(raw_input().strip())
  queries.append(n)

maxQuery = max(queries)
sortedquery = sorted(queries)
friendsdict = dict()

# generate friends
index = 0
nextQuery = sortedquery[index]
for res in friend(maxQuery):
  # print res
  if nextQuery == res[0]:
    friendsdict[res[0]] = res[1]
    index += 1
    if index == q: break
    nextQuery = sortedquery[index]

for q in queries:
  print friendsdict[q]
  
# print time.time() - starttime