#!/usr/bin/python
#
# This program is called mconvert2gpx.py.  It find the
# files that match *TES and converts them to
# gpx and kmz files
#
# Import modules
#

import glob
import os


#
# Find TES files
tesfiles = glob.glob('*.TES')
#
# Convert files to gpx and kmz
#
for file in tesfiles:
  cmd= 'convert2gpx.py ' + file
  os.system(cmd)
