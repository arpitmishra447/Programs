class Zeromodel:
    def __init__(self,a,b):
        self.x1=a[0]
        self.y1=a[1]
        self.x2=b[0]
        self.y2=b[1]
    def fit(self):
        x1,y1=self.x1,self.y1
        x2,y2=self.x2,self.y2
        m=(y2-y1)/(x2-x1)
        c=(y1)-(m*x1)
        return m,c
    def predict(self,x):
        m,c=Zeromodel.fit(self)
        y=m*x+c
        return y
    def __repr__(self):
        return f"{(self.x1,self.y1),(self.x1,self.y1)}"
a=2,3
b=4,5
v=Zeromodel(a,b)
v.fit()
print(v.predict(10))