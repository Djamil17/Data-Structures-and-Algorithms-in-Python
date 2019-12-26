## function
class Relation:

    def __init__(self, n, m, init=True):
        self.n = n
        self.m = m
        if init:
            self.relation = [[random.randint(0,5)] * n for x in range(m)]
        else:
            self.relation= [ ]

    def __getitem__(self, idx):
        return self.relation[idx]

    def __repr__(self):
        s = str(self.relation)
        return s

    def setTuple(self,idx, item):
      self.relation[idx] = item

    def setAtt(self, *arg):
      return self.relation.insert(0, list(arg))

    def size(self, n, m):
        return n * m

def nested_loop_join(left_relation, right_relation, attribute_a):
    for ltuple in left_relation[1:]:
      for rtuple in right_relation[1:]:
        if ltuple is attribute_a and rtuple is attribute_a and ltuple==rtuple:
           return '<' + ltuple + ',' + rtuple + '>'
