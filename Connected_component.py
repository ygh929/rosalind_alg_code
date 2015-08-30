from Breadth_First import *
class comp_graph(graph):
    def count_comp(self):

        c=0
        temp=graph()
        for i in self:
            temp.append(i)
        while temp:
            tempcomp=temp.bf(temp[0])
            newtemp=graph()
            for i in range(len(tempcomp)):
                if tempcomp[i]<0:
                    newtemp.append(temp[i])
            temp=newtemp
            c=c+1
        return (c)

f=open("rosalind_cc.txt",'r')
l1=f.readline().split()
n=int(l1[0])
E=[]
for i in f:
    E.append(map(int,i.split()))
    E.append(map(int,i.split())[::-1])

g=comp_graph()
g.setgraph(n,E)
print g.count_comp()

