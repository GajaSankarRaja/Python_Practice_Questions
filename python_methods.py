'''
def func(arr):
    temp1=arr[0]+arr[1]
    temp2=abs(arr[0]-arr[1])
    arr[0]=temp1
    arr[1]=temp2
a,b,arr=10,9,[]
arr.append(a)
arr.append(b)
print(a,b)
func(arr)
a=arr[0]
b=arr[1]
print(a,b)

a=input()
result=''
for i in a:
    if 'a'<=i<='z':
        result+=chr(ord(i)-32)
    else:
        result+=chr(ord(i)+32)
print(result)


d,num=map(int,input().split())
res=''
counter=remainder=0
while num!=0:
    remainder=num%d
    num=num//d
    if d>num:
        res=res+chr(ord('A')+counter)
        counter+=1
    print(f"Number: {num}")
    print(f"Remainder: {remainder}")
    print("##########")
print(str(remainder)+res[::-1])
'''
