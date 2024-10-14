def f(a,b):
    if b==0:
        print("enter valid value!!")
        exit()
    if a<b:
        return a
    return f(a-b,b)
        
print(f(125,0))
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