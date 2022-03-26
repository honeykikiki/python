def open_account():
  print('새로운 계좌가 생성 되었습니다.')

def deposit(bal, money):
  print("입금이 완료되었습니다. 잔액은{0}입니다".format(bal + money))
  return bal + money

def draw(bal, money):
  if bal >= money:
    print('ok')
    return bal - money
  elif bal <= money:
    print('none')
    return bal

def night(bal, money):
  commission = 100
  return commission, bal - money - commission

bal = 0
bal = deposit(bal,  1000)
# bal = draw(bal, 900)
commision, bal = night(bal, 500)
print(bal, commision)