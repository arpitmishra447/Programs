a=["car","cat","rat","act","art","tar","arc","tac"]
def func(e):
    return e[1]
newl=[]
for i in a:
    newl.append(["".join(sorted(i)),i])
newl.sort()
print(newl)