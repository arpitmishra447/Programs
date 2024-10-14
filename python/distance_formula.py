i=True
while i==True:
    c=int(input("Choose 1 for 3d fig|2 for 2d fig|3 to exit:"))
    if c==1:
        #for 3d
        x1=int(input("Enter input for x1:"))
        x2=int(input("Enter input for x2:"))
        y1=int(input("Enter input for y1:"))
        y2=int(input("Enter input for y2:"))
        z1=int(input("Enter input for z1:"))
        z2=int(input("Enter input for z2:"))
        d=((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**0.5
        print("distance between point 1 to point 2 is ",d)
    elif c==2:
        #for 2d 
        x1=int(input("Enter input for x1:"))
        x2=int(input("Enter input for x2:"))
        y1=int(input("Enter input for y1:"))
        y2=int(input("Enter input for y2:"))
        d=((x2-x1)**2+(y2-y1)**2)**0.5
        print("distance between point 1 to point 2 is ",d)
    elif c==3:
        i=False
    else:
        print("wrong Choice! try again")