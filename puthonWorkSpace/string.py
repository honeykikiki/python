# sentence = '나는 소년입니다'
# sentence2 = '파이썬은 쉬워요'
# sentence3 = """
# 나는 소년이고
# 파이썬은 쉬워요"""

# print(sentence, sentence2, sentence3)

# jumin = "970128-1999992"
# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) #0 부터 2 직전 까지 
# print("월 : " + jumin[2:4]) #0 부터 2 직전 까지 
# print("일 : " + jumin[4:6]) #0 부터 2 직전 까지 

# print("생년월일 : " + jumin[:6])
# print("뒷자리 : " + jumin[7:])
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])

# python = "Python is Anazing"
# print(python.lower()) #소문자
# print(python.upper()) #대문자
# print(python[0].isupper()) #대문자 면 True
# print(len(python)) #갯수
# print(python.replace("Python", "Java")) 

# index = python.index('n')
# print(index)
# index = python.index("n", index + 1)
# print(index)
# index = python.find("Java")
# # index = python.index("Java") # 오류
# print(python.index("n"))


# print("a" + "b")
# print("a", "b")

# 1
# print("나는 %d살입니다," %20) 
# print("나는 %s살입니다," %"파이썬")
# print("나는 %c살입니다," %"A")

# print("나는 %s색과 %s색을 좋아해요" %("파란", '빨간'))

#2
# print("나는 {}살 입니다".format(20))
# print("나는 {}살 {}살 입니다".format("20", "30"))
# print("나는 {0}살 {1}살 입니다".format("20", "30"))
# print("나는 {1}살 {0}살 입니다".format("20", "30"))


# #3
# print("나는 {age}살이며 {color}색을 좋아해요. " .format(age = 20, color = "red"))

# #4 v3.6~ 이상
# age = 20
# color = 'red'
# print(f"나는 {age}살이며, {color}색을 좋아한다")

# print("백문이 물어일견\n 백견이 불여일타")
# print("저는 "허성진" 입니다)
# print("저는 \"허성진\" 입니다")

# # \\ : 문장에서는 \
# print("~\\Desktop\\python")

# # \r : 커서를 맨앞으로
# print("red Apple \rPrin")

# # \b : 한글자 삭제
# print("redd\bApple")

# # \t 탭
# print("red\t\t\t\t\t\t\tApple")


site = "https://naver.com"
# one = site[8:]

# siteFind = site.find('.')
# two = site[8:siteFind]

# three = two
# print(three[:3], len(three), three, three("naver", "!"))

my_str = site.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")]
print(my_str)
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"

print(password)

