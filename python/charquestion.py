def convert(s):
    n=str(s)
    a=""
    for i in range(len(n)):
        if ord(n[i])>=48 and ord(n[i])<=57:
            a+=chr(ord(n[i])+2358)
        else:
            a+=n[i]
    print(a)
convert(float(input("Enter the number to convert:")))