#!/usr/bin/python
#
# This program is called convert2gpx.py.  It reads a TES file
# and converts it to GPX and KMZ formats
#
# Import modules
#

import sys
import os
import re


# parse input information

input_file = sys.argv[1]
#
# Construct command
#
print '     '

cmd1      = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmd1      = cmd1 + ' -t -i wintec_tes -f'
pwd       = os.getcwd()
cmd2      = pwd + '/' + input_file + ' -o gpx,suppresswhite=0,logpoint=0,humminbirdextensions=0,garminextensions=0 -F '
cmd3      = 'temp.gpx'
cmd1csv   = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmd1csv   = cmd1csv +  ' -t -i v900 -f '
cmd2csv  = pwd + '/' + input_file + ' -o gpx -F '
cmd3csv    = 'temp.gpx'

cmd       = cmd1    + ' ' + cmd2    + ' ' + cmd3
cmdcsv    = cmd1csv + ' ' + cmd2csv + ' ' + cmd3csv


extension = os.path.splitext(input_file)
ext       = extension[1]
if ext == '.CSV' : cmd = cmdcsv

os.system( cmd )

#
# Read temp.gpx
# 
f = open('temp.gpx', 'r')
s = f.readlines()
j = -1
for line in s:
   check= line.find('<time>')
   if check >=0:
     j= j + 1
     if j == 2:
       t       =  line
       dt      =  t[check+ 6:check+16]
       tm      =  t[check+17:check+25]
       hr      =  tm[0:2]
       mn      =  tm[3:5]
       sc      =  tm[6:8]
       root    =  dt + '-' + hr +'-' + mn + '-' + sc
       gpxfile =  root + '.gpx'
       break


os.rename('temp.gpx', gpxfile)

print 'GPS data in file   : ' + input_file 
print 'Stored in GPX file : ' + gpxfile


#
# Creating KML file
#

cmd1    = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmd1    = cmd1 + ' ' + ' -t -i wintec_tes -f '
pwd     = os.getcwd()
cmd2    = pwd + '/' + input_file + ' -o kml,lines=1,points=1,floating=1,extrude=0,track=1,trackdata=1,trackdirection=0,labels=1 -F '
kmlfile = root + '.kml'
cmd3    = ' ' + kmlfile
cmd1csv = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmd1csv = cmd1csv + '  -t -i v900 -f '
cmd2csv = pwd + '/' + input_file + ' -o kml,floating=1,track=1 -F '
cmd3csv = ' ' + kmlfile


cmd   = cmd1    + ' ' + cmd2    + ' ' + cmd3
cmdcsv= cmd1csv + ' ' + cmd2csv + ' ' + cmd3csv
if ext == '.CSV' : cmd = cmdcsv


os.system( cmd )
print 'Stored in KML file : ' + kmlfile

#
# Convert KML to KMZ file
#
kmzfile =  root +'.kmz'
cmd= 'zip -q ' + kmzfile + ' ' + kmlfile
os.system( cmd )
print 'Stored in KMZ file : ' + kmzfile
os.remove(kmlfile)
print 'Removed            : '  + kmlfile

#
# Creating CSV file
#
cmd     = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmd     = cmd + ' -t -i wintec_tes -f '
pwd     = os.getcwd()
cmd     = cmd + pwd + '/' + input_file + ' -o xcsv,style='
cmd     = cmd + '/Users/frank/scripts/trackpnt.sty ' 
cmd     = cmd + ' -F ' + root  + '.csv'
cmdcsv = '/Applications/GPSBabelFE.app/Contents/MacOS/gpsbabel'
cmdcsv = cmdcsv + '  -t -i v900 -f '
cmdcsv = cmdcsv + pwd + '/' + input_file + ' -o xcsv,style=/Users/frank/scripts/trackpnt.sty '
cmdcsv = cmdcsv + ' -F ' + root  + '.csv'
if ext == '.CSV' : cmd = cmdcsv

os.system( cmd )
csvfile = root  + '.csv'
print 'Stored in CSV file : ' + root  + '.csv'

print '     '
#
#  Create Simple Version of KMLZ FILE
#
kmlfile = root+'_b.kml'
cmd = 'csv2kml.py '+ csvfile + ' ' + kmlfile
os.system( cmd )
#
# Convert KML to KMZ file
#
kmzfile =  root +'_b.kmz'
cmd= 'zip -q ' + kmzfile + ' ' + kmlfile
os.system( cmd )
print 'Stored in KMZ file : ' + kmzfile
os.remove(kmlfile)
print 'Removed            : '  + kmlfile

