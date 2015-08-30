def notfound(x):
    if x==-1:
        return (1)
    else:
        return (0)


def bin_s(k,A,m):
    i=0


    if m>1:
        if m%2==0:
            newm=m/2
            if k>A[m/2-1]:
                i=i+m/2
                newA=A[m/2:]
            elif k==A[m/2-1]:
                return(m/2)
            else:
                newA=A[:m/2]
        else:
            newm=(m-1)/2
            if k==A[(m-1)/2]:
                return ((m+1)/2)
            elif k>A[(m-1)/2]:
                i=i+(m+1)/2
                newA=A[(m+1)/2:]
            else:
                newA=A[:(m-1)/2]

        change=bin_s(k,newA,newm)
        i=i+change
        i=i-notfound(change)*(i+1)

        return(i)
    else:
        if k==A[0]:
            return (1)
        else:
            return -1



f=open("rosalind_bins.txt","r")

m=int(f.next())
f.next()
A=f.next()
K=f.next()
f.close()
A=[int(x) for x in A.split()]
K=[int(x) for x in K.split()]
res=str([bin_s(k,A,m) for k in K]).replace(',','').replace('[','').replace(']','')
print res
