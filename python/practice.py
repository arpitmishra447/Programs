n=int(input())
#l=[list(input().split()) for i in range(n+1)]
l=[["CLASS",      "NAME",       "MARKS" ,     "ID"]
,[4      ,    "Iain"    ,   96    ,     1]
,[2       ,   "Jeremy"  ,   77    ,     2]
,[5       ,   "Derek"   ,   94    ,     3]
,[4       ,   "Ryan"   ,   52    ,     4]
,[3      ,    "Leslie"   ,  85    ,     5]]
a=[i for i in range(4) if l[0][i]=="MARKS"]
print(a)
a=2
print(a)
print(format(sum([ int(l[i][a]) for i in range(1,n+1)])/n,".2f"))