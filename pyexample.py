"""
arr=list(map(int,input("Enter: ").split()))
rat,unit=map(int,input("Enter: ").split())
sufficient=rat*unit
current=0
count=0
if len(arr):
    print(-1)
for i in arr:
    current+=i
    count+=1
    if current>=sufficient:
        print(count)
        break
else:
    print(0)

input_str=input("enter: ")
a=int(input_str[0])
i=1
while i<len(input_str):
    if input_str[i]=='A':
        a&=int(input_str[i+1])
    elif input_str[i]=='B':
        a|=int(input_str[i+1])
    else:
        a^=int(input_str[i+1])
    i+=2
print(a)

input_arr=list(map(int,input().split()))
n=len(arr)
num=int(input())
for i in range(1,n):
    if abs(arr[i]-arr[i-1])<=num:
        continue
else:
    print("Case Failed")

n,m=map(int,input().split())
current1=current=0
for i in range(1,m+1):
    if i%n==0:
        current+=i
    else:
        current1+=i
print(current1-current)

input_arr=list(map(int,input().split()))
input_sum=int(input())
first=second=float('inf')
for i in input_arr:
    if i<first and i!=first:
        second=first
        first=i
    elif i<second and (i!=first and i!=second):
        second=i
print(first,second)
if first+second<input_sum:
    print(first*second)
else:
    print(0)
"""
"""
num1,num2=map(int,input().split())
carry=0
counter=0
while num1 and num2:
    r1,r2=num1%10,num2%10
    if r1!=0 and r2!=0:
        carry+=r1+r2
        if carry!=0:
            counter+=1
    num1//=10
    num2//=10

print(counter)

a,b=map(int,input().split())
#c=a^b
num1=num2=""
while a:
    num1=str(a%2)+num1
    a//=2
while b:
    num2=str(b%2)+num2
    b//=2
counter=0
i=j=0
while i<len(num1) and j<len(num2):
    if num1[i]!=num2[j]:
        counter+=1
    i+=1
    j+=1
print(counter)

n=input()
res={}
result=""
for i in n:
    if i.isupper():
        if i in res:
            res[i]+=1
        else:
            res[i]=1
    else:
        result+=str(-1)
        break
for key,value in res.items():
    if value==1:
        continue
    else:
        result+=key
print(result)

start,end=map(int,input().split())
blocked=list(map(int,input().split()))
channels=list(map(int,input().split()))
clicks=0
last=-1
for i in range(len(channels)):
    if channels[i] in blocked:
        continue
    if channels[i]>9:
        if channels[i]!=last:
            last=channels[i-1]
            clicks+=min(channels[i]-1,2)
        else:
            clicks+=1
    else:
        if channels[i]!=last:
            last=channels[i-1]
            clicks+=min(channels[i]-1,1)
        else:
            clicks+=1
print(clicks)

def sum_of_digits(input_str):
    s=0
    for i in input_str:
        s+=int(i)
    return s
n=input()
res={}
result=''
if len(n)<=10:
    if len(n)==sum_of_digits(n):
        for i in n:
            if i in res:
                res[i]+=1
            else:
                res[i]=1
        print(res)
        for i in range(len(n)):
            result += str(res.get(str(i), 0))
        if result==n:
            print("YES")
        else:
            print(-1)
    else:
        print(-1)
else:
    print(-1)

def sum_of_digits(num):
    n=0
    while num:
        n+=(num%10)
        num//=10
    return n
n=int(input())
arr=list(map(int,input().split()))
hashmap={}
for i in arr:
    hashmap[i]=sum_of_digits(i)
small=float('inf')
small_key=-1
large_key=-1
large=float('-inf')
for key,value in hashmap.items():
    if value%2!=0:
        if value<small:
            small=value
            small_key=key
    else:
        if value>large:
            large=value
            large_key=key
print(hashmap)
print(small,large)
print(small_key,large_key)
print(small_key+large_key)

name=input("enter a name: ")
days=int(input("enter days: "))
work_days=input("Days: ")
counter=0
for i in work_days:
    if i=='P':
        counter+=1
if counter/days<0.75:
    print("Not Eligible")
else:
    print("Eligible")
def func(text,input_key):
    result = ""
    for i in text:
        if i.isalpha():
            if not result:
                result += chr(ord(i) + input_key)
            else:
                result = result + chr(ord(i) + input_key)
        elif i.isdigit():
            counter=int(i)+input_key
            if counter>9:
                result+='0'
            else:
                result+=str(counter)
    return result
plain=input().split()
key=int(input())
final=""
for i in plain:
    final+=func(i,key)+" "
print(final)

n=int(input("enter a number: "))
time=[]
amount=[]
for i in range(n):
    temp=list(map(int,input("Enter a time :").split()))
    time.append(temp)
    amount.append(int(input("enter amount: ")))
time.sort()
ans,result=[],[]
counter=0
for i in range(n):
    if not ans :
        ans.append(time[i])
    if ans[-1][1]>time[i][0] and ans[-1][1]!=time[i][0]:
        counter += 1
        ans.append(time[i])
        result.append(amount[i])
print(time)
print(counter)
print(ans)
print(result)

n=int(input("enter a number: "))
inventory={}
while n:
    key=input("Enter a product: ")
    value=int(input("Enter a quantity: "))
    inventory[key]=value
    n-=1
for key,value in inventory.items():
    if value<10:
        print(key)

n=int(input("enter a number: "))
input_sum=int(input("enter a number: "))
result=""
if input_sum>9*n:
    print("-1")
else:
    for i in range(n):
        if input_sum>=9:
            result+=str(9)
            input_sum-=9
        else:
            result+=str(input_sum)
            input_sum=0
print(result)
"""


