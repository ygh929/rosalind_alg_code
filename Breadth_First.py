
class node(object):
    def __init__(self):
        self.out=[]
        self.traveled=False
        self.step=-1

class graph(list):
    def setgraph(self,n,E):
        for i in range(n):
            self.append(node())
        for i in E:
            self[i[0]-1].out.append(self[i[1]-1])

    def bf(self,node):
        Q=[node]
        node.step=0
        node.traveled=True
        while Q:
            temp=Q.pop(0)
            for i in temp.out:
                if i.traveled==False:
                    i.traveled=True
                    Q.append(i)
                    i.step=temp.step+1
        return [i.step for i in self]

if __name__=='__main__':
    f=open("rosalind_bfs.txt",'r')
    l1=f.readline().split()
    n=int(l1[0])
    E=[]
    for i in f:
        E.append(map(int,i.split()))
    g=graph()
    g.setgraph(n,E)
    print ' '.join(map (str,g.bf(g[0])))




