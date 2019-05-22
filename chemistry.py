#숫자인지 아닌지 반환해주는 함수
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False


#분자 내 원소의 구성비는 괄호 안에 넣어주세요
#구성하는 분자들의 입력을 받는다
list_i = []
list_f = []
i = input('반응물의 수를 알려주세요')
for j in range(int(i)) :
    list_i.append(input('반응물을 모두 넣어주세요'))
f = input('생성물의 수를 알려주세요')
for j in range(int(f)) :
    list_f.append(input('반응물을 모두 넣어주세요'))
print(list_i)
print(list_f)

#서로 다른 원소를 구분한다
lists_i = []
lists_f = []#초기
for i in list_i :
    lists_i.append(list(i))
for i in list_f :
    lists_f.append(list(i)) 

next_list_i = []
next_list_f = []
for a in lists_i :
    for i in range(len(a)) :
        if isNumber(a[i]) == True :
            next_list_i.append(a[i])
        else :
            if a[i].isupper == True and a[i+1].isupper == True :
                next_list_i.append(a[i])
            if a[i].isupper == True and a[i+1].isupper == False :
                next_list_i.append(a[i]+a[i+1])
            else :
                continue
print(next_list_i)
print(next_list_f)
        
        
        


#서로 다른 원소의 수를 구분한다
dict_i = {}
dict_f = {}
