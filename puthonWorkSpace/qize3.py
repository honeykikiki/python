from random import random


from random import *

cnt = 0 
for i in range(1,51):
  time = randrange(5, 51)
  if 5 <= time <= 15:
    print("[0] {0}번쨰 손님 (서ㅗ요시간 : {1}분)".format(i, time))
    cnt += 1
  else:
    print("[] {0}번쨰 손님 (서ㅗ요시간 : {1}분)".format(i, time))
    
print('총 : {0}분'.format(cnt))