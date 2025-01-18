def multiplyby1(arr1,digit):
    l=len(arr1)
    res=[]
    carry=0
    l=len(arr1)
    while l>0:
        tmp=arr1[l-1]*digit
        res.append((tmp+carry)%10)
        carry=tmp//10
        l-=1
    if carry!=0:
        res.append(carry)
    return (res[::-1])
def shiftandadd(arr1,arr2):
    x=arr1
    x.append(0)
    a1,a2=len(x),len(arr2)
    narr1=[]
    narr2=[]
    if a1<a2:
        d=a2-a1
        for i in range(d+1):
            if i==d:
                narr1.extend(x)
            else:
                narr1.append(0)
        narr2=arr2
    else:
        d=a1-a2
        for i in range(d+1):
            if i==d:
                narr2.extend(arr2)
            else:
                narr2.append(0)
        narr1=x
    l=len(narr1)
    carry=0
    result=[]
    while l>0:
        tmp=narr1[l-1]+narr2[l-1]
        result.append((tmp+carry)%10)
        carry=tmp//10
        l-=1
    if carry!=0:
        result.append(carry)
    return (result[::-1])
        
def multiply(num1,num2):
    l=len(num2)
    arr=[]
    while l>0:
        arr.append(multiplyby1(num1,num2[l-1]))   
        l-=1
    arr1,arr2=arr[l-1],arr[l-2]
    x=shiftandadd(arr1,arr2)
    return shiftandadd(x,arr[0])
print(multiply([1,2,3],[4,5,6]))