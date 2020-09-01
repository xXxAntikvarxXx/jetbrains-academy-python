# the list "walks" is already defined
# your code here
avg = int(sum(walk.get('distance', 0) for walk in walks) / len(walks))
print(avg)
