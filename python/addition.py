def add(arr1,arr2):
    a1,a2=len(arr1),len(arr2)
    narr1=[]
    narr2=[]
    if a1<a2:
        d=a2-a1
        for i in range(d+1):
            if i==d:
                narr1.extend(arr1)
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
        narr1=arr1
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
print(add([8,8,9,6],[3,6,4,8,8]))