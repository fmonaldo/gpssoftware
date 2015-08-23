#!/usr/bin/python
#
# This program is called mconvert2gpx.py.  It find the
# files that match *TES and converts them to
# gpx and kmz files
#
# Import modules
#
# 2015 Aug 13 Frank Monaldo Add *CSV files from Columbus v990 receiver

import glob
import os


#
# Find TES and CSV files
inputfiles = glob.glob('*.TES') + glob.glob('*.CSV')
#
# Convert files to gpx and kmz
#
for file in inputfiles:
  cmd= 'convert2gpx.py ' + file
  os.system(cmd)
