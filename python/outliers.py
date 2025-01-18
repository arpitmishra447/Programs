def mean(arr):
    s,l=0,len(arr)
    for i in range(l):
        s+=arr[i]
    return s/l
def sd(arr):
    l,m=len(arr),mean(arr)
    for i in range(l):
        s=+(arr[i]-m)**2
    s=(s/l)**0.5
    return s
def outliers(arr):
    s=sd(arr)
    m=mean(arr)
    rpos=m+2*s
    rneg=m-2*s
    for i in range(len(arr)):
        if arr[i]>rpos or arr[i]<rneg:
            print(f"{arr[i]} is an outlier present at index {i}")            
outliers([7, 7, 8, 8, 3])