################### program for forming shift cipher ########################
from __future__ import division
import numpy as np
import string
a = raw_input("Enter the cipher text: ").lower()
key=raw_input('Enter the Key:')#enter the required number of shift
key=int(key)
num = dict(zip(range(0,26),string.ascii_lowercase))# for reverse mapping: numbers to letter
def shift(l1,n1): # for left shift operation
    return l1[n1:] + l1[:n1]
a1=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
S1=[]
for character in a:
    number= ord(character)-97
#    print number
    number=((number + key)%26)
#    print number
    S1.append(number)
a2=[]
for i2 in S1:
    a2.append(num[i2])
print '\n','Your shift ciphered text for the given key:',''.join(str(elm) for elm in a2)
