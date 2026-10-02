h=int(input("enter no of holidays"))
if h<0 or h>365:
    print("invalid input")
else:
    w=365-h
    p=(w*63)+h*127
    n=30000
    diff=abs(norm-p)
    hours=diff//60
    min=diff%60
    if p<=norm:
        print("tom sleeps well")
    else:
        print("tom will run away")