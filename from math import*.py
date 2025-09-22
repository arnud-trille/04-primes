def est_premier1 (n):
    if n==1:
        return(False)
    for k in range (2,n):
        if n%k==0:
            return(False)
    return(True)
print(est_premier1(11))