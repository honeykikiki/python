# for wainting in range(1, 6):
#     print('대기번호 : {0}'.format(wainting))

# star = [1, 2, 3]
# for cus in star:
#   print('{0}, 커피가 준비 되었습니다'.format(cus))

#while

# cus = "토르"
# index = 5
# while index >= 1:
#   print('{0}, 커피가 준비 되었습니다, {1} 번 남았어여'.format(cus, index))
#   index -= 1
#   if index == 0:
#     print('커피는 폐기처분 되었습니다')

# cus ='아이언맨'
# index = 1
# while True:
#   print('{0}, 커피가 준비 되었습니다,  {1} 번 남았어여'.format(cus, index))
#   index += 1

cus = '토르'
per = 'U'

while per != cus:
  print('{0}, 커피가 준비 되었습니다,'.format(cus))
  per = input('이름')