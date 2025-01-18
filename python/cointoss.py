import random
import numpy as np
#task 1
'''def cointoss():
    x=np.random.choice([0,1])
    if x==0:
        print("Head")
    else:
        print("Tail")'''
#task 2
'''def cointoss():
    x=np.random.choice([0,1,1,1])
    if x==0:
        print("Head")
    else:
        print("Tail")'''
#task 3
def number(probs):
    x=[]
    
    for i in range(len(probs)):
        for j in range(int(probs[i]*100)):
            x.append(i)
    y=np.array(x)
    print(np.random.choice(x))
    
number([0.1, .2, .7])