""" Minerr :  """

from __future__ import print_function
import sys
import argparse
import numpy as np
import babin as ba
from math import *

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

# Define options

#---------------------------------------------------------------------
#Hack for negative floats as option
for i, arg in enumerate(sys.argv):
  if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg
#---------------------------------------------------------------------
parser = argparse.ArgumentParser(description="Program to compute rms")
parser.add_argument("fin1",help="Input binary file")
parser.add_argument("fin2",help="Input binary file")
#parser.add_argument("fout",help="Output binary file")
#parser.add_argument("-shift",dest="shift", default=0)

#Parse arguments
args = parser.parse_args()


#Get the data
fin1 = ba.bin(args.fin1)
data1=fin1.readb()
#Get the data
fin2 = ba.bin(args.fin2)
data2=fin2.readb()
shift= args.shift

n = data1.shape[0]

err = np.zeros((n))
for l in range(0:shift) :
    err[:] = 0.0
    for i in range (0: n-l) :
        err[i] = data1[i]-data2[i+l]
    nrm = sqrt(np.mean(np.square()))
    print(nrm)
