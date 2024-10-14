#function to convert from your base to decimal number system
def btod(b,n):
    s=str(n)
    l=len(s)
    a=0
    j=-1
    for i in range(l):
        d=int(s[j])
        a=a+(b**i)*d
        j-=1
    print("The Value of given number in decimal is ",a)
    main()
#function to convert decimal number to your base number system 
def dtob(b,n):
    q=n//b
    r=n%b
    d=str(r)
    while q>=b:
        r=q%b
        q=q//b
        d+=str(r)
    else:
        d+=str(q)
    d=int(d[::-1])
    print("The Value of given decimal in base is ",d)
    main()
def main():
    print('''choose 1 for converting your base to decimal
choose 2 for converting your decimanl to your base
Choose 3 to exit''')
    c=int(input("Enter your Choice:"))
    if c==3:
        print("Have a Nice Day!")
        exit
    else:
        if c==1:
            b=int(input("Enter your Base:"))
            n=int(input("Enter your Value to convert:"))
            n1=str(n)
            d=[]
            bl=[]
            for k in range(b):
                bl.append(k)
            for i in range(len(n1)):
                d.append(int(n1[i]))
            for j in range(len(d)):
                if d[j] not in bl:
                    print("Enter Valid Value!")
                    main()
                    break
                else:
                    if j==(len(d)-1):
                        btod(b,n)
                    else:
                        continue
        elif c==2:
            b=int(input("Enter your Base:"))
            n=int(input("Enter your Value to convert:"))
            dtob(b,n)
        else:
            print("wrong input")
main()
