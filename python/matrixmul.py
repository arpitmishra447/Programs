import numpy as np
def mul(arr1,arr2):
    r1,c1=len(arr1),len(arr1[0])
    r2,c2=len(arr2),len(arr2[0])
    result=[]
    if c1!=r2:
        None
    else:
        for i in range(r1):
            r=[]
            for j in range(c2):
                s=0
                for k in range(c1):
                    s+=(arr1[i][k]*arr2[k][j])
                r.append(s)
            result.append(r)
    return result 
                
x=mul([[1,2],[3,4],[5,6]],[[1,3,5],[2,4,6]])
for i in x:
    print(i)
