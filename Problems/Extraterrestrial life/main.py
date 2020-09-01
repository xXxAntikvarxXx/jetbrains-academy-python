# The parental gene sequences are stored here
one_ancestor = input()
other_ancestor = input()

# Calculate the identity of a new alien here
new_alien = int((id(one_ancestor) + id(other_ancestor)) / 2)
