names = ['tarun','karthik','kiran','shreyas','prithvi','arunraj','errol','shantanu','atul','subramani']

print "names in random order are"
print names

for x in range(len(names)):
 for y in range(len(names)-1):
  if names[y] > names[y+1]:
    t = names[y]
    names[y] = names[y+1]
    names[y+1] = t
	
	
print "names sorted according to alphabetical order is"
print names