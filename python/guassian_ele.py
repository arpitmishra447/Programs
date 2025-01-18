def solve1(arr):
    if len(arr)!=2:
        return None
    return [arr[1]/arr[0]]
def solve_substitute(eqn,val):
    if (len(eqn)<=2):
        return None
    e=len(eqn)
    v=len(val)
    lhs=[]
    rhs=eqn[-1]
    result=[]
    for i in range(1,v):
            lhs.append(eqn[i]*val[i-1])
    for i in range(v):
            rhs-=lhs[i]
    rhs=rhs/eqn[0]
    result.append(rhs)
    result.extend(val)
    return result        
#print(solve_substitute([2,5,78],[2]))
#print(solve_substitute([2,5,7.5,78],[2,1]))
def eliminate(arr1,arr2):
    m=arr2[0]/arr1[0]
    result=[]
    for i in range(len(arr1)):
        result.append(arr2[i]-arr1[i]*m)
    result=result[1:]
    return result
#print(eliminate([2,2,2,20],[2,3,4,50]))
def reduce(eqns):
    e=len(eqns)
    r=[]
    if e<1:
        return None
    elif e==1:
        return eqns
    else:
        f=eqns[0]
        for i in range(1,e):
            s=eqns[i]
            r.append(eliminate(f,s))
        return r
eq1 = [1, 1, 1, 10]
eq2 = [2, 3, 4, 50]
eq3 = [3, 5, -8, 100]
eqns = [eq1, eq2, eq3]
#print(reduce(eqns))
def solve(eqns):
    if len(eqns) < 1 or len(eqns) < len(eqns[0]) - 1:
        return None
    cr=[]
    if len(eqns) == 1:
        return solve1(eqns[0])
    else:
        new=reduce(eqns)
        res=solve(new)
        cr.append(res)
        for i in range(len(cr)):
            cr.append(solve_substitute(new[i],cr[0]))
        print(cr)
        #cr.append(solve_substitute(eqns[0],cr))
eq1 = [1, 1, 1, 10]
eq2 = [2, 3, 4, 50]
eq3 = [3, 5, -8, 100]
eqns = [eq1, eq2, eq3]
print(solve(eqns))
                
            
        
        
        
