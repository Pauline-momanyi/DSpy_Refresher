
s = [1, 2, 3, 4, 1]
# print (3 in s)
# print (s+s)

# print (s[-1])
# print (s[-1:-3:-1])
# print (s[-2:])
# print (s[3:5])
# del(s[0:3])
# print (s)

# DICTIONARY


size_to_ounce_map = {
    "tall": 12,
    "grande": 16,
    "venti": 20,
}

def asize(size):
    size_to_ounce_map = {
    "tall": 12,
    "grande": 16,
    "venti": 20,
    }
    
    return size_to_ounce_map.get(size, "non-existent")

print (asize("tall"))
print (asize("short"))

