"""
Script: membership_structures_algorithms.py
Authors: Carlos Perez, Djamil Lakhdar-Hamina

m= number of bits,  n= number of items, k= number of hash functions , p false positive probability 
n = ceil(m / (-k / log(1 - exp(log(p) / k))))
p = pow(1 - exp(-k / (m / n)), k)
m = ceil((n * log(p)) / log(1 / pow(2, log(2))));
k = round((m / n) * log(2)); 

"""
import sys
import time
import bitarray 
import mmh3

class BloomFilter: 
