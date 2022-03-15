

# list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

# one = shuffle(list)
# twe = shuffle(list)
# three = shuffle(list)

# four = shuffle(list)

# print(one, twe, three, four)

from random import *
users = range(1, 21)
users = list(users)

shuffle(users)

winners = sample(users, 4)

print('치킨 담청자 : {0}'.format(winners[0]))
print('코피 담청자 : {0}'.format(winners[1:]))
print()