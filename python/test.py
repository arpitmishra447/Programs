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
age = int(input()) # int: Read a number as integer from standard input
dob = input() # str: Read a string of format dd/mm/yy from standard input
day, month, year = int(dob[0:2]),int(dob[3:5]),int(dob[6:8]) # int, int, int: Get the correct parts from dob as int

fifth_birthday =f"{day}/{month}/{year+5}" # str: fifth birthday formatted as day/month/year 

last_birthday = f"{day}/{month}/{year+age}" # str: last birthday formatted as day/month/year

tenth_month = f"{day}/{((month+10)%12)+1}/{year}" # str: dob same day after 10 months formatted as day/month/year

# print tenth_month, fifth_birthday and last_birthday in same line separated by comma and a space
print(f"{tenth_month},{fifth_birthday},{last_birthday}")

weight = float(input()) # float: Read a number as float from stdin(Standard input)

weight_readable = f"{int(weight)} kg {int(weight%1*1000)} grams" # str: reformat weight of format 55 kg 250 grams

# print weight_readable 
print(weight_readable,end="")
