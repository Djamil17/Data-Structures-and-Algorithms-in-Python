"""
Script:join_algorithms.py
Description: Description, explanation of join algorithms, 
especially as applies to tables, or relations 
Author: Djamil Lakhdar-Hamina, Carlos Perez 
Contents: 
1. Join algorithms, relational algebra, relation/tuple ADT 
2. Relation, tuple, implentation 
3. Nested loop join
4. Hash table join
5. Merge sort join 
"""

import random

## treating relation as matrix with header column 
## in pythonic terms, a nested list with a header column at list[0]
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

#### endregion 

if __name__ == '__main__': 
