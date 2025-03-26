#sorti g achieved using .sort() or sorted() depending on wheteher it is a list, tuple or dictionary
#list - both
# tuple - no sort() attribute, hence sorted

ages = [6, 7, 4, 18, 2]
agest = (6, 7, 4, 18, 2)
agest.sort()
ages.sort(reverse=True)
print(ages)
print(sorted(agest))
print(sorted(ages))