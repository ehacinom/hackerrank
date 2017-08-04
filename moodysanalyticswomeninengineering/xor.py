# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
# from math import ceil

# read input: n, q, node values
n, q = map(int, raw_input().strip().split())
values = map(int, raw_input().strip().split())

# read input: subtree, tree
tree = defaultdict(list)       # both directions
subtree = defaultdict(list)    # 1 direction - only leads to subelements
for i in xrange(n-1):
  i1, i2 = raw_input().strip().split()
  tree[i1].append(i2)
  tree[i2].append(i1)
  subtree[i1].append(i2)

# memoization 
# using global variable shortPaths because it's just so much easier to read
nMemo = 10                     # when n > nMemo we memoize
shortPaths = defaultdict(list) # shortPaths saves { k: [ [path], [path] ] }

# find shortest path
# input tree variable
def find_shortest_path(graph, start, end, path=[]):
  path = path + [start]
  if start == end: return path
  if not graph.has_key(start): return None
  
  shortest = None
  for node in graph[start]:
    if node not in path:
      newpath = find_shortest_path(graph, node, end, path)
      if newpath:
        if not shortest or len(newpath) < len(shortest):
          shortest = newpath
  return shortest

# find index of nodes in subtree
# input subtree variable
def find_subtree(graph, start):
  path = graph[start]
  if not len(path): return []
  for node in path:
    path.extend(find_subtree(graph, node))
  return path

# -------------------------------------------------------------------------

# queries! / tree operations
for i in xrange(q):
  op = raw_input().strip().split()
  cmd = op[0]
  
  # switch
  if cmd == 'Divide':
    u, v, w = op[1], op[2], int(op[3])
    
    # memoize and get path (indexes are strings)
    path = False
    foundAPath = False
    if n > nMemo:
      # possible paths lists
      uPaths = shortPaths[u]
      vPaths = shortPaths[v]
      
      # use shorter list
      if len(uPaths) > len(vPaths): paths = vPaths
      else: paths = uPaths
      
      # find min path
      for sp in paths:
        if u in sp and v in sp:
          foundAPath = True
          ui, vi = sp.index(u), sp.index(v)
          path = sp[ui:vi+1]
          #print 'path found!'
          break
    if not path:
      path = find_shortest_path(tree, u, v)
    
    # divide and memoize
    for k in path:
      j = int(k) - 1    
      tmp = values[j]
      if tmp % w: values[j] = tmp / w + 1
      else: values[j] = tmp / w
      
      # memoize
      if n > nMemo and not foundAPath: shortPaths[k].append(path)
  elif cmd == 'Multiply':
    j, w = int(op[1]) - 1, int(op[2])
    values[j] = (values[j] * w) % 1009
  else:
    # XOR
    k, j, w = op[1], int(op[1]) - 1, int(op[2])
    maxXOR = values[j] ^ w
    
    # check subtree for larger XOR
    path = map(int, find_subtree(subtree, k))  # could be memoized too lol
    for j in path:
      tmp = values[j-1] ^ w
      if tmp > maxXOR: maxXOR = tmp
    
    # print
    print maxXOR