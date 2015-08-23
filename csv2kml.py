#!/usr/bin/python
#
# This program is called csv2kml.py.  It reads a CSV file
# and converts it to KMZ format using simple formattin.
# 2014 Jan 11 Frank Monaldo Modified to start a new LineString
#                           if there is a time gap of grater than
#                           120 seconds.
#
# Import modules
#
import sys
import os
import re
import math

# parse input information

input_file  = sys.argv[1]
output_file = sys.argv[2]

#
# Constants
#
radius_earth = 6371.00 # kilometers
max_distance = 2.0     # kilometers
#
# Read csvfile
# 
f = open(input_file, 'r')
s = f.readlines()
n=  len(s)
#
# Open output file
#

out    = open(output_file, "w")
#
# Write prefix
#	
out.write('<?xml version="1.0" encoding="UTF-8"?>          \n')
out.write('<kml xmlns="http://earth.google.com/kml/2.1">   \n')
out.write('<Folder>                                        \n')


red      = 'FF1400FF'
blue     = 'FFFF7800'
yellow   = 'FF78FFF0'
green    = 'FF00FF14'
pink     = 'FFB478F0'
color    = [ red, blue, yellow, green, pink]
i        = 0       
ci       = 0
old_time = 0
long0    = 0.00
lat0     = 90
print '                                   Seconds  Kilometers'
for line in s:
   check= line.find('index')
   #
   # In the word 'index is in the line, we are at a header line
   # check will be les than zero and we do not process
   #
   if check <0:
     x = line.split()
     t              = int(x[1]) # Convert from string to integer
     longitude      = x[3]
     latitude       = x[4]
     altitude       = x[5]
     long1          = float(longitude)
     lat1           = float(latitude)
     phi0           = math.radians(lat0)
     phi            = math.radians(lat1)
     lam0           = math.radians(long0)
     lam            = math.radians(long1)
     dphi           = phi - phi0
     dlam           = lam - lam0
     a              = math.sin(dphi/2.0)**2 + math.cos(phi0) * math.cos(phi) * math.sin(dlam/2)**2
     c              = 2.0 * math.atan2( math.sqrt(a), math.sqrt(1.0-a) )
     d              = radius_earth * c
     #
     # If there is at least one position written to the kml file
     # and if there is greater than 120 second in time
     # start a new line string
     #

     if i == 0 or (t - old_time) >60 or (d > max_distance): 
       print 'New seqment time/dist delta = ' + '{0:12d}'.format((t - old_time)) + '  ' + '{:f}'.format(d)
       #
       # close out old line i > 0
       #
       if i > 0 :
         out.write('      </coordinates>                          \n')     
         out.write('    </LineString>                             \n')     
         out.write('  </Placemark>                                \n')     
       out.write('                                                \n')
       out.write('  <Placemark>                                   \n')
       out.write('    <Style>                                     \n')
       out.write('      <LineStyle>                               \n')
       cci       = ci % 5
       colorline = '        <color>' + color[cci] +'</color>                 \n'
       ci        = ci + 1
       out.write(colorline)
       #print colorline
       #out.write('        <color>AA3030FF</color>                 \n')
       out.write('        <width>6</width>                        \n')
       out.write('      </LineStyle>                              \n')
       out.write('    </Style>                                    \n')
       out.write('    <LineString>                                \n')
       out.write('      <coordinates>                             \n')
     outline        = '      '+ longitude + ','+latitude +','+ altitude+ ' \n'
     out.write(outline)        
     i        = i + 1
     long0    = float(longitude)
     lat0     = float(latitude)
     old_time = t
out.write('      </coordinates>                           \n')     
out.write('    </LineString>                              \n')     
out.write('  </Placemark>                                 \n')     
out.write('</Folder>                                      \n')
out.write('</kml>                                         \n')
out.close()


