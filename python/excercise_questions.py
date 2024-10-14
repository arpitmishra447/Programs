#stock question
def maxprofit(a):
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
maxprofit(a)