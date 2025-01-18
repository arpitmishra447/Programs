def solve1(eqn):
    if (len(eqn) !=2):
        return None
    result=[eqn[1]/eqn[0]]
    return result
def solveBySubstitution(eqn, variableValues):
    L=len(eqn)
    if (len(eqn)<=2):
        return None
    #print ("Testing replacement for EQN:",eqn, "and results:", variableResults)
   
    totalVariables = len(variableValues)
    solvedEqn=[]
    lhsVal = 0
    rhsVal =  eqn[L-1]
    k=L-1
    for i in range(0 , totalVariables):
        val = variableValues[i]
        k-=1
        lhsVal += eqn[k] * val
        
    solvedVal = rhsVal - lhsVal
    #print("LHS:", lhsVal, ", RHS:", rhsVal, ", SolvedVal:", solvedVal)
    solvedEqn =[]
    for j in range (0, k):
        solvedEqn.append(eqn[j])
    solvedEqn.append(solvedVal)
        
    #print(i,"Solved Equation:", solvedEqn)
    return solvedEqn
def eliminateOne(arr1, arr2):
    #print("Eliminating One from:", arr1, ",", arr2)
    multiple = arr2[0]/arr1[0]
    L = len(arr2)
    result = []
    for i in range(1,L):
        res = arr2[i] - arr1[i] * multiple
        result.append(res)
    return result
def reduce(eqns) :
    #print("Eliminating for:", eqns)
    L = len(eqns)
    if (L < 1):
        return None
    elif (L == 1):
        return eqns
    else:
        firstEqn = eqns[0]
        new_eqns=[]
        for i in range(1, L) :
            secondEqn = eqns[i]
            result = eliminateOne(firstEqn, secondEqn)
            new_eqns.append(result)
        #print("Elimination result:", new_eqns)
        return new_eqns
def solve(eqns):
    if len(eqns) < 1 | len(eqns) < len(eqns[0]) - 1:
        return None
    
    complete_results = []
    
    if len(eqns) == 1:
        #[0 10]
        return solve1(eqns[0])
    else :
        # eliminiate one variable and call solve(new_eqns)
        new_eqns = reduce(eqns)
        results = solve(new_eqns)
        
        L = len(results)
        for i in range(0 , L):
            complete_results.append(results[i])
   
        if (len(complete_results) < len (eqns)):
            #need to solve by substituting the results
            substituted_eqn =solveBySubstitution(eqns[0], complete_results)
            solved_eqns=[]
            solved_eqns.append(substituted_eqn)
            results = solve(solved_eqns)
            L = len(results)
            for i in range(0, L):
                complete_results.append(results[i])
    
    return complete_results
eq1 = [1, 1, 1,  6]
eq2 = [2, 1, -1,  1]
eq3 = [3, -2, 1, 2]

eqns = [eq1, eq2, eq3]
result = solve(eqns)
print(result)
eq1 = [1, 1, 1, 1, 10]
eq2 = [2, -1, 3, -1, 5]
eq3 = [4, 2,-1,1, 9]
eq4 = [1, -2,2, 3, 15]
eqns = [eq1, eq2, eq3, eq4]
result = solve(eqns)
print(result)