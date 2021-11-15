import random

members = ["foo", "bar", "test"]
members_temp = members.copy()

random.shuffle(members_temp)
finish =  False
x = 0

for x in range(len(members_temp)):
    if members[x] == str(members_temp[x]):
        members_temp[x], members_temp[x+1] = members_temp[x+1], members_temp[x]
    
for x in range(len(members)):
    print("%s gets %s" % (members[x], members_temp[x]))
