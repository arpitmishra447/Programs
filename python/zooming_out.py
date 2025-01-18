import matplotlib.pyplot as plt
import matplotlib.image as img
#image = img.imread("C:\programes\python\istockphoto-2155904673-1024x1024.jpg")
def clone(arr):
    newarr=[]
    for k in range(2):
        for i in range(len(arr)):
            tmp=[]
            for j in range(len(arr[0])):
                tmp.append(arr[i][j])
                tmp.append(arr[i][j])
            newarr.append(tmp)
    return (newarr)
image=[[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0],[1,1,0,0]]

print(plt.imshow(image))
x=clone(image)
for i in x:
    print(i)
print(plt.imshow(x))