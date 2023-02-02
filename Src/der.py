""" Der : Differentiate"""
from __future__ import print_function
import sys
import argparse
import numpy as np
import babin as ba

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def df(u,v,dx) :
    nx=v.shape[0]
    for i in range(1,nx):
        v[i] = (u[i]-u[i-1])/dx
    return(v)   

# Define options

#---------------------------------------------------------------------
#Hack for negative floats as option
for i, arg in enumerate(sys.argv):
  if (arg[0] == '-') and arg[1].isdigit(): sys.argv[i] = ' ' + arg
#---------------------------------------------------------------------
parser = argparse.ArgumentParser(description="program to integrate (trapez) along axis of binary cube")
parser.add_argument("fin",help="Input binary file")
parser.add_argument("fout",help="Output binary file")
parser.add_argument("-n1",dest="n1",type=int,help="first dimension of data")
parser.add_argument("-n2",dest="n2",type=int,default=1,help="second dimension of data")
parser.add_argument("-n3",dest="n3",type=int,default=1,help="third dimension of data")
parser.add_argument("-ax",dest="ax",type=int,default=1,help="Axis to integrate")
parser.add_argument("-d1",dest="d1",type=float,default=1.0,help="Sampling interval along axis 1")

#Parse arguments
args = parser.parse_args()

# Axis
if args.n1 is not None:
    n1 = args.n1
else :
    sys.exit("Missing n1!")

n2 = args.n2
n3 = args.n3
d1 = args.d1

if n1 <= 0 :
    sys.exit("n1 0 or negative \n")
if n2 <= 0 :
    sys.exit("n2 0 or negative \n")
if n3 <= 0 :
    sys.exit("n3 0 or negative \n")

if(args.ax == 1) :
    ax = 3
elif(args.ax == 2) :
    ax = 2
elif(args.ax == 3) : 
    ax = 1

#Get the data
fin = ba.bin(args.fin)
data=fin.read((n3,n2,n1))
print(np.shape(data))
der = np.zeros((n3,n2,n1))

#differentiate the data along axis 1
for i in range(0,n3) :
    for j in range(0,n2) :
        der[i,j,:] = df(data[i,j,:],der[i,j,:],d1)

fout = ba.bin(args.fout,"w")
fout.write(der)
