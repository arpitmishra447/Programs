'''def f(a,b):
    if b==0:
        print("enter valid value!!")
        exit()
    if a<b:
        return a
    return f(a-b,b)
        
print(f(4,2))'''
'''def is_inside_rectangle(x1,y1,x2,y2,x,y):
    return (x<=x1 and x>=x2 and y<=y1 and y>=y2) or (x>=x1 and x<=x2 and y>=y1 and y<=y2) 
 
print(is_inside_rectangle(1,2,3,4,2,3)==True)
print(is_inside_rectangle(-1,-2,-3,-4,-2,-3)==True)
print(is_inside_rectangle(3,4,1,2,2,3)==True)
print(is_inside_rectangle(-3,-4,-1,-2,-2,-3)==True)
print(is_inside_rectangle(1,2,3,4,5,6)==False)
print(is_inside_rectangle(-1,-2,-3,-4,-5,-6)==False)
print(is_inside_rectangle(3,4,1,2,5,6)==False)
print(is_inside_rectangle(-3,-4,-1,-2,-5,-6)==False)'''
'''x=4
y=3
x=x^y
y=y^x
x=x^y
print(x,y)'''
'''def HCF(n, m):
    print(f"Calling {n}, {m}")
    if n > m:
        print("Swapping")
        n, m = m, n
    rem = m % n
    print(f"Remainder: {rem}")
    if rem == 0:
        return n
    else:
        return HCF(rem, n)'''
'''def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)
print(fact(5))'''
