mylist = [10,20,10,20,30,40,50]
duplist = []

# Method 1 - By using dictionary
dupdict = {}
for item in mylist:
  if str(item) not in dupdict.keys():
    dupdict[str(item)] = 1
  else:
    dupdict[str(item)] += 1
  
for key,value in dupdict.items():
  if value > 1:
    duplist.append(int(key))

print(duplist)

# Method 2 - By using list 
duplist = []
for i in range(len(mylist)):
  k = i + 1
  for j in range(k,len(mylist)):
    if mylist[i] == mylist[j] and mylist[i] not in duplist:
      duplist.append(mylist[i])

print(duplist)