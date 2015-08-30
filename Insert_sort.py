def insert_sort(A,l):
    n=0
    for k in range(l):
        while k>0 and A[k]<A[k-1]:
            temp=A[k-1]
            A[k-1]=A[k]
            A[k]=temp
            k=k-1
            n=n+1
    return (n)

f=open('rosalind_ins.txt','r')
l=int(f.readline().strip())
A=map(int, f.readline().split(" "))
print insert_sort(A,l)