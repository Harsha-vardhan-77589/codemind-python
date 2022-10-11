t=int(input())
for i in range(t):
    n=int(input())
    n_p=n
    p_p=n
    while True:
        fc=0
        for j in range(1,n_p+1):
              if n_p%j==0:
                   fc+=1
        if fc==2:
             break
        n_p+=1
        
        
        while True:
            fj=0
            for k in range(1,p_p+1):
                if p_p%k == 0:
                     fj+=1
            if fj==2:
                   break
            p_p-=1
    if n-p_p<=n_p-n:
            print(p_p)
    else:
            print(n_p)

   