

class heap(list):
    def addnum(self, x):
        self.append(x)
        l=len(self)
        current=l-1
        while (current>=1) and self[current]>self[(current-1)/2]:
            temp=self[(current-1)/2]
            self[(current-1)/2]=self[current]
            self[current]=temp
            current=(current-1)/2


test=heap([])
f=open('rosalind_hea.txt','r')
l1=f.readline()
num=f.readline().split()
for i in num:
    i=int(i)
    test.addnum(i)

print ' '.join(map(str,test))

