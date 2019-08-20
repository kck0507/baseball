#숫자를 판별하는 함수
def isNumber(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

#숫자를 자르는 함수
def numsplit(a) : 
    cnt = 0
    number = []
    after_sp = []
    num = "0123456789"
    for i in a :
        cnt = cnt + 1
        if i in num :
            number.append(cnt)
            if len(number) == 1 :
                after_sp.append(a[0:number[-1]-1])
            else :
                after_sp.append(a[number[-2]:number[-1]-1])
            after_sp.append(int(i))
    if isNumber(a[-1]) == False :
        after_sp.append(a[number[-1]:])
    return after_sp

#원소를 자르는 함수
def wordsplit(a) :
    cnt = 0
    number = []
    after_sp = []
    if len(a) ==1 :
        after_sp.append(a)
    else :
        for i in a :
            number.append(cnt)
            if cnt == 0 :
                if a[1].isupper() == True :
                    after_sp.append(a[0])
            else :
                if a[number[-1]].isupper() == False :
                    after_sp.append(a[number[-2]:number[-1]+1])
                if a[number[-1]].isupper() == True :
                    if cnt+1 == len(a) :
                        after_sp.append(a[-1])
                    elif a[number[-1]+1].isupper() == True :
                        after_sp.append(a[number[-1]])                
            cnt = cnt + 1
    return after_sp

#원소를 쪼개주는 함수(최종)
def atomix(a) :
    atom = []
    flag = True
    for i in a :
        if isNumber(i) :
            flag = False
            break
    if flag :      
        y = wordsplit(a)
        for j in y :
            atom.append(j)
    else :
        for i in numsplit(a) :
            if isNumber(i) :
                atom.append(i)
            else :
                x= wordsplit(i)
                for j in x :
                    atom.append(j)
    return atom 

#dictionary에 들어있는지 판별해주는 함수(isNumber 응용)
def isKey(a,k) :
    try :
        a[k]
        return True
    except KeyError :
        return False

#dictionary에 저장해주는 함수
def conf(a) :
    conf = {}
    cnt = 0
    for i in a :
        if isNumber(a[cnt]) == False :
            if cnt+1 == len(a) :
                if isNumber(a[cnt]) == False :
                    if isKey(conf, a[cnt]) :
                        conf[a[cnt]] = conf[a[cnt]] + 1
                    else :
                        conf[a[cnt]] = 1
            else: 
                if isNumber(a[cnt+1]) == True :
                    if isKey(conf, a[cnt]) :
                        conf[a[cnt]] = conf[a[cnt]] + a[cnt+1]
                    else :
                        conf[a[cnt]] = a[cnt+1]
                else :
                    if isKey(conf, a[cnt]) :
                        conf[a[cnt]] = conf[a[cnt]] + 1
                    else :
                        conf[a[cnt]] = 1
        cnt = cnt+1
    return conf

#전체 key들이 모여있는 list를 만든다
def keylist(a) :
    keylist = []
    for i in a :
        b = sorted(i)
        for j in b :
            if j not in keylist :
                keylist.append(j)
    return keylist

def isresult(a,b) :
    try :
        np.linalg.solve(a,b)
        return True
    except LinAlgError :
        return False

import numpy as np
import sys
#구성하는 분자들의 입력을 받는다
list_i = []
list_f = []
i = input('반응물의 수를 알려주세요')
for j in range(int(i)) :
    list_i.append(input('반응물을 모두 넣어주세요'))
f = input('생성물의 수를 알려주세요')
for j in range(int(f)) :
    list_f.append(input('생성물을 모두 넣어주세요'))
    
dicts_i = []
dicts_f = []#성분 분해해 리스트에 모은다
for i in list_i :
    dicts_i.append(conf(atomix(i)))
for i in list_f :
    dicts_f.append(conf(atomix(i)))

keylist_i = keylist(dicts_i)
keylist_f = keylist(dicts_f)
if sorted(keylist_i) != sorted(keylist_f) :
    print('잘못된 수식입니다!')
    sys.exit()

last_e = []
for i in keylist_i :
    a = []
    for j in dicts_i :
        if i in j :
            a.append(j[i])
        else :
            a.append(0)
    for j in dicts_f :
        if i in j :
            a.append(-j[i])
        else :
            a.append(0)
    last_e.append(a)

ap = []
for i in range(len(keylist_i)) :
    ap.append(0)
ap.append(1)
last_e.append(ap)    

clean = 1
flag = False
while not flag :
    last_f = [0]
    for i in keylist_i :
        last_f.append(0)
    last_f[-1] = clean#여기를 바꾼다
    if isresult(last_e, last_f) == True :
        result = np.linalg.solve(last_e,last_f)
        for j in result :   
            if float(j) - int(j) == 0 :
                flag = True
            else :
                flag = False
                break
    else :
        print('잘못된 수식입니다!')
        sys.exit()
    clean = clean + 1

eq_i = []
eq_f = []
cnt_i = 0
cnt_j = 0
for i in list_i :
    if int(result[cnt_i]) == 1 :
        eq_i.append(str(i))
    else: 
        eq_i.append(str(int(result[cnt_i])) + str(i))
    cnt_i = cnt_i + 1
    
for j in list_f :
    if len(list_i)+cnt_j+1 <= len(result) :
        if int(result[len(list_i)+cnt_j]) == 1 :
            eq_f.append(str(j))
        else: 
            eq_f.append(str(int(result[len(list_i)+cnt_j])) + str(j))
        cnt_j= cnt_j + 1
    else :
        break

for i in eq_i :
    if eq_i[0] == i :
        a = i
    else :
        a = a + '+' + i
for i in eq_f :
    if eq_f[0] == i :
        b = i
    else :
        b = b + '+' + i

c = a + '->' + b
print(c)
