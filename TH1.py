#Dang Van Khom
#B2017051
# hom 02 


#Cau 1
print("Hello "+ input("Nhap: "))

#cau 2
kt=True
while(kt==True):
    n = int(input("Nhap vao so nguyen n: "))
    if(n> 0 and n< 10):
        a = n*10+n
        b = n*100 +a
        c= n*1000 +b
        print(n,"+",a,"+",b,"+",c,"=", n + a + b + c)
        kt=False

#cau 3
kt=True
a = int(input("Nhap vao so a: "))
while(kt==True):
    b= int(input("Nhap vao so b: "))
    if(b!=0):
        print(" a+b=  ",a+b,"\n",
              "a-b=  ",a-b,"\n",
              "a*b=  ",a*b,"\n",
              "a/b=  ",a/b,"\n",
              "a%b=  ",a%b,"\n",
              "a**b= ",a**b)
        kt=False

#cau 4
r = float(input("Nhap vao ban kinh r= "))
print("chu vi hinh tron: cv= ", 2* 3.14 *r)
print("Dien tich hinh tron: S= ", 2*3.14*r*r)

#cau 5
kt=True
s=1
i=1
while(kt==True):
    n= int(input("Nhap vao so nguyen n: "))
    if(n>0):
        for i in range(1, n+1):
            s=s*i
            i=i+1
        print(n,"!     = ",s)


#cau 6
kt=True
import math
a= float(input("Nhap vao so a: "))
b= float(input("Nhap vao so b: "))
c= float(input("Nhap vao so c: "))

while(kt==True):
    if(b!=0):
        print("Phuong trinh co dang: ",a,"X^2","  +  ",b,"X","  +  ",c,"  =   0")
        delta = b*b - 4*a*c
        if(delta<0):
            print("Phuong trinh vo nghiem ")
            print("-------the end---------")
            kt=False
        else:
            if(delta==0):
                print("Phuong trinh co 2 nghiem kep la: X1 = X2 = ", -b/2*a)
                print("------------the end--------------")
                kt=False
            if(delta>0):
                print("Phuong trinh co 2 nghiem phan biet la: ","\n")
                print("X1= ", (-b+math.sqrt(delta))/(2*a))
                print("X2= ", (-b-math.sqrt(delta))/(2*a))
                print("-----------the end-------------")
                kt=False
    else:
        b=float(input("Nhap lai b:"))

#cau 7
for i in range(5000, 7000):
    if(i%7==0 and i%5 != 0):
        print("So chia het cho 7 khong chia het cho 5 la: ", i)

#cau 8
n= int(input("Nhap vao so thap phan: "))

i = 10
while(i >= 0):
    if(int(n / (2**i)) == 1):
        print(1)
    else:
        print(0)
    n = n % 2**i
    i -= 1

# cau 9:

def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

def bscnn(a, b):
    return int((a * b) / uscln(a, b))

a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
print("Ước số chung lớn nhất của", a, "và", b, "là:", uscln(a, b))
print("Bội số chung nhỏ nhất của", a, "và", b, "là:", bscnn(a, b))


# CAU 10

def isPrimeNumber(n):
    if (n < 2):
        return False
 
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
 
n = int(input("Nhập số nguyên dương n = "))
print ("Tất cả các số nguyên tố nhỏ hơn", n, "là:")
sb = ""
if (n >= 2):
    sb = sb + "2" + " "
for i in range (3, n+1):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " "
    i = i + 2
print('[', sb, ']')
'''

# cau 11:
'''
def isPrimeNumber(n):
    if (n < 2):
        return False

    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot + 1):
        if (n % i == 0):
            return False
    return True
 
print ("Liệt kê tất cả số nguyên tố có 4 chữ số:")
sb = ""
dem = 0
for i in range (1001, 9999):
    if (isPrimeNumber(i)):
        sb = sb + str(i) + " "
        dem += 1
    i = i + 2
print('[', sb, ']')
print("Tổng các số nguyên tố có 4 chữ số là:", dem)
'''
# cau 12:
'''
def sumT(n):
    total = 0
    while (True):
        if (n >= 0):
            while (n > 0):
                total = total + n % 10
                n = int(n / 10)
            return total
        else:
            print('nhap lai: ')

 
n = int(input("Nhập số nguyên dương n = "))
print("Tổng các chữ số của", n , "là", sumT(n))
'''

# cau 13:
'''
def findOdd (n):
    if( int(i) % 2 != 0 and int(i/10)% 2 != 0 and int(i/100)% 2 != 0 and int(i/1000)% 2 != 0):
        return True
    return False

add = []
for i in range(1000,2000):
    if(findOdd(i)):
        b = i
        add.append(i)
print(add)
'''
# cau 14:
'''
n=int(input("Nhập số n: "))
s=0
for i in range(1,n+1):
    s+=i/(i+1)
print("Kết quả:",s)
'''

# cau 15:
'''
def entropy (x, y, z):
    result =float(-(x*math.log2(x)+y*math.log2(y) + z*math.log2(z)))
    return result

def entropy1 (x, y):
    result =float(-(x*math.log2(x)+y*math.log2(y)))
    return result


while (True):
    x = float(input('nhap vao x: '))
    y = float(input('nhap vao y: '))
    z = float(input('nhap vao z(neu khong co thi nhap 0): '))
    if ((x + y + z) == 1 and z != 0):
        print('entropy (',x,',', y,',', z,')','=', entropy(x, y, z))
        break
    if ((x + y + z) == 1 and z == 0):
        print('entropy (',x,',', y,')','=', entropy1(x, y))
        break
    else:
        print('loi!! nhap lai:')


