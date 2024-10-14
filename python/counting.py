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
    return d
def main():
            b=int(input("Enter your Base:"))
            n=int(input("Enter your place you want the counting upto:"))
            u=10**n
            for i in range(u):
                if len(str(dtob(b,i)))<n:
                    if int(str(dtob(b,i))[-1]) == (b-1):
                        print(dtob(b,i))
                    else:
                        print(dtob(b,i),end=" ")
                else:
                    break
main()
