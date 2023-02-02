""" Rms : Compute rms of binary data """

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
parser.add_argument("fin",help="Input binary file")
parser.add_argument("-v",dest="v",action='store_true',help="Verbose flag")

#Parse arguments
args = parser.parse_args()


#Get the data
fin = ba.bin(args.fin)
data=fin.readb()

#Compute rms value, max and min.
rms = sqrt(np.mean(np.square(data)))
max = np.amax(data)
min = np.amin(data)
pos = np.argmax(data)

if args.v :
    print("** max value: ", max)
    print("** max at pos: ", pos)
    print("** min value: ", min)
    print("** rms value: ", rms)

else :
    print(rms)
