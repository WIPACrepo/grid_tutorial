#!/bin/sh /cvmfs/icecube.opensciencegrid.org/py2-v2/icetray-start
#METAPROJECT icerec/V05-00-05

from argparse import ArgumentParser
from icecube import icetray, dataio
from I3Tray import *

parser = ArgumentParser()
parser.add_argument("-i", "--input", dest="INFILE")
parser.add_argument("-o", "--output", dest="OUTFILE")
args = parser.parse_args()

grid = 'gsiftp://gridftp-users.icecube.wisc.edu'
infile = grid + args.INFILE
outfile = grid + args.OUTFILE

tray = I3Tray()
tray.Add(dataio.I3Reader, Filename=infile)
tray.Add("Dump")
tray.Add("I3Writer", Filename=outfile)
tray.Execute(10)
