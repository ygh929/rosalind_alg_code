class pop_int(int):
    def pop(self,x):
        temp=self
        del self
        return temp


def merge(l1,l2,n1,n2):
    l=list()
    lt=list((l1,l2))
    for i in range(n1+n2):
        try:
            l.append(lt[l2[0]<l1[0]].pop(0))
        except:
            try:
                l.append(lt[0].pop(0))
            except:
                l.append(lt[1].pop(0))
    return l


f=open('rosalind_mer.txt')
n1=int(f.readline().split()[0])
l1=map(pop_int,list(f.readline().split()))
n2=int(f.readline().split()[0])
l2=map(pop_int,list(f.readline().split()))

print ' '.join(map(str,merge(l1,l2,n1,n2)))