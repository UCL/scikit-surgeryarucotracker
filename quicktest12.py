#! /usr/bin/python3.6

from sksurgeryarucotracker.arucotracker import ArUcoTracker

config1={'video source' : 'data/12markers.png',
        'aruco dictionary' : 'DICT_6X6_250'}

print ("no config")
tracker=ArUcoTracker(config1)
tracker.start_tracking()
print (tracker.get_tool_descriptions())
  
phs, tss , fns, tracking,  qls, = tracker.get_frame()
print (phs, tss, fns, tracking, qls)

tracker.stop_tracking()
tracker.close()
del tracker

