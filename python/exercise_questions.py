#stock question
'''def maxprofit(a):
    max=a[0]
    min=a[0]
    for i in range(1,len(a)):
        if a[i]>max:
            max=a[i]
    for i in range(len(a)):
        if a[i]==max:
            mi=i
            break
    for i in range(1,mi):
        if a[i]<min:
            min=a[i]
    print(((max-min)/min)*100)
a=[10,19,78,1,45,12]
maxprofit(a)'''
#permutatin question
'''articles = ['a', 'the', 'that']
adjectives = ["good", "bad", "nice", "blue", "light"]
words = ["city", "sky", "water", "person"]
for i in articles:
    for j in adjectives:
        for k in words:
            print(f"{i} {j} {k}")'''
#average and sd
l=list(map(eval,input("Enter the elements:").split()))
#l=list(eval(input("Enter the elements:")))
s=0
ds=0
for i in range(len(l)):
    s+=l[i]
a=s/len(l)
d=[(l[j]-a)**2 for j in range(len(l))]
for k in range(len(d)):
    ds+=d[k]
sd=(ds/(len(l)))**0.5
print(a,sd)