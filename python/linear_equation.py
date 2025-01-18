import numpy as np
def sol(eqns):
    pass
    
#n=int(input("Enter the Number you equations you want to enter:"))
#eqns=[list(eval(input(f"enter the eqn {i+1}:"))) for i in range(n)]
eqns=[[1, 1, 1, 10],[2, 3, 4, 50],[3, 5, -8, 100]]
x=np.array(np.array_split([eqns[i][j] for i in range(len(eqns)) for j in range(len(eqns[0])-1)],len(eqns)))
y=np.array([eqns[i][-1] for i in range(len(eqns))])
#print(f"{x}\n{y}")
print(np.linalg.solve(x,y))