def learn(x1,x2,y1,y2):
    m=(y2-y1)/(x2-x1)
    c=((y2*x1)-(y1*x2))/(x1-x2)
    return m,c
def predict(x,slope_intercept):
    y=slope_intercept[0]*x+slope_intercept[1]
    return y
slope_intercept=learn(1,5,2,9)
print(predict(10,slope_intercept))