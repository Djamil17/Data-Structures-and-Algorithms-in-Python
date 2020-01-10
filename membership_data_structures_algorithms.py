"""
Script: membership_structures_algorithms.py
Authors: Carlos Perez, Djamil Lakhdar-Hamina

m= number of bits,  n= number of items, k= number of hash functions , p false positive probability 
n = ceil(m / (-k / log(1 - exp(log(p) / k))))
p = pow(1 - exp(-k / (m / n)), k)
m = ceil((n * log(p)) / log(1 / pow(2, log(2))));
k = round((m / n) * log(2)); 

"""

import math
import bitarray as bitarr
import mmh3


class BloomFilter:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.bit_array = bitarr.bitarray(self.m)
        self.k = None
        self.p = None
        self.size=self.m

    def countHashFunc(self):
        self.k = math.trunc(self.m / self.n * math.log(2))
        return self.k

    def calcNegProb(self):
        if self.k:
            self.p = (1 - (math.e ** -self.k * self.n / self.m)) ** self.k
            return self.p
        else:
            self.countHashFunc()
            self.p = (1 -( math.e ** -self.k * self.n / self.m)) ** self.k
            return self.p

    def add(self, item):
        indexes = []
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.size
            indexes.append(index)
            self.bit_array[index] = True

    def check(self, item):
        for i in range(self.k):
            index = mmh3.hash(item, i) % self.size
            if self.bit_array[index] is True:
                return True
            else:
                return False

    def __str__(self):
        return str(self.bit_array)

def main():
a=BloomFilter(3,87)
print(a.countHashFunc())
print(a.calcNegProb())
print(a)
a.add('jesus')
print(a.check('jesus'))

if __name__== '__main__':
    main()
