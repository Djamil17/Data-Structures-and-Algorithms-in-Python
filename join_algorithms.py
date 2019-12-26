
import random

## function
class Relation:

    def __init__(self, n, m, init=True):
        self.n = n
        self.m = m
        self.size= n * m
        if init:
            self.relation = [[random.randint(0,5)] * n for x in range(m)]
        else:
            self.relation= [ ]

    def setTuple(self,idx, item):
        self.relation[idx] = item

    def setAtt(self, *arg):
      if len(list(arg)) == self.n:
        return self.relation.insert(0, list(arg))
      else:
        raise ValueError('Need to make attribute list same size as n...')

    def __setitem__(self,idx,item):
        self.relation[idx]=item

    def __getitem__(self, idx):
        return self.relation[idx]

    def __str__(self):
        return (str(self.relation))

def nested_loop_join(left_relation, right_relation):
    for ltuple in l[1:]:
        for rtuple in r[1:]:
            if ltuple == rtuple:
                yield ltuple + rtuple

#
r= Relation(5,5)
l= Relation(5,5)
l.setAtt('foo','bar','tar', 'grault','baaz')
r.setAtt('foo','bar','tar', 'grault','baaz')
print(r)
print(l)
n=nested_loop_join(l,r)
print(list(n))


