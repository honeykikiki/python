# weather = input('오늘의 날씨는 어떄요?')
# if weather == 'rain' or weather == 'rain2':
#     print('우산을 챙기세요')
# elif weather == 'snow' :
#     print('왜투를 챙기세요')
# else:
#     print('go')

temp = int(input('기온은 어떄료? '))
if 30 <= temp:
  print('더워요')
elif 10 <= temp and temp < 30:
  print('시원해요')
elif 0 <= temp < 10:
  print('외투를 챙기세요')
else: 
  print('너무 추워요 나가지마!!!')
