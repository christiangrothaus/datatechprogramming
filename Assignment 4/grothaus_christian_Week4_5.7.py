def uniqSorted(l):
  uniqueList = list(set(l))
  uniqueList.sort()
  return uniqueList

print(uniqSorted([9, 8, 73, 92, 9, 1, 3, 6, 73]))
print(uniqSorted(['hello', 'hello', 'red', 'Green', 'a']))