''' Energy: compute energy '''

import babin as ba
import numpy as np
import pylab as pl
import sys
import argparse

#---------------------------------------------------------------------
#Hack for negative floats as option
for i, arg in enumerate(sys.argv):
  if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg
#---------------------------------------------------------------------
parser = argparse.ArgumentParser(description="program to spectrum of data")
parser.add_argument("fin",help="Input binary file")
parser.add_argument("-n1",dest="n1",type=int,default=1,help="Axis to integrate")
parser.add_argument("-d1",dest="d1",type=float,default=1.0,help="Sampling interval along axis 1")

#Parse arguments
args = parser.parse_args()

n1 = args.n1
d1 = args.d1

fin = ba.bin(args.fin)
n2=1
n=int(n1/2)
realtrace=fin.read((n2,n1))
realtrace=realtrace.transpose()
en = np.zeros(n)

ten=0.0
for i in range(1,n):
    en[i] = en[i-1]+realtrace[i]*realtrace[i]
    ten   = ten + realtrace[i]*realtrace[i]

nen = en/ten

for i in range(0,n) :
    if( nen[i] > 0.99) :
        print("99 percent of energy at frequency: ", i*d1)
        break

