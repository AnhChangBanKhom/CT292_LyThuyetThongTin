#Họ Tên: Đặng Văn Khốm
#MSSV: B2017051

#câu 1
j=[]
for i in range(100, 301):
    if (i%2==0):
       j.append(str(i))
print (', '.join(j))


#câu 2
n = int(input('nhap N: '))
a=[]
for i in range(n+1):
    a=a+[ int(input('nhap a[%d]  ' %i))]
for i in range(n+1):
    if a[i]%2==1: print(a[i],end=', ' )

# câu 3
d=dict()
for i in range(1,21):
    d[i]=i*i
print (d)

# câu 4
a=[12,24,35,70,88,120,155]
del a[5]
del  a[4]
del a[0]
print(a)


# câu 5
a= {12,24,35,70,88,120}
b= {12,24,35,78,88,120,155}
#print(a | b)
print(a & b)
#print(a - b)
#rint(b - a)
#print(a ^ b)

#câu 6
li=list()
for i in range(1,21):
    li.append(i**2)
print (li[5:])


#câu 7
l1 = []
for i in range(1, 8):
    while True:
        n = input("Nhập phần tử thứ " + str(i) + " ")
        if n.isdecimal() == True:
            l1.append(int(n))
            break
        print("Giá trị là số, hãy nhập lại")
t1 = tuple(l1)
l2 = []
for i in t1:
    if i%2 == 0:
        l2.append(i)
t2 = tuple(l2)
for i in t2:
    print(i)


#câu 8
from collections import Counter
a=input("nhap chu cai ")
n = Counter(a)
print(n)


#câu 9
a = input('Nhap 1 cau bat ky: ')
print(''.join(reversed(a)))

# Câu 10
while True:
    n = input("Nhập chuỗi ")
    if len(n) >= 2:
        break
    print("chuỗi từ 2 ký tự trở lên, hãy nhập lại")
c2 = ""
if len(n) == 2:
    c2 += n[0] + n[1]
if len(n) == 3:
    c2 += n[0] + n[1] + n[2]
if len(n) > 3:
    c2 += n[0] + n[1] + n[len(n) -2] + n[len(n) -1]
print(c2)


#câu 11
c1 = input("Nhập chuỗi 1: ")
c2 = input("Nhập chuỗi 2: ")
t1 = c2[0:2]
t2 = c1[0:2]
t1 += c1[-1]
t2 += c2[-1]
t3 = t1 + "  " + t2
print(t3)

# Câu 13
c = input("Nhập chuỗi ")
l = []
for i in range(0,len(c)):
    l.append(c[i])
for i in range(0,len(l)-1):
    flag = 0
    for j in range(i+1,len(l)):
        if l[i] == l[j]:
            l[j] = "@"
            flag = 1
            break
    if flag == 1:
        break
c1 = ""
for i in l:
    c1 += i
print(c1)



# Câu 14
def getsuffix(a,b):
    s = set()
    for i in a:
        for j in b:
            if j.startswith(i) == True and len(i) < len(j):
                l = j.split(i,1)
                s.add(l[1])
    for i in b:
        for j in a:
            if j.startswith(i) == True and len(i) < len(j):
                l = j.split(i,1)
                s.add(l[1])
    return s



# Câu 15
def Kiemtradung(l, s):
    if len(s) == 0:
        return 1
    if l[0].isdisjoint(s) == False:
        return 2
    k = 0
    for i in l:
        t = i.difference(s)
        if len(t) == 0:
            k = 1
            break
    if k == 1:
        return 3
    return 0

def Kiemtrabangma(a):
    l = [set(a),getsuffix(a,a)]
    cnt = 2
    while True:
        s = getsuffix(list(l[cnt-1]),list(l[0]))
        flag = Kiemtradung(l,s)
        if flag == 1 or flag == 3:
            print ("Đây là bảng mã tách được")
            break
        if flag == 2:
            print ("Đây là bảng mã không tách được")
            break
        l.append(s)
        cnt += 1

# Câu 16
a = ["abc","a","ab","b","bcad"]
b = ["a", "ad","bbcde", "c", "deb","ebd"]
c = ["a", "ad","bbcde", "c", "deb","ebad"]
d = ["010","0001","0110","1100","00011","00110","11110","101011"]
Kiemtrabangma(c)
